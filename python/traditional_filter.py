import numpy as np
from scipy.signal import butter, filtfilt, iirnotch


def apply_traditional_filter(noisy_signal, fs):
    """
    Traditional ECG Denoising using
    1. Notch Filter (50Hz)
    2. Butterworth Bandpass Filter
    """

    # Remove Powerline Noise
    b_notch, a_notch = iirnotch(50, 30, fs)
    filtered = filtfilt(b_notch, a_notch, noisy_signal)

    # Bandpass Filter (0.5Hz – 40Hz)
    b_band, a_band = butter(
        4,
        [0.5 / (fs / 2), 40 / (fs / 2)],
        btype="band"
    )

    denoised = filtfilt(b_band, a_band, filtered)

    return denoised


def calculate_snr(clean, denoised):
    """
    Signal-to-Noise Ratio
    """

    noise = clean - denoised

    snr = 10 * np.log10(
        np.sum(clean ** 2) /
        np.sum(noise ** 2)
    )

    return snr


def calculate_mse(clean, denoised):
    """
    Mean Squared Error
    """

    return np.mean((clean - denoised) ** 2)