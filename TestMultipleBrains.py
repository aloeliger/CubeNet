from Cube import Cube
from Brain import Brain
#attempts a solve, and returns the fitness of the solve
def AttemptSolve(TheCube,TheBrain):
    Moves = 0
    while (Moves <= 100 and TheCube.IsNotSolved()):
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
    #We inverse weight the
    return 100000*NumSolvedElements+(100-Moves)

if __name__=="__main__":
    #initial Brains
    NewBrains = []
    for i in range(0,10):
        NewBrains.append(Brain())
        #try brains with 2 neuron layers, 40 neurons 
        NewBrains[i].InitializeRandomLayerNeurons(2,40)
    #okay, let each brain try and solve a hundred scrambled cubes
    HighestFitness = 0
    for i in range(0,10):
        print("Testing Brain: "+str(i))
        Fitness = 0
        BestBrain = 0
        for j in range(0,100):
            NewCube = Cube()
            NewCube.ScrambleCube(20)
            Fitness+=AttemptSolve(NewCube,NewBrains[i])
        print("Brain "+str(i)+" Overall Fitness: "+str(Fitness))
        print("Brain "+str(i)+" Average Fitness: "+str(Fitness/100.0))
        if(Fitness > HighestFitness):
            HighestFitness = Fitness
            BestBrain = i
    print("Best Fitness: "+str(HighestFitness))
    print("Best Brain: "+str(BestBrain))
    
