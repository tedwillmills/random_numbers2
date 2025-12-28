import numpy as np

def pdf(x, mean, std):
    """
    Probability Density Function for a normal distribution.

    Parameters:
        x (array-like): points at which to evaluate the PDF
        mean (float): mean of the distribution
        std (float): standard deviation of the distribution

    Returns:
        array-like: PDF values at each x
    """
    return 1/np.sqrt(2 * np.pi * std**2) * np.exp(-0.5 * ((x - mean) / std) ** 2)

