#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# uppgift3.py
# anton johansson
# 2014-12-31
"""
pseudokod
==========
fråga efter resistans
fråga efter spänningen
beräkna effekten
presentera resultet

"""
#main
if __name__=="__main__" : #run directly or imported as a module ?
#get input values
resistance = input(u"ange resistansen i ohm! :")
voltage = input(u"ange spänningen i volt :")

#check (for debug)
#print("Resistansen = {0}, Spänningen = {1}".format(resistance, voltage))
      
#calc power
try:
 power = (float(voltage) ** 2) / float(resistance)

 #present result
 print("Effekten = {0} W".format(power))



except:
    print("det gick inte att utföra beräkningen")



