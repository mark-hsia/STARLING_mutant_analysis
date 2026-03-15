#generating mutants to population MutantLibrary directory

import csv
import os

import starling
from starling import generate, load_ensemble
from tqdm import tqdm
csv_path = "/dartfs-hpc/rc/home/k/f0044gk/labhome/Mark/mutants.csv"

out_dir = "/dartfs-hpc/rc/home/k/f0044gk/labhome/Mark/MutantLibrary"

with open(csv_path, newline="") as f:
    reader = csv.DictReader(f)

    for i, row in tqdm(enumerate(reader), leave=True, desc='Iterating Mutants'):
        sequence = row["sequence"]
        ensemble = generate(sequence, conformations=1000, return_single_ensemble=True)
        out_path = os.path.join(out_dir, f"mutant{i}.pdb")
        ensemble.save(out_path)

        print(f"Saved: {out_path}")
