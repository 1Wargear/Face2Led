from Framework.DataFields import DataField
from Framework.XsvgParser import XsvgParser

def CompileIMage(data, image):
    parser:XsvgParser = data[DataField.DF_BaseImage]
    data[DataField.DF_SVG] = parser.CompileSVG(data[DataField.DF_Empotion], data[DataField.DF_Overrides])
    return data