#Probability sum comparison of contact maps across residues 5-20x25-50
#SBATCH --time=00:30:00

import os
import mdtraj as md
import numpy as np
import itertools

pdb_dir = "/dartfs-hpc/rc/lab/R/RobustelliP/Mark/MutantLibrary_pdb"
xtc_dir = "/dartfs-hpc/rc/lab/R/RobustelliP/Mark/MutantLibrary_xtc"
res_range_1 = range(4, 20)   # residues 5-20
res_range_2 = range(24, 50)  # residues 25-50

cutoff = 0.8

output_file = "blocked_contact_sum_results.csv"
with open(output_file, "w") as f_out:
    f_out.write("Mutant,ContactSum\n")

def residue_pairs(traj, res_range1, res_range2):
    pairs = []
    for i in res_range1:
        atoms_i = traj.topology.select(f"resid {i}")
        for j in res_range2:
            atoms_j = traj.topology.select(f"resid {j}")
            pairs.extend(itertools.product(atoms_i, atoms_j))
    return np.array(pairs)

for pdb_file in os.listdir(pdb_dir):
    if pdb_file.endswith(".pdb"):
        mutant_name = pdb_file[:-4]
        pdb_path = os.path.join(pdb_dir, pdb_file)
        xtc_path = os.path.join(xtc_dir, mutant_name + ".xtc")

        if not os.path.exists(xtc_path):
            print(f"Skipping {mutant_name}: missing xtc file")
            continue

        # Load trajectory
        traj = md.load(xtc_path, top=pdb_path)

        # Compute atom pairs for contacts
        pairs = residue_pairs(traj, res_range_1, res_range_2)

        # Compute contact distances
        dists = md.compute_distances(traj, pairs)  # shape: (frames, pairs)

        # Compute contact probabilities (fraction of frames < cutoff)
        contact_probs = (dists < cutoff).mean(axis=0)

        # Sum over all pairs
        contact_sum = contact_probs.sum()

        # Write result
        with open(output_file, "a") as f_out:
            f_out.write(f"{mutant_name},{contact_sum:.4f}\n")

        print(f"{mutant_name}: {contact_sum:.4f}")

print(f"Done! Results saved to {output_file}")
