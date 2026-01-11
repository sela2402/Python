'''
How often does each type of these 20 amino acids: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, 
V, W and Y
'''

sequence = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPK" 
"TNQHERGFFYTPKSICSLYQLVCGEVEQCCTTSICSLYLCGSHRGFFYTLVECGEALYLHERGICSLYQ"
"LENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKTNQHERGFFYTPKSICSLYQLVCGEVEQCCTTSIC"
"SLYLCGSQCCTTSICSLYLCGSHRGFFYTLVECGEALYLHERGICSLYQLENYCNFVNQHL"

amimo_acids = ["A","C","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]

for aa in amimo_acids:
    count = sequence.count(aa)
    print(f"{aa} = {count}")
print("The total of the sequence", sum(sequence.count(aa) for aa in amimo_acids))