import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.seq = [32768, 8192, 2048, 512]
        
        self.pool = nn.MaxPool1d(kernel_size=1)
        
        self.conv1 = nn.Conv1d(self.seq[0], int(self.seq[0] / 4), 1)
        self.conv2 = nn.Conv1d(self.seq[1], int(self.seq[1] / 4), 1)
        self.conv3 = nn.Conv1d(self.seq[2], int(self.seq[2] / 4), 1)
        self.conv4 = nn.Conv1d(self.seq[3], int(self.seq[3] / 4), 1)

        self.fc1 = nn.Linear(128, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 4)

    def forward(self, x):
        activation_maps = []  
        activation_maps.append(x.detach().cpu().numpy())  

        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))

        x = torch.flatten(x, 1)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
        return x, activation_maps
