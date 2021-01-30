import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

df = pd.read_csv(r"C:\Users\sycwd\Downloads\churning.csv")
# we use only the first 2 variables as features
# account length,number vmail messages
x = df.iloc[:, [0, 1]]
y = df.iloc[:,-1] # classification
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

with open("my_ml_model1.ml",'rb') as f:
    classifier = pickle.load(f)

y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(accuracy_score(y_test, y_pred))

while True:
    var1 = float(input("Enter value for account length:"))
    var2 = float(input("Enter value for number vmail messages:"))
    pred = classifier.predict([[var1, var2]])
    print(pred)
    if pred == [1]:
        print("Yes, likely will churn.")
    else:
        print("Unlikely will churn.")
    cont = input("Do you want to continue? y/n")
    if cont == "n":
        break