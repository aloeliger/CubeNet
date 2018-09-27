class CubeFace():
    #define cube faces as if this cube face were the top most face
    #we'll later delegate to the overall cube class to determine how
    #to join these together
    def __init__(self):
        #Just list the the overall contents of this face
        #do this in [row][column]
        self.FaceContents = [['','',''],['','',''],['','','']]
        self.LeftFace = None
        self.Rightface = None
        self.FrontFace = None
        self.RearFace = None

    def InitializeFace(self,color):
        for i in range(3):
            for j in range(3):
                self.FaceContents[i][j]=color
    #This is the only rotation we need to define on the face actually
    def RotateFaceRight(self):
        #okay, how do we do this. First, let's declare a few temporary containers
        # one for edge colors, one for corner colors
        #starting at the bottom, and bottom right
        TemporaryEdge = self.FaceContents[2][1]
        TemporaryCorner = self.FaceContents[2][2]
        #now we start replacing Colors, left goes to bottom
        self.FaceContents[2][1]=self.FaceContents[1][0]
        self.FaceContents[2][2]=self.FaceContents[2][0]
        #top goes to left
        self.FaceContents[1][0]=self.FaceContents[0][1]
        self.FaceContents[2][0]=self.FaceContents[0][0]
        #right goes to top
        self.FaceContents[0][1]=self.FaceContents[1][2]
        self.FaceContents[0][0]=self.FaceContents[0][2]
        #We now replace the right with our temporary stuff.
        self.FaceContents[1][2]=TemporaryEdge
        self.FaceContents[0][2]=TemporaryCorner
            
    #Centers never "Move" w.r.t to each other
    #this will be a useful touchstone for cube orientation
    #and for what colors it should be surrounded by on a solved cube.
    def GetCenterColor(self):
        return self.FaceContents[1][1]
    def GetFaceContents(self):
        return self.FaceContents
    def Print(self):
        print(self.FaceContents[0])
        print(self.FaceContents[1])
        print(self.FaceContents[2])
    def GetNumSolvedElements(self):
        NumSolved = 0
        for i in range(3):
            for j in range (3):
                if self.FaceContents[i][j] == self.GetCenterColor():
                    NumSolved+=1
        return NumSolved

    #just hand over the face element numbers in the row,column format,
    # it will return the relevant predetermined neuron ID that needs to
    # be activated to take this elment into account.
    def GetElementInputNeuron(self, row, column):
        FirstDigit = 0
        SecondDigit = 0
        ThirdDigit = 0
        #digit for element placement
        if(row == 0):
            FirstDigit = column + 1
        elif(row == 1):
            FirstDigit = column + 4
        elif(row == 2):
            FirstDigit = column + 7
        #digit for face
        if (self.GetCenterColor()=='Red'):
            SecondDigit = 1
        elif (self.GetCenterColor() == 'Blue'):
            SecondDigit = 2
        elif (self.GetCenterColor() == 'White'):
            SecondDigit = 3
        elif (self.GetCenterColor() == 'Green'):
            SecondDigit = 4
        elif (self.GetCenterColor() == 'Orange'):
            SecondDigit = 5
        elif (self.GetCenterColor() == 'Yellow'):
            SecondDigit = 6
        #digit for color of element
        if(self.FaceContents[row][column] == 'Red'):
            ThirdDigit = 1
        elif(self.FaceContents[row][column] == 'Blue'):
            ThirdDigit = 2
        elif(self.FaceContents[row][column] == 'White'):
            ThirdDigit = 3
        elif(self.FaceContents[row][column] == 'Green'):
            ThirdDigit = 4
        elif(self.FaceContents[row][column] == 'Orange'):
            ThirdDigit = 5
        elif(self.FaceContents[row][column] == 'Yellow'):
            ThirdDigit = 6
        return 100*FirstDigit+10*SecondDigit+ThirdDigit
        
    def ReturnInputNeuronsToActivate(self):
        InputNeuronIDs=[]
        for i in range(0,3):
            for j in range(0,3):
                InputNeuronIDs.append(self.GetElementInputNeuron(i,j))
        return InputNeuronIDs
