from deepface import DeepFace
from Framework.InputTypes import InputType
from Framework.DataFields import DataField

def DetectFaceExpression(data, analytics):
    analytics[DataField.DF_Empotion] =  detectExpression(data)
    return analytics

def detectExpression(data):
    image = data[InputType.IT_FaceCamRGB]
    result = DeepFace.analyze(image, ("emotion"), False)
    return result[0]["dominant_emotion"]
