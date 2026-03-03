#Bio.PDB is a Biopython module used to parse, a
#analyze, and extract information from protein 3D structure files (PDB format).

from Bio.PDB import PDBParser, PPBuilder
# Parse PDB file
parser = PDBParser(QUIET=True)
structure = parser.get_structure("protein", "2RGT.pdb")
# Print chain IDs
for model in structure:
    for chain in model:
        print("Chain:", chain.id)
# Extract amino acid sequence
ppb = PPBuilder()
for pp in ppb.build_peptides(structure):
    print("Sequence:", pp.get_sequence())
