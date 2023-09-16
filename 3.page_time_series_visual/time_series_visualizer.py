import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 index_col = 'date', 
                 parse_dates = True)

# Clean data
#NB: NaNs were verified with method isnan from math library

df = df[
        df['value'].between(df['value'].quantile(.025),
                            df['value'].quantile(.975))
        ]

months = ['January','February','March',
          'April','May','June','July',
          'August','September','October',
          'November','December']


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (16,8))
    ax = sns.lineplot(data = df, 
                      legend = 'brief',
                      linewidth = 1,
                      color = 'blue')
    ax.set(xlabel = 'Date', 
           ylabel = 'Page Views',
           label = 'Views',         
          )
    ax.set(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('TSV_line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.month_name()
    df_bar['year'] = df.index.year.values


    # Draw bar plot

    fig, ax = plt.subplots(figsize = (16,8))
    ax = sns.barplot(data = df_bar,
                     x = 'year',
                     hue = 'month',
                     y = 'value',
                     hue_order = months,
                     palette ='bright', 
                     errorbar = None
                     )
    
    ax.set(xlabel = 'Years', 
           ylabel = 'Average Page Views')
    ax.set(title = 'Yearly freeCodeCamp Forum Page Views 2016-2019')
    sns.move_legend(ax, "upper left")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    df_box['month_#'] = df.index.month
    df_box = df_box.sort_values('month_#')
    fig, ax = plt.subplots(1,
                           2,
                           figsize = (16,8)
                           )
    
    sns.boxplot(data = df_box,
                y = 'value',
                x = 'year',
                ax = ax[0],
                palette ='bright')
    ax[0].set(xlabel = 'Year',
              ylabel = 'Page Views', 
              title = 'Year-wise Box Plot (Trend)')
    
    sns.boxplot(data = df_box,
                y = 'value',
                x= 'month',
                ax = ax[1],
                palette ='bright')
    ax[1].set(xlabel = 'Month', 
              ylabel = 'Page Views',
              title = 'Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

    
