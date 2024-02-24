from lxml import etree
import re
import numpy as np
import logging

class XsvgParser:

    def __init__(self, xsvg) -> None:
        self.xsvg = xsvg
        self.tree = etree.fromstring(xsvg)

        svgRE = re.compile("<svg((.|\n)*)<\/svg>")
        self.svg = re.search(svgRE, xsvg).group(0)

    def CompileSVG(self, preset: str, overrides:dict):
        """ Compiles a SVG file from a preset and overrides and returns the ready to use SVG string """

        vars = self.LoadPreset(preset)

        if overrides != None:
            for vname in overrides:
                vars[vname] = self.ConstrainValue(preset, vname, "pos", overrides[vname])

        return self.ApplyVars(vars)

    def ApplyVars(self, overrides:dict) -> str:
        """ Applies the overrides to the SVG and returns the new SVG-String ready to use """

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
                logging.warn("Missing Variable")
                return None
            
            appliedSVG = appliedSVG.replace(match, vval)

        return appliedSVG

    def DefaultLookup(self, name: str):
        """ looks up the default value for a variable """

        return self.tree.xpath(f".//defaults/pos[@name=\"{name}\"]/@value")[0]
    
    def ConstrainValue(self, preset:str, name: str, type: str, value: str):
        """ Clams a value in the range of the variable for the preset """

        entry = self.GetOverride(preset, name, type)

        if entry == None:
            return value
        
        entryValue = entry.xpath("@value")[0]
        
        match type:
            case "pos":
                px, py = entryValue.split(',')
                x,y = value.split(',')
                xmin, xmax = entry.xpath("@rangeX")[0].split(',')
                ymin, ymax = entry.xpath("@rangeY")[0].split(',')
                x = int(np.clip(int(x), int(px) + int(xmin), int(px) + int(xmax)))
                y = int(np.clip(int(y), int(py) + int(ymin), int(py) + int(ymax)))
                return f"{x},{y}"
            case _:
                return value
            
    def GetOverride(self, preset:str, name:str, type:str):
        """ Gets the Variable entry for the preset. If none exists it returns the variable entry from the defaults """

        entries = self.tree.xpath(f".//preset[@name=\"{preset}\"]/{type}[@name=\"{name}\"]")

        entry = None
        if entries:
            entry = entries[0]

        if entry == None:
            entry = self.tree.xpath(f".//defaults/{type}[@name=\"{name}\"]")[0]

        return entry

    def MoveValueInRange(self, preset:etree._Element, value):
        """ Modifies the output Value to lie in the allowed range by a percentage given by the value whitch is between -1 and 1 """
        match preset.tag:
            case "pos":
                vx, vy = value.split(',')
                px, py = preset.xpath("@value")[0].split(',')
                xmin, xmax = preset.xpath("@rangeX")[0].split(',')
                ymin, ymax = preset.xpath("@rangeY")[0].split(',')
                nx = int(((float(xmax) - float(xmin)) * (float(vx) + 1 / 2)) + float(xmin))
                ny = int(((float(ymax) - float(ymin)) * (float(vy) + 1 / 2)) + float(ymin))
                return f"{int(px) + nx},{int(py) + ny}"
            case _:
                return value

    def LoadPreset(self, name: str):
        """ Creates a dictionary with all overrides from a given preset """

        presetValues = {}
        preset = self.tree.xpath(f".//preset[@name=\"{name}\"]/*")

        for i in preset:
            presetValues[i.xpath('@name')[0]] = i.xpath('@value')[0]

        return presetValues
