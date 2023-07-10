import torch
from models import *
from torch import nn
from torch.optim import Adam

from dataset import *

class GAN():
    def __init__(self, args):
        self.args = args
        self.data = LoadDataset()

        self.cnn = CNN().to(self.args.device)
        
        self.criterion = torch.nn.CrossEntropyLoss()
        self.optimizer = Adam(self.cnn.parameters(), lr=1e-3)

        self.dataLoader = torch.utils.data.DataLoader(self.data, batch_size=args.batch_size, shuffle=True)
        print("Training Dataset : {} prepared.".format(len(self.data)))

        print("Network prepared.")

    def run(self):       
        for epoch in range(self.args.epochs):
            for _iter, data in enumerate(self.dataLoader):
                sequence, labels = data
                
                sequence = sequence.reshape(32,128,1)
                sequence = sequence.to(self.args.device)
                labels = labels.to(self.args.device)
             
                outputs = self.cnn(sequence)
                loss = self.criterion(outputs, labels)
                
                self.optimizer.zero_grad()
                loss.backward() 
                self.optimizer.step() 

            print(f"Epoch:{epoch} loss is {loss.item()}")  

        torch.save({'CNN': self.cnn.state_dict()}, 'models.pt')

        text = input()
        x = torch.from_numpy(self.convertToArray(text)).repeat(32,1,1).reshape(32,128,1).to(self.args.device)
        print(torch.argmax(self.cnn(x)))
        print("Finished Training")

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