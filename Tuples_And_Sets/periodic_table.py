num_of_lines = int(input())
unique_compounds = set()

for _ in range(num_of_lines):
    chemical_compounds = input().split()
    for compound in chemical_compounds:
        unique_compounds.add(compound)

for comp in unique_compounds:
    print(comp)
