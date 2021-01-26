# Technisches

## Projektstruktur
Die Projekstruktur orientiert sich an https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files. 

## Genutzte packages
* django-allauth (Userregistrierung und Authentifizierung, Social Login)
* django-bootstrap4 (Bootstrap Styling)
* django-filters (Filter für die Trainerliste)
* environ (Environment Variables für Development und Production)
* siteflags (Favorisieren von Trainern)

Außerdem packages für die lokale MySQL-Datenbank und dependencies.

## Development
Vor dem Starten des Servers muss `libmagic` auf dem System installiert sein.
Linux: `$ sudo apt-get install libmagic1`
Mac: `brew install libmagic`
Windows: `pip install python-magic-bin`
Siehe auch https://pypi.org/project/python-magic/.

Der Server kann lokal mit `python manage.py runserver` gestartet werden.
Die Website ist erreichbar unter `http://127.0.0.1:8000`. Das ist wichtig, wenn man das Social Login verwendet, sonst gibt es Probleme mit der redirect-URI. Ohne Social Login, kann die Website auch mit `localhost:8000` aufgerufen werden.
Damit die Entwicklungsumgebung optimal läuft, eine Datei `.env` im `fitnessplatform`-Verzeichnis erstellen und die Variablen aus der `.env.example` kopieren. Für die Ausgabe von Fehlermeldungen `DEBUG=True` setzen.

### Tests
Tests können einfach mit `python manage.py test <app name>` ausgeführt werden.


### Verbindung zu einer lokalen Datenbank:
* Zugangsdaten müssen als Umgebungsvariabeln hinterlegt werden 
* dazu die Datei `fitnessplatform/.env` nach Vorlage von `.env.example` erstellen und die Variablen entsprechend anpassen

### Mails
Für lokales Development werden Emails direkt über die Konsole ausgegeben.
Dafür können die Variablen aus der `.env.example` ins lokale `.env`-file übernommen werden.

### Social Login
Eigene OAuth Github App erstellen für Trainhorizon local:
* in Github Developer Settings neue OAuth App erstellen: https://github.com/settings/developers
  * Application name: Trainhorizon
  * Homepage URL: `http://127.0.0.1:8000/`
  * Authorization callback URL: `http://127.0.0.1:8000/accounts/github/login/callback/`
* Client secret generieren und dieses zusammen mit der Client ID dem o.g. 'Social application'-Objekt im Trainhorizon Admin-Bereich übergeben

Achtung! Die Website muss unter `http://127.0.0.1:8000/` aufgerufen werden, sonst gibt es Fehler mit der Redirect-URI von GitHub.

Konfiguration im Admin-Bereich
* in Admin-Bereich einloggen und Domain name der Site in `http://127.0.0.1:8000` ändern (Displayname kann frei gewählt werden)
* im Admin-Bereich neues 'Social application' - Objekt anlegen
  * Provider: GitHub
  * Name: GitHub
  * client id und secret key angeben
  * Sites: `http://127.0.0.1:8000` zu chosen sites hinzufügen


## Production
Die Website ist erreichbar unter `https://trainhorizon.eu.pythonanywhere.com`.

### Mails
Die Mails auf Production laufen über `smtp.gmail.com`.

### Social Login
Die Zugangsdaten für GitHub sind im Adminbereich auf Production konfiguriert.


# Was ist die Fitnessplattform "Trainhorizon"?
Trainhorizon ist eine Fitnessplatform, auf der sich Trainer registrieren und darstellen können, inklusive Upload von zB PDFs und Videos. Auch normale Benutzer können sich registrieren und Trainer favorisieren.
Die Website besteht aus einer Startseite, einer Listenansicht aller registrierten Trainer mit öffentlichem Profil und den jeweiligen Trainerprofilen. Außerdem gibt es für registrierte Benutzer, die keine Trainer sind, einen Bereich, in dem ihre favorisierten Trainer angezeigt werden.

## Registrierung und Login
Über einen Link im Header (`/accounts/signup/`) können sich Benutzer registrieren. Es gibt folgende Möglichkeiten:
* Registrierung über das Formular als normaler Benutzer
* Registrierung über das Formular als Trainer
* Social Login mit GitHub als normaler Benutzer
* Social Login mit GitHub als Trainer

Nach der Registrierung wird eine Email verschickt, in der ein Bestätigungslink ist. Erst wenn die Email-Adresse bestätigt wurde, können sich neuregistrierte Benutzer einloggen.
Der Login ist auch über den Header erreichbar (`/accounts/login/`).

## Benutzereinstellungen
Sobald sich ein Benutzer, egal ob Trainer oder normaler Benutzer, eingeloggt hat, wird im Header ein Avatar für den Benutzer angezeigt. Mit Klick auf diesen ist ein Benutzermenü verfügbar.
Der aktive Link ist immer entsprechend eingefärbt.

### Your settings
Der Benutzer kann hier seine Daten ändern. Email-Adresse und Benutzername müssen allerdings unique sein, hier gibt es entsprechende Fehlermeldungen, wenn die eingebenen Daten schon existieren.
Außerdem kann der Benutzer ein Avatarbild hochladen. Dieses Bild wird im Ordner `/media/user_<user_id>/avatar` abgelegt. Sobald ein bestehendes Avatarbild durch ein neues ersetzt wird, wird das bestehende aus dem Ordner gelöscht (auch wenn vorher ein .png-Bild hochgeladen wurde und das neue ein .jpg-Bild ist). Dadurch wird sichergestellt, dass es keinen Datenmüll gibt. Das hochgeladene Avatarbild wird im Header für eingeloggte Benutzer angezeigt. Bei Trainern ist es zudem das Profilbild für die Trainerprofile.
Über einen Reiter kommt man zu den Password-Settings, in denen man das Passwort ändern kann. Wurde das User-Profil via Social Login erstellt, so ist für den entsprechenden User kein Passwort gesetzt, da der Login über Github authentifiziert wird. Dem User steht aber frei, hier ein Passwort zu hinterlegen und damit zusätzlich zum Social Login den normalen Login mit Username und Passwort zu aktivieren.

### Your favorite trainers (nur für normale Benutzer)
Hier wird für normale Benutzer eine Liste an Trainern angezeigt, die von dem entsprechenden Benutzer favorisiert wurden. Trainer, die ihr Profil nicht öffentlich geschaltet haben, werden nicht angezeigt. Über einen Button kommt man zum Trainerprofil, über einen anderen Button kann man den Trainer schnell wieder entfavorisieren.
Wenn ein Benutzer keine Trainer favorisiert hat, wird eine Meldung mit Link zur Trainerliste angezeigt.

### Your trainer profile (nur für Trainer)
Hier wird das Profil des eingeloggten Trainers angezeigt, so wie es auch andere Benutzer sehen würden. Allerdings sehen Trainer, die ihr eigenes Profil betrachten, zusätzlich den Edit Button. 
Wenn das Profil auf invisible gesetzt wurde, wird hier für den Trainer, dem das Profil gehört, eine Warnung angezeigt. Für andere Benutzer ist dieses Profil dann nicht sichtbar.

Wenn ein Trainer noch kein Profil angelegt hat, dann sieht er hier die entsprechende Meldung mit einem Button, um ein Profil zu erstellen. Diese Meldung wird nur für den Trainer angezeigt, dem das Profil gehört.

#### Trainer profile edit form
Wenn ein Trainer auf den Edit- oder Create-Button klickt, dann kann er sein Trainerprofil editieren (oder ein neues anlegen).
Es kann die Sportart und ein Motto angegeben werden. In dem About-Textfeld kann der Trainer über sich schreiben, auch Zeilenumbrüche werden richtig dargestellt.
Die Checkox "visible" bestimmt, ob das Profil für andere Benutzer (oder anonyme Besucher) sichtbar ist.
Über den Reiter kommt der Trainer zu Locations. Hier können die verschiedenen Orte angegeben werden, an denen der Trainer seine Kurse anbietet. Bestehende Orte können hier auch gelöscht werden.
Weiter gibt es den Reiter Uploads. Hier kann der Trainer verschiedene Dateien wie PDFs oder Videos hochladen (oder auch wieder löschen). Diese werden dann in seinem öffentlichen Trainerprofil angezeigt. Diese werden dann in seinem öffentlichen Trainerprofil angezeigt. Die erlaubten Dateien sind auf ausgewählte Formate von maximal 2MB beschränkt.
Die Uploads werden später nach Titel geordnet angezeigt, der Trainer hat also durch die Vergabe des Titels die Möglichkeit, die Reihenfolge seiner Uploads zu bestimmen.
Wenn ein Trainer noch kein Profil angelegt hat, dann sind die Links "Locations" und "Uploads" nicht aktiv und eine Warnung wird angezeigt. Erst wenn das Profil das erste Mal gespeichert und somit angelegt wurde, kann ein Trainer Orte und Uploads zu seinem Profil hinzugügen.

### Logout
Sobald hier geklickt wird, wird der Benutzer sofort ausgeloggt. Die allauth-Settings wurden angepasst, damit keine extra Bestätigungsseite angezeigt wird.

## Trainerliste
Über die Navigation im Header kommt man zur Trainerliste (`/trainerlist/`). Diese ist für alle Besucher der Seite sichtbar, egal ob eingeloggt oder nicht. Jedoch werden hier nur Trainer gelistet, die ein öffentliches Profil haben.
Über die Filter in der Liste kann man die Anzeige einschränken. Der Filter "Trainer name" sucht den angegebenen Namen (oder Teil des Namens) in den Vor- und Nachnamen aller Trainer. "Sport" schränkt die Suche auf die angegebene Sportart ein, "Location" sucht in den Orten, in denen der Trainer seine Kurse anbietet.
Die Anzahl der Suchresultate wird über der Liste angezeigt.
Über einen Button kommt der Besucher auf das jeweilige Trainerprofil.

## Trainerprofile
Das Trainerprofil zeigt alle Daten für den jeweiligen Trainer. Hier wird das Avatarbild des Trainers und das Motto angezeigt, darunter sieht man, wieviele Benutzer den Trainer favorisiert haben.

Für eingeloggte normale Benutzer (nicht für Trainer oder anonyme Benutzer) wird darunter noch ein Button angezeigt, mit dem ein Trainer favorisiert werden kann. Sobald ein Trainer favorisiert wurde, ändert sich der Button und der eingeloggte normale Benutzer kann den Trainer wieder entfavorisieren. 

Außerdem werden im Trainerprofil natürlich noch die About-Beschreibung und die Orte angezeigt, in denen der Trainer seine Kurse anbietet, sowie die Uploads des Trainers.

Am Ende wird die Sportart des Trainers angezeigt, mit Klick auf diese kommt man zu einer gefilterten Trainerliste mit Trainern, die nur diese Sportart anbieten (und ein öffentliches Profil haben).

Nur wenn der Benutzer, der dieses Profil betrachtet, eingeloggt ist und der Eigentümer des Profils, dann wird unter den Likes noch ein Edit Button angezeigt.

## Admin Bereich
Über `/admin` ist der Administrationsbereich für Superuser erreichbar. Hier können die Benutzer und die Accounts, die über das Social-Login erstellt wurden, verwaltet werden. Außerdem können hier auch Trainerprofile mit den dazugehörigen Daten wie Locations und Uploads vom Administrator angelegt und, wenn nötig, geändert oder gelöscht werden.
Auch die Favorisierungen sind hier sichtbar und können geändert werden.
