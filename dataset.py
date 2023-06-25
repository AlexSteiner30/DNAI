import torch.utils.data as data
import numpy as np
import torch
import json

class LoadDataset(data.Dataset):
    def __init__(self):
        self.sequences = []
        self.problems = []

        f = open("captions.json")
        self.data = json.load(f)

        for i, itObject in enumerate(self.data):
            self.sequences.append(itObject['sequence'])
            self.problems.append(itObject['problem'])
           
        f.close()
  
    def __getitem__(self, idx):
        sequence = torch.tensor(self.sequences[idx])
        problem = torch.tensor(self.problems[idx])

        return sequence, problem
    
    def __len__(self):
        return len(self.sequences)