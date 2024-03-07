import mysql.connector
def haekentantiedot(icao):
    sql = "select name, municipality from airport where ident ='" +icao+"'";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(rivi)
    return
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='12345',
         autocommit=True
         )


icao = input("Anna haluamasi kentätn ICAO-koodi: ")
haekentantiedot(icao)

if yhteys.is_connected():
    yhteys.close()