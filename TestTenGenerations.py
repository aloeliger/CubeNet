from Cube import Cube
from Brain import Brain
from copy import deepcopy
import HelperFunctions

if __name__=="__main__":
    #initialize 10 random brains
    TheBrains = []
    for i in range(0,10):
        TheBrains.append(Brain())
        #try brains with 2 internal layes, each with 40 neurons
        TheBrains[i].InitializeRandomLayerNeurons(2,40)
    #test ten generations
    for Generation in range(0,19):
        print("Testing Generations: "+str(Generation))
        BestBrains = HelperFunctions.TestAGeneration(TheBrains,5)
        TheBrains = []
        for BrainElement in BestBrains:
            TheBrains = TheBrains + HelperFunctions.MakeNewGenerationFromBrain(BrainElement,2)
    BestBrains = HelperFunctions.TestAGeneration(TheBrains,1) #Here is our leading contender
    DemoCube = Cube()
    DemoCube.ScrambleCube(20)
    HelperFunctions.PerformExhibitionSolve(DemoCube,BestBrains[0])
    
