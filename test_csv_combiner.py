import unittest
import csv_combiner

class TestCsv_combiner(unittest.TestCase):

    def test_csv_combiner(self):
        list1 = ["csv_combiner.py", "household_cleaners.csv"]
        result = csv_combiner.csvcombiner(list1)
        self.assertEqual(result, "combined.csv")

    def test_csv_combiner2(self):
        list2 = ["csv_combiner.py"]
        result = result = csv_combiner.csvcombiner(list2)
        self.assertEqual(result, "No files detected")




if __name__ == "__main__":
    unittest.main()