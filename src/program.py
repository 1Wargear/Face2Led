import SoftwareMatrix as sm
import numpy as np

def main():
    mtx = sm.SoftwareMatrix(2, 2, 50)

    while mtx.isRunning:
        mtx.Update([[(255,0,255), (0, 255, 255)],[(255,255,0),(255,0,0)]])

if __name__ == "__main__":
    main()