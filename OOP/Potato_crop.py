# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:10:41 2015

@author: 97oskmal
"""

from Crop import Crop

class Potato(Crop):
    """A potato crop"""
    
    """The constructor"""
    def __init__(self):
        """call the original class constructor with defult values, light, growth rate etc"""
        super().__init__(1,3,6)
        self._type = "Potato"
        
    """now to override the growth method or pholymorphism"""
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        """Now increament the growing over the day"""
        self._days_growing += 1
        """Then update status"""
        self._update_status()
        
def main():
    """The new potato crop"""
    potato_crop = Potato()
    print(potato_crop.report())
    """Now to manually grow the crop"""
    manual_grow(potato_crop)
    print(potato_crop.report())
    
if __name__ == "__main__":
    main()