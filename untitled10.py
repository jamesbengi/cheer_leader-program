# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:44:57 2021

@author: james
"""
print("welcome to cheer you platform")
an_letters = "qwertyuiAASDFGH"
word=input("enter your name  motherfucker:")
times=int(input("how man times do you want me to call your name(1-10):"))
for char in word:
    if char in an_letters:
        print("give me a"+ char+"!"+ char)
else:
            print("give me a" + char+"!"+char)
            print("let me cheer for you motherfucker !!")
    
for i in range(times):
    print(word)