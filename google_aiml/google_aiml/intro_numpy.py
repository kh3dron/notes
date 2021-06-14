import numpy as np

"Arrays"
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
sequence_of_integers = np.arange(5, 12)     #[ 5  6  7  8  9 10 11]

"Randomness"
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6)) #never generates a 101
#random_floats_between_0_and_1 = np.random.random([6])

"Math on arrays, or Broadcasting"
"""
random_floats_between_0_and_1 = np.random.random([6])
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
"""