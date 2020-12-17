# Technical stuff


## About
Team: Fitness-Plattform, Gruppe mit Diana Schilling, Vincent Rottloff und Veronika Kustermann
Technologie: Django
Thema: Fitness-Plattform

Trainer können auf einer Plattform Profile erstellen, Material hochladen und Benutzer (gegen Bezahlung) freischalten. Benutzer können sich auch ein Profil erstellen, nach Angeboten suchen und sich Trainingspläne zusammenstellen.

Basis:
* Trainer können ein Profil erstellen mit Feldern wie
	* Sportart
	* Ort
	* Kontaktdaten
	* …
* Trainer können in ihrem Profil PDFs und Videos hochladen
* Alle Trainer werden in einer Liste angezeigt
* Benutzer können (ohne Profil) in der Liste filtern (nach zB Sportart)
* es gibt eine Detailansicht der Trainer und Benutzer können alle Materialien und Kontaktdaten der Trainer sehen

Erweiterungen (optional):
* Benutzer können sich Profile erstellen
* Trainer können den Zugriff auf Materialien beschränken
* Benutzer mit Profil können dem Trainer eine Anfrage schicken, um Zugriff auf die Materialien zu bekommen
* Trainer können Benutzer für ihre Materialien freischalten (Adminoberfläche für Trainer)
* Trainer können in ihrem Profil “Trainingspläne” erstellen und Bilder mit Beschreibungen hochladen, die dann der Reihe nach angezeigt werden
* Benutzer können Trainer Nachrichten schicken (und umgekehrt)
* Benutzer können sich Trainingspläne erstellen
* Implementierung von Zahlungsmöglichkeiten und automatischer Freischaltung von Trainingsangeboten