# -*- coding: utf-8 -*-

import random

def random_analysis(sample_size):
    '''
    Run random analysis using 0 and 1 using which we estimate how often \
        a streak of 6 coin flips appears which are the same outcome.

    Parameters
    ----------
    sample_size : FLOAT
        Sample size is the number of times we conduct the random experiment.

    Returns
    -------
    Percentage of experiments containing at least one streak of 6.
    '''
    WINDOW_CHECK = 6
    EXPERIMENT_SIZE = 100
    number_of_streaks = 0
    
    if sample_size <= 0:
        return 0.0
    for _ in range(sample_size):
        flips = []
        for i in range(EXPERIMENT_SIZE):
            result = random.randint(0, 1)
            if result == 0:
                flips.append('H')
            else:
                flips.append('T')
    
        for i in range(len(flips) - WINDOW_CHECK + 1):
            window = flips[i:i + WINDOW_CHECK]
            if window == ['H'] * WINDOW_CHECK or window == ['T'] * WINDOW_CHECK:
                number_of_streaks += 1
                break
    
    return (number_of_streaks / sample_size) * 100


print(random_analysis(10000))
