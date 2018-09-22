import CubeFace

TestFace = CubeFace.CubeFace()
TestFace.InitializeFace('White')

TestFace.Print()
TestFace.FaceContents[0][0]='TL'
TestFace.FaceContents[0][1]= 'T'
TestFace.FaceContents[0][2]='TR'
TestFace.FaceContents[1][0]='L'
TestFace.FaceContents[1][2]='R'
TestFace.FaceContents[2][0]='BL'
TestFace.FaceContents[2][1]='B'
TestFace.FaceContents[2][2]='BR'

print("\n")
TestFace.Print()

TestFace.RotateFaceRight()

print("\n")
TestFace.Print()

TestFace.RotateFaceRight()
print("\n")
TestFace.Print()

TestFace.RotateFaceLeft()
print("\n")
TestFace.Print()
