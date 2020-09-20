#gits profile --email test --name test

import os
import sys
import subprocess

def gits_set_profile(args):
    """
    Function that prints hello message
    to user console
    """
    print(args.email)
    print("Hello from GITS Commandline Tools-Profile")

    subprocess.call(["git config --global --unset user.name"], shell=True)    
    subprocess.call(["git config --global --unset user.email"], shell=True)

    cmd = "git config --global user.email " + args.email
    print(cmd)
    subprocess.call([cmd], shell=True)

    cmd = "git config --global user.name " + args.name
    print(cmd)
    subprocess.call([cmd], shell=True)
    
    verify_email = subprocess.call(["git config --list | grep \"user.email\""], shell = True)   
    #print(verify_email)

    verify_name = subprocess.call(["git config --list | grep \"user.name\""], shell = True) 
    #print(verify_name)

