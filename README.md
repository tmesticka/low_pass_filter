# low_pass_filter
Tatiana Mestická - 6077633
Proposal

This package is designed to assist users in filtering out high-frequency noise from time-series data using a low-pass filter. The concept of a low-pass filter is fundamental in signal processing, where it allows the passage of signals with frequencies lower than a certain cutoff frequency while reducing frequencies higher than the cutoff frequency. The package focuses on automating this process, simplifying its implementation for users working with time-series data.

The process begins by converting the input data, typically a time-series dataset, into the frequency domain. This transformation is achieved using the Fast Fourier Transform (FFT) algorithm, which is well-suited for efficiently handling large datasets. Once the data is in the frequency domain, the low-pass filter is applied. The purpose of this filter is to remove high-frequency components (typically noise). By filtering out these unwanted frequencies, the dataset is smoothed, making it easier to analyze and interpret.

In addition to performing the low-pass filtering, the package includes functionality for data visualization. A built-in plotting function will generate a graph displaying both the original and filtered datasets. This visual comparison is essential for users to understand how the filtering process impacts their data, offering insights into what frequencies have been removed and how the data has been smoothed.

This package relies on two widely used Python libraries: NumPy and Matplotlib. NumPy is essential for numerical operations, such as executing the FFT, while Matplotlib is used to create the visual output for comparing the original and filtered datasets. These libraries have to be installed (easily done with the command pip install numpy matplotlib). The choice of these well-established libraries ensures the package is built on a reliable foundation, which many users are already familiar with. 

This package aims to simplify the process of applying a low-pass filter to time-series data, particularly for those without further knowledge in signal processing. By taking care of the complex steps involved in converting data to the frequency domain and offering an easy-to-use graphing tool, this package helps users more efficiently and save time. Whether you're working with financial data, scientific data, or any other type of time-series information, the package makes it easier to remove noise and improve the quality of your data, so that it is easier to interpret. 
