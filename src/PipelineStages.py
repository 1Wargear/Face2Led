from enum import Enum

class PipelineStage(Enum):
    PS_PhysicalData = 0
    PS_DataAnalysing = 1
    PS_FrameComposition = 2
    PS_Animation = 3
    PS_Rendering = 4
    PS_PostProcessing = 5