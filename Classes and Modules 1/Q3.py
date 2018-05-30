# Q3.

class Temperature:


	def convertFahrenheit(self,celsius):
		self.fahren=((9*celsius)/5)+32
		print("Fahrenheit In Degree:", self.fahren)
	def convertCelsius(self,fahrenheit):
		self.cels=((fahrenheit-32)/9)*5
		print("Celsius In Degree:", self.cels)
temp=Temperature()
temp.convertFahrenheit(50)
temp.convertCelsius(80)

'''
OUTPUT:
Fahrenheit In Degree: 122.0
Celsius In Degree: 26.666666666666664
'''