#!/usr/local/bin/python3
# -*-coding:Utf-8 -*

import random
import math

def jouer(numero, mise):
  gain = 0
  tirage = random.randrange(50)
  print("numéro tiré : ", tirage)
  if tirage == numero:
    gain = mise + mise * 3
  elif tirage % 2 == numero % 2:
    gain = mise + math.ceil(mise / 2)
  return gain

if __name__ == "__main__":
  numero = input("Choisissez un numéro entre 0 et 49 : ")
  mise = input("Choisissez la mise associée au numéro : ")
  try:
    numero = int(numero)
    mise = int(mise)
    assert numero >= 0 and numero <=49
    assert mise >= 0
    gain = jouer(numero, mise)
    print("Vous avez gagné : ")
    print(gain)
  except ValueError:
    print("Merci de saisir un nombre pour le numéro et la mise.")  
  except AssertionError:
    print("Le numéro doit être compris entre 0 et 49 inclu et la mise positive.")