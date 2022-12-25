import numpy as np
from numpy import linalg

class KNN:

	def __init__(self, k):

		self.k = k


	def euclidean_dist(self, array1, array2):

		array1 = np.array(array1)

		array2 = np.array(array2)

		return linalg.norm(array1 - array2)


	def k_neighbors(self, test_row):

		distances = []

		for i in range(len(self.X_train)):

			distance = self.euclidean_dist(test_row, self.X_train[i])

			distances.append((distance, self.y_train[i]))

		distances.sort()

		return distances[:self.k]


	def get_nn(self):

		self.X_train = np.array(self.X_train)

		self.X_test = np.array(self.X_test)

		self.y_train = np.array(self.y_train)

		neighbors = []

		for j in range(len(self.X_test)):

			neighbors.append(self.k_neighbors(self.X_test[j]))

		return neighbors


	def vote_count(self, lst):
		"""
		returns dictionary containing counts of each element of list
		"""

		lst_count = dict()

		for element in lst:

			if element in lst_count:

				lst_count[element] += 1

			else:

				lst_count[element] = 1

		return lst_count


	def fit(self, X_train, y_train):

		self.X_train = X_train

		self.y_train = y_train


	def predict(self, X_test):

		self.X_test = X_test

		nbrs = self.get_nn()

		predictions = []

		for row in nbrs:

			dist, labels = zip(*row)

			label_dict = self.vote_count(labels)

			predictions.append(max(label_dict, key = label_dict.get))

		return predictions

	def evaluate(self, y_pred, y_test):

		count = 0

		for act, pred in zip(y_pred, y_test):
			if act == pred:
				count += 1

		return count / len(y_test)
