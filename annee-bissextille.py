#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

annee = input("Saisissez une année : ")

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
  print("Année bissextile !")
else:
  print("Année  non bissextile.")