#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Low pass filter that removes high frequency noise from a 1D time-series data. 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def low_pass_filter(signal, cutoff_freq, sampling_rate):
    """
    Applies a low-pass filter using FFT (Fast Fourier Transform) to remove 
    frequencies higher than the cutoff frequency.

    Parameters:
    - signal: 1D numpy array representing the time series data
    - cutoff_freq: cutoff frequency in Hz for the low-pass filter
    - sampling_rate: sampling rate of the signal in Hz

    Returns:
    - filtered_signal: the filtered signal in time domain
    """
   
    fft_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=1/sampling_rate)
    """
    Applying the Fast Fourier Transform.
    """
    
    fft_signal[np.abs(freqs) > cutoff_freq] = 0
    """
    Applying the low_pass filter.
    """
 
    filtered_signal = np.fft.ifft(fft_signal)
    """
    Applying the Inverse Fast Fourier Transform. 
    """
    
    return np.real(filtered_signal)


def plot_signals(original_signal, filtered_signal, sampling_rate):
    """
    Plots the original and filtered signals for comparison.
    """
    
    time = np.arange(len(original_signal)) / sampling_rate
    
    plt.figure(1)
    plt.plot(time, original_signal, label="Original Signal")
    plt.plot(time, filtered_signal, label="Filtered Signal", linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Original vs Filtered Signal')
    plt.show()

def extract_values(csv_file):
    csv_file = ('~/low_pass_filter/Electric_production.csv.xls')
    signal = pd.read_csv(csv_file)
    values = signal['IPG2211A2N'].astype(float).tolist()
    return values
    """""
    Function that turns a csv file into an array. 
    """""

def main():
    csv_file = ('~/low_pass_filter/Electric_production.csv.xls')
    signal = extract_values(csv_file)
    cutoff_freq = 2 #Hz
    sampling_rate = 44100
    """""
    Trial dataset to check if the code works. 
    """""
    print (signal)
    filtered_signal = low_pass_filter(signal, cutoff_freq, sampling_rate)
    plot_signals(signal, filtered_signal, sampling_rate)
    
if __name__ == "__main__":
    main()