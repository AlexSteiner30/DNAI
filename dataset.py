import torch.utils.data as data
import numpy as np
import torch
import json

class LoadDataset(data.Dataset):
    def __init__(self):
        self.sequences = []
        self.problems = []

        f = open('dataset.json')
        self.data = json.load(f)

        for i, itObject in enumerate(self.data):
            self.sequences.append(self.convertToArray(itObject['sequence']))
            self.problems.append(int(itObject['problem']))
           
        f.close()

    def convertToArray(self,x):
        sequence = []

        for i in x:
            if i == 'A':
                sequence.append(0)
            elif i == 'T':
                sequence.append(1)
            elif i == "G":
                sequence.append(2)
            else:
                sequence.append(3)

        return np.array(sequence, dtype=np.float32)
  
    def __getitem__(self, idx):
        sequence = torch.tensor(self.sequences[idx])
        problem = torch.tensor(self.problems[idx])

        return sequence, problem
    
    def __len__(self):
        return len(self.sequences)