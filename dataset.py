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
            self.sequences.append(self.convertToNumbers(itObject['sequence']))
            self.problems.append(int(itObject['problem']))
           
        f.close()

    def convertToNumbers(self,x):
        string = ''
        for i in x:
            if i == 'A':
                string = string + '0'
            elif i == 'T':
                string = string + '1'
            elif i == "G":
                string = string + '2'
            else:
                string = string + '3'

        print(string + "\n\n")

        return int(string)
  
    def __getitem__(self, idx):
        sequence = torch.tensor(self.sequences[idx])
        problem = torch.tensor(self.problems[idx])

        return sequence, problem
    
    def __len__(self):
        return len(self.sequences)