# Feedback für AutoCommit
https://github.com/Justus2004/Auto-Commit-PG1

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung.
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->
Die While-Schleife wurde verstanden, wie die Überprüfung funktioniert und wie man aus ihr ausbrechen kann, siehe [access_random_website](https://github.com/Justus2004/Auto-Commit-PG1/commentOnGit.py)

Funktionen werden verwendet, um Code aufzuteilen und können richtig aufgerufen werden. [main](https://github.com/Justus2004/Auto-Commit-PG1/main_script.py)

Sie haben an mehreren Stellen If- und Else-Statements verwendet.


## Sie können die Syntax und Semantik von Python
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
Verwenden des With-Statements um Dateien zu öffnen und Auszulesen [save_code_to_file](https://github.com/Justus2004/Auto-Commit-PG1/clipboard_extractor.py)

    with open(handle) as file: 

Verwenden von verschiedenen String Escapes und Sequenzpräfixen wie **r (raw)** und **f (format)**

## Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden.
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

Verwenden von Listen als Inline-Parameter für Funktionsaufrufe [create_and_push_commit_file](https://github.com/Justus2004/Auto-Commit-PG1/push_idea.py)

Für das Laden der Git-URLs und die dazugehörigen Namen wird ein Dictionary verwendet, um dem Repository einen Namen zuzuordnen, [load_urls_and_names](https://github.com/Justus2004/Auto-Commit-PG1/commentOnGit.py).

## Weiteres Feedback für die Zukunft:
1. Einheitlicher Namensstil für Funktionen, hier wurde zwischen Snake- und Camel-Case beliebig gewechselt.

2. Entfernen von auskommentiertem Code, wenn man den nach dem Commit noch bräuchte, kann man ihn aus der Commit-History wieder herstellen. So würde der Code lesbarer werden.

3. Verwenden von Konfigurationsdateien, um Repositories und Namen zu Pflegen, anstelle von Hart codierten Werten, macht das Ganze flexibler und besser zu lesen.