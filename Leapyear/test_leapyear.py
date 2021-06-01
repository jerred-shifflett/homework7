import unittest
import leapyear

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(leapyear.isItLeapYear(2000),True)
	def test2(self):
		self.assertEqual(leapyear.isItLeapYear(2019),False)
	
if __name__ == '__main__':
	unittest.main()