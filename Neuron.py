class Neuron():
    def __init__(self,AssignedNumber):
        self.IDNumber=AssignedNumber
        self.ForwardPropagatorWeights = {}
        self.ForwardPropagatorNodes = {}

    def Activate(Weight):
        for i in ForwardPropagatorNodes:
            ForwardPropagarorNodes[i].Activate(Weight+ForwardPropagatorWeights[i])
    
class OutputNeuron(Neuron):
    def __init__(self,AssignedNumber):
        self.IDNumber=AssignedNumber
        self.AccumulatedWeight = 0
    def Activate(Weight):
        AccumulatedWeight+=Weight
