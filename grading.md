<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->
Auch wenn der [X-SVG-Parser](/src/Framework/XsvgParser.py) eine Klasse ist, sind dennoch einige prozedurale Elemente wie
* Schleifen
* If-Bedingungen
* Switch (match) Case

verwendet worden

Für die Verwendung von Prozeduralen-ansätzen ist die [Pipeline](/src/Framework/Pipeline.py) bzw. der dazugehörige [Builder](/src/Framework/PiplineBuilder.py) ein Beispiel, auch wenn diese ebenfalls in Klassen gekapselt sind, ist der Aufbau und Aufrufen dennoch rein prozedural.

# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
Hier kommt wieder als Beispiel der [X-SVG-Parser](/src/Framework/XsvgParser.py), da hier Typenannotationen, Funktionen, Klassen und weitere Sprachfunktionen von Python verwendet wurden.


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
Ich habe zu Beginn des Projekts mithilfe von draw.io eine Architektur entwickelt. Im Anschluss habe ich mich auf die Suche nach Paketen gemacht, die mir bei der Entwicklung des Projekts helfen können. Danach habe ich mich an die Programmierung gesetzt. Zuletzt habe ich auf Funktionsfähigkeit geprüft, allerdings ohne automatische Tests.

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
Verwendung von Dictionaries mit Enums, um Datenfelder durch die [Pipeline](/src/Framework/Pipeline.py) zu propagieren. Ein weiteres Beispiel ist die Verwendung von Callables im [Pipeline-Builder](/src/Framework/PiplineBuilder.py) um Funktionsstrukturen vorzugeben.

    
## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden, um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->

* ![VS-Code](/docs/VSCode.png)

* ![GIT](/docs/Git.png)

* ![Draw-IO](/docs/DrawIO.png)
Für die Planung der Architektur habe ich die Draw.io Integration für VS-Code verwendet.




## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Ich habe mir bei der Gruppe TowerDefense Hilfe geholt, um ein Paket zu finden, mit dem ich die Software LED-Matrix darstellen kann. Sie haben mir dann PyGame empfohlen, weil es einfach zu verwenden ist und viele Funktionen bietet.
![Nachricht](/docs/Nachricht.png)


# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
Ich habe der Gruppe [AutoCommit](https://github.com/Justus2004/Auto-Commit-PG1/) in dem [Dokument](/feedbackAutoCommit.md) Feedback gegeben.

# Sie können sich selbständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->

Ich habe außer den im Unterricht gelernten noch folgende Technologien eingesetzt:
* DeepFace
* Open-CV
* PyGame
* Fast-API


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
Ich finde die Implementierung der für das Erzeugen des Bildes recht elegant. Ich würde aber in Zukunft die Pipeline objektorientiert mithilfe von Interfaces programmieren, um einige der Probleme, welche ich mit globalen Daten hatte, zu vermeiden und um die Informationen besser an den Verwendungszweck zu binden.

![Pipeline](/docs/Pipeline.drawio.svg) 


## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen


