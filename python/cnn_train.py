import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


# ---------------------------------------------------
# ECG Dataset
# ---------------------------------------------------

class ECGDataset(Dataset):

    def __init__(self, noisy_signal, clean_signal):

        self.noisy = torch.tensor(
            noisy_signal,
            dtype=torch.float32
        )

        self.clean = torch.tensor(
            clean_signal,
            dtype=torch.float32
        )

        self.window_size = 256

    def __len__(self):

        return len(self.noisy) - self.window_size

    def __getitem__(self, idx):

        return (

            self.noisy[idx:idx+self.window_size],

            self.clean[idx:idx+self.window_size]

        )


# ---------------------------------------------------
# CNN Denoiser
# ---------------------------------------------------

class CNN_Denoiser(nn.Module):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(

            nn.Conv1d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                padding=2
            ),

            nn.ReLU(),

            nn.Conv1d(
                16,
                32,
                5,
                padding=2
            ),

            nn.ReLU(),

            nn.Conv1d(
                32,
                16,
                5,
                padding=2
            ),

            nn.ReLU(),

            nn.Conv1d(
                16,
                1,
                5,
                padding=2
            )

        )

    def forward(self, x):

        return self.network(x)


# ---------------------------------------------------
# Training Function
# ---------------------------------------------------

def train_model(noisy_signal,
                clean_signal,
                epochs=2,
                batch_size=128):

    dataset = ECGDataset(
        noisy_signal,
        clean_signal
    )

    loader = DataLoader(

        dataset,

        batch_size=batch_size,

        shuffle=True

    )

    model = CNN_Denoiser()

    criterion = nn.MSELoss()

    optimizer = torch.optim.Adam(

        model.parameters(),

        lr=0.001

    )

    print("\nTraining Started...\n")

    for epoch in range(epochs):

        total_loss = 0

        for noisy_batch, clean_batch in loader:

            noisy_batch = noisy_batch.unsqueeze(1)

            clean_batch = clean_batch.unsqueeze(1)

            output = model(noisy_batch)

            loss = criterion(

                output,

                clean_batch

            )

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        print(

            f"Epoch {epoch+1}/{epochs}"

            f"  Loss = {total_loss:.4f}"

        )

    print("\nTraining Completed Successfully!")

    return model