from Framework.XsvgParser import XsvgParser
from Framework.DataFields import DataField

def ComposeExpression(input, aggregate):
    image:XsvgParser = input[DataField.DF_BaseImage]
    aggregate[DataField.DF_Overrides] = image.LoadPreset(input[DataField.DF_Empotion])
    return aggregate