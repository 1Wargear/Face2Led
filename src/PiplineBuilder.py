from typing import Callable
import numpy as np
import Pipeline

class PipelineBuilder:

    def Build() -> Pipeline:
        pass

    def AddPhysicalSensor(f: Callable[[], dict]):
        pass

    def AddDataAnalyser(f: Callable[[dict, dict], dict]):
        pass

    def AddAnimationLayer(f: Callable[[dict], dict]):
        pass

    def AddRenderingLayer(f: Callable[[np.ndarray, dict], dict]):
        pass

    def AddPostProcessingEffect(f: Callable[[np.ndarray], np.ndarray]):
        pass