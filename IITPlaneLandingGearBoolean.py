#This is a comment line that describes the purpose of the program
#This program determines whether the plane's landing gear is deployed based on various conditions
#input a function is a mathamatical express that takes input processes info then returns a value
 
sensorLW = int(input("Please enter LW: ")) 
sensorRW = int(input("Please enter RW: ")) 
sensorDG = int(input("Please enter DG: ")) 
gLed =  not sensorLW == 1 and  not sensorRW == 1 and not sensorDG == 1
print ("Landing Gear Deployed: " + str(gLed))
