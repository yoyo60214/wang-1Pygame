# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 13:36:00 2021

@author: EDISON
"""

class Car():
    def __init__(self,speed,position,color):
        self.speed=speed
        self.position=position
        self.color=color
    def run(self):
        self.position=self.position+self.speed
    def getPosition(self):
        return self.position
    
    
class ElectricCar(Car):
    def __init__(self,speed,position,color):
        super().__init__(speed,position,color)
        self.power=100
    def run(self):
        if self.power>0:
            self.power=self.power-1
            self.position=self.position+self.speed
car1=Car(30,0,(255,255,255))    
for i in range(200):
    car1.run()    
print("Car1 position is:"+str(car1.getPosition()))    
for i in range(200):
    car1.run()    
print("Car1 position is:"+str(car1.getPosition()))    
print("Car1 position is:"+str(car1.position))

car2=ElectricCar(50,0,(0,255,100))  
while car2.power>0:
    car2.run()
    print("Car2 position is:"+str(car2.position))
    print("Car2 power is:"+str(car2.power))
    
class Human():
    def __init__(self,name,height,weight):
        
        self.name=name
        self.height=height
        self.weight=weight
    def bmi(self):
        bmi=self.weight/(self.height*self.height)
        return bmi
Yoyo=Human("Yoyo", 1.91, 86)    
bmi=Yoyo.bmi()    
print("Yoyo bmi is:"+str(bmi))    
    


Tom=Human("Tom",1.45,49)
bmi=Tom.bmi()
print("Tom bmi is:"+str(bmi))



class Robot(Human):
    def __init__(self,name,height,weight):
        super(),__init__(name,height,weight)
        self.energy=100
        self.voice=100
    def voice(self):
        if self.voice==100:
            print("too loud")






























