import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user="root",
         password="12345",
         autocommit=True
         )

def haekentantiedot(icao1, icao2):
    sql = "select latitude_deg, longitude_deg from airport where ident ='" +icao1+"'";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()

    sql = "select latitude_deg, longitude_deg from airport where ident ='" + icao2 + "'";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos2 = kursori.fetchall()

    from geopy.distance import geodesic
    airport1 = tulos1[0]
    airport2 = tulos2[0]
    distance = geodesic(airport1,airport2).km
    print(float(distance))


icao1 = input("Anna ensimmäinen lentokentän ICAO-koodi: ")
icao2 = input("Anna toinen lentokentän ICAO-koodi: ")

haekentantiedot(icao1, icao2)