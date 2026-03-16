import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

# x = {   "water": 50,
#         "coffee": 18,
#         "milk": 100,
#         }
# print(total_ml_of_liquids(x))