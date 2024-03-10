#Question 1

def join_a_list(example_list):
    New_example = " ".join(example_list)
    return New_example.lower()

print(join_a_list(["The", "Quick", "Brown", "Fox", "Jumps", "Over", "The", "Lazy", "Dog"]))

#Question 2

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def apply_model(model, x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    plt.scatter(x_train, y_train, color='y')
    plt.plot(x_test, predictions, color='g')
    plt.show()
    return model, x_test, predictions

file_path = 'C:\\Users\\atang\\OneDrive\\Documents\\Data Science MSc\\Advanced programming for data science\\Tutorial 3 cars.csv'
Dataset = pd.read_csv(file_path)
x = Dataset[['dist']]
y = Dataset[['speed']]
model = linear_model.LinearRegression()

print(apply_model(model, x, y))


R_squared = r2_score(x, y)
print('The coefficient of determination is', R_squared)
