from Framework.XsvgParser import XsvgParser
from Framework.DataFields import DataField

def ComposeExpression(input, aggregate):
    image:XsvgParser = input[DataField.DF_BaseImage]
    d = image.LoadPreset(input[DataField.DF_Empotion])
    
    for k in d:
        aggregate[k] = d[k]

    return aggregate