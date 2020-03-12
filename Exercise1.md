# Exercise 1: The basics
Skip this exercise if you feel comfortable coding in Python. This exercise is meant a repetition of the Python learned in BIOS1100.

Try to solve everything first before looking at the solution. If you are stuck, have a look at the slides or other material online.

## Exercise 1a
* Write a program that stores the two sequences `ACTG` and `TCCG` in two separate variables.
* Write Python codes that prints these two sequences joined together (the sequence `ACTGTCCG` should be printed)
* What is the length of the resulting sequence? Write Python code that prints the length of the resulting sequence.

## Exercise 1b
The formula for DNA melting temperature is `4(G+C) + 2(A+T)` where G, C, A and T are the number of times the bases occur in the sequence.
Assume you start with the following code, add a line that computes the melting temperature and another line that pints the melting temperature:
```python
A = 2
C = 4
G = 3
T = 5
# add your code here ...
```

# Exercise 1c
Now create a function that takes four arguments, A, C, G, and T and returns the melting temperature. 
The name of your function should be `compute_meting_temperature`.

Call your functions with the values for A, C, G, and T given in the previous exercise, print the return value and make sure you get the same melting temperature in the previous exercise.

# Exercise 1d
The following function is supposed to return True if a DNA sequence is valid DNA and False if not. There is something wrong this code. Find the error and make the code work.
If you find this difficult, try testing the code with a few sequences, and insert print statements in the code that can help you understand what happens.
```python
def sequence_is_valid_dna(sequence):
    for base in sequence:
        if base is not "A" or base is not "C" or base is not "G" or base is not "T" or base is not "N":
            return False
            
        return True

``` 
PS: We allow A, C, T, G and N (since N is used to denote unknown nucleotide).

Bonus task: The if-sentence is a bit clumsy. Do you know a way to make it more concise? Hint: Lists


# Exercise 1e


# Exercise 1d
GC-content is the ratio of number of `G`s and `C`s in a DNA sequence.


