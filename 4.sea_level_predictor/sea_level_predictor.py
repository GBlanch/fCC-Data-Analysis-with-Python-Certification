import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    col_x1 = df['Year']
    col_y1 = df['CSIRO Adjusted Sea Level']
    fig = plt.figure()
    plt.scatter(col_x1,
                col_y1,
                marker = '^',
                s = 5
                )
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level Rise (1880 to 2051)')
    plt.savefig('sea_level_scatter_plot.png')

    # Create first line of best fit  
    reg1 = linregress(col_x1, 
                      col_y1)
    x1 = np.arange(col_x1.min(),
                   2051)
    y1 = reg1.slope * x1 + reg1.intercept
    plt.plot(x1,
             y1,
            color='blue',
            linewidth = 1)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level Rise (1880 to 2051)')
    plt.savefig('sea_level_plot(XIXth).png')

    # Create second line of best fit  
    df2 = df[col_x1 >= 2000]
    col_x2 = df2['Year']
    col_y2 = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(col_x2, 
                      col_y2)
    x2 = np.arange(col_x2.min(),
                   2051)
    y2 = res2.slope * x2 + res2.intercept 
    plt.plot(x2,
             y2,
             color='orange',
             linewidth = 1)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# NB: not-needed visualizations were added for further-on showcasing purposes.