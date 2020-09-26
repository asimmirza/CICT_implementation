

import os
import subprocess

os.system("clear")
username = subprocess.check_output("whoami",shell=True)
msg = "Hello " + username.decode("ascii")
print("msg")
print("Welcome to CI-CT Application \n\n")
ip =0
while True:
    print("CI-CT Option:")
    print("1. Test Data")
    print("2. Pipeline")
    ip = int(input("Please Enter your choice:"))
    if ip==1 or ip==2:
        break
    else:
        os.system("clear")
        print("INVALID CHOICE \n")


if ip==2:
    while True:
        print("You have choose : pipeline")
        print("1. Create new pipeline")
        print("2. Clone existing pipeline")
        print("3. Run Pipeline")
        ip = int(input("Please Enter your choice:"))
        if ip==1 or ip==2 or ip==3:
            break
        else:
            os.system("clear")
            print("INVALID CHOICE \n")
