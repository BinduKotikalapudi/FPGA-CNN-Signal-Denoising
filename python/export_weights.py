import numpy as np


# -------------------------------------------------------
# Floating Point to Fixed Point (Q1.15)
# -------------------------------------------------------

def float_to_fixed(values, q=15):
    """
    Convert floating point values to Q1.15 format
    """

    scale = 2 ** q

    return np.round(values * scale).astype(np.int16)


def fixed_to_float(values, q=15):

    return values / (2 ** q)


# -------------------------------------------------------
# Adaptive Quantization
# -------------------------------------------------------

def adaptive_q_format(values, total_bits=16):

    max_val = np.max(np.abs(values))

    integer_bits = int(np.ceil(np.log2(max_val + 1e-6)))

    fractional_bits = total_bits - 1 - integer_bits

    scale = 2 ** fractional_bits

    fixed = np.round(values * scale).astype(np.int16)

    return fixed, fractional_bits


# -------------------------------------------------------
# Save Floating and Fixed Point Weights
# -------------------------------------------------------

def save_weights(model):

    print("\nSaving Model Weights...\n")

    fixed_weights = {}

    for name, param in model.state_dict().items():

        weights = param.detach().numpy()

        float_name = (
            "../weights/"
            + name.replace(".", "_")
            + "_float.txt"
        )

        np.savetxt(

            float_name,

            weights.flatten()

        )

        fixed = float_to_fixed(weights)

        fixed_name = (
            "../weights/"
            + name.replace(".", "_")
            + "_Q15.txt"
        )

        np.savetxt(

            fixed_name,

            fixed.flatten(),

            fmt="%d"

        )

        fixed_weights[name] = fixed

        print(name, "saved.")

    print("\nAll weights saved successfully.")

    return fixed_weights


# -------------------------------------------------------
# Export COE File for Vivado BRAM
# -------------------------------------------------------

def export_to_coe(weights, filename):

    with open(filename, "w") as file:

        file.write("memory_initialization_radix=10;\n")

        file.write("memory_initialization_vector=\n")

        flat = weights.flatten()

        for value in flat[:-1]:

            file.write(str(value))

            file.write(",\n")

        file.write(str(flat[-1]))

        file.write(";")

    print(filename, "generated successfully.")