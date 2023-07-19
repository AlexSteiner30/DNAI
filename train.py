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

        print("Finished Training")