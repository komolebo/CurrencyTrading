__author__ = 'oleh'

import copy
import csv


class Cash:
    def __init__(self, cur, val):
        self.cur = cur  # Currency type
        self.val = val  # Currency value (nominal)


# Holds money conversion data:
class Sequence:
    def __init__(self, cur_index):
        self.cash = Cash(cur_index, 1.0)  # how much money taken
        self.seq = [cur_index]            # conversion sequence
        self.prof = 1.0                   # predicted profit

    # convert taken money to new currency 'cur_index' with rate 'cur_rate'
    # update predicted profit with rate 'cur_rate_to_init'
    def convert(self, cur_index, cur_rate, cur_rate_to_init):
        self.seq.append(cur_index)
        self.cash = Cash(cur_index, self.cash.val * cur_rate)
        self.prof = self.cash.val * cur_rate_to_init

    # after conversions finally convert to initial currency
    def convert_to_init(self):
        self.seq.append(self.seq[0])

    # getters
    def current_currency(self):
        return self.seq[len(self.seq) - 1]

    def init_currency(self):
        return self.seq[0]

    def sequence(self):
        return self.seq

    def profit(self):
        return self.prof


# Check input data validity, returns False if invalid data
def check_valid(table):
    # check if not empty table
    if not len(table):
        return False

    # check if number of rows equals number of columns
    for row in table:
        if len(row) != len(table):
            return False

    return True


def read(name, currencies, matrix):
    with open(name, 'r') as f:
        try:
            table = list(csv.reader(f))

            # check data
            if not check_valid(table):
                print "Incorrect data"
                exit(-1)

            for currency in table[0][1:]:
                currencies.append(currency)  # vector of currencies names

            for row in table[1:]:
                matrix.append(row[1:])       # matrix of currency conversion
        except:
            print 'Wrong csv encoding'
            exit(-1)


# Breadth-first recursive search for profit conversion sequences
def analyze_sequences(sequences, matrix):
    # check if there is at least one sequence
    if not len(sequences):
        return None

    # Check if there's a profit sequence. If so then search best profit
    best_seq = max(sequences, key=lambda p: p.profit())
    if best_seq.profit() > 1.0:
        best_seq.convert_to_init()
        return best_seq

    # keep converting money
    new_sequences = []
    for s in sequences:
        # find unused currencies
        l = list(set(range(len(matrix))) - set(s.seq))
        for new_cur_index in l:
            new_seq = copy.deepcopy(s)
            rate = float(matrix[s.current_currency()][new_cur_index])
            init_rate = float(matrix[new_cur_index][s.init_currency()])
            new_seq.convert(new_cur_index, rate, init_rate)

            new_sequences.append(new_seq)

    # recursive call
    return analyze_sequences(new_sequences, matrix)


# Finds and returns result as object with conversion sequence data
def find_profit(matrix, currencies):
    # create initial sequences
    sequences = []
    for i in range(len(currencies)):
        sequences.append(Sequence(i))

    return analyze_sequences(sequences, matrix)