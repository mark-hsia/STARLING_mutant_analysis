#Convert .starling mutants to .pdb .xtc and save to respective directories
#SBATCH --time=10:00:00

from pathlib import Path
import subprocess
import starling

mutantlibrary = Path('/dartfs-hpc/rc/home/k/f0044gk/labhome/Mark/MutantLibrary')

for mutant in mutantlibrary.iterdir():
    if mutant.suffix != ".starling":
        continue

    xtc_out = Path('/dartfs-hpc/rc/home/k/f0044gk/labhome/Mark/MutantLibrary_xtc') / f"{mutant.stem}.xtc"
    pdb_out = Path('/dartfs-hpc/rc/home/k/f0044gk/labhome/Mark/MutantLibrary_pdb') / f"{mutant.stem}.pdb"

    xtcconvert = subprocess.run(["starling2xtc", str(mutant), "-o", str(xtc_out)])
    print(f"{mutant.name} → XTC return code: {xtcconvert.returncode}")

    pdbconvert = subprocess.run(["starling2pdb", str(mutant), "-o", str(pdb_out)])
    print(f"{mutant.name} → PDB return code: {pdbconvert.returncode}")
~                                                                              
