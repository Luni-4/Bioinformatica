# Recall --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
# Precision --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
# F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

# AUPRC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
# AUROC ---> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
# Precision-Recall-F-score --> http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support


# cross_val_score parameters

# score --> default value is the same used by the classifier, otherwise you can decide it modifying the score parameter
# cv --> number of k-group used as train/test set
# n_jobs --> if its value is -1, the work load is subdivided on the avaliable CPU

# cross_val_predict parameters
# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict
# It returns the prediction for each example

def metrics(y_true, y_pred):
   # Run SVMs, print their execution time and save in a list the cross-validation scores
    y_pred = [timer(cross_val_predict, x + 1)(c[x], X, Y.getcol(x).toarray().reshape(-1), cv = 5, n_jobs = -1, verbose = 5) for x in range(2)]   

