import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
#from data import nba_data, okcupid_data

df = pd.read_csv('/Users/stevenslater/Desktop/nba.csv')

heights = df['player_height']
print(heights.head())
nba_mean = np.mean(heights)
print(nba_mean)
#okcupid_mean = np.mean(okcupid_data)

#Change this variable to your height (in inches)!
your_height = 185

nba_standard_deviation = np.std(heights)
print(nba_standard_deviation)



plt.title("NBA Player Heights")
plt.xlabel("Height (inches)")

plt.hist(heights)

plt.axvline(nba_mean, color='#FD4E40', linestyle='solid', linewidth=2, label = "Mean")

plt.axvline(nba_mean + nba_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2, label = "Standard Deviations")
plt.axvline(nba_mean - nba_standard_deviation, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(nba_mean + nba_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_standard_deviation * 2, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(nba_mean + nba_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_standard_deviation * 3, color='#FFB908', linestyle='solid', linewidth=2)

plt.axvline(your_height, color='#62EDBF', linestyle='solid', linewidth=2, label = "You")

plt.legend()

plt.tight_layout()
plt.show()
