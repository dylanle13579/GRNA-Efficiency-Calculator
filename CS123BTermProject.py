import sys
import re
import csv

def read_fasta(filepath):
    """
    Reads a FASTA file and returns the seuqence in the FASTA file
    """
    sequences = {}
    header = None
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                header = line[1:]
                sequences[header] = ''
            elif header:
                sequences[header] += line.upper()
    return sequences

def gc_content(seq):
    """
    Calculates GC(Guanine Cytosine) content as a percentage
    """
    gc = seq.count('G') + seq.count('C')
    return round((gc / len(seq)) * 100, 2)

def predict_efficiency(grna):
    """
    List efficiency based on the following criteria
    - High if GC content is 40-60% and no TTTT
    - Medium if GC > 60%
    - Low if GC < 40%
    - Poor if 'TTTT' present
    """
    gc = gc_content(grna)
    if 'TTTT' in grna:
        return 'Poor'
    elif 40 <= gc <= 60:
        return 'High'
    elif gc > 60:
        return 'Medium'
    else:
        return 'Low'

def find_grnas(sequence, pam='GG'):
    """
    Searches for all 20 base pair gRNAs followed by PAM
    """
    grnas = []
    for i in range(len(sequence) - 23):
        gRNA = sequence[i:i+20]
        pam_seq = sequence[i+20:i+23]
        if pam_seq.endswith(pam):
            gc = gc_content(gRNA)
            score = predict_efficiency(gRNA)
            grnas.append({
                'gRNA': gRNA,
                'PAM': pam_seq,
                'Position': i,
                'GC%': gc,
                'Predicted_Efficiency': score
            })
    return grnas

def write_to_csv(results, output_path):
    keys = results[0].keys()
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

def run_grna_analysis(input_path, output_path):
    all_results = []
    sequences = read_fasta(input_path)
    for header, seq in sequences.items():
        grnas = find_grnas(seq)
        for result in grnas:
            result['Sequence_ID'] = header
            all_results.append(result)
    if not all_results:
        print("No valid gRNAs found.")
    else:
        return write_to_csv(all_results, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python CS123BTermProject.py input.fasta output.csv")
        sys.exit(1)

    input_fasta = sys.argv[1]
    output_csv = sys.argv[2]

    df = run_grna_analysis(input_fasta, output_csv)
    if df is not None:
        print(df.head())
