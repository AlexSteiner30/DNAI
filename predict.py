import torch
import models
import generate_pdf
import generate
import torch.nn.functional as F
import numpy as np

device = torch.device('cuda:'+ str(0) if torch.cuda.is_available() else 'cpu')

if torch.cuda.is_available():
    CNN = models.CNN().cuda()
else:
    CNN = models.CNN().cpu()

cnn_path = "models.pt" 

checkpoint = torch.load(cnn_path,  map_location=device)
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
    print("Predicting...")
    
    sequence = sequence.upper()

    x = torch.from_numpy(convertToArray(sequence)).repeat(32,1,1).reshape(32,length,1).to(device)

    results = []
    patterns = f"<p class=MsoNormal style='text-align:justify><span lang=EN-GB style='font-size:1.0pt line-height:115%'></span>"

    ouput, activation_maps = CNN(x)

    print(ouput[0])

    print("Prediction Done!")

    sequence = convertToArray(sequence)

    for i, j in enumerate(sequence):
        if torch.argmax(ouput) != 0:
            if sequence[i] == activation_maps[0][1][i] == True and (ouput[0][1].item() > 10 or ouput[0][1].item() == torch.argmax(ouput)):
                print(1)
                patterns = patterns + f"<mark style='background-color: yellow;'>{convertToString(sequence[i])}</mark>"

            elif sequence[i] == activation_maps[0][2][i] == True and (ouput[0][2].item() > 10 or ouput[0][2].item() == torch.argmax(ouput)):
                print(2)
                patterns = patterns + f"<mark style='background-color: lightgreen;'>{convertToString(sequence[i])}</mark>"

            elif sequence[i] == activation_maps[0][3][i] == True and (ouput[0][3].item() > 10 or ouput[0][3].item() == torch.argmax(ouput)):
                print(3)
                patterns = patterns + f"<mark style='background-color: lightblue;'>{convertToString(sequence[i])}</mark>"
            
            else:
                print(4)
                patterns = patterns + f"{convertToString(sequence[i])}"

        else:
            print(0)
            if sequence[i] == activation_maps[0][0][i] == True and (ouput[0][0].item() > 10 or ouput[0][0].item() == torch.argmax(ouput)):
                patterns = patterns + f"<mark style='background-color: orange;'>{convertToString(sequence[i])}</mark>"
            
            else:
                patterns = patterns + f"{convertToString(sequence[i])}"

    if ouput[0][1].item() > 10 or ouput[0][1].item() == torch.argmax(ouput):
        results.append("lactose intolerance")
        print(1)
    if ouput[0][2].item() > 10 or ouput[0][2].item() == torch.argmax(ouput):
        results.append("haemophilia")
    if ouput[0][3].item() > 10 or ouput[0][3].item() == torch.argmax(ouput):
        results.append("autism")
    if ouput[0][1].item() == torch.argmax(ouput):
        results = ["no diseases found in the provided DNA sequence."]

    patterns = patterns + "<o:p></o:p></span></p>"

    print(results)

    generate_pdf.generate_pdf(results, patterns, count)

    return results

#predict(generate.generate_random_dna_sequence(length),1)