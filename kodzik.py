import requests
import time

KLUCZ_API = "TWOJ_KLUCZ_API_YOUTUBE"
ID_KANALU = "ID_TWOJEGO_KANALU"
INTERWAL_SPRAWDZANIA = 60

URL_API = (
    f"https://www.googleapis.com/youtube/v3/search?key={KLUCZ_API}"
    f"&channelId={ID_KANALU}&part=snippet,id&order=date&maxResults=1"
)

def sprawdz_nowy_film(ostatni_id_filmu):
    odpowiedz = requests.get(URL_API)
    if odpowiedz.status_code != 200:
        print(f"Błąd: {odpowiedz.status_code}, {odpowiedz.text}")
        return ostatni_id_filmu

    dane = odpowiedz.json()
    if "items" not in dane or not dane["items"]:
        print("Brak wyników. Sprawdź ID kanału lub klucz API.")
        return ostatni_id_filmu

    najnowszy_film = dane["items"][0]
    id_filmu = najnowszy_film["id"].get("videoId")

    if not id_filmu:
        print("Nie znaleziono nowego filmu.")
        return ostatni_id_filmu

    if id_filmu != ostatni_id_filmu:
        tytul_filmu = najnowszy_film["snippet"]["title"]
        link_filmu = f"https://www.youtube.com/watch?v={id_filmu}"
        print(f"Nowy film: {tytul_filmu}\nLink: {link_filmu}")
        return id_filmu

    return ostatni_id_filmu

def monitoruj_kanal():
    ostatni_id_filmu = None
    print("Rozpoczęto monitorowanie kanału...")
    while True:
        ostatni_id_filmu = sprawdz_nowy_film(ostatni_id_filmu)
        time.sleep(INTERWAL_SPRAWDZANIA)

if __name__ == "__main__":
    monitoruj_kanal()
