import requests

API_AVAIN = "951e6e21d8d3a65becbbca18b3fdaa4e"

def hae_saa(paikkakunta):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&lang=fi&appid={API_AVAIN}"
    try:
        vastaus = requests.get(url)
        vastaus.raise_for_status()
        json_vastaus = vastaus.json()
        kuvaus = json_vastaus["weather"][0]["description"]
        lämpötila_kelvin = json_vastaus["main"]["temp"]
        lämpötila_celsius = lämpötila_kelvin - 273.15
        return kuvaus, lämpötila_celsius
    except requests.exceptions.RequestException as e:
        print("Virhe:", e)
        return None, None

def main():
    paikkakunta = input("Anna paikkakunnan nimi: ")
    kuvaus, lämpötila = hae_saa(paikkakunta)
    if kuvaus is not None and lämpötila is not None:
        print(f"Sää paikkakunnalla {paikkakunta}:")
        print("Kuvaus:", kuvaus)
        print("Lämpötila:", round(lämpötila, 1), "Celsius-astetta")
    else:
        print("Sään hakeminen epäonnistui.")

if __name__ == "__main__":
    main()
