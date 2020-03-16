
# 2a

def read_fasta_file(file_name):
    f = open(file_name)
    first_line = f.readline()

    sequence = ""
    for line in f:
        sequence += line.strip()

    return sequence


# 2b
ecoli_sequence = read_fasta_file("ecoli.fasta")
print("Length of sequence: ", len(ecoli_sequence))
print("There are ", ecoli_sequence.count("G"), " Gs in the genome.")



#2c/2d
def find_all_tataat_locations(genome_seuquence):

    # We start by making a list that we can store all the locations in
    locations = []

    # Iterate all locations except the last 6 base pairs (since we are picking out the next 6 base pairs)
    for i in range(0, len(genome_seuquence) - 6):
        subsequence = genome_seuquence[i:i+6]

        if subsequence == "TATAAT":
            locations.append(i)

    return locations


covid_genome = read_fasta_file("covid-19.fasta")
matches = find_all_tataat_locations(covid_genome)

print("There are ", len(matches), " matches")
print("Ratio of matches to genome size: ", len(matches) / len(covid_genome))
