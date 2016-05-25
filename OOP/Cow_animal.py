# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:36:55 2016

@author: 97oskmal
"""

from Animal import Animal

class Cow(Animal):
    """A new cow animal"""
    
    """The constructor"""
    def __init__(self):
        """Call on the original class constructor with defult values like light, growth rate.."""
        super().__init__(1,3,6)
        self._type = "Cow"
        
    """Override the growth method of pholymorphism"""
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Kiddo" and water > self._water_need:
                self._growth += self._growth_rate * 2.3
            elif self._status == "Child" and water > self._water_need:
                self._growth += self._growth_rate * 2.2
            else:
                self._growth += self._growth_rate
        """Now increament the growing over the day"""
        self._days_growing += 1
        """Then update status"""
        self._update_status()
        
def main():
    """The new Cow Animal!"""
    cow_animal = Cow()
    print(cow_animal.report())
    """Grow the animals manually"""
    manual_grow(cow_animal)
    print(cow_animal.report())
    
if __name__ == "__main__":
    main()