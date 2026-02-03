from sklearn.linear_model import LinearRegression
import pandas as pd

class LinearRegressionModel:
    def __init__(self, **kwargs):
        self.model = LinearRegression(**kwargs)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        self.predicts = self.model.predict(X)
        return self.predicts

    def predict_proba(self, X):
        return self.model.predict_proba(X)
    
    def evaluate(self, X, y):
        return self.model.score(X, y)

    # def plot_confusion_matrix(self, X, y, labels=None, cmap='Blues'):
    #     from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    #     import matplotlib.pyplot as plt
    #     y_pred = self.predicts
    #     cm = confusion_matrix(y, y_pred, labels=labels)
    #     disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    #     disp.plot(cmap=cmap)
    #     plt.title('Confusion Matrix')
    #     plt.show()

    def f1_score(self, X, y, average='binary'):
        from sklearn.metrics import f1_score
        y_pred = self.predicts
        return f1_score(y, y_pred, average=average)
    
if __name__ == "__main__":
    X_train = pd.read_csv('./test_split_output/X_train.csv')
    y_train = pd.read_csv('./test_split_output/y_train.csv')
    X_test = pd.read_csv('./test_split_output/X_test.csv')
    y_test = pd.read_csv('./test_split_output/y_test.csv')
    # Initialize and train model
    model = LinearRegressionModel()
    model.fit(X_train, y_train)

    # Make predictions
    model.predict(X_test)

    # Evaluate model
    accuracy = model.evaluate(X_test, y_test)
    print(f'Accuracy: {accuracy:.2f}')

    # Plot confusion matrix
    # model.plot_confusion_matrix(X_test, y_test, labels=model.model.classes_)

    # Calculate F1 score
    # f1 = model.f1_score(X_test, y_test)
    # print(f'F1 Score: {f1:.2f}')