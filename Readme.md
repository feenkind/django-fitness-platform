# Technisches

## Projektstruktur
Die Projekstruktur orientiert sich an https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files. 

## Genutzte packages
* django-allauth
* django-bootstrap4
* django-environ
* django-filters

## Development
Die Website ist erreichbar unter `localhost:8080`.

### Implementierung einer lokalen Datenbank:

* Zugangsdaten müssen als Umgebungsvariabeln hinterlegt werden 
* dazu die Datei `fitnessplatform/.env` nach Vorlage von `.env.example` erstellen und die Variablen entsprechend anpassen

### Mails
Für lokales Development werden Emails direkt über die Konsole ausgegeben.
Dafür können die Variablen aus der `.env.example` ins lokale `.env`-file übernommen werden.


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




### Benutzer
Momentan gibt es außer den Trainern nur anonyme Benutzer.
