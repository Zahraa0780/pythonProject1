lentoasemat = {"EFHK" : "helsinki-vantaa lentoasema",
               "LFPG":"Frnce lentoasema",
               "EDDM":"Germany lentoasema",
               "LIRA":"Italy lentoasema",
               "EKCH":"Denmark lentoasema"}
while True:
    päätös = input("""
uusi lentoasema: 
hakea lentoasema: 
lopeta: 
  """)
    if päätös == "uusi":
      koodi = input("Anna ICAO-koodi: ")
      kenttä = input("Anna lentoasema: ")
      if koodi in lentoasemat:
       print("koodi on jo olemassa. ")
      else:
       lentoasemat[koodi] = kenttä
       print("uusi lentokenttä lisätty!")


    elif päätös == "hakea":
        koodi = input("Anna ICAO-koodi: ")
        if koodi in lentoasemat:
         print(f"ICAO-koodi {koodi} on {lentoasemat[koodi]}")
        if koodi not in lentoasemat:
         print("valitettavasti, koodi ei löytää, yritä uudelleen tai lisää sitä. ")
         päätös = input("""
uusi lentoasema: 
hakea lentoasema: 
lopeta: 
""")
    elif päätös == "lopeta":
        break
    else:
        print("Virheellinen valinta.yritä uudellen.")

print("lopettaa")
