import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.main = nn.Sequential(
            nn.Conv1d(128, 64, 1), 
            nn.ReLU(),

            nn.Conv1d(64, 32, 1), 
            nn.ReLU(),

            nn.Conv1d(32, 16, 1), 
            nn.ReLU(),

            nn.Flatten(), 
            nn.Linear(16, 4)  
        )
    def forward(self, x):
        x = self.main(x)
        return x
