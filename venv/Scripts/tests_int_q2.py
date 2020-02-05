import unittest
from unittest.mock import patch
from int_q2 import satellite


class MyTestCase(unittest.TestCase):

    @patch('int_q2.satellite._findUpdateOperations')
    def test_make_sat_grid_dict(self, update_mock):
        g = [[1, 0], [0, 1]]
        update_mock.return_value = False
        test_sat = satellite(g, 2, 2)
        self.assertEqual(test_sat.sat_grid_dict,  { 0: {'Status': 1, 'UpdatedToday': False, 'UpdateOperations': False},
                                                    1: {'Status': 0, 'UpdatedToday': False, 'UpdateOperations': False},
                                                    2: {'Status': 0, 'UpdatedToday': False, 'UpdateOperations': False},
                                                    3: {'Status': 1, 'UpdatedToday': False, 'UpdateOperations': False},
                                                   })

    def test_find_correct_position_type(self):
        g = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        test_sat = satellite(g, 3, 3)
        self.assertEqual(test_sat._findUpdateOperations(0), (1, 3))
        self.assertEqual(test_sat._findUpdateOperations(1), (-1, 1, 3))
        self.assertEqual(test_sat._findUpdateOperations(2), (-1, 3))
        self.assertEqual(test_sat._findUpdateOperations(3), (1, 3, -3))
        self.assertEqual(test_sat._findUpdateOperations(4), (-1, 1, 3, -3))
        self.assertEqual(test_sat._findUpdateOperations(5), (-1, 3, -3))
        self.assertEqual(test_sat._findUpdateOperations(6), (1, -3))
        self.assertEqual(test_sat._findUpdateOperations(7), (-1, 1, -3))
        self.assertEqual(test_sat._findUpdateOperations(8), (-1, -3))

    def test_run_updating_sequence(self):
        g = [[0, 0, 0, 1],
             [0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]
        test_sat = satellite(g, 4, 4)
        self.assertEqual(test_sat.runUpdatingSequence(print_grid=False), 3)

    def test_run_updating_sequence_with_all_zeros(self):
        g = [[0, 0],
             [0, 0]]
        test_sat = satellite(g, 2, 2)
        self.assertEqual(test_sat.runUpdatingSequence(print_grid=False), -1)

if __name__ == '__main__':
    unittest.main()
