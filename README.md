# GRNA-Finder-and-Efficiency-Calculator
What the code does
1.Reads DNA sequences from a FASTA file
-FASTA file is a plain text file that stores DNA,RNA and protein sequences
2.Identifies valid CRISPR gRNAs(guide RNAs)
-Outputs 20 base pairs followed by the PAM(Protospacer Adjacent Motif).
    -The PAM is a short DNA sequence ~2-6 base pairs located next to the protospacer, which is the target DNA sequence recognized by the CRISPR-Cas9 system.
3.Calculates GC(guanine-cytosine) content
-This gives insight into the efficiency of gRNAs
4.Predicts an efficiency score
5.Outputs the results to a CSV file

Step by step tutorial
1. Download any gene example FASTA file. For example you can find some in the NCBI database.
2. Using that file you input the command into terminal with the files(CS123BTermProject.py and the FASTA file you downloaded) all in same directory
3. Command should follow this structure:
 python CS123BTermProject.py inputfilename.fasta outputfilename
4.Code should run and your result is outputted into a file with the name of whatever your you chose to be your outputfilename
5.In the output file, it will display the gRNA, PAM, Position of the gRNA, GC%, the predicted efficiency, and Sequence ID of all found gRNAs all in the file.
