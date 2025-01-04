# Instrukcja obsługi skryptu monitorującego kanał YouTube i dodającego komentarze

## Wymagania
1. **Python 3.9 lub nowszy**
2. Zainstalowane biblioteki Python:
   - `google-auth`
   - `google-auth-oauthlib`
   - `google-auth-httplib2`
   - `google-api-python-client`
   - `requests`
3. Konto Google z dostępem do YouTube.
4. Klucz API oraz poświadczenia OAuth 2.0 wygenerowane w konsoli Google Cloud.

---

## Kroki instalacji

### 1. Pobranie i instalacja bibliotek
Zainstaluj wymagane biblioteki Python za pomocą programu "instalator.bat"

### 2. Utworzenie projektu w Google Cloud
1. Wejdź na stronę [Google Cloud Console](https://console.cloud.google.com/).
2. Utwórz nowy projekt.
3. Włącz API **YouTube Data API v3** dla projektu.
4. Przejdź do sekcji "Poświadczenia" i utwórz:
   - Klucz API (zapisz go w zmiennej `KLUCZ_API` w skrypcie).
   - Poświadczenia OAuth 2.0 (plik JSON, nazwij go `client_secrets.json`).

### 3. Skopiowanie pliku poświadczeń
Umieść plik `client_secrets.json` w tym samym folderze, co skrypt.

---

## Konfiguracja skryptu

### 1. Edycja zmiennych w skrypcie
Otwórz skrypt i uzupełnij następujące zmienne:
- `KLUCZ_API`: Twój klucz API.
- `ID_KANALU`: ID kanału YouTube, który chcesz monitorować.
- `TEKST_KOMENTARZA`: Treść komentarza, który ma być dodawany.
- `INTERWAL_SPRAWDZANIA`: Czas w sekundach między kolejnymi sprawdzeniami (np. 60).

### 2. Uruchomienie skryptu
Uruchom skrypt w terminalu (CMD) za pomocą polecenia:

python nazwa_skryptu.py


Podczas pierwszego uruchomienia zostaniesz poproszony o zalogowanie się na konto Google, aby autoryzować działanie skryptu. Po pomyślnej autoryzacji dane zostaną zapisane w pliku `token.json`.

---

## Jak działa skrypt
1. Skrypt sprawdza najnowsze filmy na wskazanym kanale co określony czas (domyślnie 60 sekund).
2. Jeśli wykryje nowy film, automatycznie dodaje komentarz o ustalonej treści.
3. Skrypt działa w nieskończonej pętli, monitorując kanał.

---

## Uwagi
- Upewnij się, że Twoje komentarze są zgodne z zasadami YouTube, aby uniknąć zablokowania konta.
- Token dostępu OAuth 2.0 wygasa po pewnym czasie. Skrypt automatycznie odświeża token, jeśli to konieczne.
- Używaj tego skryptu wyłącznie na swoim koncie lub za zgodą właściciela kanału.

---

## Rozwiązywanie problemów

### Problem: "Błąd podczas pobierania danych"
- Sprawdź, czy Twój klucz API jest poprawny i aktywny.
- Upewnij się, że ID kanału jest poprawne.

### Problem: "Błąd podczas dodawania komentarza"
- Sprawdź, czy token OAuth 2.0 jest ważny (plik `token.json`).
- Upewnij się, że konto Google ma uprawnienia do komentowania.

### Problem: Skrypt nie wykrywa nowych filmów
- Upewnij się, że kanał faktycznie opublikował nowy film.
- Zwiększ wartość `INTERWAL_SPRAWDZANIA`, aby uniknąć limitów API.

---

## Licencja
Skrypt jest dostarczony "tak jak jest" i może być wykorzystywany wyłącznie w celach edukacyjnych lub prywatnych.

