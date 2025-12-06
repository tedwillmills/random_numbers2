# Computational Tools

A collection of Python simulations and numerical methods as part of my ongoing work on random numbers and Monte Carlo simulations, including PRNGs, inverse transform sampling and data analysis.  

## Purpose
This repository expands upon content covered in my Computationl Tools lectures through various projects as I attempt to learn code beyond the syllabus. The aim of this repository is to build practical experience in simulation algorithms, data manipulation and optimisation. Doing this not only helps to improve my fundamentals in Python and teaches me new tools, but also gives me the skills to complete my own, more complex engineering projects alongside my degree.

## Contents
figures/
- exponential_PDF_and_histogram.png
- exponential_PDFs.png
- exponential_inverse_CDFs.png
- monte_carlo_histogram.png
- numerical_recipes_LCG_histogram.png
- numerical_recipes_LCG_scatter.png

notebooks/
- monte_carlo_simulation.ipynb
    - Simulation of a biased six-sided die (1000 x 2000 samples)
    - Histogram plot and comparison with normal distribution to demonstrate CLT
    - Statistical analysis (mean, median, std)
- random_numbers.ipynb
    - Linear Congruential Generator (LCG) for pseudo-random numbers using 'Numerical Recipes' parameter set
    - Scatter and histogram plotting
    - Inverse transform sampling for exponential distribution
    - PDF and quantile function plotting for varying λ

scripts/

## Example Outputs

![Monte Carlo Distribution](figures/monte_carlo_histogram.png)

The histogram shows that the total sums from the Monte Carlo simulation of a biased die converges to an approximately normal distribution, demonstrating the Central Limit Theroem even for non-uniform underlying probabilities.

![Monte Carlo Distribution](figures/exponential_PDFs.png)

The graph shows that the PDF generated via inverse transform sampling accurately matches the expected exponential distribution for different values of λ.

![Monte Carlo Distribution](figures/exponential_PDF_and_histogram.png)

The graph shows that there is a clear comparison between the PDF and histogram for the exponential distribution at a fixed λ value, confirming the reliability of the sampling method.

## Technical Skills
I have demonstrated and improved my competency in the following skills in writing these scripts:
- pseudo-random number generators using NumPy
- numerical simulations (Monte Carlo)
- inverse transform sampling
- data visualisation through Matplotlib
- statistical analysis (CLT, non-uniform distributions)

## Lessons Learnt
Through this repository, I have developed my understanding in the following areas:
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
