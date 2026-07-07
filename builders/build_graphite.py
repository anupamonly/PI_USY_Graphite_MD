#!/usr/bin/env python3

from ase.build import graphene
from ase.io import write
from ase import Atoms
import numpy as np
import os

# -----------------------------
# Parameters
# -----------------------------
a = 2.46           # lattice constant
vacuum = 3.35      # graphite interlayer spacing (Å)

nx = 8
ny = 8
nz = 4

# -----------------------------
# Build one graphene layer
# -----------------------------
layer = graphene(formula="C2",
                 a=a,
                 vacuum=0.0)

layer = layer.repeat((nx, ny, 1))

atoms = Atoms()

# -----------------------------
# Stack layers
# -----------------------------
for i in range(nz):

    new_layer = layer.copy()

    pos = new_layer.get_positions()

    pos[:,2] += i * vacuum

    new_layer.set_positions(pos)

    atoms += new_layer

# -----------------------------
# Simulation cell
# -----------------------------
cell = layer.cell.copy()

cell[2,2] = nz * vacuum + 10.0

atoms.set_cell(cell)

atoms.set_pbc([True, True, True])

# -----------------------------
# Output
# -----------------------------
os.makedirs("data", exist_ok=True)

write("data/graphite.xyz", atoms)
write("data/graphite.cif", atoms)
write("data/graphite.data", atoms, format="lammps-data")

print("="*60)
print("GRAPHITE GENERATED")
print("="*60)
print("Atoms :", len(atoms))
print("Files:")
print(" data/graphite.xyz")
print(" data/graphite.cif")
print(" data/graphite.data")
print("="*60)
