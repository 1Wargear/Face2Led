from lxml import etree
import re
import numpy as np

class XsvgParser:

    def __init__(self, xsvg) -> None:
        self.xsvg = xsvg
        self.tree = etree.fromstring(xsvg)

        svgRE = re.compile("<svg((.|\n)*)<\/svg>")
        self.svg = re.search(svgRE, xsvg).group(0)

    def CompileSVG(self, preset: str, overrides:dict):
        vars = self.LoadPreset(preset)

        if overrides != None:
            for vname, vval in overrides:
                vars[vname] = self.ConstrainValue(preset, vname, "pos", vval)

        return self.ApplyVars(vars)

    def ApplyVars(self, overrides:dict) -> str:
        appliedSVG = self.svg
        varRE = re.compile("\$.*?\$")

        for match in re.findall(varRE, self.svg):
            vname = match.replace('$', '')

            vval = None
            if overrides.__contains__(vname):
                vval = overrides[vname]
            else:
                vval = self.DefaultLookup(vname)

            if vval == None:
                # Logger.CurrentLogger.WriteLog(Logger.LogLevel.LL_Error, "Missing Variable")
                print("Fuckup")
                return None
            
            appliedSVG = appliedSVG.replace(match, vval)

        return appliedSVG

    def DefaultLookup(self, name: str):
        return self.tree.xpath(f".//defaults/pos[@name=\"{name}\"]/@value")
    
    def ConstrainValue(self, preset:str, name: str, type: str, value: str):
        entry = self.tree.xpath(f".//preset[@name=\"{preset}\"]/{type}][@name=\"{name}\"]")

        if entry == None:
            entry = self.tree.xpath(f".//defaults/{type}][@name=\"{name}\"]")

        if entry == None:
            return value
        
        match type:
            case "pos":
                x,y = value.split(',')
                xmin, xmax = entry.xpath("@rangeX").split(',')
                ymin, ymax = entry.xpath("@rangeY").split(',')
                x = np.clip(x, xmin, xmax)
                y = np.clip(y, ymin, ymax)
                return f"{x},{y}"
            case _:
                return value

    def LoadPreset(self, name: str):
        presetValues = {}
        preset = self.tree.xpath(f".//preset[@name=\"{name}\"]/*")

        for i in preset:
            presetValues[i.xpath('@name')[0]] = i.xpath('@value')[0]

        return presetValues


xp = XsvgParser(open("./assets/face.xsvg").read())
svg = xp.CompileSVG("neutral", None)
print(svg)
