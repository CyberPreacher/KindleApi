import os
from lector import KindleCloudReaderAPI

# Zugriff auf Umgebungsvariablen
email = os.getenv("KINDLE_EMAIL")
password = os.getenv("KINDLE_PASSWORD")

# API-Initialisierung
api = KindleCloudReaderAPI(email, password)

# Bibliothek abrufen und aktuellen Lesefortschritt anzeigen
my_library = api.get_library_metadata()
book = my_library[0]
book_progress = api.get_book_progress(book.asin)
_, current_page, last_page = book_progress.page_nums

print("Currently reading %s (Page %d of %d)" % (book.title, current_page, last_page))
