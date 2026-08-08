# FPGA-Based CNN Signal Denoising for ECG using Verilog HDL

## 📌 Overview

This project presents a hardware implementation of a Convolutional Neural Network (CNN) for ECG signal denoising on FPGA using Verilog HDL. The objective is to remove different types of noise from Electrocardiogram (ECG) signals while preserving important cardiac features.

The project combines Artificial Intelligence and Digital Hardware Design by training a CNN model in Python and implementing the inference architecture in Verilog for FPGA deployment.

---

## 🚀 Features

- ECG Signal Denoising using CNN
- MIT-BIH Arrhythmia Database
- Traditional Filtering (Notch + Butterworth)
- CNN-based Denoising
- Fixed-Point (Q1.15) Weight Conversion
- FPGA Hardware Implementation
- Verilog HDL Design
- Testbench for Functional Verification
- COE File Generation for Vivado Block RAM

---

## 🏗 Project Architecture

```
MIT-BIH ECG Dataset
        │
        ▼
 Noise Generation
        │
        ▼
 Traditional Filtering
        │
        ▼
 CNN Training (Python)
        │
        ▼
 Weight Quantization (Q1.15)
        │
        ▼
 COE File Generation
        │
        ▼
 FPGA Verilog Implementation
        │
        ▼
 Denoised ECG Output
```

---

## 📂 Repository Structure

```
FPGA-CNN-Signal-Denoising
│
├── python
│   ├── preprocess.py
│   ├── traditional_filter.py
│   ├── cnn_train.py
│   ├── inference.py
│   └── export_weights.py
│
├── verilog
│   ├── cnn_top.v
│   ├── conv1d.v
│   ├── input_buffer.v
│   ├── relu.v
│   ├── xor_encrypt.v
│   ├── cnn_controller.v
│   ├── conv_layer1.v
│   ├── conv_layer2.v
│   ├── conv_layer3.v
│   └── conv_layer4.v
│
├── testbench
│   └── tb_cnn.v
│
├── weights
├── docs
├── images
├── results
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🛠 Technologies Used

### Programming

- Python
- Verilog HDL

### AI / Machine Learning

- PyTorch
- CNN
- NumPy
- SciPy

### FPGA

- Xilinx Vivado
- Verilog HDL
- Block Memory Generator

### Dataset

- MIT-BIH Arrhythmia Database

---

## 📊 Results

Performance metrics evaluated include:

- Signal-to-Noise Ratio (SNR)
- Mean Squared Error (MSE)
- Traditional Filtering vs CNN
- ECG Signal Reconstruction

---

## 📸 Project Screenshots

Add screenshots inside the **images** folder.

Example:

- CNN Architecture
- ECG Waveforms
- Simulation Waveform
- Vivado RTL Schematic
- FPGA Implementation

---

## ▶ How to Run

### Python

```bash
pip install -r requirements.txt
```

Run preprocessing

```bash
python preprocess.py
```

Train CNN

```bash
python cnn_train.py
```

Run inference

```bash
python inference.py
```

Export weights

```bash
python export_weights.py
```

---

## FPGA Implementation

1. Open Vivado
2. Create a new project
3. Add Verilog files
4. Import COE weight files
5. Run Simulation
6. Synthesize
7. Generate Bitstream

---

## Future Enhancements

- Real-time FPGA deployment
- Multi-channel ECG processing
- Hardware acceleration using DSP slices
- Edge AI implementation
- Lightweight CNN architectures

---

## 📄 Project Documentation

The complete project documentation is available in the **docs** folder.

**Included document:**

- 📘 Major Report.pdf

The report contains:

- Project overview
- Literature survey
- Methodology
- CNN architecture
- FPGA implementation
- Experimental results
- Performance analysis
- Conclusion and future work

Refer to:

docs/Major Report.pdf

for detailed information about the project.

---
## Author

**Bindu Kotikalapudi**

B.Tech Electronics & Communication Engineering

Anurag University

GitHub:
https://github.com/BinduKotikalapudi

LinkedIn:
https://www.linkedin.com/in/bindu-kotikalapudi-496901309

---

## License

This project is developed for academic and educational purposes.