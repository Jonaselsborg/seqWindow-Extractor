# Sequence Window Extractor
A small Python script to extract sequence windows from protein FASTA files around specified sites.

## Overview
This script reads protein sequences from FASTA files and extracts sequence windows around user-specified sites. It is useful for sequence analysis tasks where context around a particular residue is needed (e.g., PTM site analysis).  

- **Input:** Protein ID and site position in a protein.  
- **Output:** Sequence windows around the site.  
- **Default window size:** ±25 residues (total 51 amino acids).  
- Pads with underscores (`_`) if the window extends beyond the protein termini.

## Requirements

- Python 3.x
- Standard Python libraries: `os`, `glob`
- **FASTA files:** Should have `.fasta` extension. Protein ID is extracted from the second field of the header (`>sp|ProteinID|...`).
- **Input files:** Plain text files with two columns:  

### Input example
```
P09874 499
P33778 10
```
## Usage

1. Place all FASTA files in the `fasta/` folder.
2. Place input files with protein IDs and sites in the `input/` folder.
3. Run the script:

*... directly*
```python
python seqWindow-Extractor.py
```
*... as module*
```python
from sequence_window_extractor import process_input

process_input()
```
4. Results will be saved in the `output/` folder as `result_<input_filename>.txt`, with columns:
```
ProteinID    Site    Sequence_Window
```

## Functions
* `read_fasta_files(folder="fasta")`
Reads all FASTA files in the specified folder and returns a dictionary of protein sequences.

* `extract_window(sequence, site, window_size=51)`
Extracts a sequence window around the given site, padding with underscores if necessary.

* `process_input(input_folder="input", output_folder="output", fasta_folder="fasta")`
Reads input files, extracts sequence windows for all specified sites, and writes results to the output folder.
