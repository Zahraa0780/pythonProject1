import random

def heita_noppaa():
    return random.randint(1, 6)

def main():
    while True:
        silmaluku = heita_noppaa()
        print("Heitto:", silmaluku)
        if silmaluku == 6:
            print("Kuutonen! Heitto lopetetaan.")
            break


