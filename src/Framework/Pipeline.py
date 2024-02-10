import numpy as np
from typing import Callable
from Framework.DataFields import DataField
from Framework.InputTypes import InputType
from Framework.PipelineStages import PipelineStage

class Pipeline:

    def __init__(self, stages: dict[PipelineStage, list[Callable]]) -> None:
        self.stages = stages
        self.tick = 0

    def Execute(self, parameters: dict) -> np.ndarray:

        parameters[DataField.DF_Tick] = self.tick

        # Execute physical data gatering
        physicalData = parameters
        for i in self.stages[PipelineStage.PS_PhysicalData]:
            k, v = i(parameters)
            physicalData[k] = v

        # Execute Data analysis
        analyticResults = parameters
        for i in self.stages[PipelineStage.PS_DataAnalysing]:
            analyticResults = i(physicalData, analyticResults)

        if InputType.IT_UserOverride in parameters and DataField.DF_Empotion in parameters[InputType.IT_UserOverride]:
            analyticResults[DataField.DF_Empotion] = parameters[InputType.IT_UserOverride][DataField.DF_Empotion]

        print(analyticResults[DataField.DF_Empotion])

        # Execute Frame Composition
        composition = parameters
        for i in self.stages[PipelineStage.PS_FrameComposition]:
            composition = i(analyticResults, composition)

        # Execute Animatonstage
        for i in self.stages[PipelineStage.PS_Animation]:
            composition = i(composition)
        
        # Execute Renderstage
        frame = np.empty
        for i in self.stages[PipelineStage.PS_Rendering]:
            frame = i(composition, frame)
        
        # Exeute Post processing stage
        for i in self.stages[PipelineStage.PS_PostProcessing]:
            frame = i(frame)

        self.tick += 1

        return frame
