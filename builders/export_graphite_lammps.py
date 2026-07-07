#!/usr/bin/env python3

from ase.io import read, write

atoms = read("data/graphite.xyz")

# Write a proper LAMMPS atomic data file
write(
    "data/graphite_lammps.data",
    atoms,
    format="lammps-data",
    atom_style="atomic"
)

print("Created data/graphite_lammps.data")


