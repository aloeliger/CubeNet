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

    def ReturnInputNeuronsToActivate():
        InputNeuronIDs=[]
        
        return InputNeuronIDs
