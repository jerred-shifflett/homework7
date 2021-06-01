import unittest
import  FizzBuzz

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(FizzBuzz.fizzBuzz(15),"FizzBuzz")
	
if __name__ == '__main__':
	unittest.main()