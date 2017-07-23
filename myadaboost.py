# BaseEstimator ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html
# ClassifierMixin ---> http://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from abc import ABCMeta, abstractmethod
from sklearn.tree import DecisionTreeClassifier
from utility import with_metaclass
import numpy as np
from scipy import sparse
from functools import reduce


class AdaBoostBase(with_metaclass(ABCMeta, BaseEstimator, ClassifierMixin)):
    
    @abstractmethod
    def __init__(self, n_estimator):
        if n_estimator < 1:
            raise ValueError("n_estimator must be greater than 0")
        self.n_estimator = n_estimator
        self.estimators = []
        self.est_weights = []

    def fit(self, X, y):
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
        while len(self.estimators) < self.n_estimator:
            weak = DecisionTreeClassifier(max_depth=1)
            weak.fit(X, y, sample_weight=sample_weights)
            errors = np.array([weak.predict(t[0]) != t[1] for t in zip(X, y)])
            epsilon = np.sum([b * sw for b, sw in zip(errors, sample_weights)])
            if epsilon == 0:
                self.estimators.append(weak)
                self.est_weights.append(1)
                # print('epsilon=%.5f a=%.5f' % (epsilon, 1))
                break
            alpha = 0.5 * np.log((1 - epsilon) / epsilon)
            # print('epsilon=%.5f a=%.5f' % (epsilon, alpha))
            w = np.zeros(len(y))
            for i in range(len(y)):
                if errors[i] == 1:
                    w[i] = sample_weights[i] * np.exp(alpha)
                else:
                    w[i] = sample_weights[i] * np.exp(-alpha)
            sample_weights = w / w.sum()
            self.estimators.append(weak)
            self.est_weights.append(alpha)
        # print('{} weaks. Their weights: {}'.format(len(self.estimators), self.est_weights))

    def decision_function(self, X):
        if not self.weights:
            raise ValueError("You must call ""fit"" before ""decision_function""")


    def predict(self, X):
        # if _enc attribute isn't defined, the user hasn't launched fit function yet
        if not hasattr(self, "_enc"):
            raise ValueError("You must call ""fit"" before ""predict""")

        # if sparse.issparse(X):
        #     print("X is sparse!")
        p = [weak.predict(X) * w for w, weak in zip(self.est_weights, self.estimators)]
        p = reduce(lambda x, y: x+y, p)

        # Apply sgn function on the discriminant function f(x)    
        p[p>=0] = 1
        p[p<0] = 0

        # Convert predictions floating-point values into int32 values
        p = p.astype(np.int32, copy = False)

        # Decode labels with their original value
        return self._enc.inverse_transform(p)

class AdaBoost(AdaBoostBase):
    def __init__(self, n_estimator = 10):
        
        super(AdaBoost, self).__init__(
            n_estimator = n_estimator)
if __name__ == '__main__':
    X = np.array([[1,1,1], [1,1,0], [1,0,0], [0,0,0], [0,1,1], [0,0,1]])
    y = np.array([1,1,1,1,0,0])

    ada = AdaBoost()
    ada.fit(X, y)
    for x, label in zip(X, y):
        print(ada.predict(x), label)
