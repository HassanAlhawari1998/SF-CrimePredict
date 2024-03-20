from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier


def evaluate_rf_model(X_train, y_train, X_test, y_test, best_params=None):
    if best_params is None:
        best_params = {}

    rf_clf = RandomForestClassifier(**best_params, random_state=42)

    rf_clf.fit(X_train, y_train)
    y_pred = rf_clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    roc_auc = roc_auc_score(y_test, rf_clf.predict_proba(X_test), multi_class='ovo', average='weighted')

    return rf_clf, accuracy, f1, roc_auc
