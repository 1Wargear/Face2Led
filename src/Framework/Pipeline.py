import numpy as np
import PipelineStages
from typing import Callable

class Pipeline:

    def __init__(self, stages: dict[PipelineStages.PipelineStage, list[Callable]]) -> None:
        self.stages = stages

    def Execute(self) -> np.ndarray:

        # Execute physical data gatering
        physicalData = {}
        for i in self.stages[PipelineStages.PipelineStage.PS_PhysicalData]:
            k, v = i()
            physicalData[k] = v

        # Execute Data analysis
        analyticResults = {}
        for i in self.stages[PipelineStages.PipelineStage.PS_DataAnalysing]:
            analyticResults = i(physicalData, analyticResults)

        # Execute Frame Composition
        composition = {}
        for i in self.stages[PipelineStages.PipelineStage.PS_FrameComposition]:
            composition = i(analyticResults, composition)

        # Execute Animatonstage
        for i in self.stages[PipelineStages.PipelineStage.PS_Animation]:
            composition = i(composition)
        
        # Execute Renderstage
        frame = np.empty
        for i in self.stages[PipelineStages.PipelineStage.PS_Rendering]:
            frame = i(composition, frame)
        
        # Exeute Post processing stage
        for i in self.stages[PipelineStages.PipelineStage.PS_PostProcessing]:
            frame = i(frame)

        return frame
