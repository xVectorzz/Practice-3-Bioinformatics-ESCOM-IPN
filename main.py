from collections import defaultdict
import periodictable

def get_mass(symbol):
    try:
        return getattr(periodictable, symbol).mass
    except AttributeError:
        return 0.0

f = open("1JMQ.pdb","r")
text = f.read().splitlines()
f.close()


chains = defaultdict(list)

for r in text:
    if r.startswith("ATOM"):
        element = r[76:78].strip()   # columna del elemento químico
        chain = r[21]                # cadena (A, B, etc.)
        x = float(r[30:38])
        y = float(r[38:46])
        z = float(r[46:54])
        chains[chain].append((x, y, z, element))

# 3. Calcular centroides y COM
for chain, atoms in chains.items():
    # --- Todos los átomos ---
    n = len(atoms)
    centroid_all = (
        sum(a[0] for a in atoms)/n,
        sum(a[1] for a in atoms)/n,
        sum(a[2] for a in atoms)/n
    )
    total_mass = sum(get_mass(a[3]) for a in atoms)
    com_all = (
        sum(a[0]*get_mass(a[3]) for a in atoms)/total_mass,
        sum(a[1]*get_mass(a[3]) for a in atoms)/total_mass,
        sum(a[2]*get_mass(a[3]) for a in atoms)/total_mass
    )

    # --- Excluyendo hidrógenos ---
    atoms_noH = [a for a in atoms if a[3] != "H"]
    n_noH = len(atoms_noH)
    centroid_noH = (
        sum(a[0] for a in atoms_noH)/n_noH,
        sum(a[1] for a in atoms_noH)/n_noH,
        sum(a[2] for a in atoms_noH)/n_noH
    )
    total_mass_noH = sum(get_mass(a[3]) for a in atoms_noH)
    com_noH = (
        sum(a[0]*get_mass(a[3]) for a in atoms_noH)/total_mass_noH,
        sum(a[1]*get_mass(a[3]) for a in atoms_noH)/total_mass_noH,
        sum(a[2]*get_mass(a[3]) for a in atoms_noH)/total_mass_noH
    )

    # 4. Imprimir resultados
    print(f"Cadena {chain}")
    print("  Centroide (todos):", centroid_all)
    print("  COM (todos):      ", com_all)
    print("  Centroide (no H): ", centroid_noH)
    print("  COM (no H):       ", com_noH)
