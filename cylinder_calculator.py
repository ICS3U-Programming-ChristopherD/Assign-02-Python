#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Sep. 29, 2022
# This program calculates the surface area and volume of a cylinder.

import math
from termcolor import colored


def main():

    user_unit = input(
        colored("Enter the units of the cylinder's dimensions: ", "magenta")
    )
    print("")
    # Asks the user if they would like to enter the radius or diameter
    print(
        colored(
            "Enter a number OTHER THAN 1 to enter the diameter of the cylinder.",
            "yellow",
        )
    )
    print("")
    measurement_choice = int(
        input(colored("Enter 1 to use the cylinder's radius: ", "magenta"))
    )
    print()
    # Asking the user for the RADIUS and height of the cylinder.
    if measurement_choice == 1:
        radius = float(
            input(
                colored(f"Enter the radius of the cylinder in {user_unit}: ", "magenta")
            )
        )
        print("")
        height = float(
            input(
                colored(f"Enter the height of the cylinder in {user_unit}: ", "magenta")
            )
        )
        print("")
        # If the user entered a value equal to 0 or less using the radius:
        while radius <= 0 or height <= 0:
            print(colored("One or both of the dimensions is zero or less.", "red"))
            print("")
            print(colored("Please enter a positive number.", "red"))
            print("")
            radius = float(
                input(
                    colored(
                        f"Enter the radius of the cylinder in {user_unit}: ", "magenta"
                    )
                )
            )
            print("")
            height = float(
                input(
                    colored(
                        f"Enter the height of the cylinder in {user_unit}: ", "magenta"
                    )
                )
            )
    else:
        # Asking the user for the DIAMETER and height of the cylinder.
        diameter = float(
            input(
                colored(
                    f"Enter the diameter of the cylinder in {user_unit}: ", "magenta"
                )
            )
        )
        # Diameter is converted to the radius by diving the diameter by 2.
        radius = diameter / 2
        print("")
        height = float(
            input(
                colored(f"Enter the height of the cylinder in {user_unit}: ", "magenta")
            )
        )
        print("")
        # If the user entered a value equal to 0 or less using the DIAMETER:
        while radius <= 0 or height <= 0:
            print(colored("One or both of the dimensions is zero or less.", "red"))
            print("")
            print(colored("Please enter a positive number.", "red"))
            print("")
            # Asking the user for the DIAMETER and height of the cylinder.
            diameter = float(
                input(
                    colored(
                        f"Enter the diameter of the cylinder in {user_unit}: ",
                        "magenta",
                    )
                )
            )
            # If the user entered a value equal to 0 or less using the DIAMETER:
            radius = diameter / 2
            print("")
            height = float(
                input(
                    colored(
                        f"Enter the height of the cylinder in {user_unit}: ", "magenta"
                    )
                )
            )
            print("")

    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    volume = math.pi * radius**2 * height

    print(
        colored(
            "The surface area of the cylinder is {:.2f}cm^2.".format(surface_area),
            "green",
        )
    )
    print("")
    print(colored("The volume of the cylinder is {:.2f}cm^3".format(volume), "green"))


if "__main__" == __name__:
    main()
