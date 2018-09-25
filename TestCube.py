from Cube import Cube

NewCube = Cube()

NewCube.Print()

print()
NewCube.RotateWhiteFaceRight()
NewCube.Print()

print()
NewCube.RotateWhiteFaceLeft()
NewCube.Print()

print()
print()
NewCube.RotateGreenFaceRight()
NewCube.RotateGreenFaceRight()

NewCube.RotateBlueFaceRight()
NewCube.RotateBlueFaceRight()

NewCube.RotateRedFaceRight()
NewCube.RotateRedFaceRight()

NewCube.RotateOrangeFaceRight()
NewCube.RotateOrangeFaceRight()

NewCube.RotateWhiteFaceRight()
NewCube.RotateWhiteFaceRight()

NewCube.RotateYellowFaceRight()
NewCube.RotateYellowFaceRight()

NewCube.Print()

print()
print(NewCube.GetNumSolvedElements())
print()

NewCube.RotateGreenFaceLeft()
NewCube.RotateGreenFaceLeft()

NewCube.RotateBlueFaceLeft()
NewCube.RotateBlueFaceLeft()

NewCube.RotateRedFaceLeft()
NewCube.RotateRedFaceLeft()

NewCube.RotateOrangeFaceLeft()
NewCube.RotateOrangeFaceLeft()

NewCube.RotateWhiteFaceLeft()
NewCube.RotateWhiteFaceLeft()

NewCube.RotateYellowFaceLeft()
NewCube.RotateYellowFaceLeft()

NewCube.Print()

print()
print(NewCube.GetNumSolvedElements())

print()

NewCube.ScrambleCube(25)
NewCube.Print()
