# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:03:30 2015

@author: 97oskmal
"""

from Wheat_crop import Wheat
from Potato_crop import Potato
from Cow_animal import Cow
from Sheep_animal import Sheep

def display_menu():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("please select an option from the above menu")
    
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice
    
def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop
    
def main():
    new_crop = create_crop()
    manage_crop(new_crop)
    
if __name__ == "__main__":
    main()