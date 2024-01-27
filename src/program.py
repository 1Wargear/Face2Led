import SoftwareMatrix as sm
import numpy as np

import Layer.SVGRasteriser

def main():
    tw = 100
    th = 100

    mtx = sm.SoftwareMatrix(tw, th, 1)

    img = Layer.SVGRasteriser.RasterizeSVG(None, np.ndarray((tw, th, 3)))

    while mtx.isRunning:
        mtx.Update(img)

if __name__ == "__main__":
    main()