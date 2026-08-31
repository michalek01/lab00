# Lab 00
# Isaac Michalek
# ToDo: The Scenario: You need to process a 2D grid of raw sensor readings, flattening the data into a single sequence while filtering out noise.

# Your Task: Write a function flatten_and_filter(matrix) that takes a list of lists containing integers.
#Use nested for loops to iterate through each row, and each item within that row.
#Filter the items to keep only even int elements.
#Cube each of these filtered elements (e.g., x ** 3).
#Append the results to a single 1D list and return it.
def flatten_and_filter(matrix):
    result = []
    for row in matrix:
        for item in row:
            if item % 2 == 0:
                result.append(item ** 3)
    return result
print(flatten_and_filter([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#ToDo: The Scenario: You need to calculate the number of steps required for a starting integer to resolve to 1 under the rules of the Collatz conjecture.
#Your Task: Write a function collatz_steps(n) that uses a while loop.
#Define a loop that continues as long as n > 1.
#Inside the loop, if n is even, divide it by 2 (using integer division //).
#If n is odd, multiply it by 3 and add 1.
#Keep track of how many total steps (iterations) it takes to reach 1, and return that count.
def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps
print(collatz_steps(6))


#ToDo: The Scenario: You are analyzing a string of genetic data and need to determine the frequency of each nucleotide.
#Your Task: Write a function nucleotide_count(sequence).
#Accept a string representing a sequence (e.g., "GATTACA").
#Iterate through the string and populate a dictionary counting the occurrences of each character.
#Ensure your code safely handles the first time it encounters a character without throwing a KeyError (you may use .get() or a manual if/else check).
#Return the resulting dictionary.
def nucleotide_count(sequence):
    count_dict = {}
    for nucleotide in sequence:
        if nucleotide in count_dict:
            count_dict[nucleotide] += 1
        else:
            count_dict[nucleotide] = 1
    return count_dict
print(nucleotide_count("GATTACA"))

#ToDo: The Scenario: You have two separate lists of student IDs representing rosters for CS 202 and CS 303, and you need to find the enrollment overlaps and differences.

#Your Task: Write a function compare_enrollments(roster_a, roster_b).

#Convert the two input lists into Python set objects.
#Using built-in set operations, return a new dictionary containing:
#"both": IDs present in both rosters.
#"only_a": IDs exclusively in roster A.
#"only_b": IDs exclusively in roster B.
#"all_unique": A combined set of every unique ID across both rosters.
def compare_enrollments(roster_a, roster_b):
    set_a = set(roster_a)
    set_b = set(roster_b)

    result = {
        "both": list(set_a & set_b),
        "only_a": list(set_a - set_b),
        "only_b": list(set_b - set_a),
        "all_unique": list(set_a | set_b)
    }

    return result
print(compare_enrollments([1, 2, 3, 4], [3, 4, 5, 6]))

# The code that felt most unfamilar with me was the nucleotide_count function.
# I struggled with github and cloning the repo
# For function 2, For me to prevent an infinite loop I had to make sure that the while loop had a condition that would eventually be met, which was n > 1. I also had to ensure that the operations inside the loop would eventually lead to n becoming 1.