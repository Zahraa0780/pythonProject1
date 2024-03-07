import mysql.connector

def hae_lentoasemien_tyypit_maakodilla(iso_country):
    sql = f"select  type, count(type)  as count from airport where iso_country ='{iso_country}' group by type;"
    print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user="root",
         password="12345",
         autocommit=True
         )
iso_country = input("Anna maan ISO tunnus: ")
lentoasemien_tyypit = hae_lentoasemien_tyypit_maakodilla(iso_country)
if lentoasemien_tyypit:
   for lentoasemien_tyypi in lentoasemien_tyypit:
      print(f'Tyypi: {lentoasemien_tyypi["type"]} - {lentoasemien_tyypi["count"]} kpl')
else:
    print('koodilla ei löydy kenttä')