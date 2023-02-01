import unittest
import geometric_sequence_n


class TestRunner(unittest.TestCase):

    def test_seq(self):
        list1 = [2, 4, 8, 18, 12, 213, 213123, 213]
        list2 = [3, 6, 9, 24]

        self.assertEqual(geometric_sequence_n.geom_seq(list1), (True,[18, 12, 213, 213123, 213]))
        self.assertEqual(geometric_sequence_n.geom_seq(list2), (True,[9, 24]))


if __name__ == "__main__":
    unittest.main()
