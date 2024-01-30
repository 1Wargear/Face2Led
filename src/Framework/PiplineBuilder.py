from typing import Callable
import numpy as np
from Framework.Pipeline import Pipeline
from Framework.PipelineStages import PipelineStage
from Framework.InputTypes import InputType

class PipelineBuilder:

    pipelineDefinition: dict[PipelineStage, list[Callable]]

    def __init__(self) -> None:
        self.pipelineDefinition = { PipelineStage.PS_PhysicalData: [],
                                    PipelineStage.PS_DataAnalysing: [],
                                    PipelineStage.PS_FrameComposition: [],
                                    PipelineStage.PS_Animation: [],
                                    PipelineStage.PS_Rendering: [],
                                    PipelineStage.PS_PostProcessing: [] }

    def Build(self) -> Pipeline:
        return Pipeline(self.pipelineDefinition)

    def AddPhysicalSensor(self, f: Callable[[dict], tuple[InputType, ...]]):
        self.pipelineDefinition[PipelineStage.PS_PhysicalData].append(f)

    def AddDataAnalyser(self, f: Callable[[dict, dict], dict]):
        self.pipelineDefinition[PipelineStage.PS_DataAnalysing].append(f)

    def AddFrameComposer(self, f: Callable[[dict, dict], dict]):
        self.pipelineDefinition[PipelineStage.PS_FrameComposition].append(f)

    def AddAnimationLayer(self, f: Callable[[dict], dict]):
        self.pipelineDefinition[PipelineStage.PS_Animation].append(f)

    def AddRenderingLayer(self, f: Callable[[dict, np.ndarray], np.ndarray]):
        self.pipelineDefinition[PipelineStage.PS_Rendering].append(f)

    def AddPostProcessingEffect(self, f: Callable[[np.ndarray], np.ndarray]):
        self.pipelineDefinition[PipelineStage.PS_PostProcessing].append(f)