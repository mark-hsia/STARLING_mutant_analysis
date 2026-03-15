#Generate array of potential mutation for generation loop to operate on
import csv
import pandas as pd

def Mutator(sequence, residues):
    with open("mutants.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["position", "wild-type", "mutant", "sequence"])

        for i in range(len(sequence)):
            for n in residues:
                if n == sequence[i]:
                    continue

                copy_sequence = list(sequence)
                copy_sequence[i] = n
                mutant_seq = "".join(copy_sequence)

                writer.writerow([i + 1, sequence[i], n, mutant_seq])

tau_sequence = 'LDYGSAAAAAAAQCRYGDLASLHGAGAAGPGSGSPSAAASSSAHTLFTAEEGQLYG'

tau_sequence_list = list (tau_sequence)

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
amino_acids_list = list (amino_acids)

Mutator(tau_sequence, amino_acids)

df = pd.read_csv("mutants.csv")
print(df.head())
