import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.seq = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32]
        self.main = nn.Sequential()

        for i in self.seq:
            i = int(i)
            self.main.append(nn.Conv1d(i,int(i / 2), 1))
            self.main.append(nn.ReLU())
        
        self.main.append(nn.Flatten())
        self.main.append(nn.Linear(16, 4))

    def forward(self, x):
        x = self.main(x)
        return x
