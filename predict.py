import torch
import models
import generate_pdf

import numpy as np

CNN = models.CNN().cuda()

cnn_path = "models.pt" 

checkpoint = torch.load(cnn_path,  map_location=torch.device('cpu'))
CNN.load_state_dict(checkpoint['CNN'])

length = 32768

def convertToArray(x):
    sequence = []

    '''
    Possible combination 
        - AT
        - TA
        - CG
        - GC
    '''

    for i in range(len(x)):
        if i < len(x) - 1 and i % 2 == 0:
            if x[i] + x[i+1] == 'AT':
                sequence.append(0)
            elif x[i] + x[i+1] == 'TA':
                sequence.append(1)
            elif x[i] + x[i+1] == "CG":
                sequence.append(2)
            else:
                sequence.append(3)

    return np.array(sequence, dtype=np.float32)

def predict(sequence, count):
    x = torch.from_numpy(convertToArray(sequence)).repeat(1,1,1).reshape(1,length,1).to('cuda')
    result = "No diseases found in the provided DNA sequence."
    patterns = f"<p class=MsoNormal style='text-align:justify'><span lang=EN-GB style='font-size:1.0pt line-height:115%'>{sequence}<o:p></o:p></span></p>"
    ouput = torch.argmax(CNN(x)).item()
    
    out = CNN(x)
    for i in out:
        print(i)

    if ouput == 1:
        result = "lactose intolorante"

    generate_pdf.generate_pdf(result, patterns, count)

    return result