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

    #so I think the plan is this?, what we do is we generate neurons in layers,
    #and focibly connect layer to layer. Each neuron in the preceding layer to each
    #neuron in the next layer. Not quite the net I had in mind, but...
    #whatever, flying by the seat of my pants here. We can change this after the brain works
    def InitializeRandomLayerNeurons(self):
        IDNumber=1000
        PreviousNeuronLayer = self.InputNeurons
        CurrentLayerNeurons={}
        for i in range(1,2): # Let's try two layers for now
            for j in range (0,100): #100 neurons each
                #CurrentLayerNeurons.append(Neuron(IDNumber))
                CurrentLayerNeurons[IDNumber]=Neuron(IDNumber)
                self.LayerNodes[IDNumber]=CurrentLayerNeurons[IDNumber]
                for NodeElement in PreviousNeuronLayer:
                    PreviousNeuronLayer[NodeElement].ForwardPropagatorNodes[IDNumber]=CurrentLayerNeurons[IDNumber]
                    PreviousNeuronLayer[NodeElement].ForwardPropagatorWeights[IDNumber]=random.randint(-100,100)
            PreviousNeuronLayer = CurrentLayerNeurons
            CurrentLayerNeurons = {}
            IDNumber+=1.0
        #now we attach the last layer of neurons to the output neuron layer.
        for NodeElement in PreviousNeuronLayer:
            for i in range(1,13):
                PreviousNeuronLayer[NodeElement].ForwardPropagatorNodes[i]=self.OutputNeurons[i]
                PreviousNeuronLayer[NodeElement].ForwardPropagatorWeights[i]=random.randint(-100,100)

    def GetHighestOutputNeuron(self):
        HighestNeuronID = 1
        for ID in range(2,13):
            if(self.OutputNeurons[ID].AccumulatedWeight > self.OutputNeurons[HighestNeuronID].AccumulatedWeight):
                HighestNeuronID = ID
        return HighestNeuronID
        
    def ClearOutputNeurons(self):
        for NeuronID in self.OutputNeurons:
            self.OutputNeurons[NeuronID].Clear()
