# Sampling Distributions Dance Party!

## Data Scientist: Analytics - Codecademy

Get your dancing shoes ready! You are a DJ trying to make sure you are ready for a big party. You don’t have time to go through all the songs you can work with. Instead, you want to make sure that any sample of 30 songs from your playlist will get the party started. To do this, you will use the power of sampling distributions!

The dataset we are using for this project can be found [here](https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify). For simplicity, we have removed some unnecessary columns.

Note that a **helper_function.py** file is loaded for you in the workspace. This file contains functions that you will use throughout this project. 

### Tasks

#### Loading in the Data

1. You will be working with a dataset called **spotify_data.csv**. In **script.py**, use the <code>read_csv</code> pandas function to load in **spotify_data.csv** into a variable called <code>spotify_data</code>.

2. Use the pandas <Code>.head()</code> function to preview the <code>spotify_data</code>.

3. For this project, we are going to focus on the tempo variable. This column gives the beats per minute (bpm) of each song in **spotify.csv**. The other columns in our dataset are:

* <code>danceability</code>
* <code>energy</code>
* <code>instrumentalness</code>
* <code>liveness</code>
* <code>valences</code>

For now, we are going to ignore these other columns.
Create a variable called <code>song_tempos</code> that contains the <code>tempo</code> column data.

#### Helper Functions

4. Let’s investigate the helper functions we will use in the following sections. A file called **helper_functions.py** should be opened in the workspace for you. It contains three functions: <code>choose_statistic()</code>, <code>population_distribution()</code>, and <code>sampling_distribution()</code>. The code in these functions is similar to what we saw in the previous lesson, but let’s explore these together.
   
<code>choose_statistic()</code> allows us to choose a statistic we want to calculate for our sampling and population distributions. It contains two parameters:
* <code>x</code>: An array of numbers
* <code>sample_stat_text</code>: A string that tells the function which statistic to calculate on x. It takes on three values: “Mean”, “Minimum”, or “Variance”.
  
<code>population_distribution()</code> allows us to plot the population distribution of a dataframe with one function call. It takes the following parameter:
* <code>population_data</code>: the dataframe being passed into the function
  
<code>sampling_distribution()</code> allows us to plot a simulated sampling distribution of a statistic. The simulated sampling distribution is created by taking random samples of some size, calculating a particular statistic, and plotting a histogram of those sample statistics. It contains three parameters:
* <code>population_data</code>: the dataframe being sampled from
* <code>samp_size</code>: the size of each sample
* <code>stat</code>: the specific statistic being measured for each sample — either “Mean”, “Minimum”, or “Variance”
Read through these functions in **helper_function.py** to familiarize yourself with them.

#### Sampling Distribution Exploration

5. Now that our data is loaded into **script.py** and we have gone over the functions in **helper_functions.py** let’s start our sampling distributions exploration. Make sure to write your code in **script.py**.
To start off, let’s use the <code>population_distribution()</code> function to graph distribution of <code>song_tempos</code>.
When you click run, you should see a graph with the following title:
```
Population Distribution
```
How would you describe this distribution?

6. Now let’s plot the sampling distribution of the sample mean with sample sizes of 30 songs. To do this, use the <code>sampling_distribution()</code> helper function.
Once you hit run, you should see a graph with the following title:
```
Sampling Distribution of the Mean
Mean of the Sample Means: {Mean of the Sample Means} 
Population Mean: {Population Mean}
```

7. Compare your sampling distribution of the sample means to the population mean. Is the sample mean an unbiased or biased estimator of the population?

8. Now let’s plot the sampling distribution of the sample minimum with sample sizes of 30 songs. To do this, use the <code>sampling_distribution()</code> helper function.
Once you hit run, you should see a graph with the following title:
```
Sampling Distribution of the Minimum
Mean of the Sample Minimums: {Mean of the Sample Minimums}
Population Minimum: {Population Minimum}
```

9. Compare your sampling distribution of the sample minimums to the population minimum. Is the sample minimum an unbiased or biased estimator of the population?

10. Now let’s plot the sampling distribution of the sample variance with sample sizes of 30 songs. To do this, use the <code>sampling_distribution()</code> helper function.
Once you hit run, you should see a graph with the following title:
```
Sampling Distribution of the Variance
Mean of the Sample Variances: {Mean of the Sample Variances}
Population Variance: {Population Variance}
```

11. Compare your sampling distribution of the sample variance to the population variance. Does the sample variance appear to be an unbiased or biased estimator of the population?

12.Go to line 17 in helper_functions.py. You should see the following line of code:
```
np.var(x)
```
Change this to:
```
np.var(x, ddof=1)
```
Adding this <code>ddof=1</code> parameter will divide our input by n-1 instead of n, therefore applying the sample variance formula.
After changing this line of code, run **script.py**. Does the sample variance appear to be an unbiased or biased estimator of the population?

#### Calculating Probabilities

13. We have a good sense of some sample statistics now that we’ve investigated sampling distributions. Let’s take our analysis further by calculating probabilities.
First, calculate the population mean and population standard deviation of <code>song_tempos</code>. Save these values in two separate variables called <code>population_mean</code> and <code>population_std</code>.

14. Use <code>population_mean</code> and <code>population_std</code> to calculate the standard error of the sampling distribution of the sample mean with a sample size of 30.
Save this value in a variable called <code>standard_error</code>.

15. You are afraid that if the average tempo of the songs you randomly select is less than 140bpm that your party will not be enjoyable.
Using <code>population_mean</code> and <code>standard_error</code> in a CDF, calculate the probability that the sample mean of 30 selected songs is less than 140bpm.
Remember to print your result into the output terminal.

16. You know the party will be truly epic if the randomly sampled songs have an average tempo of greater than 150bpm.
Using <code>population_mean</code> and <code>standard_error</code> in a CDF, calculate the probability that the sample mean of 30 selected songs is GREATER than 150bpm.
Remember to print your result into the output terminal.
Does this probability make you feel confident about the party?

#### Extras
17. Awesome job! You are ready to throw an awesome party! If you want to do some more exploration of sampling distributions, here are some more opportunities:
* Add another sample statistic to the <code>choose_statistic()</code> function in **helper_functions.py** — such as median, mode, or maximum.
* Explore a different column of data from the **spotify_data.csv** dataset.
* Use the sampling distribution of the sample minimum to estimate the probability of observing a specific sample minimum. For example, from the plot, what is the chance of getting a sample minimum that is less than 130bpm?
Happy coding!
