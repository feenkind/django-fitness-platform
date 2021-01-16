# Technisches

## Projektstruktur
Die Projekstruktur orientiert sich an https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files. 

## Genutzte packages
* django-allauth
* django-bootstrap4
* django-filters
* environ
* siteflags

## Development
Die Website ist erreichbar unter `http://127.0.0.1:8000`. Das ist wichtig, wenn man das Social Login verwendet, sonst gibt es Probleme mit der redirect-URI. Ohne Social Login, kann die Website auch mit `localhost:8080` aufgerufen werden.
Damit die Entwicklungsumgebung optimal läuft, eine Datei `.env` im `fitnessplatform`-Verzeichnis erstellen und die Variablen aus der `.env.example` kopieren. Für die Ausgabe von Fehlermeldungen `DEBUG=True` setzen.

### Implementierung einer lokalen Datenbank:

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

Achtung! Die Website muss unter `http://127.0.0.1:8000/` sonst gibt es Fehler mit der Redirect-URI von GitHub.

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


# Über die Fitnessplattform
Trainhorizon ist eine Fitnessplatform, auf der sich Trainer registrieren und darstellen können.
Es gibt zudem die Möglichkeit, Besuchern kostenlos Trainingsangebote per PDF und Video zur Verfügung zu stellen.

## Allgemeine Funktionalität
Die Website besteht aus einer Startseite, einer Listenansicht aller registrierten Trainer mit öffentlichem Profil und den jeweiligen Trainerprofilen.
Über den Link im Header kommt der (anonyme oder eingeloggte) Benutzer auf die Übersicht aller Trainer (`/trainerlist/`). Hier werden alle Trainer mit angelegtem Trainerprofil angezeigt und können nach Name, angebotener Sportart und Stadt gefiltert werden.
Durch Klick auf den jeweiligen Trainer kommt man zur Detailansicht des Profils, in dem die Daten des jeweiligen Trainers angezeigt werden:
* Name des Trainers
* Motto des Trainers
* Ort, an dem der Trainer seine Angebote bereitstellt - ein Trainer kann das prinzipiell an mehreren Orten tun
* Allgemeine Informationen über den Trainer und seine Angebote


### Trainer
* Trainer können sich über den Link im Header registrieren (`/user/signup/`). Sobald sich ein Benutzer über die Website registriert hat, wird er in der Datenbank mit der Rolle "trainer" angelegt. Nicht über die Website registrierte Benutzer (wie z.B der superuser) werden mit der Rolle "user" angelegt.
* Registrierte Trainer können sich über den Link im Header einloggen (`/user/login/`). 
* Eingeloggte Benutzer sehen ihr Avatar im Header und haben Zugriff auf eine Benutzernavigation.
  * Der Link "Your settings" führt zu den Profil Settings `/user/` und der Benutzer kann hier seine Daten und sein Passwort ändern. Außerdem kann hier ein Avatarbild hochgeladen werden, das im Header angezeigt wird. Bei jedem neuen Avatarupload wird der alte Avatar automatisch aus dem Filesystem gelöscht.
  * Der Link Logout loggt den aktuellen Benutzer aus.
  * Benutzer mit der Rolle "trainer" sehen zusätzlich den Link "Your trainer profile" (`/trainer/`), der zum Trainerprofil des eingeloggten Trainers führt. Hier kann der Trainer sein öffentliches Profil anlegen und editieren.
* Trainer können ihr Profil sichtbar oder unsichtbar schalten. Hierzu können sie eine Checkbox in ihrem Trainerprofil setzen. Unsichtbare Trainer erscheinen nicht in der Trainerliste und andere Benutzer haben auch keinen Zugriff auf das Trainerprofil.




### Benutzer
Momentan gibt es außer den Trainern nur anonyme Benutzer.
