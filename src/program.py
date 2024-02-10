import cv2
import logging

import API.ApiServer
import uvicorn
import globaldata

from SoftwareMatrix import SoftwareMatrix
from Framework.XsvgParser import XsvgParser
from Framework.DataFields import DataField
from Framework.InputTypes import InputType
from Framework.PiplineBuilder import PipelineBuilder
from Framework.Pipeline import Pipeline

from Layer.CameraSensor import GetCameraImage
from Layer.ExpressionDetection import DetectFaceExpression
from Layer.ExpressionComposer import ComposeExpression
from Layer.BlinkingAnimation import EyeBlinkingAnimation
from Layer.ImageCompiler import CompileIMage
from Layer.SVGRasteriser import RasterizeSVG

def main():
    logging.basicConfig(level=logging.WARN, format="%(asctime)s\t%(name)s\t%(levelname)s:\t%(message)s")

    tw = 100
    th = 100

    mtx = SoftwareMatrix(tw, th, 4)

    globaldata.data[InputType.IT_UserOverride] = {}
    globaldata.data[DataField.DF_TargetSize] = (tw, th)
    globaldata.data[DataField.DF_VideoDevice] = cv2.VideoCapture(0)
    with open("./assets/face.xsvg") as file: 
        globaldata.data[DataField.DF_BaseImage] = XsvgParser(file.read())

    builder = PipelineBuilder()
    builder.AddPhysicalSensor(GetCameraImage)
    builder.AddDataAnalyser(DetectFaceExpression)
    builder.AddFrameComposer(ComposeExpression)
    builder.AddAnimationLayer(EyeBlinkingAnimation)
    builder.AddRenderingLayer(CompileIMage)
    builder.AddRenderingLayer(RasterizeSVG)

    pipeline:Pipeline = builder.Build()

    config = uvicorn.Config("API.apimain:app", port=4500, log_level="info")
    server = API.ApiServer.Server(config=config)

    with server.run_in_thread():
        while mtx.isRunning:
            img = pipeline.Execute(globaldata.data)
            mtx.Update(img)

    globaldata.data[DataField.DF_VideoDevice].release()

if __name__ == "__main__":
    main()