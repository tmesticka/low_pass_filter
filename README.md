# Low-pass filter python package
- name: [Tatiana Mestická] 
- student number: [6077633]

## Project Overview:
The Low-pass filter package is designed to assist its users in removing high-frequency noise from time-series data. These kind of filters are essential in signal processing given they only allow frequencies bellow the cutoff frequency, making the signal easier to interpret and work with. This package makes this process of multiple advanced steps less time consuming and much easier. 

## Main concepts and methods used:
- Low-pass filtering
    The package converts time-series data into frequency domain using the Fast Fourier Transform - FFT. After the transformation is done it removes unwanted high-frequency components (higher than given curoff frequency), effectively smoothing the data and reducing noise. Filtered signal is then transformed back into the time domain using the Inverse Fast Fourier Transform (IFFT) giving users output data that is easier to interpret. 
- Data visualization
    The package contains a plotting function that generates graphs comparing the original and filtered signal in time domain. 
        
## Libraries and dependencies: 
     The project utilizes basic Python libraries which are: 
    - Numpy - numerical computations, including executing FFT, 
    - Matplotlib - visualizations, graphs, 
    - Pytest - test functions
    These can be installed easily using pip install (given library). 

## How It Works: 
    Input Data:
        The package processes 1D time-series datasets. Users can either provide raw numerical arrays or load data from CSV files.
    Filtering Process:
        The data undergoes FFT to convert it to the frequency domain.
        A low-pass filter is applied, removing frequencies above the chosen cutoff value.
        The Inverse FFT is then used to transform the filtered data back into the time domain.
    Output:
        The smoothed, noise-reduced signal is returned, ready for analysis or further processing.
        Additionally, a plot comparing the original and filtered signals is generated for easy visual assessment.

## Testing
    A file with test functions is also a part of this project. It helps develop the package and check its functionality. A screenshot of tests is provided here: /Users/macuser/Desktop/Screenshot 2024-11-10 at 23.44.30.png
    
### Example use case: 
    Suppose working with scientific time-series data which contains non-neglectable high-frequency noise. Applying this package will simplify the process of cleaning the dataset, improving its quality and most importantly making it easier to interpret. 

### Why Use This Package: 
    User-Friendly: 
        Ideal for users with minimal knowledge of signal processing. The package abstracts the complex math involved in filtering, providing an intuitive interface.
    Time-Saving: 
        Automates the transformation, filtering, and visualization steps, making data cleaning efficient and straightforward.
    Versatile: 
        Suitable for any type of time-series data, from financial and environmental datasets to scientific measurements.
    Whether you need to smooth data for clearer trends or prepare signals for further analysis, this package streamlines the noise removal process, improving your workflow and data quality.