import CubeFace
import random

class Cube():
    def __init__(self):
        self.WhiteFace = CubeFace.CubeFace()
        self.WhiteFace.InitializeFace('White')

        self.RedFace = CubeFace.CubeFace()
        self.RedFace.InitializeFace('Red')

        self.BlueFace = CubeFace.CubeFace()
        self.BlueFace.InitializeFace('Blue')

        self.GreenFace = CubeFace.CubeFace()
        self.GreenFace.InitializeFace('Green')

        self.OrangeFace = CubeFace.CubeFace()
        self.OrangeFace.InitializeFace('Orange')

        self.YellowFace = CubeFace.CubeFace()
        self.YellowFace.InitializeFace('Yellow')
        
    def RotateWhiteFaceRight(self):
        self.WhiteFace.RotateFaceRight()
        #Hold the blue face in storage
        BlueFaceTopCorner = self.BlueFace.FaceContents[0][2]
        BlueFaceEdge = self.BlueFace.FaceContents[1][2]
        BlueFaceLowCorner = self.BlueFace.FaceContents[2][2]

        self.BlueFace.FaceContents[0][2] = self.RedFace.FaceContents[2][2]
        self.BlueFace.FaceContents[1][2] = self.RedFace.FaceContents[2][1]
        self.BlueFace.FaceContents[2][2] = self.RedFace.FaceContents[2][0]

        self.RedFace.FaceContents[2][2] = self.GreenFace.FaceContents[2][0]
        self.RedFace.FaceContents[2][1] = self.GreenFace.FaceContents[1][0]
        self.RedFace.FaceContents[2][0] = self.GreenFace.FaceContents[0][0]

        self.GreenFace.FaceContents[2][0]=self.OrangeFace.FaceContents[0][0]
        self.GreenFace.FaceContents[1][0]=self.OrangeFace.FaceContents[0][1]
        self.GreenFace.FaceContents[0][0]=self.OrangeFace.FaceContents[0][2]

        self.OrangeFace.FaceContents[0][0] = BlueFaceTopCorner
        self.OrangeFace.FaceContents[0][1] = BlueFaceEdge
        self.OrangeFace.FaceContents[0][2] = BlueFaceLowCorner

    def RotateBlueFaceRight(self):
        self.BlueFace.RotateFaceRight()
        #hold the red left face in storage
        RedLowerCorner = self.RedFace.FaceContents[2][0]
        RedEdge = self.RedFace.FaceContents[1][0]
        RedTopCorner = self.RedFace.FaceContents[0][0]
        #white left side goes to red left side
        self.RedFace.FaceContents[2][0]=self.WhiteFace.FaceContents[2][0]
        self.RedFace.FaceContents[1][0]=self.WhiteFace.FaceContents[1][0]
        self.RedFace.FaceContents[0][0]=self.WhiteFace.FaceContents[0][0]        
        #orange left side goes to white left side.
        self.WhiteFace.FaceContents[2][0]=self.OrangeFace.FaceContents[2][0]
        self.WhiteFace.FaceContents[1][0]=self.OrangeFace.FaceContents[1][0]
        self.WhiteFace.FaceContents[0][0]=self.OrangeFace.FaceContents[0][0]
        #yellow left side goes to orange left side
        self.OrangeFace.FaceContents[2][0]=self.YellowFace.FaceContents[2][0]
        self.OrangeFace.FaceContents[1][0]=self.YellowFace.FaceContents[1][0]
        self.OrangeFace.FaceContents[0][0]=self.YellowFace.FaceContents[0][0]
        #red left side goes to yellow left side
        self.YellowFace.FaceContents[2][0]=RedLowerCorner
        self.YellowFace.FaceContents[1][0]=RedEdge
        self.YellowFace.FaceContents[0][0]=RedTopCorner

    def RotateRedFaceRight(self):
        self.RedFace.RotateFaceRight()
        #hold the yellow bottom in storage
        YellowLeftCorner = self.YellowFace.FaceContents[2][0]
        YellowEdge = self.YellowFace.FaceContents[2][1]
        YellowRightCorner = self.YellowFace.FaceContents[2][2]
        #green top goes to yellow bottom
        self.YellowFace.FaceContents[2][0] = self.GreenFace.FaceContents[0][2]
        self.YellowFace.FaceContents[2][1] = self.GreenFace.FaceContents[0][1]
        self.YellowFace.FaceContents[2][2] = self.GreenFace.FaceContents[0][0]
        #white top goes to green top
        self.GreenFace.FaceContents[0][0] = self.WhiteFace.FaceContents[0][0]
        self.GreenFace.FaceContents[0][1] = self.WhiteFace.FaceContents[0][1]
        self.GreenFace.FaceContents[0][2] = self.WhiteFace.FaceContents[0][2]
        #blue top goes to white top
        self.WhiteFace.FaceContents[0][0] = self.BlueFace.FaceContents[0][0]
        self.WhiteFace.FaceContents[0][1] = self.BlueFace.FaceContents[0][1]
        self.WhiteFace.FaceContents[0][2] = self.BlueFace.FaceContents[0][2]
        #yellow bottom goes to blue top
        self.BlueFace.FaceContents[0][0] = YellowRightCorner
        self.BlueFace.FaceContents[0][1] = YellowEdge
        self.BlueFace.FaceContents[0][2] = YellowLeftCorner
        
    def RotateGreenFaceRight(self):
        self.GreenFace.RotateFaceRight()
        #store the red face right side
        RedTopCorner = self.RedFace.FaceContents[0][2]
        RedEdge = self.RedFace.FaceContents[1][2]
        RedLowerCorner = self.RedFace.FaceContents[2][2]
        #yellow right side goes to red right side
        self.RedFace.FaceContents[0][2] = self.YellowFace.FaceContents[0][2]
        self.RedFace.FaceContents[1][2] = self.YellowFace.FaceContents[1][2]
        self.RedFace.FaceContents[2][2] = self.YellowFace.FaceContents[2][2]
        #orange goes to yellow
        self.YellowFace.FaceContents[0][2] = self.OrangeFace.FaceContents[0][2]
        self.YellowFace.FaceContents[1][2] = self.OrangeFace.FaceContents[1][2]
        self.YellowFace.FaceContents[2][2] = self.OrangeFace.FaceContents[2][2]
        #White goes to orange
        self.OrangeFace.FaceContents[0][2] = self.WhiteFace.FaceContents[0][2]
        self.OrangeFace.FaceContents[1][2] = self.WhiteFace.FaceContents[1][2]
        self.OrangeFace.FaceContents[2][2] = self.WhiteFace.FaceContents[2][2]
        #red goes to white
        self.WhiteFace.FaceContents[0][2] = RedTopCorner
        self.WhiteFace.FaceContents[1][2] = RedEdge
        self.WhiteFace.FaceContents[2][2] = RedLowerCorner
        
    def RotateOrangeFaceRight(self):
        self.OrangeFace.RotateFaceRight()
        #store the white bottom row
        WhiteLeftCorner = self.WhiteFace.FaceContents[2][0]
        WhiteEdge = self.WhiteFace.FaceContents[2][1]
        WhiteRightCorner = self.WhiteFace.FaceContents[2][2]
        #green bottom row goes to white
        self.WhiteFace.FaceContents[2][0] = self.GreenFace.FaceContents[2][0]
        self.WhiteFace.FaceContents[2][1] = self.GreenFace.FaceContents[2][1]
        self.WhiteFace.FaceContents[2][2] = self.GreenFace.FaceContents[2][2]
        #yellow top row goes to green bottom row, but reversed
        self.GreenFace.FaceContents[2][0] = self.YellowFace.FaceContents[0][2]
        self.GreenFace.FaceContents[2][1] = self.YellowFace.FaceContents[0][1]
        self.GreenFace.FaceContents[2][2] = self.YellowFace.FaceContents[0][0]
        #blue bottom becomes yellow top, but reversed
        self.YellowFace.FaceContents[0][2] = self.BlueFace.FaceContents[2][0]
        self.YellowFace.FaceContents[0][1] = self.BlueFace.FaceContents[2][1]
        self.YellowFace.FaceContents[0][0] = self.BlueFace.FaceContents[2][2]
        #white bottom becomes blue bottom
        self.BlueFace.FaceContents[2][0] = WhiteLeftCorner
        self.BlueFace.FaceContents[2][1] = WhiteEdge
        self.BlueFace.FaceContents[2][2] = WhiteRightCorner
    
    def RotateYellowFaceRight(self): 
        self.YellowFace.RotateFaceRight()
        #here's the hard one
        BlueTopCorner = self.BlueFace.FaceContents[0][0]
        BlueEdge = self.BlueFace.FaceContents[1][0]
        BlueLowerCorner = self.BlueFace.FaceContents[2][0]
        #orange Bootom goes to blue blue left
        self.BlueFace.FaceContents[0][0]=self.OrangeFace.FaceContents[2][0]
        self.BlueFace.FaceContents[1][0]=self.OrangeFace.FaceContents[2][1]
        self.BlueFace.FaceContents[2][0]=self.OrangeFace.FaceContents[2][2]
        #green right goes to orange bottom
        self.OrangeFace.FaceContents[2][0]=self.GreenFace.FaceContents[2][2]
        self.OrangeFace.FaceContents[2][1]=self.GreenFace.FaceContents[1][2]
        self.OrangeFace.FaceContents[2][2]=self.GreenFace.FaceContents[0][2]
        #red top goes to green right
        self.GreenFace.FaceContents[0][2]=self.RedFace.FaceContents[0][0]
        self.GreenFace.FaceContents[1][2]=self.RedFace.FaceContents[0][1]
        self.GreenFace.FaceContents[2][2]=self.RedFace.FaceContents[0][2]
        #blue left goes to red top
        self.RedFace.FaceContents[0][0]=BlueLowerCorner
        self.RedFace.FaceContents[0][1]=BlueEdge
        self.RedFace.FaceContents[0][2]=BlueTopCorner
        
    #This is really stupid, but...
    #technically speaking as long as the rotate face right code is correct
    #a leftward turn of a face really is just 3 rightward turns of the same face.
    def RotateWhiteFaceLeft(self):
        self.RotateWhiteFaceRight()
        self.RotateWhiteFaceRight()
        self.RotateWhiteFaceRight()    
    def RotateBlueFaceLeft(self):
        self.RotateBlueFaceRight()
        self.RotateBlueFaceRight()
        self.RotateBlueFaceRight()
    def RotateRedFaceLeft(self):
        self.RotateRedFaceRight()
        self.RotateRedFaceRight()
        self.RotateRedFaceRight()
    def RotateGreenFaceLeft(self):
        self.RotateGreenFaceRight()
        self.RotateGreenFaceRight()
        self.RotateGreenFaceRight()
    def RotateOrangeFaceLeft(self):
        self.RotateOrangeFaceRight()
        self.RotateOrangeFaceRight()
        self.RotateOrangeFaceRight()
    def RotateYellowFaceLeft(self):
        self.RotateYellowFaceRight()
        self.RotateYellowFaceRight()
        self.RotateYellowFaceRight()

    def Print(self):
        #scan each of the faces looking for the longest length "line" in one of them
        #we'll use this to help format the print
        MaxLength = 0
        for i in range(3):
            if len(str(self.RedFace.FaceContents[i])) > MaxLength:
                MaxLength = len(str(self.RedFace.FaceContents[i]))
            if len(str(self.BlueFace.FaceContents[i])) > MaxLength:
                MaxLength = len(str(self.BlueFace.FaceContents[i]))
            if len(str(self.WhiteFace.FaceContents[i])) > MaxLength: 
                MaxLength = len(str(self.WhiteFace.FaceContents[i]))
            if len(str(self.GreenFace.FaceContents[i])) > MaxLength:
                MaxLength = len(str(self.GreenFace.FaceContents[i]))
            if len(str(self.OrangeFace.FaceContents[i])) > MaxLength:
                MaxLength = len(str(self.OrangeFace.FaceContents[i]))
            if len(str(self.YellowFace.FaceContents[i])) > MaxLength:
                MaxLength = len(str(self.YellowFace.FaceContents[i]))
        #print(MaxLength)
        #now we print the red face, center justified based on the max length
        for i in range(3):
            print(('{:^'+str(MaxLength*3)+'}').format(str(self.RedFace.FaceContents[i])))
        print()
        #now print the blue white and green face
        for i in range (3):
            print(('{:^'+str(MaxLength)+'}').format(str(self.BlueFace.FaceContents[i]))
                  +('{:^'+str(MaxLength)+'}').format(str(self.WhiteFace.FaceContents[i]))
                  +('{:^'+str(MaxLength)+'}').format(str(self.GreenFace.FaceContents[i])))
        #print the orange face
        print()
        for i in range(3):
            print(('{:^'+str(MaxLength*3)+'}').format(str(self.OrangeFace.FaceContents[i])))
        print()
        for i in range(3):
            print(('{:^'+str(MaxLength*3)+'}').format(str(self.YellowFace.FaceContents[i])))

    #use this for scrambling the cube:
    #there are 6 faces * two turn directions = 12 possible moves
    def ScrambleCube(self,Moves):
        for i in range(Moves):
            Turn = random.randint(1,12)
            if Turn == 1:
                self.RotateWhiteFaceRight()
            elif Turn == 2:
                self.RotateWhiteFaceLeft()
            elif Turn == 3:
                self.RotateRedFaceRight()
            elif Turn == 4:
                self.RotateRedFaceLeft()
            elif Turn == 5:
                self.RotateBlueFaceRight()
            elif Turn == 6:
                self.RotateBlueFaceLeft()
            elif Turn == 7:
                self.RotateGreenFaceRight()
            elif Turn == 8:
                self.RotateGreenFaceLeft()
            elif Turn == 9:
                self.RotateOrangeFaceRight()
            elif Turn == 10:
                self.RotateOrangeFaceLeft()
            elif Turn == 11:
                self.RotateYellowFaceRight()
            elif Turn == 12:
                self.RotateYellowFaceLeft()

    def GetNumSolvedElements(self):
        return (self.RedFace.GetNumSolvedElements()+self.BlueFace.GetNumSolvedElements()
                +self.WhiteFace.GetNumSolvedElements()+self.GreenFace.GetNumSolvedElements()
                +self.OrangeFace.GetNumSolvedElements()+self.YellowFace.GetNumSolvedElements())

    def GetInputNeuronsToActivate(self):
        InputNeurons = []
        InputNeurons = InputNeurons + self.RedFace.ReturnInputNeuronsToActivate()
        InputNeurons = InputNeurons + self.BlueFace.ReturnInputNeuronsToActivate()
        InputNeurons = InputNeurons + self.WhiteFace.ReturnInputNeuronsToActivate()
        InputNeurons = InputNeurons + self.GreenFace.ReturnInputNeuronsToActivate()
        InputNeurons = InputNeurons + self.OrangeFace.ReturnInputNeuronsToActivate()
        InputNeurons = InputNeurons + self.YellowFace.ReturnInputNeuronsToActivate()
        return InputNeurons

    def IsNotSolved(self):
        return (self.GetNumSolvedElements != 54)
