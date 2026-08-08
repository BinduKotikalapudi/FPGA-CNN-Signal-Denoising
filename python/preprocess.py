import wfdb
import numpy as np


def load_ecg_record(record_name="100", samples=20000):
    """
    Load ECG signal from MIT-BIH Arrhythmia Database
    """

    record = wfdb.rdrecord(record_name, pn_dir="mitdb")

    signal = record.p_signal[:, 0]
    signal = signal[:samples]

    fs = record.fs

    signal = signal / np.max(np.abs(signal))

    return signal, fs


def generate_noise(signal, fs):
    """
    Generate Powerline, Baseline Wander and EMG Noise
    """

    t = np.arange(len(signal)) / fs

    powerline_noise = 0.2 * np.sin(2 * np.pi * 50 * t)

    baseline_wander = 0.3 * np.sin(2 * np.pi * 0.5 * t)

    emg_noise = 0.1 * np.sin(2 * np.pi * 120 * t)

    noisy_signal = (
        signal
        + powerline_noise
        + baseline_wander
        + emg_noise
    )

    return noisy_signal