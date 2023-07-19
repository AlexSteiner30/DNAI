import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.main = nn.Sequential(
            nn.Conv1d(128, 64, 1, bias=False),
            nn.LeakyReLU(negative_slope=0.2),

            nn.Conv1d(64, 32, 1, bias=False),
            nn.LeakyReLU(negative_slope=0.2),

            nn.MaxPool1d(kernel_size=1),
            nn.Flatten(),

            nn.Linear(32, 16),
            nn.LeakyReLU(negative_slope=0.2),

            nn.Linear(16, 8)
        )
    def forward(self, x):
        x = self.main(x)
        return x
