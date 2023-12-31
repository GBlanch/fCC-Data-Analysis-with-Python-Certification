## Sea Level Predictor

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

+ Use Pandas to import the data from [`epa-sea-level.csv.`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/4.sea_level_predictor/epa-sea-level.csv)
+ Use matplotlib to create a scatter plot using the `Year` column as the x-axis and the `CSIRO Adjusted Sea Level` column as the y-axis.
+ Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
+ Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
+ The x label should be `Year`, the y label should be `Sea Level (inches)`, and the title should be `Rise in Sea Level.`

Unit tests are written for you under [`test_module.py.`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/4.sea_level_predictor/py%20files/test_module.py)

The boilerplate also includes commands to save and return the image.

### Development

For development, you can use main.py to test your functions to elaaborate your code in the file [`sea_level_predictor`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/4.sea_level_predictor/py%20files/sea_level_predictor.py). 

### Testing

Refer to section [how to test these projects](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/tree/main#how-to-test-this-projects)

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

### Data Source

[Global Average Absolute Sea Level Change](https://datahub.io/core/sea-level-rise), 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

Original source : https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer
