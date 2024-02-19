from sklearn.model_selection import cross_validate
import numpy as np


def perform_cross_validation(model, X_train, y_train, cv=4, scoring=None):
    if scoring is None:
        scoring = {
            'accuracy': 'accuracy',
            'f1_macro': 'f1_macro',
            'roc_auc_ovr': 'roc_auc_ovr'
        }

    cv_results = cross_validate(model, X_train, y_train, cv=cv, scoring=scoring, return_train_score=True)

    results = {}
    for metric in scoring.keys():
        test_metric_key = f'test_{metric}'
        train_metric_key = f'train_{metric}'
        results[f'Average {metric}'] = np.mean(cv_results[test_metric_key]) * 100
        results[f'Standard deviation {metric}'] = np.std(cv_results[test_metric_key]) * 100
        results[f'Difference in std between train and test {metric}'] = (np.std(cv_results[train_metric_key]) - np.std(
            cv_results[test_metric_key])) * 100

    return results