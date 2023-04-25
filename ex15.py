# KNN application on processes ID of an operating system. Are there intrusive or not?
import math
import EXAMPLES as EXAMPLES # this is the source of the data


class Solution(object):

    # Should use find_k_nearest_neigbors function below:
    def predict_label(self, features, k, label_key="is_intrusive"):
        k_nearest_neighbors = self.find_k_nearest_neighbors(EXAMPLES, features, k)
        k_nearest_neighbors_labels = [EXAMPLES[pid][label_key] for pid in k_nearest_neighbors]
        return round(sum(k_nearest_neighbors_labels) / k)            # produce a percentage of the K-nearest neighbors which have the label one.

    def find_k_nearest_neighbors(self, features, k):
        distances = {}
        for pid, features_label_map in EXAMPLES.items():
            distance = self.get_euclidean_distance(features, features_label_map["features"])    # calculate euclidean distance
            distances[pid] = distance                                                      # store this distance between a PID and the input features
        return sorted(distances, key = distances.get)[:k]

    def get_euclidean_distance(features, other_features):
        squared_differences = []
        for i in range(len(features)):
            squared_differences.append((other_features[i] - features[i]) ** 2)
        return math.sqrt(sum(squared_differences))





