import random
import numpy

class KohonenNetwork:

	def __init__(self, inputNodes, outputNodes, learningRate, learningRateMod):
		self.inputNodes = inputNodes
		self.outputNodes = outputNodes
		self.learningRate = learningRate
		self.learningRateMod = learningRateMod
		weightMatrix = [[random.random() for x in range(inputNodes)] for y in range(outputNodes)]
		self.weightMatrix = numpy.array(weightMatrix)
		print "New Kohonen Network created with " + str(inputNodes) + " input nodes and " + str(outputNodes) + " output nodes"

	def printSelf(self):
		print self.weightMatrix

	def learn(self, sequence_list):
		for sequence in sequence_list:
			self.learnSequence(map(int, sequence))

	def learnSequence(self, sequence):
		outputNode = self.determineOutputNode(sequence)
		for weightIndex in range(self.inputNodes):
			# print "weightIndex: " + str(weightIndex)
			weight = self.weightMatrix[outputNode, weightIndex]
			# print "weight: " + str(weight)
			inputVal = sequence[weightIndex]
			# print "inputVal: " + str(inputVal)
			modifier = inputVal - weight
			# print "modifier: " + str(modifier)
			netModifier = self.learningRate * modifier
			# print "netModifier: " + str(netModifier)
			newWeight = weight + netModifier
			# print "newWeight: " + str(newWeight)
			self.weightMatrix[outputNode, weightIndex] = newWeight
		if self.learningRate > 0:
			self.learningRate = self.learningRate - self.learningRateMod

	def determineOutputNode(self, sequence):
		bestScore = -1
		bestIndex = -1
		for index in range(self.outputNodes):
		 	weightConfig = self.weightMatrix[index, 0:]
		 	score = self.calcScore(sequence, weightConfig)
		 	if score > bestScore:
		 		bestScore = score
		 		bestIndex = index
		return bestIndex

	def calcScore(self, lista, listb):
		return numpy.sum([a*b for a,b in zip(lista,listb)])

	def classifySequence(self, sequence):
		print "Input " + str(sequence) + " is classified as type " + str(self.determineOutputNode(sequence))

	def classify(self, sequence_list):
		for sequence in sequence_list:
			intSequence = map(int, sequence)
			self.classifySequence(intSequence)