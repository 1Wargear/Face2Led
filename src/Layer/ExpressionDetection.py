from deepface import DeepFace
from Framework.InputTypes import InputType
from Framework.DataFields import DataField

def DetectFaceExpression(data, analytics):
    image = data[InputType.IT_FaceCamRGB]
    result = DeepFace.analyze(image, ("emotion"), False)
    analytics[DataField.DF_Empotion]  = result[0]["dominant_emotion"]
    return analytics


