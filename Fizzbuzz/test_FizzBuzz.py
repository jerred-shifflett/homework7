import unittest
import  FizzBuzz

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(FizzBuzz.fizzBuzz(15),"FizzBuzz")
	def test2(self):
		self.assertEqual(FizzBuzz.fizzBuzz(9),"Fizz")
	def test3(self):
		self.assertEqual(FizzBuzz.fizzBuzz(10),"Buzz")
	
if __name__ == '__main__':
	unittest.main()