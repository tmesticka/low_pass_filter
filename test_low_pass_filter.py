import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pytest
from low_pass_filter import low_pass_filter, plot_signals, extract_values

empty_array = []
def test_empty_array():
    signal = []
    result = empty_array(signal)
    assert result == None


def test_a_pytest_fail():
    signal = []
    result = empty_array(signal)
    assert result == 1
    

def test_visualization(): 
    t = np.linspace(0, 1, 1000, endpoint = False)
    original_signal  = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)
    cutoff_freq = 100
    sampling_rate = 1000
    
    filtered_signal = low_pass_filter(original_signal, cutoff_freq, sampling_rate)
    plt.figure(2)
    plt.plot(t, original_signal, label='Original Signal')
    plt.plot(t, filtered_signal, label='Filtered Signal', linestyle='--')
    plt.legend()
    plt.title('Original vs Filteres Signal with a cutoff frequency of {cutoff_freq} Hz')
    plt.show()

pytest -vv
