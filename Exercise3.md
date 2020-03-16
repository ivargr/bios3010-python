**NOTE:** This Exercise is a more difficult version of Exercise 2. If you find this one tricky, it is okay to do Exercise 2 instead.

# Exercise 3: Using a promoter sequence profile from E. coli to look for matches in its genome


You may remember the E. coli promoter sequence profile from week 11 (page 4 in the slides).

The matrix tells you how often A, C, T and G are observed at the various positions in promoter sequences from E. coli:

```python
    1       2       3       4       5       6
A   0.04    0.88    0.26    0.59    0.49    0.03
C   0.09    0.03    0.11    0.13    0.22    0.05 
G   0.07    0.01    0.12    0.16    0.12    0.02 
T   0.8     0.08    0.51    0.12    0.17    0.89
```

From the matrix, one can for instance see that C occurs 11% of the times at position 2 in the observed sequences.

We here provide Python code that represents this matrix as a list of dictionaries. The outer list represents all the positions (0 to 5). Every element in the list is a dictionary where we can look up the probabilities for A, C, G and T at the given position.


```python
profile = [
    {"A": 0.04, "C": 0.09, "G": 0.07, "T": 0.8, "N": 0},
    {"A": 0.88, "C": 0.03, "G": 0.01, "T": 0.08, "N": 0},
    {"A": 0.26, "C": 0.11, "G": 0.12, "T": 0.51, "N": 0},
    {"A": 0.59, "C": 0.13, "G": 0.16, "T": 0.12, "N": 0},
    {"A": 0.49, "C": 0.22, "G": 0.12, "T": 0.17, "N": 0},
    {"A": 0.03, "C": 0.05, "G": 0.02, "T": 0.90, "N": 0},
]
```
Note: We include N with probability 0 to later support sequences that contains Ns.

# Exercise 3a
Copy the above code to your own Python script. Write a print statement that prints the dictionary at position 2. Verify that you get this output:
```python
{'A': 0.88, 'C': 0.03, 'G': 0.01, 'T': 0.08, 'N': 0}
```

Write Python code that returns the probability of observing a C on position 2. You should get `0.03` if you do this correctly.


# Exercise 3b
Write a function that takes a profile matrix, a position and a nucleotide as parameters, and returns the probability of observing the given nucleotide at that position. Your function should look like this:

```python
def probability(profile, position, nucleotide):
    # fill in the function body ...
    
    return ...
```

Note: There will not be much code in this function body, and it may seem a bit unecessary to create a function for this. 
However, you will see in the later exercises that this makes things a bite easier and your code more pretty since you can forget about indexing the profile matrix.


# Exercise 3c
We assume the probability of observing a given 6 base pairs long sequence in a promoter is the product of the profile probability for each nucleotide.

For instance, using this asssumption, the probability of observing the sequence `AAAAAT` is `0.04 * 0.88 * 0.26 * 0.59 * 0.49 * 0.89`.

Write a function that takes two arguments -- a profile matrix and a 6 base pair long sequence -- and returns the probability of observing that sequence given the profile matrix.

```python
def probability_of_sequence(profile, sequence):
    # continue here ...
    # hint, you will need a for loop iterating over each nucleotide in the sequence
    
    return ....
```

Call this function with the sequence "AAAAAT". Verify that you get the same output that you get if you compute the probability by hand.

# Exercise 3d
We now want to read the whole E. coli genome sequence and compute the probability at every position in the genome. This way we can predict where promoters are likely to occur.

The E. coli fasta sequence can be [downloaded here](https://github.com/ivargr/bios3010-python/raw/master/ecoli.fasta). The first line is a header line, and the full sequence is on the rest of the lines.

Write a function `read_fasta` that takes a file name as argument and returns the sequence in the fasta file (assuming the fasta file only has one header line and one sequence spread out on the rest of the lines).

You will need to iterate the lines and merge all the sequences. Remember to strip each line so that you don't get line breaks.

# Exercise 3e
Call the `read_fasta` function with `ecoli.fasta` as input parameter. How long is the E. coli sequence?

# Exercise 3f
Write a function that computes the probability of every 6 base pair long sequence in a genome sequence. Your function should take a profile matrix and a genome sequence as input, and return a list of probabilities.

Note: For every position in the genome you will need to get the 6 nucleotides starting at that position. You will not be able to compute the probability for subsequences closer than 6 base pairs to the end of the genome.
Remember that you can get a 6 base pair long subsequence at position `i` like this: `genome_sequence[i:i+6]`.

Call your function with the E. coli sequence and the profile you have used in the previous exercises.

Create a for-loop that goes through all the probabilities that are returned and count how many of the probabilites are above 5%.

# Exercise 3g
We want to also run the analysis in 2f on the COVID-19 genome sequence, which you [will find here](https://raw.githubusercontent.com/ivargr/bios3010-python/master/covid-19.fasta).

Since you have structured your program with functions, that should be easy to do. 

How many positions give more than 5% in the COVID-19 genome? Is this high or low compared to the E. coli genome? What if you divide those numbers by the genome sizes? 
Are you able to explain the differences from a biological perspective?



