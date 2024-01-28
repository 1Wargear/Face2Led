from lxml import etree
import re

class XsvgParser:

    def __init__(self, xsvg) -> None:
        self.xsvg = xsvg
        self.tree = etree.fromstring(xsvg)

        svgRE = re.compile("<svg((.|\n)*)<\/svg>")
        self.svg = re.search(svgRE, xsvg).group(0)
        print(self.svg)

        res = self.tree.xpath(".//preset[@name=\"neutral\"]")

    def CompileSVG(preset: str, overrides:dict):
        pass

    def CompileSVG(overrides:dict):
        pass

