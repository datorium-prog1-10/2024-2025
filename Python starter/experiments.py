import random

animals = ['cat', 'dog', 'sheep']
weights = [0.5, 0.4, 0.1]

selected_values = random.choices(animals, weights=weights, k=1000)

