# Takes an input of binary numbers and just tries to classify them using a Kohonen network

from KohonenNetwork import KohonenNetwork

input_file_name = "input.txt"
inputNodes = 4
outputNodes = 4
learningRate = 0.6
learningRateMod = 0.01

def get_sequences_from_input():
	print "Getting sequences from input file..."
	input_file = open(input_file_name, "r")
	content = input_file.read()
	sequence_list = content.split("\n")
	print str(len(sequence_list)) + " sequences read from input file"
	return sequence_list

sequence_list = get_sequences_from_input()
unique_sequences = set(sequence_list)
k_net = KohonenNetwork(inputNodes, outputNodes, learningRate, learningRateMod);
k_net.printSelf()
k_net.classify(unique_sequences)
k_net.learn(sequence_list)
k_net.printSelf()
k_net.classify(unique_sequences)