# SF-CrimePredict
SF-CrimePredict" prognostiziert Verbrechen in San Francisco, fokussiert auf Larceny, Assault, Drug, Vehicle Theft, Burglary. Der Ansatz umfasst deskriptive Datenanalyse, Merkmalsdefinition, Klassifikationsmodellierung mit Evaluierung und Vergleich. Ein klares, präzises Jupyter Notebook dokumentiert den Prozess
# Projekt-Anforderungs-Checkliste für Regression
* **Deskriptive Datenanalyse**
 - [x] Eine deskriptive Analyse der Daten sollte durchgeführt werden.
   - [x] Die Daten hinsichtlich der Datentypen analysieren
   - [x] Die Daten hinsichtlich der Wertebereiche analysieren
   - [x] Die Daten hinsichtlich fehlender Werte untersuchen
   - [x] Die Daten hinsichtlich inkorrekter Werte untersuchen
 - [x] Visualisierung der Daten:
   - [x] Crime per Month
   - [x] Crime per Year
   - [x] Crime hotspot on worldmap (wenn möglich)
 - [x] Es sollten Korrelationen zwischen den Merkmalen (Spalten) identifiziert werden.
   - [x] Visualisierungen der Korrelationen erstellen.
 - [x] Erkenntnisse aus der deskriptiven Analyse zum Problem.
   - [x] Zusammenfassung

  - **Modell 1: Gradient Boosting XGBoost**
    - [x] Anwendung des ersten Regressionsmodells.
    - [x] Kreuzvalidierung zur Optimierung der Hyperparameter.
    - [x] Evaluation der Modellqualität mit sinnvollen Metriken.
    - [ ] Zusammenfassen der Ergebnisse
          
  - **Modell 2: Random Forest Classifier**
    - [ ] Anwendung des zweiten Regressionsmodells.
    - [ ] Kreuzvalidierung zur Optimierung der Hyperparameter.
    - [ ] Evaluation der Modellqualität mit sinnvollen Metriken.
    - [ ] Zusammenfassen der Ergebnisse

## Vergleich der Ergebnisse
- [ ] Vergleichen der Ergebnisse der drei Regressionsmodelle.
  - [ ] Messung der Güte
  - [ ] AUC
  - [ ] ...
