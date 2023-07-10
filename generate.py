import json
import random

# 0 = Nothing
# 1 = Lactose
# 2 = Cancer
# 3 = Autismus 

def generate_random_dna_sequence(length):
    bases = ['A', 'T', 'G', 'C']
    sequence = ''.join(random.choice(bases) for _ in range(length))
    return sequence

sequences = []

for i in range(128):
    sequence = generate_random_dna_sequence(128)
    sequences.append({"sequence": sequence,"problem": "0"})

    sequence = generate_random_dna_sequence(128)
    sequences.append({"sequence": sequence,"problem": "1"})

    sequence = generate_random_dna_sequence(128)
    sequences.append({"sequence": sequence,"problem": "2"})

    sequence = generate_random_dna_sequence(128)
    sequences.append({"sequence": sequence,"problem": "3"})

 
with open("dataset.json", 'w') as json_file:
    json.dump(sequences, json_file, 
                        indent=4,  
                        separators=(',',': '))
 