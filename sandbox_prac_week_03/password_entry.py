"""Callum"""
MIN_LENGTH = 4
password = input("Please enter a password:")
while len(password) < MIN_LENGTH:
    password = input("Please enter a password with four or more letters:")
for letters in password:
    print("*", end="")
