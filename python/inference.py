import torch
import numpy as np
import matplotlib.pyplot as plt

from traditional_filter import (
    calculate_snr,
    calculate_mse
)


def run_inference(
        model,
        signal,
        noisy_signal,
        traditional_denoised):
    """
    Run CNN model on ECG signal
    """

    print("\nRunning CNN Inference...\n")

    model.eval()

    with torch.no_grad():

        test_input = torch.tensor(
            noisy_signal[:2000],
            dtype=torch.float32
        ).unsqueeze(0).unsqueeze(0)

        cnn_output = model(test_input)

        cnn_output = cnn_output.squeeze().numpy()

    # -------------------------
    # Performance Evaluation
    # -------------------------

    snr_cnn = calculate_snr(
        signal[:2000],
        cnn_output
    )

    mse_cnn = calculate_mse(
        signal[:2000],
        cnn_output
    )

    print("CNN SNR :", snr_cnn)

    print("CNN MSE :", mse_cnn)

    # -------------------------
    # Plot Results
    # -------------------------

    plt.figure(figsize=(12, 9))

    plt.subplot(4, 1, 1)

    plt.plot(signal[:2000])

    plt.title("Original ECG Signal")

    plt.subplot(4, 1, 2)

    plt.plot(noisy_signal[:2000])

    plt.title("Noisy ECG Signal")

    plt.subplot(4, 1, 3)

    plt.plot(traditional_denoised[:2000])

    plt.title("Traditional Denoised Signal")

    plt.subplot(4, 1, 4)

    plt.plot(cnn_output)

    plt.title("CNN Denoised Signal")

    plt.tight_layout()

    plt.show()

    # -------------------------
    # Save Output
    # -------------------------

    np.savetxt(

        "../results/cnn_denoised_signal.txt",

        cnn_output

    )

    print("\nCNN Denoised Signal Saved Successfully!")

    return cnn_output