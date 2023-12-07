# SF-CrimePredict
SF-CrimePredict" prognostiziert Verbrechen in San Francisco, fokussiert auf Larceny, Assault, Drug, Vehicle Theft, Burglary. Der Ansatz umfasst deskriptive Datenanalyse, Merkmalsdefinition, Klassifikationsmodellierung mit Evaluierung und Vergleich. Ein klares, präzises Jupyter Notebook dokumentiert den Prozess
# Projekt-Anforderungs-Checkliste für Regression
* **Deskriptive Datenanalyse**
 - [ ] Eine deskriptive Analyse der Daten sollte durchgeführt werden.
   - [x] Die Daten hinsichtlich der Datentypen analysieren
   - [x] Die Daten hinsichtlich der Wertebereiche analysieren
   - [x] Die Daten hinsichtlich fehlender Werte untersuchen
   - [ ] Die Daten hinsichtlich inkorrekter Werte untersuchen
 - [ ] Visualisierung der Daten:
   - [ ] Crime per Month
   - [ ] Crime per Year
   - [ ] Crime hotspot on worldmap (wenn möglich)
 - [ ] Es sollten Korrelationen zwischen den Merkmalen (Spalten) identifiziert werden.
   - [ ] Visualisierungen der Korrelationen erstellen.
 - [ ] Erkenntnisse aus der deskriptiven Analyse zum Problem.
   - [ ] Zusammenfassung

  - **Modell 1: Gradient Boosting XGBoost**
    - [ ] Anwendung des ersten Regressionsmodells.
    - [ ] Kreuzvalidierung zur Optimierung der Hyperparameter.
    - [ ] Evaluation der Modellqualität mit sinnvollen Metriken.

  - **Modell 2: Random Forest Classifier**
    - [ ] Anwendung des zweiten Regressionsmodells.
    - [ ] Kreuzvalidierung zur Optimierung der Hyperparameter.
    - [ ] Evaluation der Modellqualität mit sinnvollen Metriken.

  - **Modell 3: Support Vector Machine**
    - [ ] Anwendung des dritten Regressionsmodells.
    - [ ] Kreuzvalidierung zur Optimierung der Hyperparameter.
    - [ ] Evaluation der Modellqualität mit sinnvollen Metriken.

## Vergleich der Ergebnisse
- [ ] Vergleichen der Ergebnisse der drei Regressionsmodelle.
  - [ ] Messung der Güte
  - [ ] AUC
  - [ ] ...
