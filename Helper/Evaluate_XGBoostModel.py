from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score


def evaluate_xgb_model(X_train, y_train, X_test, y_test, best_params=None):
    if best_params is None:
        best_params = {}

    xgb_clf = XGBClassifier(**best_params, objective="multi:softprob", use_label_encoder=False,
                                 eval_metric='mlogloss')
    xgb_clf.fit(X_train, y_train)
    y_pred = xgb_clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    roc_auc = roc_auc_score(y_test, xgb_clf.predict_proba(X_test), multi_class='ovo', average='weighted')

    return xgb_clf, accuracy, f1, roc_auc, y_pred
