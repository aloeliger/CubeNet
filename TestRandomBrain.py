from Cube import Cube
from Brain import Brain

NewCube = Cube()
NewBrain = Brain()

#We have nothing to go on so we just implement a random brain
#let's start with a simple test 1 layer, 40 neurons
NewBrain.InitializeRandomLayerNeurons(1,40)

NewCube.ScrambleCube(20)

print("Starting Cube:")
NewCube.Print()
print()

for Moves in range(0,10):
    print("Move: "+str(Moves))
    #Feed our brain the information and let it reach a decision
    InputNeuronsToActivate = NewCube.GetInputNeuronsToActivate()
    for NeuronID in InputNeuronsToActivate:
        NewBrain.InputNeurons[NeuronID].Activate(0) #don't weight the starting gun
    HighestOutputNeuron = NewBrain.GetHighestOutputNeuron()
    print("Highest Output Neuron is: "+str(HighestOutputNeuron))
    print("With Weight: "+str(NewBrain.OutputNeurons[HighestOutputNeuron].AccumulatedWeight))
    #perform the move
    if HighestOutputNeuron == 1:
        NewCube.RotateWhiteFaceRight()
    elif HighestOutputNeuron == 2:
        NewCube.RotateWhiteFaceLeft()
    elif HighestOutputNeuron == 3:
        NewCube.RotateRedFaceRight()
    elif HighestOutputNeuron == 4:
        NewCube.RotateRedFaceLeft()
    elif HighestOutputNeuron == 5:
        NewCube.RotateBlueFaceRight()
    elif HighestOutputNeuron == 6:
        NewCube.RotateBlueFaceLeft()
    elif HighestOutputNeuron == 7:
        NewCube.RotateGreenFaceRight()
    elif HighestOutputNeuron == 8:
        NewCube.RotateGreenFaceLeft()
    elif HighestOutputNeuron == 9:
        NewCube.RotateOrangeFaceRight()
    elif HighestOutputNeuron == 10:
        NewCube.RotateOrangeFaceLeft()
    elif HighestOutputNeuron == 11:
        NewCube.RotateYellowFaceRight()
    elif HighestOutputNeuron == 12:
        NewCube.RotateYellowFaceLeft()
    print("Leaves us with cube:")
    print()
    NewCube.Print()
    print()
    print("No. Solved Elements: "+str(NewCube.GetNumSolvedElements())+"/54")

    NewBrain.ClearOutputNeurons()
