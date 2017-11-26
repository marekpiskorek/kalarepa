## KALAREPA

Narzędzie do pobierania w prosty sposób informacji o ofertach pracy w IT i (potencjalnie) automatycznego ich parsowania, unifikujące wiele źródeł o różnych formach do ujdnoliconej postaci.

### Założenia początkowe projektu:
* projekt wykonuję pod siebie i swoje potrzeby, ale wszelkie uwagi osób zainteresowanych są mile widziane
* ustawienia:
    * miasto: Warszawa albo praca zdalna
    * technologia: Python
    * zakres: backend

### Gryplan (a.k.a. backlog):
* Przygotowanie scraperów do stron z detalami ofert dla przygotowanych stron
* Postawienie instancji MongoDB
* Zapisywanie ofert do Mongo w lekko ujednoliconej postaci
* Opakowanie całości w lekką aplikację (flask albo django)
* Przygotowanie widoków RESTowych pozwalających na filtrowanie i listowanie wyników
* Wywoływanie scraperów w CRONie (np. django celery beat) raz dziennie

### Źródła:

* nofluffjobs.com
* justjoin.it
* 4programmers.net

#### W planach:

* pracuj.pl
* stackoverflow.com/jobs
* careerjet.pl (generator linków do ofert pracy z wielu źródeł)
* python.org/jobs/location/telecommute/
* remotepython.com/
* remoteok.io/remote-python-jobs
* indeed.com/jobs?q=remote+python&sort=date

#### Odrzucone pomysły:

* LinkedIn [1]
* sii.pl [2]

[1] Ich zabezpieczenia przed crawlowaniem są zniechęcające a same oferty często słabo dobrane (dla ustalonych jasno preferencji "Warszawa, Python" dostaję oferty dla programisty Java w Krakowie).

[2] Brak znalezionych ofert dla słów kluczowych Python, Warszawa, wszystkich ofert (we wszystkich kategoriach) 207, czyli dość mała baza.
