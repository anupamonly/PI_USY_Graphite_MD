#!/usr/bin/env python3
"""
export_lammps.py

Utility functions for writing LAMMPS data files.
Author: Anupam Malviya
"""

import numpy as np


class LammpsDataWriter:

    def __init__(self):
        self.atoms = []

    def add_atom(self,
                 atom_id,
                 mol_id,
                 atom_type,
                 charge,
                 x,
                 y,
                 z):

        self.atoms.append([
            atom_id,
            mol_id,
            atom_type,
            charge,
            x,
            y,
            z
        ])

    def write(self,
              filename,
              box,
              masses):

        xmin, xmax, ymin, ymax, zmin, zmax = box

        with open(filename, "w") as f:

            f.write("LAMMPS data generated automatically\n\n")

            f.write(f"{len(self.atoms)} atoms\n")
            f.write(f"{len(masses)} atom types\n\n")

            f.write(f"{xmin:.6f} {xmax:.6f} xlo xhi\n")
            f.write(f"{ymin:.6f} {ymax:.6f} ylo yhi\n")
            f.write(f"{zmin:.6f} {zmax:.6f} zlo zhi\n\n")

            f.write("Masses\n\n")

            for atom_type in sorted(masses.keys()):
                f.write(f"{atom_type} {masses[atom_type]}\n")

            f.write("\nAtoms # full\n\n")

            for atom in self.atoms:

                atom_id,\
                mol_id,\
                atom_type,\
                charge,\
                x,\
                y,\
                z = atom

                f.write(
                    f"{atom_id} "
                    f"{mol_id} "
                    f"{atom_type} "
                    f"{charge:.5f} "
                    f"{x:.6f} "
                    f"{y:.6f} "
                    f"{z:.6f}\n"
                )


if __name__ == "__main__":

    writer = LammpsDataWriter()

    writer.add_atom(
        1,
        1,
        1,
        0.0,
        0.0,
        0.0,
        0.0
    )

    writer.write(
        "test.data",
        (
            0,
            10,
            0,
            10,
            0,
            10
        ),
        {
            1:12.011
        }
    )

    print("test.data written.")
