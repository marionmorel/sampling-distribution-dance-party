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