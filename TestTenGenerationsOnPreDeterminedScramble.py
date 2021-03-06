from Cube import Cube
from Brain import Brain
from copy import deepcopy
import HelperFunctions

#training 50 brains on one cube.
if __name__=="__main__":
    #initialize 50 random brains
    TheBrains = []
    for i in range(0,50):
        TheBrains.append(Brain())
        #try brains with 2 internal layers, each with 50 neurons
        TheBrains[i].InitializeRandomLayerNeurons(2,50)
    #Determine the initial scrambles for our cubes
    ScrambleList = []
    for i in range(0,1):
        ScrambleList.append(HelperFunctions.GenerateScramble(20))
    #test ten generations
    for Generation in range(0,59):
        print()
        print("Testing Generation: "+str(Generation))
        BestBrains = HelperFunctions.TrainAGeneration(TheBrains,ScrambleList,5)
        TheBrains = []
        for BrainElement in BestBrains:
            TheBrains = TheBrains + HelperFunctions.MakeNewGenerationFromBrain(BrainElement,10)
    BestBrains = HelperFunctions.TrainAGeneration(TheBrains,ScrambleList,1) #Here is our leading contender
    DemoCube = Cube()
    DemoCube.PerformPredeterminedScramble(ScrambleList[0])
    HelperFunctions.PerformExhibitionSolve(DemoCube,BestBrains[0])
    
