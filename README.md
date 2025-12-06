# Computational Tools

Ongoing Work on Random Numbers and Monte Carlo simulations (PRNGs, inverse transform sampling and data handling).

## Purpose
This repository takes content covered in my Computationl Tools lectures and expands upon it, through various projects as I attempt to learn code beyond the syllabus. Doing this not only helps to improve my fundamentals in Python and teach me new tools, but also gives me the tools to complete my own, more complex engineering projects alongside my degree.

## Contents
- figures/
- notebooks/
    - monte_carlo_simulation.ipynb - simulation of a biased six-sided die, histogram plot and comparison with normal distribution (CLT)
    - random_numbers.ipynb - Linear Congruential Generator (LCG) for pseudo-random numbers using 'Numerical Recipes' parameter set, scatter and histogram plotting; inverse transform sampling for exponential distribution, PDF and quantile function plotting for varying λ
- scripts/

## Example Outputs

![Monte Carlo Distribution](figures/monte_carlo_histogram.png)
The histogram shows the distribution of total sums from the Monte Carlo simulation of a biased die, which follows a normal distribution.

## Lessons Learnt
I have developed my understanding in the following areas:
- creating and improving functions
- using for loops to iterate processes
- plotting curves, histograms and scatter graphs for data analysis
- using libraries like NumPy and Matplotlib
 
It has also been interesting to use and work upon statistical principles that I studied in Further Maths A Level in Python. Concepts like the Central Limit Theorem (CLT), PDFs, CDFs, uniform and non-uniform distributions (binomial, normal, exponential) and inverse functions are all areas that I have learnt about, but actually putting them into practice and implementing them into Python scripts has been very rewarding.

I have also grown to appreciate the shear power of Python in running simulations and lengthy scripts, something I look forward to harnessing in more projects going forwards.

## Future Plans
There are a number of projects I would like to attempt over the coming months (this list will likely update and change as these are completed):
- aerofoil optimisation script
- flight trajectory simulation
- more extensive work with Monte Carlo simulations
- NASA data analysis using open datasets
- any other tasks relevant to engineering and the aerospace industry

I am currently working on an RC plane project outside of my degree, so I am hoping to incorporate Python into its design and improvements. With than in mind, this may become a large source of potential Python scripts in the future. As examples, I would like to explore methods for optimisation of variables like L/D, and a simple deskop GUI to visualise the plane's perfomance.
