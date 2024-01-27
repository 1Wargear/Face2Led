import io
import cairosvg
from PIL import Image
import numpy as np

def RasterizeSVG(data, image):
    target = np.shape(image)

    mem = io.BytesIO()
    cairosvg.svg2png(url="./assets/face.svg", write_to=mem, output_width=target[0], output_height=target[1])
    img = Image.open(mem)
    return np.array(img)