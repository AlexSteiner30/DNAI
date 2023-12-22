import torch
import models
import generate_pdf
import generate

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

def convertToString(x):
    '''
    Possible combination 
        - AT
        - TA
        - CG
        - GC
    '''

    if x == 0:
        return "AT"
    elif x == 1:
        return "TA"
    elif x == 2:
        return "CG"
    else:
        return "GC"

def predict(sequence, count):
    sequence = sequence.upper()

    x = torch.from_numpy(convertToArray(sequence)).repeat(32,1,1).reshape(32,length,1).to('cuda')

    result = "no diseases found in the provided DNA sequence."
    patterns = f"<p class=MsoNormal style='text-align:justify><span lang=EN-GB style='font-size:1.0pt line-height:115%'>"

    ouput, activation_maps = CNN(x)

    ouput =  torch.argmax(ouput).item()
    if ouput != 0:
        sequence = convertToArray(sequence)
        a = activation_maps[0][0] == sequence

        for i, j in enumerate(sequence):
            if sequence[i] == activation_maps[0][0][i] == True:
                patterns = patterns + f"<mark>{convertToString(sequence[i])}</mark>"
            else:
                patterns = patterns + f"{convertToString(sequence[i])}"

        patterns = patterns + "<o:p></o:p></span></p>"

    else:
        patterns = patterns = f"<p class=MsoNormal style='text-align:justify><span lang=EN-GB style='font-size:1.0pt line-height:115%'>{sequence}<o:p></o:p></span></p>"

    if ouput == 1:
        result = "lactose intolerant"
    elif ouput == 2:
        result = "haemophilia"
    elif ouput == 3:
        result = "autism"

    generate_pdf.generate_pdf(result, patterns, count)

    return result

#predict(generate.generate_random_dna_sequence(length),1)