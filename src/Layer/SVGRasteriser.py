import io
import cairosvg
import numpy as np
from PIL import Image
from Framework.DataFields import DataField

def RasterizeSVG(data, image):
    target = data[DataField.DF_TargetSize]

    mem = io.BytesIO()
    svgBytes = data[DataField.DF_SVG].encode()
    cairosvg.svg2png(bytestring=svgBytes, write_to=mem, output_width=target[0], output_height=target[1])
    img = Image.open(mem)
    return np.array(img)