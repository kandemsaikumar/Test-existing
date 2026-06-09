#!/usr/bin/env python3
"""
Sample Python Script
Author: Your Name
Description: This script takes a user's name and age, validates the input,
and prints a greeting with the calculated birth year.
"""

from datetime import datetime

def main():
    try:
        # Get user name
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        # Get and validate age
        age_input = input("Enter your age: ").strip()
        if not age_input.isdigit():
            print("Age must be a positive number.")
            return

        age = int(age_input)
        if age <= 0 or age > 120:
            print("Please enter a realistic age.")
            return

        # Calculate birth year
        current_year = datetime.now().year
        birth_year = current_year - age

        # Output result
        print(f"Hello, {name}! You were born in {birth_year}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
