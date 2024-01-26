import cv2
import Framework.InputTypes

def GetCameraImage():
    image = cv2.VideoCapture(0).read()
    return (Framework.InputTypes.InputType.IT_FaceCamRGB, image)