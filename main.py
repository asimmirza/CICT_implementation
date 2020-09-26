

import os
import subprocess

print("Welcome to CI-CT Application \n\n")
while True:
    print("CI-CT Option:")
    print("1. Test Data")
    print("2. Pipeline")
    ip = int(input("Please Enter your choice:"))
    if ip==1 or ip==2:
        break
    else:
        print("INVALID CHOICE")
