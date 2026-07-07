#!/usr/bin/env python3

import matplotlib.pyplot as plt

steps = []
temp = []
pe = []
ke = []
etotal = []
press = []

reading = False

with open("log.lammps") as f:
    for line in f:

        if line.startswith("Step"):
            reading = True
            continue

        if reading:

            if line.startswith("Loop"):
                reading = False
                continue

            cols = line.split()

            if len(cols) != 6:
                continue

            try:
                steps.append(int(cols[0]))
                temp.append(float(cols[1]))
                pe.append(float(cols[2]))
                ke.append(float(cols[3]))
                etotal.append(float(cols[4]))
                press.append(float(cols[5]))
            except:
                pass


plt.figure(figsize=(8,5))
plt.plot(steps,temp)
plt.xlabel("Step")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs Time")
plt.grid()
plt.tight_layout()
plt.savefig("analysis/temperature.png",dpi=300)

plt.figure(figsize=(8,5))
plt.plot(steps,pe)
plt.xlabel("Step")
plt.ylabel("Potential Energy (eV)")
plt.title("Potential Energy")
plt.grid()
plt.tight_layout()
plt.savefig("analysis/potential_energy.png",dpi=300)

plt.figure(figsize=(8,5))
plt.plot(steps,etotal)
plt.xlabel("Step")
plt.ylabel("Total Energy (eV)")
plt.title("Total Energy")
plt.grid()
plt.tight_layout()
plt.savefig("analysis/total_energy.png",dpi=300)

plt.figure(figsize=(8,5))
plt.plot(steps,press)
plt.xlabel("Step")
plt.ylabel("Pressure (bar)")
plt.title("Pressure")
plt.grid()
plt.tight_layout()
plt.savefig("analysis/pressure.png",dpi=300)

print("\nAnalysis Complete!\n")
print("Generated:")
print("analysis/temperature.png")
print("analysis/potential_energy.png")
print("analysis/total_energy.png")
print("analysis/pressure.png")
