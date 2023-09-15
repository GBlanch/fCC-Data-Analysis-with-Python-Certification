Create a function named `calculate()` in [`mean_var_std.py`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/0.mvsd.calc/mean_var_std.py) that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

![image](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/assets/136500426/9a7388e2-430d-4b71-9ae6-513cccb83c90)

If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:

![image](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/assets/136500426/e0b883ee-def7-4325-bfa3-1261b59c936a)


The unit tests for this project are in [`test_module.py`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/0.mvsd.calc/test_module.py).

### Development
For development, you can use [`main.py`](https://github.com/GBlanch/fCC-Data-Analysis-with-Python-Certification/blob/main/0.mvsd.calc/main.py) to test your `calculate()` function. 

### Testing
We imported the tests from `test_module.py` to `main.py` for your convenience. 

### Submitting
Copy your project's URL and submit it to freeCodeCamp.

Original website : **https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator**