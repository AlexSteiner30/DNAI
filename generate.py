import json
import random

# 0 = Nothing
# 1 = Lactose
# 2 = Cancer
# 3 = Autismus 

def generate_random_dna_sequence(length):
    bases = ['AT', 'TA', 'GC', 'CG']
    sequence = ''.join(random.choice(bases) for _ in range(length))
    return sequence

sequences = []
length = 32768
for i in range(2):
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
