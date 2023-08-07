import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2))

  def test_getDataPoint_calculatePriceBidEqualsAsk(self):
    quotes = [
      {'top_ask': {'price': 120, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 150, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 150, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price']+quote['top_bid']['price'])/2))  


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
      stockPrice_pairs = [
        {"A": 15, "B": 30},
        {"A": 30, "B": 15}

      ]
      """ ------------ Add the assertion below ------------ """
      for stockPair in stockPrice_pairs:
        self.assertEqual(getRatio(stockPair["A"], stockPair["B"]), stockPair["A"]/stockPair["B"])

  def test_getRatio_calculateRatio_B_Equals_0(self):
      stockPrice_pairs = [
        {"A": 15, "B": 0},
        {"A": 30, "B": 0}

      ]
      """ ------------ Add the assertion below ------------ """
      for stockPair in stockPrice_pairs:
        self.assertEqual(getRatio(stockPair["A"], stockPair["B"]), "Price_b is 0")


if __name__ == '__main__':
    unittest.main()
