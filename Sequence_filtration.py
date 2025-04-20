import sys
from Bio import SeqIO

# Check for correct number of command-line arguments
if len(sys.argv) != 3:
    print("Usage: python Sequence_filtration.py input.fasta output.fasta")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

all_seqs = list(SeqIO.parse(input_file, "fasta"))
print(f"Total sequences: {len(all_seqs)}")

with open(output_file, "w") as out_handle:
    # Iterate through each sequence in the input file
    for record in SeqIO.parse(input_file, "fasta"):
        # Only keep sequences with length >= 300
        if len(record.seq) >= 300:
            # Write the sequence in single-line format
            out_handle.write(f">{record.id} {record.description}\n{str(record.seq)}\n")

filtered_seqs= list(SeqIO.parse(output_file, "fasta"))
print(f"Sequences with length >= 300 nt: {len(filtered_seqs)}")
print(f"Filtered single-line FASTA saved as: {output_file}")
