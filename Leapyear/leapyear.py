def isItLeapYear(year):
	if(year%4)==0:
		if(year%100)==0:
			if(year%400)==0:
				return True
			else:
				return False
		else:
			#it is not divisable by 100
			return False
	else:
		#it is not divisable by 4
		return False
