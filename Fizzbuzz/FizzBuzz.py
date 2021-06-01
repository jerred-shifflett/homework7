def fizzBuzz(number):
	if (number%5==0 and number%3==0):
		string = "FizzBuzz"
		return string
	elif (number%3==0):
		string = "Fizz"
		return string
	elif (number%5==0):
		string = "Buzz"
		return string
