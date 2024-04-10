import unittest

import main


class TestFunctionsMethods(unittest.TestCase):

  def test_sin(self):
      self.assertEqual(main.calcSin(10, "deg", 5.5), 'error')
      self.assertEqual(main.calcSin(10, "rad", 5.5), 'error')
      self.assertEqual(main.calcSin(10, "lol", 5.5), 'error')
      self.assertEqual(main.calcSin("ghjgj", "rad", 5), 'error')
      self.assertEqual(main.calcSin("10", "rad", "hjkhk"), 'error')
      self.assertEqual(main.calcSin(-10, "rad", 2), '0.54')
      self.assertEqual(main.calcSin(-10, "deg", 2), '-0.17')

  def test_cos(self):
      self.assertEqual(main.calcCos(10, "deg", 5.5), 'error')
      self.assertEqual(main.calcCos(None, "deg", 5), 'error')
      self.assertEqual(main.calcCos(" ", "deg", 5), 'error')
      self.assertEqual(main.calcCos("", "deg", 5), 'error')
      self.assertEqual(main.calcCos(10, None, 5.5), 'error')
      self.assertEqual(main.calcCos(10, "deg", None), 'error')
      self.assertEqual(main.calcCos(10, "rad", 5.5), 'error')
      self.assertEqual(main.calcCos(10, "nichego", 5.5), 'error')
      self.assertEqual(main.calcCos("10", "rad", 5), 'error')
      self.assertEqual(main.calcCos("10", "rad", "2"), 'error')
      self.assertEqual(main.calcCos(-10, "rad", 2), '-0.84')
      self.assertEqual(main.calcCos(-10, "deg", 2), '0.98')

  def test_tan(self):
      self.assertEqual(main.calcTan(10, "deg", 5.5), 'error')
      self.assertEqual(main.calcTan(10, "ne", 5.5), 'error')
      self.assertEqual(main.calcTan(10, "rad", 5.5), 'error')
      self.assertEqual(main.calcTan("10", "rad", 5), 'error')
      self.assertEqual(main.calcTan("10", "rad", "2"), 'error')
      self.assertEqual(main.calcTan(-10, "rad", 3), '-0.648')
      self.assertEqual(main.calcTan(-10, "deg", 2), '-0.18')

if __name__ == '__main__':
    unittest.main()