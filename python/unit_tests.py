import unittest

from Functions import Sequence, check_valid, find_profit, analyze_sequences


class ServerTest(unittest.TestCase):
    def test_class_Sequence1(self):
        s = Sequence(0)
        self.assertEqual(s.sequence(), [0], 'Wrong initial sequence forming')

        s.convert(1, 2.0, 0.8)
        self.assertEqual(s.current_currency(), 1, 'convert method does not update sequence')
        self.assertEqual(s.init_currency(), 0, 'convert method resets initial currency')
        self.assertEqual(s.sequence(), [0, 1], 'convert method does not form sequence')
        self.assertEqual(s.profit(), 2.0 * 0.8, 'convert method does not update profit')

        s.convert_to_init()
        self.assertEqual(s.current_currency(), s.init_currency(),
                         "convert_to_init method does not update current_currency")
        self.assertEqual(s.profit(), 2.0 * 0.8, 'convert_to_init method does not update profit')

    def test_class_Sequence2(self):
        s = Sequence(2)
        self.assertEqual(s.sequence(), [2], 'Wrong initial sequence forming')

        s.convert(0, 0.2, 1.5)
        self.assertEqual(s.current_currency(), 0, 'convert method does not update sequence')
        self.assertEqual(s.init_currency(), 2, 'convert method resets initial currency')
        self.assertEqual(s.sequence(), [2, 0], 'convert method does not form sequence')
        self.assertEqual(s.profit(), 0.2 * 1.5, 'convert method does not update profit')

        s.convert_to_init()
        self.assertEqual(s.current_currency(), s.init_currency(),
                         "convert_to_init method does not update current_currency")
        self.assertEqual(s.profit(), 0.2 * 1.5, 'convert_to_init method does not update profit')

    def test_check_valid(self):
        table = [['', 'USD', 'UA'], ['USD', 1, 25], ['UA', 0.04, 1]]
        self.assertTrue(check_valid(table), 'check_valid breaks correct solution')

        table.append([])
        self.assertFalse(check_valid(table), 'check_valid does not check matrix dimensions')
        self.assertFalse(check_valid([]), 'check_valid does not provide empty values')

        table = [['', 'USD', 'UA', 'RUB'], ['USD', 1, 25], ['UA', 0.04, 1]]
        self.assertFalse(check_valid(table), 'check_valid does not provide empty values')

        table = [['', 'USD', 'UA'], ['UA', 0.04, 1]]
        self.assertFalse(check_valid(table), 'check_valid does not provide empty values')

    def test_profit(self):
        currencies = ['UA', 'USD']
        matrix = [[1.0, 2], [0.5, 1.0]]
        self.assertIsNone(find_profit(matrix, currencies), 'find_profit finds unreal profit')

        matrix = [[1.0, 2], [0.6, 1.0]]
        self.assertIsNotNone(find_profit(matrix, currencies), 'find_profit does not find profit')

        matrix = [[1.0, 2], [0.4, 1.0]]
        self.assertIsNone(find_profit(matrix, currencies), 'find_profit finds unreal profit')

    def test_analyze_sequences(self):
        matrix = [[1.0, 2], [0.6, 1.0]]
        sequences = [Sequence(0)]

        self.assertIsNotNone(analyze_sequences(sequences, matrix), 'analyze_sequences looses solutions')

        matrix = [[1.0, 2], [0.4, 1.0]]
        self.assertIsNone(analyze_sequences(sequences, matrix), 'analyze_sequences finds unreal solutions')
