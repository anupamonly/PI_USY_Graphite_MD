#!/usr/bin/env python3

from pathlib import Path
from rdkit import Chem
from rdkit.Chem import AllChem

INPUT = Path("packmol")
OUTPUT = Path("packmol")

files = [
    "EC.sdf",
    "DMC.sdf",
    "DEC.sdf",
    "LiPF6.sdf",
]

for fname in files:
    path = INPUT / fname

    suppl = Chem.SDMolSupplier(str(path), removeHs=False)
    mol = suppl[0]

    if mol is None:
        print(f"Failed to read {fname}")
        continue

    # Generate 3D coordinates if needed (e.g. LiPF6 downloaded as 2D)
    if mol.GetNumConformers() == 0:
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, randomSeed=42)
        AllChem.UFFOptimizeMolecule(mol)

    xyz = OUTPUT / fname.replace(".sdf", ".xyz")

    conf = mol.GetConformer()

    with open(xyz, "w") as f:
        f.write(f"{mol.GetNumAtoms()}\n")
        f.write(f"{fname}\n")

        for atom in mol.GetAtoms():
            pos = conf.GetAtomPosition(atom.GetIdx())
            f.write(
                f"{atom.GetSymbol():2s} "
                f"{pos.x:12.6f} "
                f"{pos.y:12.6f} "
                f"{pos.z:12.6f}\n"
            )

    print(f"Created {xyz}")
