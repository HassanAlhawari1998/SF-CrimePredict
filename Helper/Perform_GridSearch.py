from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

def perform_grid_search(X_train, y_train):
    param_grid = {
        'max_depth': [3, 4, 5],
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [100, 200, 300],
        'subsample': [0.8, 0.9, 1.0]
    }

    xgb_clf = XGBClassifier()
    grid_search = GridSearchCV(estimator=xgb_clf, param_grid=param_grid, scoring='accuracy', cv=4, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    best_accuracy = grid_search.best_score_ * 100

    return best_params, best_accuracy