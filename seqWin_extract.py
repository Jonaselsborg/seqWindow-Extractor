# Jonas Elsborg
# jonas.elsborg@cpr.ku.dk
# Small script to extract sequence windows from fasta files
# input: protein id; site in protein
# default windows are +/- 25 around the site

import os
import glob

def read_fasta_files(folder="fasta"):
    # Reads all FASTA files in the given folder and returns a dictionary of protein sequences.
    db = {}
    fasta_files = glob.glob(os.path.join(folder, "*.fasta"))  # Get all .fasta files

    for fasta_file in fasta_files:
        with open(fasta_file, "r") as f:
            protein_id = None
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    protein_id = line.split("|")[1]  # Extract protein entry
                    db[protein_id] = ""
                elif protein_id:
                    db[protein_id] += line  # Append sequence to the corresponding protein
    return db


def extract_window(sequence, site, window_size=51):
    # Extracts a sequence window around the given site, padding with underscores if necessary.
    half_window = (window_size - 1) // 2  # 25 residues before and after
    seq_length = len(sequence)

    # Determine start and end positions
    start = max(0, site - half_window - 1)
    end = min(seq_length, site + half_window)

    # Extract sequence and pad if out of bounds
    seq_window = sequence[start:end]
    left_pad = "_" * max(0, half_window - site + 1)
    right_pad = "_" * max(0, half_window - (seq_length - site))

    return left_pad + seq_window + right_pad


def process_input(input_folder="input", output_folder="output", fasta_folder="fasta"):
    # Reads all .txt input files, extracts sequence windows, and writes results to output files.
    db = read_fasta_files(fasta_folder)
    input_files = glob.glob(os.path.join(input_folder, "*.txt"))  # Get all .txt files

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create output folder if it doesn't exist

    for input_file in input_files:
        output_file = os.path.join(output_folder, os.path.basename(input_file))  # Keep same filename

        with open(input_file, "r") as f, open(output_file, "w") as out:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue  # Skip invalid lines
                protein_id, site = parts[0], int(parts[1])

                if protein_id in db:
                    sequence = db[protein_id]
                    seq_window = extract_window(sequence, site)
                    out.write(f"{protein_id}\t{site}\t{seq_window}\n")


# Example usage
process_input()
