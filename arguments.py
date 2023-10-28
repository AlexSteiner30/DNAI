import argparse

class Arguments:

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        
        self._parser.add_argument('--batch_size', type=int, default=1, help='Integer value for batch size.')
        
        self._parser.add_argument('--gpu', type=int, default=0, help='GPU number to use.')
        self._parser.add_argument('--epochs', type=int, default=250, help='Integer value for epochs.')
        self._parser.add_argument('--lr', type=float, default=0.001 , help='Float value for learning rate.')

    def parser(self):
        return self._parser