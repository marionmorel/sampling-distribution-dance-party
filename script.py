from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Task 1
spotify_data = pd.read_csv('spotify_data.csv')

# Task 2
print(spotify_data.head())

# Task 3
song_tempos = spotify_data['tempo']

# Task 5
population_distribution(song_tempos)
# The population distribution is normal, a little bit skewed to the right

# Task 6
sampling_distribution(song_tempos, 30, "Mean")

# Task 7
# The sampling distribution of the sample means and the population mean are very similar, which means the mean is an unbiased estimator of the population

# Task 8
sampling_distribution(song_tempos, 30, "Minimum")

# Task 9
# The sampling distribution of the sample minimums is a lot higher than the population minimum, which means the minimum is a biased estimator of the population

# Task 10
sampling_distribution(song_tempos, 30, "Variance")

# Task 11
# The sampling distribution of the sample variances is lower than the population variance, which means the variance is a biased estimator of the population

# Task 12
# After changing the code in helper_functions.py, the variance still appear to be an unbiased estimator of the population as the sampling distribution of the sample variances and the population variance are very similar

# Task 13
population_mean = song_tempos.mean()
population_std = song_tempos.std()

# Task 14
standard_error = population_std / (30 ** 0.5)

# Task 15
print('The probability that the sample mean of 30 selected songs is less than 140bpm is: ' + str(stats.norm.cdf(140, population_mean, standard_error)))

# Task 16
print('The probability that the sample mean of 30 selected songs is greater than 150bpm is: ' + str(1 - stats.norm.cdf(150, population_mean, standard_error)))