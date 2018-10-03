from Brain import Brain
from copy import deepcopy

FirstBrain = Brain()
FirstBrain.InitializeRandomLayerNeurons(2,40)

SecondBrain = deepcopy(FirstBrain)
SecondBrain.MutateBrain()
#SecondBrain.AddRandomConnection()
