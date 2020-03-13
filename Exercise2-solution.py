
# 2a
profile = [
    {"A": 0.04, "C": 0.09, "G": 0.07, "T": 0.8, "N": 0},
    {"A": 0.88, "C": 0.03, "G": 0.01, "T": 0.08, "N": 0},
    {"A": 0.26, "C": 0.11, "G": 0.12, "T": 0.51, "N": 0},
    {"A": 0.59, "C": 0.13, "G": 0.16, "T": 0.12, "N": 0},
    {"A": 0.49, "C": 0.22, "G": 0.12, "T": 0.17, "N": 0},
    {"A": 0.03, "C": 0.05, "G": 0.02, "T": 0.90, "N": 0},
]

print(profile[1])


# 2b
def probability(profile, position, nucleotide):
    return profile[position][nucleotide]


print(probability(profile, 3, "T"))


# 2c
def probability_of_sequence(profile, sequence):
    prob = 1.0
    i = 0
    for base in sequence:
        prob *= probability(profile, i, base)
        i += 1

    return prob

print(probability_of_sequence(profile, "AAAAAT"))
print(probability_of_sequence(profile, "TATAAT"))


# 2d
def read_fasta_file(file_name):
    f = open(file_name)
    first_line = f.readline()

    sequence = ""
    for line in f:
        sequence += line.strip()

    return sequence


# 2e
ecoli_sequence = read_fasta_file("ecoli.fasta")
print("Length of sequence: ", len(ecoli_sequence))


# 2f / 2g
def probabilities_across_genome(profile, genome_sequence):
    probabilities = []
    for i in range(0, len(genome_sequence)):
        subsequence = genome_sequence[i:i+6]
        probabilities.append(probability_of_sequence(profile, subsequence))

    return probabilities


#genome_sequence = read_fasta_file("ecoli.fasta")
genome_sequence = read_fasta_file("covid-19.fasta")  # 2g

probabilities = probabilities_across_genome(profile, genome_sequence)
n_high = 0
for p in probabilities:
    if p > 0.02:
        n_high += 1

print(n_high)
print(n_high / len(genome_sequence))



