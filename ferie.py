#!/usr/bin/env python
# -*- coding: utf-8 -*-

# file      : ferie.py
# purpose   : calculating the vacation plans for businesses with shift workers.
#
# author     Stefan Johansson
# date      : 2019/02/XX
# version   : v0.0.1
#
# changelog  :

"""
    ferie.py - Calculating vacation for shift workers

    This module requires ...
    See ... for support.
"""

# Import the modules

import os
import time
import sys
import json
import math

reload(sys)
sys.setdefaultencoding('utf-8')

empReg = {}
emp_reg_file = 'ansattregister.txt'

class Employee:
    def __init__(self, name, team):
        self.name = name
        self.team = str(team)

    def printEmp(self):
        print("Navn: " + self.name)
        print("Lag: " + self.team)

def openReg():
    if os.path.isfile(emp_reg_file) == True:
        with open(emp_reg_file) as raw_data:
            for item in raw_data:
                if ':' in item:
                    empNr, namn, lag  = item.split(':', 2)
                    empReg[empNr] = Employee(namn, lag)
                else:
                    pass
    else:
        pass

def saveReg(empNr, navn, team):
    with open(emp_reg_file, 'a') as f:
        f.write('%s:%s:%s\n' % (empNr, navn, team))

def addEmp(ansatt):
    print("===== LEGG TIL ANSATT =====")
    navn = raw_input("Navn: ")
    lag = raw_input("Lag: ")
    saveReg(ansatt, navn, lag)

def delEmp(ansatt):
    print("===== SLETT ANSATT =====")
    slette = raw_input("Er du sikker på at du ønsker å slette " + str(empReg[ansatt].printEmp()) +"? (y/n) ").lower()
    if slette == 'y':
        raw_data = open(emp_reg_file, 'r+')
        d = raw_data.readlines()
        raw_data.seek(0)
        for item in d:
            if not ansatt in item:
                raw_data.write(item)
        raw_data.truncate()
        raw_data.close()
        empReg[ansatt] = ""
    else:
        pass


def checkEmpNr(nummer):
    if empReg.get(nummer):
        if empReg[nummer] <> "":
            return True
        else:
            return False
    else:
        return False

def locate(user_string, x=0, y=0):
    x = int(x)
    y = int(y)
    if x >= 255:
        x = 255
    if y >= 255:
        y = 255
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0
    HORIZ = str(x)
    VERT = str(y)
    print('\033[' + VERT + ';' + HORIZ + 'f' + user_string)

def menu():
    a = 0    
    while a <> "q":
        clrScr()
        height, width = os.popen('stty size', 'r').read().split()
        user_string = '-= FERIEBEREGNEREN =-'
        str_len = len(user_string)
        corr_width = int(width) - str_len
        locate(user_string, corr_width, 0)
        choice = raw_input("Ønsker du legge till, printe eller ta bort ansatt?\n(a, p, d, q)? ")
        if choice == "p":
            nummer = raw_input("Ansattnummer: ")
            if checkEmpNr(nummer):
                openReg()
                empReg[nummer].printEmp()
                raw_input("")
            else:
                print("Ingen ansatt med det ansattnummeret ...")
                raw_input("")
        elif choice == "a":
            nummer = raw_input("Ansattnummer: ").lower()
            if not checkEmpNr(nummer):
                empReg[nummer] = nummer 
                addEmp(nummer)
            else:  
                print("Allerede en ansatt med det ansattnummeret ...")
                raw_input("")
        elif choice == "q":
            exit()
        elif choice == "d":
            nummer = raw_input("Ansattnummer: ").lower()
            if checkEmpNr(nummer):
                openReg()
                delEmp(nummer) 
            else:
                print(empReg)
                print("Ingen ansatt med det ansattnummeret ...")
                raw_input("")
        else:
            pass

def clrScr():
    for n in range(0, 64, 1): print('\r\n')

def main():
    clrScr()
    empReg = openReg()
    menu()

main()

