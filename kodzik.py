import time
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
PLIK_UWIERZYTELNIANIA = "client_secrets.json"
KLUCZ_API = "TWÓJ_KLUCZ_API"
ID_KANALU = "ID_TWOJEGO_KANALU"
INTERWAL_SPRAWDZANIA = 60
TEKST_KOMENTARZA = "To jest automatyczny komentarz!"

def uzyskaj_usluge_uwierzytelniona():
    poświadczenia = None
    try:
        poświadczenia = Credentials.from_authorized_user_file("token.json", SCOPES)
    except Exception:
        pass
    if not poświadczenia or not poświadczenia.valid:
        if poświadczenia and poświadczenia.expired and poświadczenia.refresh_token:
            poświadczenia.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PLIK_UWIERZYTELNIANIA, SCOPES
            )
            poświadczenia = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(poświadczenia.to_json())
    return poświadczenia

def pobierz_najnowszy_film():
    url = (
        f"https://www.googleapis.com/youtube/v3/search?key={KLUCZ_API}"
        f"&channelId={ID_KANALU}&part=snippet,id&order=date&maxResults=1"
    )
    odpowiedz = requests.get(url)
    if odpowiedz.status_code != 200:
        return None
    dane = odpowiedz.json()
    if "items" in dane and len(dane["items"]) > 0:
        film = dane["items"][0]
        if "videoId" in film["id"]:
            return film["id"]["videoId"]
    return None

def dodaj_komentarz(pozwolenia, id_filmu, tekst_komentarza):
    from googleapiclient.discovery import build
    youtube = build("youtube", "v3", credentials=pozwolenia)
    try:
        zapytanie = youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": id_filmu,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": tekst_komentarza
                        }
                    }
                }
            },
        )
        zapytanie.execute()
    except Exception:
        pass

def monitoruj_kanal():
    pozwolenia = uzyskaj_usluge_uwierzytelniona()
    ostatni_id_filmu = None
    while True:
        id_filmu = pobierz_najnowszy_film()
        if id_filmu and id_filmu != ostatni_id_filmu:
            dodaj_komentarz(pozwolenia, id_filmu, TEKST_KOMENTARZA)
            ostatni_id_filmu = id_filmu
        time.sleep(INTERWAL_SPRAWDZANIA)

if __name__ == "__main__":
    monitoruj_kanal()
