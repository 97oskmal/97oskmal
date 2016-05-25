# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:54:30 2016

@author: 97oskmal
"""

from Animal import Animal

class Sheep(Animal):
    """A new sheep animal"""
    
    """The constructor"""
    def __init__(self):
        """Call on the original class constructor with defult values like light, growth rate.."""
        super().__init__(1,3,6)
        self._type = "Sheep"
        
    """Override the growth method of pholymorphism"""
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Kiddo" and water > self._water_need:
                self._growth += self._growth_rate * 2.7
            elif self._status == "Child" and water > self._water_need:
                self._growth += self._growth_rate * 2.35
            else:
                self._growth += self._growth_rate
        """Now increament the growing over the day"""
        self._days_growing += 1
        """Then update status"""
        self._update_status()
        
def main():
    """The new Sheep Animal!"""
    sheep_animal = Sheep()
    print(sheep_animal.report())
    """Grow the animals manually"""
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    
if __name__ == "__main__":
    main()