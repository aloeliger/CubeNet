from Cube import Cube
from Brain import Brain
from copy import deepcopy
import random

#takes a scrambled cube, and a test brain
#returns a special fitness number, that details how well the brain did solving this cube
def AttemptSolve(TheCube, TheBrain):
    Moves = 0
    while (Moves < 100 and TheCube.IsNotSolved()):
        InputNeuronsToActivate = TheCube.GetInputNeuronsToActivate()
        for NeuronID in InputNeuronsToActivate:
            TheBrain.InputNeurons[NeuronID].Activate(0) #don't weight the starting gun
        HighestOutputNeuron = TheBrain.GetHighestOutputNeuron()
        if HighestOutputNeuron == 1:
            TheCube.RotateWhiteFaceRight()
        elif HighestOutputNeuron == 2:
            TheCube.RotateWhiteFaceLeft()
        elif HighestOutputNeuron == 3:
            TheCube.RotateRedFaceRight()
        elif HighestOutputNeuron == 4:
            TheCube.RotateRedFaceLeft()
        elif HighestOutputNeuron == 5:
            TheCube.RotateBlueFaceRight()
        elif HighestOutputNeuron == 6:
            TheCube.RotateBlueFaceLeft()
        elif HighestOutputNeuron == 7:
            TheCube.RotateGreenFaceRight()
        elif HighestOutputNeuron == 8:
            TheCube.RotateGreenFaceLeft()
        elif HighestOutputNeuron == 9:
            TheCube.RotateOrangeFaceRight()
        elif HighestOutputNeuron == 10:
            TheCube.RotateOrangeFaceLeft()
        elif HighestOutputNeuron == 11:
            TheCube.RotateYellowFaceRight()
        elif HighestOutputNeuron == 12:
            TheCube.RotateYellowFaceLeft()

        TheBrain.ClearOutputNeurons()
        Moves += 1
    #out of the loop. Evaluate how we did
    #fitness of this particular solve is broken down into two parts.
    #did the brain solve the cube?
    #and how many moves did it take?
    #The solve can be broken down into how many elements are solved
    #we give a full solve a score of a perfect hundred
    NumSolvedElements = TheCube.GetNumSolvedElements()
    if(NumSolvedElements == 54):
        NumSolvedElements = 100
    return 1000*NumSolvedElements+(100-Moves)

#This will take in a list of brains and a number (x) of brains to return
# returns the x best brains of this generation
def TestAGeneration(BrainList, NumToReturn):
    BrainFitnesses = []
    for i in range(0,len(BrainList)):
        print("Testing Brain #"+str(i))
        Fitness = 0
        for j in range(0,100):
            NewCube = Cube()
            NewCube.ScrambleCube(20)
            Fitness+=AttemptSolve(NewCube,BrainList[i])
        print("Brain Fitness: "+str(Fitness))
        BrainFitnesses.append(Fitness)
    BrainsToReturn = []
    for i in range (0,NumToReturn):
        MaxFitness = max(BrainFitnesses)
        BrainsToReturn.append(BrainList[BrainFitnesses.index(MaxFitness)])
        BrainList.pop(BrainFitnesses.index(MaxFitness))
        BrainFitnesses.pop(BrainFitnesses.index(MaxFitness))
    return BrainsToReturn

#similar to the test a generation function
#except it takes a list of prescrambles
def TrainAGeneration(BrainList, ScrambleList, NumToReturn):
    BrainFitnesses = []
    for i in range(0,len(BrainList)):
        #print("Brain: "+str(i))
        Fitness = 0
        for j in range(0,len(ScrambleList)):
            NewCube = Cube()
            NewCube.PerformPredeterminedScramble(ScrambleList[j])
            Fitness+=AttemptSolve(NewCube,BrainList[i])
        #print("BrainFitness: "+str(Fitness))
        BrainFitnesses.append(Fitness)
        BrainList[i].Fitness = Fitness
    BrainsToReturn = []
    for i in range (0,NumToReturn):
        MaxFitness = max(BrainFitnesses)
        BrainsToReturn.append(BrainList[BrainFitnesses.index(MaxFitness)])
        BrainList.pop(BrainFitnesses.index(MaxFitness))
        BrainFitnesses.pop(BrainFitnesses.index(MaxFitness))
    return BrainsToReturn

#Takes a brain, and a number x
# it then makes x mutated copies of that brain, and returns them
def MakeNewGenerationFromBrain(TheBrain, NumCopies):
    BrainsToReturn = []
    for i in range(0,NumCopies):
        BrainsToReturn.append(deepcopy(TheBrain))
        BrainsToReturn[i].MutateBrain()
    return BrainsToReturn

#Takes a scrambled Cube and a Brain,
#makes the brain perform a solve, and prints the results step by step
def PerformExhibitionSolve(TheCube, TheBrain):
    print("Initial Position:")
    TheCube.Print()
    print()
    Moves = 0
    while (Moves < 100 and TheCube.IsNotSolved()):
        InputNeuronsToActivate = TheCube.GetInputNeuronsToActivate()
        for NeuronID in InputNeuronsToActivate:
            TheBrain.InputNeurons[NeuronID].Activate(0) #don't weight the starting gun
        HighestOutputNeuron = TheBrain.GetHighestOutputNeuron()
        if HighestOutputNeuron == 1:
            TheCube.RotateWhiteFaceRight()
        elif HighestOutputNeuron == 2:
            TheCube.RotateWhiteFaceLeft()
        elif HighestOutputNeuron == 3:
            TheCube.RotateRedFaceRight()
        elif HighestOutputNeuron == 4:
            TheCube.RotateRedFaceLeft()
        elif HighestOutputNeuron == 5:
            TheCube.RotateBlueFaceRight()
        elif HighestOutputNeuron == 6:
            TheCube.RotateBlueFaceLeft()
        elif HighestOutputNeuron == 7:
            TheCube.RotateGreenFaceRight()
        elif HighestOutputNeuron == 8:
            TheCube.RotateGreenFaceLeft()
        elif HighestOutputNeuron == 9:
            TheCube.RotateOrangeFaceRight()
        elif HighestOutputNeuron == 10:
            TheCube.RotateOrangeFaceLeft()
        elif HighestOutputNeuron == 11:
            TheCube.RotateYellowFaceRight()
        elif HighestOutputNeuron == 12:
            TheCube.RotateYellowFaceLeft()
        TheBrain.ClearOutputNeurons()
        Moves += 1
        print("Move: "+str(Moves))
        TheCube.Print()
        print()

#takes in a number of moves to scramble by
#returns a list to be read by the cube to generate a scramble
def GenerateScramble(NumOfMoves):
    TheScramble = []
    for i in range (0,NumOfMoves):
        TheScramble.append(random.randint(1,12))
    return TheScramble
