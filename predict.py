import torch
import models

import numpy as np

CNN = models.CNN().cuda()

cnn_path = "models.pt" 

checkpoint = torch.load(cnn_path)
CNN.load_state_dict(checkpoint['CNN'])

def convertToArray(x):
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

def predict():
    print("DNA sequence: ")
    text = input()

    x = torch.from_numpy(convertToArray(text)).repeat(32,1,1).reshape(32,8192,1).to('cuda')
    result = "you seem to not have any illness"

    ouput = torch.argmax(CNN(x)).item()

    if ouput == 1:
        result = "it seems like you are lactose intolorante"
    elif ouput == 2:
        result = "it seems like you have cancer"
    elif ouput == 3:
        result = "it seems like you have autismus"

    print("Result: " + result)

predict()