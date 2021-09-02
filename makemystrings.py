#!/bin/python3

import readline

shell = input("Enter your value: ")

n = input("Enter your value: ")

f1 = str(shell)
f2 = int(n)

chunks = [f1[i:i+f2] for i in range(0, len(f1), f2)]
print(chunks)
for thing in chunks:
    print("Str = Str + \"" + str(thing) + "\"")
