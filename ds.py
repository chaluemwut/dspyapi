from sklearn.model_selection import train_test_split
from sklearn import tree
import pickle

if __name__ == '__main__':
    f = open('Iris.csv', 'r')
    x = []
    y = []
    for o in f:        
        line = o.replace('\n', '').split(',')
        x.append(line[1:5])
        y_label = line[5]
        if y_label == 'Iris-setosa':
            y.append(1)
        elif y_label == 'Iris-versicolor':
            y.append(2)
        elif y_label == 'Iris-virginica':
            y.append(3)                
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    obj = open('model.obj', 'wb')
    pickle.dump(clf, obj)
    # p = clf.predict([X_test[0]])