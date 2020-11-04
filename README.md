# K-Nearest Neighbor Classifier; from Scratch, in Python

You can find the project article on [Medium](https://medium.com/can-it-be-predicted/k-nearest-neighbor-classifier-from-scratch-in-python-61c05b4055c).

- [Project Overview](#project-overview)
    - Tech Stack
    - Data Sources
- [Getting Started](#getting-started)
    - Locally
        - Pre-requisite python packages
        - Use created algorithm
- [Contributing](#contributing)
    - Issue/Bug Request
    - Feature Requests
    - Pull Requests
    - Attribution
- [Documentation](#documentation)

## Project Overview

The goal of this project was to create a K-nearest neighbors algorithm from scratch. 
The goal of the article was to explain to new users the usefulness and steps to implement 
and run their own KNN algorithm.

 - Personal model matched the official scikit-learn model’s accuracy.
 - Demonstrated object-oriented programming by packaging the model in a python class.

### Tech Stack

- numpy
- scikit-learn
- pandas

### Data Sources

Iris dataset, used for example purposes, obtained from [Kaggle](https://www.kaggle.com/uciml/iris).

## Getting Started

### Locally

#### Pre-requisite python packages

 - numpy
 - sklearn

#### Use created algorithm

Save knn.py in desired folder and import the class into your desired project.

```python
from knn import KNN
```

The KNN class must be fit to an X_train and y_train, derived from your dataset. 
This can be achieved by using sklearn's 'train_test_split' function, from its 'model_selection' method.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 30)

nearest_neighbors = KNN(3).fit(X_train, y_train)
```
*Note: This code trains classification based on the **3** nearest neighbors*

Our K-nearest neighbors algorithm is now trained on the training data and ready for prediction.
You can use the KNN class' 'predict' function to save predictions and analyze your results. 
Use the 'evaluate' function to check accuracy.

```python
y_pred = nearest_neighbors.predict(X_test)

nearest_neighbors.evaluate(y_pred, y_test)
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

I would love to hear from you about new features which would improve this project and furthers the aims of the project. Please provide as much detail and information as possible to show why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this project, please submit a pull request. It is best to communicate your ideas with the developer first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to the existing code conventions.
- Include the relevant issue number, if applicable.
- Your Pull Request will be merged in once you have the sign-off of the developer.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

Find definitions of iris dataset's columns and values from [Kaggle](https://www.kaggle.com/uciml/iris).

Official scikit-learn K-nearest neighbors algorithm found on their [website](https://scikit-learn.org/stable/modules/neighbors.html).
