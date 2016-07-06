# Generates a list of 100 non-unique 4 digit binary sequences
# Maximum unique codes is 16

import random

input_file_name = "input.txt"
lines = 10000
sequence_length = 4

def generate_input():
	global lines
	genned_lines = 0
	sequences = ""
	while genned_lines < lines:
		sequences = sequences + gen_binary_sequence() + "\n"
		genned_lines = genned_lines + 1
	if sequences.endswith("\n"):
		sequences = sequences[:-1]
	return sequences

def gen_binary_sequence():
	global sequence_length
	sequence = ""
	while len(sequence) < sequence_length:
		sequence = sequence + str(random.randint(0, 1))
	return sequence

random.seed(14051991)
input_file = open(input_file_name, "w")
input_file.write(generate_input())