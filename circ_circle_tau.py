#!/usr/bin/env python3
# Created by: Angel
# Created on: Feb 26,2025
# This program asks the user for teh radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.
# import theTAU constant from the constants.py
from constants import TAU


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculates the circumference
    circumference = TAU * radius

    # displays teh circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
