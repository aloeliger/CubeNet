import Neuron
import random

class Brain():
    def __init__(self):
        ResetInputNeurons()
        ResetOutputNeurons()
        self.LayerNodes = {}
    #neuron ID's 111-966 are reserved for input neurons
    #Special mapping will tell what each neuron is.
    def ResetInputNeurons(self):
        self.InputNeurons={}
        for i in range(1,10):
            for j in range(1,7):
                for k in range(1,7):
                    InputNeurons[i*100+j*10+k]=Neuron(i*100+j*10+k)

    #Neuron ID's 1-12 are reserved for output
    def ResetOutputNeurons(self):
        self.OutputNeurons={}
        for i in range(1,13):
            OutputNeurons[i]=OutputNeuron(i)

    #so I think the plan is this?, what we do is we generate neurons in layers,
    #and focibly connect layer to layer. Each neuron in the preceding layer to each
    #neuron in the next layer. Not quite the net I had in mind, but...
    #whatever, flying by the seat of my pants here. We can change this after the brain works
    def InitializeRandomLayerNeurons(self):
        IDNumber=1000
        PreviousNeuronLayer = self.InputNeurons
        CurrentLayerNeurons=[]
        for i in range(1,6): # Five layers
            for j in range (1,100): #100 neurons each
                CurrentLayerNeurons.append(Neuron(IDNumber))
                IDNumber+=1.0
                self.LayerNodes[IDNumber]=CurrentLayerNeurons[j]
                for NodeElement in PreviousNeuronLayer:
                    NodeElement.ForwardPropagatorNodes[IDNumber]=CurrentLayerNeurons[j]
                    NodeElement.ForwardPropagotWeights[IDNumber]=random.randint(-100,100)
                PreviousNeuronLayer = CurrentLayerNeuons
                CurrentLayerNeurons = []
        #now we attach the last layer of neurons to the output neuron layer.
        for NodeElement in PreviousNeuronLayer:
            for i in range(1,13):
                NodeElement.ForwardPropagatorNodes[i]=self.OutputNeurons[i]
                NodeElement.ForwardPropagatorWeights[i]=random.randint(-100,100)
        
