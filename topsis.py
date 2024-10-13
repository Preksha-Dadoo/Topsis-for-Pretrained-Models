import numpy as np

data = np.array([
    [0.87, 0.65, 5, 0.95, 0.90],  
    [0.85, 0.60, 3, 0.93, 0.88],  
    [0.89, 0.70, 7, 0.92, 0.91]
])

weights = np.array([0.25, 0.20, 0.15, 0.20, 0.20])  

impacts = np.array([1, 1, -1, 1, 1])

norm_data = data / np.sqrt((data**2).sum(axis=0))

weighted_data = norm_data * weights

ideal_solution = np.max(weighted_data * impacts, axis=0)
negative_ideal_solution = np.min(weighted_data * impacts, axis=0)

distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
distance_to_negative = np.sqrt(((weighted_data - negative_ideal_solution) ** 2).sum(axis=1))

topsis_score = distance_to_negative / (distance_to_ideal + distance_to_negative)

rankings = np.argsort(topsis_score)[::-1] + 1

