import math
import datetime
from Framework.DataFields import DataField
from Framework.XsvgParser import XsvgParser

def animateEyeBlink(params, xsvg, name, animValue):
    rightlidEntry = xsvg.GetOverride(params[DataField.DF_Empotion], name, "pos")
    rightidNew = xsvg.MoveValueInRange(rightlidEntry, animValue)
    params[DataField.DF_Overrides][name] = rightidNew

def EyeBlinkingAnimation(params):
    tick = params[DataField.DF_Tick]
    xsvg:XsvgParser = params[DataField.DF_BaseImage]
    
    animCurve = math.sin(tick) * math.sin(tick) + math.sin(tick) - 1
    animValue = f"0,{animCurve}"

    animateEyeBlink(params, xsvg, "lefteyelidleft", animValue)
    animateEyeBlink(params, xsvg, "lefteyelidright", animValue)
    animateEyeBlink(params, xsvg, "righteyelidleft", animValue)
    animateEyeBlink(params, xsvg, "righteyelidright", animValue)

    return params