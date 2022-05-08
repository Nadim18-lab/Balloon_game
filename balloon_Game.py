from cmath import cos, sin
from math import radians
from random import random
from turtle import *

class balloon:
    def __init__(self,speed):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = window_height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])
    
    def move(self):
        direct = random.choice(self.probPool)
        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10
        self.y += self.speed*sin(radians(self.angle))
        self.x += self.speed*cos(radians(self.angle))
        if (self.x + self.a > width) or self.y > window_height + 30:
            if self.y > window_height/5:
                self.x -= self.speed*cos(radians(self.angle))
            else:
                self.reset()
            
