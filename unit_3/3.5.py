'''5) Create a Temperature class. Create 2 methods named convertFarenheit() 
and convertCelsius()'''

class Temperature():

    def convertFarenheit(self):
        self.cel = float(input("Enter celsious:"))
        self.con_fer = (self.cel * 9/5) + 32
        print(f"Converted celsious to farenheit:{self.con_fer}")
        

    def convertCelsius(self):
        self.fer = float(input("Enter ferenheit:"))
        self.con_cel = (self.fer-32)/1.8
        print(f"Converted ferenheit to celsious:{self.con_cel}")

temp = Temperature()
temp.convertFarenheit()
temp.convertCelsius()




