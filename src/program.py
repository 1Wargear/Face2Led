import SoftwareMatrix as sm
import cv2

from Framework.XsvgParser import XsvgParser
from Framework.DataFields import DataField
from Framework.PiplineBuilder import PipelineBuilder
from Framework.Pipeline import Pipeline

from Layer.CameraSensor import GetCameraImage
from Layer.ExpressionDetection import DetectFaceExpression
from Layer.ExpressionComposer import ComposeExpression
from Layer.BlinkingAnimation import EyeBlinkingAnimation
from Layer.ImageCompiler import CompileIMage
from Layer.SVGRasteriser import RasterizeSVG

def main():
    tw = 100
    th = 100

    mtx = sm.SoftwareMatrix(tw, th, 4)

    data = {}
    data[DataField.DF_TargetSize] = (tw, th)
    data[DataField.DF_VideoDevice] = cv2.VideoCapture(0)
    with open("./assets/face.xsvg") as file: 
        data[DataField.DF_BaseImage] = XsvgParser(file.read())

    builder = PipelineBuilder()
    builder.AddPhysicalSensor(GetCameraImage)
    builder.AddDataAnalyser(DetectFaceExpression)
    builder.AddFrameComposer(ComposeExpression)
    builder.AddAnimationLayer(EyeBlinkingAnimation)
    builder.AddRenderingLayer(CompileIMage)
    builder.AddRenderingLayer(RasterizeSVG)

    pipeline:Pipeline = builder.Build()

    while mtx.isRunning:
        img = pipeline.Execute(data)
        mtx.Update(img)

    data[DataField.DF_VideoDevice].release()

if __name__ == "__main__":
    main()