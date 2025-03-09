# -*- coding: utf-8 -*-
"""
You are given an array of numerical values, bootstrap samples, and size for a confidence interval.

Write a function that performs bootstrap sampling on the given array and calculates the confidence interval based on the given size.

Note: The function should return a tuple containing the minimum and maximum values of the confidence interval rounded to the tenths place.

Example

Input:

values = [1, 2, 3, 4, 5]
Output

bootstrap_conf_interval(values, 1000, 0.95) -> (1.2, 4.8)
In this case, the function returns a tuple indicating that we are 95% confident that the population parameter lies between 1.2 and 4.8 based on our bootstrap samples.
"""

import random
import numpy as np
def bootstrap_conf_interval(data, num_samples, conf_interval):
    s_mean=[]
    for i in range(num_samples):

        s=random.choices(data,k=len(data))
        shat=np.mean(s)
        s_mean.append(shat)
    
    lb=round(((1-conf_interval)/2)*100,1)
    ub=round((1-(1-conf_interval)/2)*100,1)          
    print(lb,ub)
    return np.percentile(s_mean,[lb,ub])
    