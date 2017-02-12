#!/usr/local/bin/python3
# -*-coding:Utf-8 -*

def estBissextile(annee):
  if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("Année bissextile !")
  else:
    print("Année non bissextile.")
    
if __name__ == "__main__":
  annee = input("Saisissez une année : ")
  try:
    annee = int(annee)
    assert annee > 0
    estBissextile(annee)
    input("Appuyez sur la touche ENTREE pour continuer...")
  except ValueError:
    print("Merci de saisir un nombre.")
  except AssertionError:
    print("Merci de saisir une année positive.")
  
