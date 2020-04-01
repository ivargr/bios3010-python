**Note:** Do either this exercise of Exercise 3. Exercise 3 is a more difficult version of this exercise.

# Exercise 2
In this exercise we will analyse the the E. coli genome sequence. You will write function for reading the genome from a fasta file, and analyse it in different ways.


## Exercise 2a
The E. coli fasta sequence can be [downloaded here](https://github.com/ivargr/bios3010-python/raw/master/ecoli.fasta). The first line is a header line, and the full sequence is on the rest of the lines.

Write a function `read_fasta` that takes a file name as argument and returns the sequence in the fasta file (assuming the fasta file only has one header line and one sequence spread out on the rest of the lines).

You will need to iterate the lines and merge all the sequences. Remember to strip each line so that you don't get line breaks.

Hint: If you get stuck, a very similar piece of code is shown in the lectures.

## Exercise 2b
Call your function and store the full sequence in a variable.

What is the genome size (length of the sequence)?

How many G's are there in the sequence? (Remember that you can count the number of subsequences in a sequence with `sequence.count(subsequence)`).

## Exercise 2c
From the lectures in week 11, you might noticed that the sequence `TATAAT` is commoon in promotor regions in the E. coli genome.

We want to find all position in the E. coli genome where the sequence TATAAT is found.

A simple way of doing this in Python is to iterate over every base pair in the genome using a for-loop, picking out the 6 base pair long subsequence from that position,
and checking whether that subsequence is identical to TATAAT.

Write a function called `find_all_tataat_locations(genome_sequence)` that takes a genome sequence as input and returns a list 
of all locations matching `TATAAT`. You can use the following code as a skeleton for your code:

```python
def find_all_tataat_locations(genome_seuquence):

    # We start by making a list that we can store all the locations in
    locations = []
    
    # Iterate all locations except the last 6 base pairs (since we are picking out the next 6 base pairs)
    for i in range(0, len(genome_seuquence) - 6):
        subsequence = genome_seuquence[i:i+6]
        
        # Check match here, 
        
    # continue here ...

matches = find_all_tataat_locations(ecoli_sequence)
print(matches)

```


## Exercise 2d
How many matches are there? 

Divide the number of matches with the length of the genome to get the ratio of matches to genome size.

## Exercise 2e
We want to also run the analysis in 2c and 2d on the COVID-19 genome sequence, which you [will find here](https://raw.githubusercontent.com/ivargr/bios3010-python/master/covid-19.fasta).

Since you have written your program using functions, it should be straight-forward to redo the analysis with the COVID-19 genome.

How many matches do you get in the COVID-19 genome? Is this high or low compared to the E. coli genome? 
Are you able to explain the differences from a biological perspective?


