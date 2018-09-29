from Neuron import Neuron
from Neuron import OutputNeuron
import random

class Brain():
    def __init__(self):
        self.ResetInputNeurons()
        self.ResetOutputNeurons()
        self.LayerNodes = {}
    #neuron ID's 111-966 are reserved for input neurons
    #Special mapping will tell what each neuron is.
    def ResetInputNeurons(self):
        self.InputNeurons={}
        for i in range(1,10):
            for j in range(1,7):
                for k in range(1,7):
                    self.InputNeurons[i*100+j*10+k]=Neuron(i*100+j*10+k)

    #Neuron ID's 1-12 are reserved for output
    def ResetOutputNeurons(self):
        self.OutputNeurons={}
        for i in range(1,13):
            self.OutputNeurons[i]=OutputNeuron(i)

    #takes the numbers of layers to generate, and the numbers of neurons in a layer.
    #layer Neuron ID's are 1000 up.
    def InitializeRandomLayerNeurons(self,layers,neurons):
        IDNumber=1000
        PreviousNeuronLayer = self.InputNeurons
        CurrentLayerNeurons={}
        for i in range(0,layers):
            for j in range(0,neurons):
                CurrentLayerNeurons[IDNumber]=Neuron(IDNumber)
                self.LayerNodes[IDNumber]=CurrentLayerNeurons[IDNumber]
                #I think that before I'm done with this function and this class,
                #I'm going to want a list with dictionaries for each of the layers.
                IDNumber+=1
            for PreviousNeuronID in PreviousNeuronLayer:
                #pick the element we're going to use
                ElementID = random.choice(list(CurrentLayerNeurons.keys()))
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorNodes[ElementID]=CurrentLayerNeurons[ElementID]
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorWeights[ElementID]=random.randint(-2,2)
            for NeuronID in CurrentLayerNeurons:
                if(not IsConnectedInLayer(PreviousNeuronLayer,NeuronID)):
                    #Pick an ID at random from the previous layer, and hook it up.
                    PreviousNeuronID = random.choice(list(PreviousNeuronLayer.keys()))
                    PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorNodes[NeuronID] = CurrentLayerNeurons[NeuronID]
                    PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorWeights[NeuronID] = random.randint(-2,2)
            #make a few more random connections
            for PreviousNeuronID in PreviousNeuronLayer:
                NumExtraNeurons = random.randint(2,5)
                NeuronsToAdd = random.sample(list(CurrentLayerNeurons.keys()),NumExtraNeurons)
                for NeuronID in NeuronsToAdd:
                    PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorNodes[NeuronID] = CurrentLayerNeurons[NeuronID]
                    PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorWeights[NeuronID] = random.randint(-2,2)
            PreviousNeuronLayer = CurrentLayerNeurons
            CurrentLayerNeurons = {}
        # hook up next-to-last layer and output neurons.
        for PreviousNeuronID in PreviousNeuronLayer:
            NumFinalConnections = random.randint(2,5)
            NeuronsToAdd = random.sample(list(self.OutputNeurons.keys()),NumFinalConnections)
            for NeuronID in NeuronsToAdd:
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorNodes[NeuronID] = self.OutputNeurons[NeuronID]
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorWeights[NeuronID] = random.randint(-2,2)
        for OutputNeuronID in self.OutputNeurons:
            if(not IsConnectedInLayer(PreviousNeuronLayer,OutputNeuronID)):
                PreviousNeuronID = random.choice(list(PreviousNeuronLayer.keys()))
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorNodes[OutputNeuronID] = self.OutputNeurons[OutputNeuronID]
                PreviousNeuronLayer[PreviousNeuronID].ForwardPropagatorWeights[OutputNeuronID] = random.randint(-2,2)        
                
    def GetHighestOutputNeuron(self):
        HighestNeuronID = 1
        for ID in range(2,13):
            if(self.OutputNeurons[ID].AccumulatedWeight > self.OutputNeurons[HighestNeuronID].AccumulatedWeight):
                HighestNeuronID = ID
        return HighestNeuronID
        
    def ClearOutputNeurons(self):
        for NeuronID in self.OutputNeurons:
            self.OutputNeurons[NeuronID].Clear()

    #okay, how do we modify the brain?
    #options:
    #1.) Take the best brain, copy it, with random modifications.
    #2.) Take the two best brains. find a way to cross the weights/genomes.
    #        -Add in random mutations at points to keep the process moving forward.
    #3.) Others?
    #We'll start with the easiest to implement: 1.)
    #def MutateBrain(self):

# a helper function that doesn't really need to be a part of the class?
#Takes the previous Layer Dictionary, and a urrent layer ID number
#it will then search the previous layer dictionary
def IsConnectedInLayer(PreviousLayer,CurrentNodeID):
    IsConnected = False
    for PreviousNodeID in PreviousLayer:
        for ConnectedNodes in PreviousLayer[PreviousNodeID].ForwardPropagatorNodes:
            if(CurrentNodeID == ConnectedNodes):
                IsConnected = True
    return IsConnected
