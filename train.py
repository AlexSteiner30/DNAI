from matplotlib import pyplot as plt
import torch
import torch.optim as optim

from models import *

from dataset import *
from arguments import Arguments

import time

class GAN():
    def __init__(self, args):
        self.args = args
        self.data = LoadDataset()

        self.cnn = CNN()
        
        self.criterion = torch.nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.cnn.parameters(), lr=0.001, weight_decay=0.01)

        self.dataLoader = torch.utils.data.DataLoader(self.data, batch_size=args.batch_size, shuffle=True)
        print("Training Dataset : {} prepared.".format(len(self.data)))

        print("Network prepared.")

    def run(self):      
        G_losses = []
        D_losses = []

        for epoch in range(args.epochs):
            for _iter, data in enumerate(self.dataLoader):
                sequence, labels = data
                sequence = sequence.to(self.args.device)
                labels = labels.to(self.args.device)

                outputs = self.cnn(sequence)
                loss = self.criterion(outputs, labels)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                train_loss += loss.item()

        torch.save({'G_state_dict': self.G.state_dict()}, '../TrainedModels/' + args.type + '.pt')

        plt.figure(figsize=(10,5))
        plt.title("Generator and Discriminator Loss During Training")
        plt.plot(G_losses,label="G")
        plt.plot(D_losses,label="D")
        plt.xlabel("Iterations")
        plt.ylabel("Loss")
        plt.legend()
        plt.savefig("graph.png")
        #plt.show()

if __name__ == '__main__':
    args = Arguments().parser().parse_args()

    args.device = torch.device('cuda:'+ str(args.gpu) if torch.cuda.is_available() else 'cpu')
    torch.cuda.set_device(args.device)

    model = GAN(args)
    model.run()