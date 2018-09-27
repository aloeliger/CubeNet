class Neuron():
    def __init__(self,AssignedNumber):
        self.IDNumber=AssignedNumber
        self.ForwardPropagatorWeights = {}
        self.ForwardPropagatorNodes = {}

    def Activate(self,Weight):
        for i in self.ForwardPropagatorNodes:
            self.ForwardPropagatorNodes[i].Activate(Weight+self.ForwardPropagatorWeights[i])
    
class OutputNeuron(Neuron):
    def __init__(self,AssignedNumber):
        self.IDNumber=AssignedNumber
        self.AccumulatedWeight = 0
    def Activate(self,Weight):
        self.AccumulatedWeight+=Weight
    def Clear(self):
        self.AccumulatedWeight = 0
