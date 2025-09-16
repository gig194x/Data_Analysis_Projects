import unittest
import pandas as pd

class TestBooksCleaning(unittest.TestCase):
    def setUp(self):
        # load the cleaned data
        self.df = pd.read_csv("books_clean.csv")

    def test_not_empty(self):
        self.assertGreater(len(self.df), 0, "DataFrame is empty!")

    def test_price_is_numeric(self):
        self.assertTrue(pd.api.types.is_float_dtype(self.df["price"]),
                        "Price column is not float!")

    def test_rating_range(self):
        self.assertTrue(self.df["rating"].between(1,5).all(),
                        "Ratings are not between 1 and 5!")

    def test_no_nulls(self):
        self.assertFalse(self.df.isnull().any().any(),
                         "There are NaN values in the DataFrame!")

if __name__ == "__main__":
    unittest.main()
