# Weights

This folder stores the trained CNN model weights used for FPGA implementation.

The weights are exported after training the CNN model using:

```bash
python python/export_weights.py
```

Generated files include:

- Floating-point weights (*.txt)
- Fixed-point Q1.15 weights (*.txt)
- Vivado COE files (*.coe)

These files are used during FPGA synthesis and Block RAM initialization in Xilinx Vivado.