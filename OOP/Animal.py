# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:51:44 2015

@author: 97oskmal
"""

import random

class Animal:
    """the constructor"""
    def __init__(self, growth_rate, food_need, water_need):
        """atttributes for the initial values are being set"""
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Cub"
        self._type = "Generic"
        self._name = ""
        
    def needs(self):
        return {'food_need' :self._food_need, 'water_need' :self._water_need}
        
    def report(self):
        return {'type' :self._type, 'status' :self._status, 'weight' :self._weight, 'days_growing' :self._days_growing}
        
    def _update_status(self):
        if self._weight > 50:
            self._status = "Grown"
        elif self._weight > 25:
            self._status = "Young"
        elif self._weight > 10:
            self._status = "Child"
        elif self._weight > 0:
            self._status = "Kiddo"
        elif self._weight == 0:
            self._status = "Cub"
            
    def grow(self, food,water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        """increment days growing"""
        self._days_growing += 1
        """update the status"""
        self._update_status()
        
def auto_grow(animal, days):
    """grow the animal with an automatic grow function"""
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)
        
def manual_grow(animal):
    """Need to get food and water values from the one using the program"""
    valid = False
    while not valid:
        try:
            food = int(input("Enter a food value (1-10)"))
            if 1 <= food <= 10:
                valid = True
            else:
                print("The value you entered is not valid, please enter a value between 1 and 10")
        except ValueError:
            print("The value you entered is not valid, please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Enter a water value (1-10)"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("The value you entered is not valid, please enter a value between 1 and 10")
        except ValueError:
            print("The value you entered is not valid, please enter a value between 1 and 10")
    """grow the crop"""
    animal.grow(food,water)
    
def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit the test program")
    print()
    print("Please select one of the options presented in the menu above")
          
          
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
                print("Please enter a valid option")
    return choice
    
def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thanks for using the program mate!")
            
    
def main():
    """instaniate the class"""
    new_animal = Animal(1, 3, 6)
    """No longer need for testing"""
    manage_animal(new_animal)

if __name__ == "__main__":
    main()