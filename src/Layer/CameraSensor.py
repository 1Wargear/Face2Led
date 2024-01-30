from Framework.InputTypes import InputType
from Framework.DataFields import DataField

def GetCameraImage(parameters):
    ret, image = parameters[DataField.DF_VideoDevice].read()
    return (InputType.IT_FaceCamRGB, image)