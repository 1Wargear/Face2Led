import numpy as np
import PipelineStages

class Pipeline:

    def __init__(self, stages: dict[PipelineStages.PipelineStage, list[callable]]) -> None:
        self.stages = stages

    def Execute(self) -> np.ndarray:
        pass