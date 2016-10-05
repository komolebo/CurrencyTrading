from Functions import read, find_profit
from bottle import get, static_file, run, post, put

matrix = []      # trading table
currencies = []  # currency names


@get('/')
def server():
    return static_file('Main.html', root='../static')


@get('/static/<filename>')
def send_static(filename):
    return static_file(filename, root='../static/')


@get('/scripts/<filename>')
def send_script(filename):
    return static_file(filename, root='../scripts/')


@get('/currencies')
def get_currencies():
    m = {}

    n = len(currencies)
    for i in range(n):
        d = {}
        for j in list(set(range(n))):
            d[currencies[j]] = matrix[i][j]
        m[currencies[i]] = d

    return m


@get('/currency/<currency_name>')
def get_currency(currency_name):
    if not (currency_name in currencies):
        return 'Not found currency: ' + currency_name

    i = currencies.index(currency_name)
    d = {}
    for j in range(len(currencies)):
        d[currencies[j]] = matrix[i][j]
    return d


@get('/sequence')
def get_sequence():
    result = find_profit(matrix, currencies)

    message = ''
    if result:
        conversion_sequence = [currencies[i] for i in result.sequence()]
        message += 'profit_percent: +' + str(result.profit()) + '<br/>'
        message += 'sequence: ' + str(conversion_sequence)
    else:
        message += 'no risk-free opportunities exist yielding over 1.00% profit exist'
    return message


@post('/currency/<new_currency>')
def post_currency(new_currency):
    if new_currency in currencies:
        return

    # Add new column to matrix
    for i in range(len(matrix)):
        matrix[i].append(1.0)

    # Add new row to matrix
    matrix.append([1.0 for i in range(len(currencies) + 1)])

    # Update list of currencies
    currencies.append(new_currency)


@put('/currency/<_from>/<_to>/<rate>')
def put_currency(_from, _to, rate):
    if float(rate) <= 0:
        return

    i = currencies.index(_from)
    j = currencies.index(_to)
    matrix[i][j] = rate


if __name__ == '__main__':
    read('../examples/example1.csv', currencies, matrix)
    run(host='localhost', port=8080, debug=True)
