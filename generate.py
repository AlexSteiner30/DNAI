import json
import random

# 0 = Nothing
# 1 = Lactose
# 2 = Haemophilia
# 3 = Autismus 

def generate_random_dna_sequence(length):
    bases = ['AT', 'TA', 'GC', 'CG']
    sequence = ''.join(random.choice(bases) for _ in range(length))
    return sequence

def main():
    sequences = []
    length = 32768
    for i in range(400):
        sequence = generate_random_dna_sequence(length)
        sequences.append({"sequence": sequence,"problem": "0"})

        sequence = generate_random_dna_sequence(length)
        sequences.append({"sequence": sequence,"problem": "1"})

        sequence = generate_random_dna_sequence(length)
        sequences.append({"sequence": sequence,"problem": "2"})

        sequence = generate_random_dna_sequence(length)
        sequences.append({"sequence": sequence,"problem": "3"})
    
    with open("dataset.json", 'w') as json_file:
        json.dump(sequences, json_file, 
                            indent=4,  
                            separators=(',',': '))

#main()