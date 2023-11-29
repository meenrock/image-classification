from sklearn import svm, datasets
import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

class mcsvm:

    def iris_test_data_mcsvm():
        # load testing dataset from sklearn
        iris = datasets.load_iris()
        # split training and testing dataset
        X = iris.data[:, :2]
        y = iris.target
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=101)
        # select kernel to create 2 object
        rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(X_train, y_train)
        poly = svm.SVC(kernel='poly', degree=3, C=1).fit(X_train, y_train)
        # prediction efficiency
        poly_pred = poly.predict(X_test)
        rbf_pred = rbf.predict(X_test)
        # calculate metrics for poly kernel
        poly_accuracy = accuracy_score(y_test, poly_pred)
        poly_f1 = f1_score(y_test, poly_pred, average='weighted')
        print('Accuracy (Polynomial Kernel): ', "%.2f" % (poly_accuracy*100))
        print('F1 (Polynomial Kernel): ', "%.2f" % (poly_f1*100))
        # calculate metrics for rbf kernel
        rbf_accuracy = accuracy_score(y_test, rbf_pred)
        rbf_f1 = f1_score(y_test, rbf_pred, average='weighted')
        print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy*100))
        print('F1 (RBF Kernel): ', "%.2f" % (rbf_f1*100))

        return { poly_accuracy: poly_accuracy }



