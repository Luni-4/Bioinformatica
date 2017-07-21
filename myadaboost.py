# BaseEstimator ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html
# ClassifierMixin ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np


class AdaBoost(BaseEstimator, ClassifierMixin):
    def __init__(self, n_estimator=10):
        if n_estimator < 1:
            raise ValueError("n_estimator must be greater than 0")
        self.n_estimator = n_estimator
        self.estimators = []
        self.est_weights = []

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        # Encode labels with value between 0 and n_classes-1
        self._enc = LabelEncoder()

        # Y contains the encoded labels
        y = self._enc.fit_transform(y)

        # Number of classes
        if len(self._enc.classes_) != 2:
            raise ValueError("The number of classes must be 2")

        # Map 0 labels as -1
        y[y == 0] = -1

        # Check if X and Y have the same dimension
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y don't have the same dimension\n"
                             "X has %s samples, but y has %s." % (X.shape[0], Y.shape[0]))
        sample_weights = np.ones(X.shape[0]) / X.shape[0]
        while len(self.estimators) <= self.n_estimator:
            weak = DecisionTreeClassifier(max_depth=1)
            weak.fit(X, y, sample_weight=sample_weights)
            errors = np.array([weak.predict(t[0].reshape(1, -1)) != t[1] for t in zip(X, y)])
            # print(errors)
            # print(errors * sample_weights)

            # questo e non dovrebbe essere 1!
            # e = (errors * sample_weights).sum()
            # this should be correct
            e = np.sum([b * sw for b, sw in zip(errors, sample_weights)])

            alpha = 0.5 * np.log((1 - e) / e)
            print('e=%.2f a=%.2f' % (e, alpha))
            w = np.zeros(len(y))
            for i in range(len(y)):
                if errors[i] == 1:
                    w[i] = sample_weights[i] * np.exp(alpha)
                else:
                    w[i] = sample_weights[i] * np.exp(-alpha)
            sample_weights = w / w.sum()
            self.estimators.append(weak)
            self.est_weights.append(alpha)

    def predict(self, X):
        # if _enc attribute isn't defined, the user hasn't launched fit function yet
        if not hasattr(self, "_enc"):
            raise ValueError("You must call ""fit"" before ""predict""")
        print('predico x = {}'.format(X))
        p = [w * weak.predict(X.reshape(1,-1)) for w, weak in zip(self.est_weights, self.estimators)]
        p = np.sum(p)
        # Apply sgn function on the discriminant function f(x)
        p = 0 if p < 0 else 1

        # Decode labels with their original value
        return self._enc.inverse_transform(p)


if __name__ == '__main__':
    X = np.array([[1,1,1], [1,1,0], [1,0,0], [0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    ada = AdaBoost()
    ada.fit(X, y)
    for x, label in zip(X, y):
        print(ada.predict(x), label)
