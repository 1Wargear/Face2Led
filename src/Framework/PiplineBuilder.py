from typing import Callable
import numpy as np
import Pipeline
import PipelineStages
import InputTypes

class PipelineBuilder:

    pipelineDefinition: dict[PipelineStages.PipelineStage, list[Callable]]

    def __init__(self) -> None:
        self.pipelineDefinition = { PipelineStages.PipelineStage.PS_PhysicalData: [],
                                PipelineStages.PipelineStage.PS_DataAnalysing: [],
                                PipelineStages.PipelineStage.PS_FrameComposition: [],
                                PipelineStages.PipelineStage.PS_Animation: [],
                                PipelineStages.PipelineStage.PS_Rendering: [],
                                PipelineStages.PipelineStage.PS_PostProcessing: [] }

    def Build(self) -> Pipeline:
        return Pipeline(self.pipelineDefinition)

    def AddPhysicalSensor(self, f: Callable[[], tuple[InputTypes.InputType, ...]]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_PhysicalData].append(f)

    def AddDataAnalyser(self, f: Callable[[dict, dict], dict]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_DataAnalysing].append(f)

    def AddFrameComposer(self, f: Callable[[dict, dict], dict]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_FrameComposition].append(f)

    def AddAnimationLayer(self, f: Callable[[dict], dict]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_Animation].append(f)

    def AddRenderingLayer(self, f: Callable[[dict, np.ndarray], np.ndarray]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_Rendering].append(f)

    def AddPostProcessingEffect(self, f: Callable[[np.ndarray], np.ndarray]):
        self.pipelineDefinition[PipelineStages.PipelineStage.PS_PostProcessing].append(f)