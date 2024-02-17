import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

from Features import FeatureColumns
from sklearn.model_selection import train_test_split


def loadData():
    data_path = 'train_with_feature.csv'
    data = pd.read_csv(data_path, sep=",")
    data_cleaned = data.dropna()
    sample_size = 20000
    data_cleaned = data_cleaned.sample(n=sample_size, random_state=42)


    feature_columns = [feature.value for feature in FeatureColumns]
    target_column = 'Category'

    categorical_features = [col for col in feature_columns if data_cleaned[col].dtype == 'object']
    numerical_features = [col for col in feature_columns if col not in categorical_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numerical_features),
            ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_features)
        ]
    )

    X = data_cleaned[feature_columns]
    y = data_cleaned[target_column]

    # Anwenden des Preprocessors
    X_processed = preprocessor.fit_transform(X)
    encoded_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)

    all_feature_names = np.concatenate([numerical_features, encoded_feature_names])
    X_final = pd.DataFrame(X_processed, columns=all_feature_names)


    # Aufteilung von Daten für Training und Test

    # Stratified Sampling ist eine Technik, die sicherstellt, dass die Stichproben,
    # die für das Training und Testen von maschinellen Lernmodellen verwendet werden,
    # die gleiche Verteilung der Klassen(oder eines anderen wichtigen Merkmals) aufweisen
    # wie der gesamte Datensatz.
    # Diese Methode ist besonders nützlich bei ungleichmäßig verteilten Klassen,
    # um Verzerrungen in den Trainings - und Testergebnissen zu vermeiden.
    # In Python wird Stratified Sampling häufig mit der Bibliothek Scikit - learn durchgeführt,
    # speziell mit der Funktion train_test_split, die ein Argument stratify akzeptiert.
    # Hier ist ein einfaches Beispiel, wie man Stratified Sampling für einen Datensatz durchführt,
    # wobei angenommen wird, dass Sie bereits NumPy, pandas, oder ähnliche Bibliotheken für die Datenmanipulation und Scikit - learn installiert haben:
    X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2, stratify=y, random_state=42)
    label_encoder = LabelEncoder()

    label_encoder.fit(y_train)
    # y_test = label_encoder.transform(y_test)
    y_train = label_encoder.transform(y_train)
    y_test = label_encoder.transform(y_test)

    return X_train, X_test, y_train, y_test, data_cleaned, feature_columns, categorical_features, target_column
