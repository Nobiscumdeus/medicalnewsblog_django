#Case 1
class Robot:
    def introduce_self(self):
        print(f" My name is {self.name}")
        
r1=Robot()
r1.name='Tom'
#print(r1.introduce_self())

#Case 2
class Robotics:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print(f"My name is {self.name} , and my color is {self.color} and my weight is ,{self.weight}")
        
        
#Case 3
class Animal(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f"Hi I am {self.name}, and I am {self.age} years old ")
        
    def talk(self):
        print("Bark")
        
        
class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
        
    def talk(self):
        print(f" Mew ")
tim=Cat("tim",23,"Blue")


#Fourth Case 
class Vehicle():
    def __init__(self,price,gas,color):
        self.price=price
        self.gas=gas
        self.color=color
        
    def fillUpTank(self):
        self.gas=100
        
    def emptyTank(self):
        self.gas=0
    
    def gasLeft(self):
        return self.gas
    
    
class Gas(Vehicle):
    def __init__(self,price,gas,color,speed):
        super().__init__(price,gas,color)
        self.speed=speed
        
    def beep(self):
        print("Beep ")
        
        
#Fifth Case
class Dog:
    dogus=[]
    
    def __init__(self,name):
        self.name=name
        self.dogus.append(self)
        
    @classmethod
    def num_dogs(cls):
        return len(cls.dogus)
    
    @staticmethod
    def bark(n):
        ''' barks n times'''
        for _ in range(n):
            print("Bark: ")
            
class _Private:
    def __init__(self,name):
        self.name=name
        
class NotPrivate:
    def __init__(self,name):
        self.name=name
        self.priv=_Private(name)
        
    def _display(self):
        print("Hello")
        
    def display(self):
        print("Hi")