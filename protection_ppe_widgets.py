#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Widgets made using the reportlab toolkit implementing the various
warning symbols for mandatory PPE signs.

Currently implements widgets for:
"EarProtectionPPE", "GlovesPPE", "HazmatSuitPPE"
"""


#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.

import random, string

#hope we have svglib installed...
from svglib.svglib import NoStrokePath

#used by make_elements()
import sys, os, copy
from types import *

try:
    import reportlab
except ImportError:
    print "\n***ERROR! ***\n"
    print "This program requires the reportlab Open Source toolkit."
    print "Download it from https://www.reportlab.com/dev/downloads/"
    print "\n"
    raise

#reportlab imports
from reportlab.lib import colors
from reportlab.lib.validators import *
from reportlab.lib.attrmap import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.graphics import shapes
from reportlab.graphics.widgetbase import Widget
from reportlab.graphics import renderPDF
from reportlab.graphics import renderPM

from reportlab.graphics.shapes import Drawing, Group, Path, Ellipse, Circle, Polygon, PolyLine, String, Rect
#from reportlab.lib.colors import Color, CMYKColor, PCMYKColor


import scp_widgets, hazard_widgets, objects
from objects import KNOWN_SCPS_DICT, GetRisks 

#register fonts
pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'Bauhaus_Demi.ttf')))
#pdfmetrics.registerFont(TTFont('Gill Sans Nova', os.path.join("fonts", 'GillSansNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Bold', os.path.join("fonts", 'GillSansBoNova.ttf')))


MAKE_ELEMENTS = 1
MAKE_ELEMENTS = 0


#DEFINE OUR CUSTOM COLORS...
PPE_blue = colors.Color(0,.329412,.647059,1)


class _Symbol(Widget):
    """Abstract base widget
    possible attributes:
    'x', 'y', 'size', 'fillColor', 'strokeColor'
    """
    _nodoc = 1
    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc='symbol x coordinate'),
        y = AttrMapValue(isNumber,desc='symbol y coordinate'),
        dx = AttrMapValue(isNumber,desc='symbol x coordinate adjustment'),
        dy = AttrMapValue(isNumber,desc='symbol x coordinate adjustment'),
        size = AttrMapValue(isNumber),
        fillColor = AttrMapValue(isColorOrNone),
        strokeColor = AttrMapValue(isColorOrNone),
        strokeWidth = AttrMapValue(isNumber),
        )
    def __init__(self):
        assert self.__class__.__name__!='_Symbol', 'Abstract class _Symbol instantiated'
        self.x = self.y = self.dx = self.dy = 0
        self.size = 100
        self.fillColor = colors.red
        self.strokeColor = None
        self.strokeWidth = 0.1

    def demo(self):
        D = shapes.Drawing(200, 100)
        s = float(self.size)
        ob = self.__class__()
        ob.x=50
        ob.y=0
        ob.draw()
        D.add(ob)
        D.add(shapes.String(ob.x+(s/2),(ob.y-12),
                            ob.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=10))
        return D


class GlovesPPE(_Symbol):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor = PPE_blue
        self.strokeColor = colors.white

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[2620.92,1008.4,2620.92,1008.4,2594.25,968.398,2600.4,927.379,2600.4,892.5,2600.4,892.5,2601.43,865.578,2584.76,862.238,2447.57,861.73,2447.57,861.73,2422.45,858.141,2424.5,899.68,2447.75,900.02,2447.75,900.02,2475.96,900.359,2478.34,933.52,2510.15,1100.72,2657.84,1096.61,2657.84,1096.61,2660.92,1075.08,2620.92,1008.4,2422.19,932.762,2360.39,928.66,2361.76,969.77,2361.76,969.77,2361.76,1018.32,2335.77,1019.68,2306.37,1020.37,2320.74,1044.99,2320.74,1044.99,2353.56,1173.54,2489.96,1174.05,2502.79,1173.54,2501.59,1158.49,2501.59,1158.49,2500.74,1150.29,2498.86,1137.63,2498.86,1137.63,2471.17,961.219,2460.14,941.469,2460.14,941.469,2453.48,918.141,2450.14,918.91,2450.14,918.91,2422.7,918.91,2443.14,1260.72,2443.81,1190.29,2367.57,1190.63,2390.14,1234.39,2443.14,1260.72,2443.14,1260.72,2656.82,1142.77,2517.33,1143.79,2517.33,1143.79,2525.53,1181.75,2506.56,1187.89,2506.04,1270.47,2506.04,1270.47,2636.3,1263.8,2656.82,1142.77,2662.63,1190.63,2662.63,1190.63,2634.59,1260.38,2543.66,1283.62,2543.66,1283.62,2423.99,1326.37,2346.03,1190.97,2307.05,1189.95,2307.05,1189.95,2281.75,1187.56,2281.41,1148.23,2282.43,929.43,2282.43,929.43,2280.9,893.781,2312.19,893.781,2406.04,897.879,2406.04,897.879,2401.42,844.289,2443.47,843.52,2586.04,843.781,2586.04,843.781,2617.84,843.609,2618.19,884.629,2618.19,884.629,2616.82,946.52,2622.28,966.352,2622.28,966.352,2622.46,979.172,2656.82,1034.04,2656.82,1034.04,2700.92,1093.53,2662.63,1190.63],operators=[0,2,1,2,1,2,1,2,1,1,2,3,0,2,1,1,2,1,1,2,2,2,2,1,3,0,1,1,2,3,0,1,2,1,2,3,0,2,2,1,2,1,2,1,2,1,2,2,2,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
#        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[2417.83,1104.18,2417.83,1094.05,2409.62,1085.84,2399.49,1085.84,2389.38,1085.84,2381.16,1094.05,2381.16,1104.18,2381.16,1114.3,2389.38,1122.51,2399.49,1122.51,2409.62,1122.51,2417.83,1114.3,2417.83,1104.18],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))
        g.add(Path(points=[2417.83,1104.18,2417.83,1094.05,2409.62,1085.84,2399.49,1085.84,2389.38,1085.84,2381.16,1094.05,2381.16,1104.18,2381.16,1114.3,2389.38,1122.51,2399.49,1122.51,2409.62,1122.51,2417.83,1114.3,2417.83,1104.18],operators=[0,2,2,2,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[2479.84,686.398,2302.71,686.398,2159.11,542.801,2159.11,365.672,2159.11,188.531,2302.71,44.9414,2479.84,44.9414,2656.98,44.9414,2800.57,188.531,2800.57,365.672,2800.57,542.801,2656.98,686.398,2479.84,686.398],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.fillColor))
        g.add(Path(points=[2479.84,686.398,2302.71,686.398,2159.11,542.801,2159.11,365.672,2159.11,188.531,2302.71,44.9414,2479.84,44.9414,2656.98,44.9414,2800.57,188.531,2800.57,365.672,2800.57,542.801,2656.98,686.398,2479.84,686.398],operators=[0,2,2,2,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,1,1,2,3],strokeOpacity=1,strokeLineJoin=0,points=[2435.54,454.578,2435.54,454.578,2421.92,448.371,2426.06,435.09,2450.76,380.699,2450.76,380.699,2453.4,376.352,2449,374.191,2449,374.191,2444.94,371.43,2442.23,376.781,2409.23,453.281,2409.23,453.281,2402.7,465.84,2389.31,461.051,2389.31,461.051,2373.4,456.07,2378.84,440.031,2412.35,360.129,2412.35,360.129,2414.03,357.059,2410.95,354.789,2410.95,354.789,2407.94,352.078,2405.16,357.219,2373.1,434.57,2373.1,434.57,2366.62,447.238,2352.23,441.121,2352.23,441.121,2340.23,436.379,2342.74,422.32,2377.76,339.172,2377.76,339.172,2380.26,334.512,2376.2,332.75,2376.2,332.75,2372.28,329.859,2369.48,335.629,2342.4,404.379,2342.4,404.379,2337.37,416.02,2323.26,411.75,2323.26,411.75,2307.29,406.969,2311.56,392.738,2410.53,138.891,2568.89,194.27,2455.73,448.879,2455.73,448.879,2449.69,460.441,2435.54,454.578],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))
#        g.add(Path(points=[2435.54,454.578,2435.54,454.578,2421.92,448.371,2426.06,435.09,2450.76,380.699,2450.76,380.699,2453.4,376.352,2449,374.191,2449,374.191,2444.94,371.43,2442.23,376.781,2409.23,453.281,2409.23,453.281,2402.7,465.84,2389.31,461.051,2389.31,461.051,2373.4,456.07,2378.84,440.031,2412.35,360.129,2412.35,360.129,2414.03,357.059,2410.95,354.789,2410.95,354.789,2407.94,352.078,2405.16,357.219,2373.1,434.57,2373.1,434.57,2366.62,447.238,2352.23,441.121,2352.23,441.121,2340.23,436.379,2342.74,422.32,2377.76,339.172,2377.76,339.172,2380.26,334.512,2376.2,332.75,2376.2,332.75,2372.28,329.859,2369.48,335.629,2342.4,404.379,2342.4,404.379,2337.37,416.02,2323.26,411.75,2323.26,411.75,2307.29,406.969,2311.56,392.738,2410.53,138.891,2568.89,194.27,2455.73,448.879,2455.73,448.879,2449.69,460.441,2435.54,454.578],operators=[0,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,1,1,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,1,3],strokeOpacity=1,strokeLineJoin=0,points=[2431.75,470.961,2431.75,470.961,2431.92,463.379,2439,462.859,2439,462.859,2449,461.648,2448.66,470.621,2449,542.379,2449,542.379,2447.28,555.148,2458.49,555.32,2458.49,555.32,2469.88,557.039,2469.52,543.422,2469.52,469.762,2469.52,469.762,2469.7,463.211,2477.46,463.211,2477.46,463.211,2486.95,462.512,2486.6,469.762,2486.95,555.32,2486.95,555.32,2487.3,570.16,2502.47,572.23,2502.47,572.23,2517.83,574.98,2517.32,556.531,2515.07,497.359,2515.07,497.359,2515.07,490.809,2522.48,490.289,2522.48,490.289,2531.12,489.602,2531.62,497.879,2534.56,563.949,2534.56,563.949,2534.74,577.219,2548.19,577.57,2548.19,577.57,2560.1,579.988,2560.1,565.328,2560.1,494.43,2560.1,494.43,2560.61,487.871,2568.37,487.359,2568.37,487.359,2576.99,486.32,2577.17,495.289,2578.21,546.012,2578.21,546.012,2577.17,558.43,2589.59,559.109,2589.59,559.109,2601.15,561.352,2602.01,542.73,2602.01,447.34,2602.01,447.34,2604.43,331.59,2609.94,266.719,2563.02,254.988,2563.02,254.988,2556.13,250.16,2563.02,246.02,2627.2,252.23,2627.2,252.23,2615.46,415.078,2618.23,423.359,2618.23,423.359,2614.78,489.602,2617.53,539.969,2617.53,539.969,2619.08,570.672,2597.18,572.75,2597.18,572.75,2581.65,574.641,2575.62,570.16,2575.62,570.16,2574.58,592.762,2550.43,592.41,2550.43,592.41,2532.32,593.621,2524.21,580.68,2524.21,580.68,2515.07,589.832,2498.85,586.539,2498.85,586.539,2480.39,582.93,2473.66,566.539,2473.66,566.539,2459,573.609,2447.45,568.43,2447.45,568.43,2430.72,561.531,2431.75,532.719,2431.75,470.961],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))

        g.add(Path(points=[2431.75,470.961,2431.75,470.961,2431.92,463.379,2439,462.859,2439,462.859,2449,461.648,2448.66,470.621,2449,542.379,2449,542.379,2447.28,555.148,2458.49,555.32,2458.49,555.32,2469.88,557.039,2469.52,543.422,2469.52,469.762,2469.52,469.762,2469.7,463.211,2477.46,463.211,2477.46,463.211,2486.95,462.512,2486.6,469.762,2486.95,555.32,2486.95,555.32,2487.3,570.16,2502.47,572.23,2502.47,572.23,2517.83,574.98,2517.32,556.531,2515.07,497.359,2515.07,497.359,2515.07,490.809,2522.48,490.289,2522.48,490.289,2531.12,489.602,2531.62,497.879,2534.56,563.949,2534.56,563.949,2534.74,577.219,2548.19,577.57,2548.19,577.57,2560.1,579.988,2560.1,565.328,2560.1,494.43,2560.1,494.43,2560.61,487.871,2568.37,487.359,2568.37,487.359,2576.99,486.32,2577.17,495.289,2578.21,546.012,2578.21,546.012,2577.17,558.43,2589.59,559.109,2589.59,559.109,2601.15,561.352,2602.01,542.73,2602.01,447.34,2602.01,447.34,2604.43,331.59,2609.94,266.719,2563.02,254.988,2563.02,254.988,2556.13,250.16,2563.02,246.02,2627.2,252.23,2627.2,252.23,2615.46,415.078,2618.23,423.359,2618.23,423.359,2614.78,489.602,2617.53,539.969,2617.53,539.969,2619.08,570.672,2597.18,572.75,2597.18,572.75,2581.65,574.641,2575.62,570.16,2575.62,570.16,2574.58,592.762,2550.43,592.41,2550.43,592.41,2532.32,593.621,2524.21,580.68,2524.21,580.68,2515.07,589.832,2498.85,586.539,2498.85,586.539,2480.39,582.93,2473.66,566.539,2473.66,566.539,2459,573.609,2447.45,568.43,2447.45,568.43,2430.72,561.531,2431.75,532.719,2431.75,470.961],operators=[0,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,1],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[2546.13,352.281,2546.13,352.281,2547.49,353.66,2548.02,368.672,2548.02,368.672,2548.02,420.941,2548.02,423.191,2548.02,423.191,2548.36,445.09,2527.32,451.301,2527.32,451.301,2513.69,454.41,2502.13,444.57,2502.13,444.57,2487.64,429.051,2485.4,417.488,2485.4,417.488,2484.48,411.949,2485.76,409.621,2485.76,409.621,2489.56,404.852,2492.64,413.871,2492.64,413.871,2498.42,427.672,2512.48,435.43,2512.48,435.43,2522.48,440.949,2528.35,432.059,2528.35,432.059,2533.87,427.84,2534.39,404.73,2534.39,404.73,2534.74,369.879,2534.56,365.57,2534.56,365.57,2534.21,358.488,2531.28,351.082,2531.28,351.082,2527.49,338.828,2526.11,332.102,2526.11,332.102,2524.39,325.719,2525.42,308.301,2525.42,308.301,2526.46,300.699,2535.42,292.941,2535.42,292.941,2534.74,309.328,2536.12,315.711,2536.12,315.711,2536.81,328.48,2546.13,352.281],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))

        g.transform = (0.75 ,0, 0, 0.75, self.x-(s*2.6),self.y)
        g.scale(float(float(s)/float(600)), float(float(s)/float(600)))

        return g


class EarProtectionPPE(_Symbol):

    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc="x offset"),
        y = AttrMapValue(isNumber,desc="y offset"),
        size = AttrMapValue(isNumber,desc="scale"),
        background = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        fillColor = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        strokeColor = AttrMapValue(isColorOrNone,desc='the color of the stroke'),
        )

    def __init__(self,width=200.0,height=200.0,*args,**kw):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor = PPE_blue
        self.strokeColor = colors.white

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[0,0,4267,0,4267,2835,0,2835],operators=[0,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[402.484,2789.71,225.355,2789.71,81.7539,2646.12,81.7539,2468.99,81.7539,2291.85,225.355,2148.26,402.484,2148.26,579.621,2148.26,723.215,2291.85,723.215,2468.99,723.215,2646.12,579.621,2789.71,402.484,2789.71],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.fillColor))

        g.add(Path(points=[402.484,2789.71,225.355,2789.71,81.7539,2646.12,81.7539,2468.99,81.7539,2291.85,225.355,2148.26,402.484,2148.26,579.621,2148.26,723.215,2291.85,723.215,2468.99,723.215,2646.12,579.621,2789.71,402.484,2789.71],operators=[0,2,2,2,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,1,2,2,2,2,1,2,2,2,2,3,0,2,1,2,1,2,2,2,2,1,2,2,2,2,1,2,1,2,1,2,2,3,0,2,2,2,1,2,1,2,2,2,1,2,2,2,1,2,1,2,3],strokeOpacity=1,strokeLineJoin=0,points=[561.094,2525.91,544.793,2527.59,537.488,2550.84,526.965,2572.29,513.465,2590.83,484.273,2631,444.867,2653.12,402.496,2653.12,360.129,2653.12,320.691,2631,291.504,2590.83,278.031,2572.29,267.488,2550.84,260.203,2527.59,243.875,2525.91,242.715,2525.78,241.551,2525.64,240.402,2525.46,254.766,2608.14,321.883,2670.71,402.496,2670.71,483.133,2670.71,550.246,2608.14,564.582,2525.44,563.445,2525.64,562.277,2525.78,561.094,2525.91,523.949,2467.7,516.313,2466.97,510.301,2460.48,510.301,2452.67,510.301,2426.8,510.301,2421.05,513.578,2416,518.344,2413.48,513.871,2370.12,513.598,2367.38,514.309,2364.72,515.707,2362.59,516.852,2360.85,518.445,2359.41,520.367,2358.47,515.988,2347.61,510.84,2337.39,505.02,2328.01,486.277,2297.85,460.648,2276.03,431.477,2267.26,373.523,2267.26,344.328,2276.06,318.688,2297.88,299.977,2328.04,294.133,2337.41,288.977,2347.61,284.605,2358.47,286.52,2359.41,288.145,2360.85,289.281,2362.59,290.684,2364.75,291.398,2367.38,291.117,2370.12,286.656,2413.48,291.418,2416.02,294.699,2421.05,294.699,2426.8,294.699,2452.67,294.699,2460.48,288.684,2466.95,281.047,2467.7,276.332,2513.54,295.52,2583.76,344.758,2633.72,402.496,2633.72,460.219,2633.72,509.477,2583.76,528.672,2513.54,585.258,2518.16,573.445,2615.07,495.984,2690.12,402.496,2690.12,309.012,2690.12,231.566,2615.07,219.73,2518.17,198.992,2506.38,185.988,2483.03,188.578,2457.89,193.449,2410.68,196.941,2376.76,227.559,2351.88,261.473,2355.37,264.832,2355.71,271.691,2337.59,280.656,2320.79,291.504,2305.82,302.906,2290.13,315.891,2277.18,330.012,2267.26,342.707,2258.29,356.336,2251.75,370.563,2247.86,434.449,2247.86,448.656,2251.75,462.277,2258.29,474.984,2267.26,489.078,2277.18,502.059,2290.13,513.465,2305.82,524.336,2320.79,533.273,2337.59,540.152,2355.71,543.5,2355.37,577.414,2351.88,608.031,2376.76,611.527,2410.68,616.398,2457.89,618.977,2483.03,605.98,2506.36,585.258,2518.16],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))

        g.transform = (0.75 ,0, 0, 0.75, self.x+(s*0.001),self.y-(s*2.63))
        g.scale(float(float(s)/float(600)), float(float(s)/float(600)))

        return g


class HazmatSuitPPE(_Symbol):

    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc="x offset"),
        y = AttrMapValue(isNumber,desc="y offset"),
        size = AttrMapValue(isNumber,desc="scale"),
        background = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        fillColor = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        strokeColor = AttrMapValue(isColorOrNone,desc='the color of the stroke'),
        strokeWidth = AttrMapValue(isNumber,desc="width of stroke"),
        )

    def __init__(self,width=200.0,height=200.0,*args,**kw):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor = PPE_blue
        self.strokeColor = colors.white

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #circle
        g.add(Path(points=[1820.75,386.93,1820.69,387.398,1819.49,391.762,1819.24,392.031,1818.95,393.141,1811.02,393.988,1809.95,393.582,1805.53,391.898,1800.87,390.238,1789.3,375.871,1789.16,375.73,1787.52,374.039,1785.16,372.738,1784.42,372.922,1784.03,373.031,1782.26,374.621,1780.82,380.469,1780.79,380.609,1780.48,382.469,1778.15,397.398,1780.84,417.488,1780.86,417.621,1782.81,427.289,1785.02,438.012,1785.54,439.941,1785.58,440.078,1786.34,442.219,1788.98,450.961,1784.23,457.141,1782.26,459.719,1778.36,462.648,1771,461.969,1770.33,461.879,1767.67,461.352,1744.08,456.57,1736.26,453.609,1735.98,453.5,1735.38,453.25,1721.23,447.441,1701.8,457.719,1701.26,458.012,1700.68,458.191,1696.65,459.391,1678.34,464.469,1665.88,461.289,1664.13,461.691,1661.76,463.738,1657.6,467.359,1656.88,468.121,1655.95,468.93,1653.85,470.621,1653.38,471.02,1653.16,471.18,1651.57,472.461,1651.53,472.5,1649.24,474.328,1645.91,473.969,1644.08,471.699,1642.87,470.199,1641.04,467.93,1641.4,464.602,1643.66,462.77,1645.75,461.09,1648.89,458.352,1656,452.18,1655.59,451.41,1652.09,442.859,1646.89,424.27,1647.14,389.551,1647.18,388.859,1647.19,388.77,1648.12,379.551,1643.03,373.441,1619.78,341.891,1619.57,341.629,1618.02,339.77,1612.63,332.59,1614.26,324.238,1615.03,320.301,1617.68,314.762,1625.98,310.699,1626.83,310.289,1627.11,310.238,1627.56,309.82,1629.08,307.98,1629.08,302.07,1629.08,300.738,1629.25,289.051,1635.16,280.109,1635.17,280.09,1635.22,280.031,1635.37,279.789,1635.17,280.078,1635.64,278.988,1638.64,270.66,1631.87,251.73,1631.77,251.398,1631.56,250.691,1626.66,233.719,1635.82,221.559,1641.42,214.141,1650.61,210.379,1663.14,210.379,1663.64,210.352,1668.33,209.891,1695.47,208.031,1728.15,222.371,1728.27,222.422,1728.93,222.73,1744.22,229.59,1756.71,219.02,1757.26,218.48,1777.44,196.289,1779.46,194.078,1782.88,193.91,1785.1,195.93,1786.33,197.039,1788.55,199.059,1788.71,202.48,1786.69,204.711,1766.03,227.441,1765.57,227.898,1747.16,244.301,1725.01,234.68,1723.06,233.789,1691.2,219.832,1664.75,222.801,1664.49,222.84,1664.08,222.879,1663.66,222.879,1655.01,222.809,1649.02,224.871,1645.84,229.059,1641,235.422,1643.16,245.449,1643.66,247.48,1643.8,247.949,1652.82,273.512,1647.07,284.66,1645.83,286.648,1645.71,286.828,1642.37,291.73,1641.59,299.5,1641.58,302.07,1641.58,316.441,1634.81,320.75,1631.44,322,1630.67,322.352,1628.84,323.352,1626.91,324.801,1626.54,326.602,1626.05,329.051,1628.15,332.441,1629.21,333.672,1629.42,333.891,1652.76,365.602,1660.3,374.781,1659.89,386.828,1659.65,389.699,1659.64,390.121,1659.46,422.539,1664.34,439.461,1667.1,446.391,1667.44,448.672,1672.86,451.281,1687.42,448.98,1696.37,446.43,1696.7,446.289,1720.24,434.18,1738.44,440.98,1740.79,441.969,1746.61,444.129,1765.22,448.102,1772.42,449.551,1772.46,449.559,1773.62,449.629,1774.54,448.621,1774.45,447.461,1774.36,446.43,1774.12,445.199,1773.77,444.211,1773.5,443.469,1772.78,440.891,1768.56,419.82,1768.5,419.441,1765.27,395.77,1768.41,378.801,1768.56,378.09,1768.6,377.809,1770.92,368.09,1775.21,362.379,1781.35,360.809,1782.43,360.52,1783.49,360.41,1784.53,360.41,1791.97,360.41,1797.88,366.719,1798.62,367.531,1798.85,367.801,1808.02,379.262,1816.29,383.711,1819.6,385.141,1820.75,386.891,1821.07,385.711,1820.75,386.922,1820.75,386.93],operators=[0,1,1,1,2,2,1,2,2,1,2,1,2,1,2,2,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,1,2,1,2,2,1,2,1,2,1,1,2,1,2,1,1,2,2,1,1,2,2,1,2,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,2,1,2,2,2,1,2,1,2,2,2,1,2,1,1,1,1],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[2479.85,2789.71,2302.71,2789.71,2159.11,2646.12,2159.11,2468.99,2159.11,2291.85,2302.71,2148.26,2479.85,2148.26,2656.98,2148.26,2800.57,2291.85,2800.57,2468.99,2800.57,2646.12,2656.98,2789.71,2479.85,2789.71],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.fillColor))
        #suit
        g.add(Path(points=[2479.85,2789.71,2302.71,2789.71,2159.11,2646.12,2159.11,2468.99,2159.11,2291.85,2302.71,2148.26,2479.85,2148.26,2656.98,2148.26,2800.57,2291.85,2800.57,2468.99,2800.57,2646.12,2656.98,2789.71,2479.85,2789.71],operators=[0,2,2,2,2],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,1,2,2,1,2,2,3,0,1,1,2,1,2,2,1,2,2,1,2,2,1,2,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[2520.2,2626.93,2502.13,2626.55,2502.13,2626.55,2497.82,2625.89,2497.54,2631.39,2497.54,2631.39,2496.84,2636.88,2501.49,2637.46,2519.62,2637.39,2519.62,2637.39,2523.69,2637.39,2524.79,2633.2,2524.79,2633.2,2525.56,2627.52,2520.2,2626.93,2620.83,2501.14,2621.53,2502.31,2565.58,2666.44,2559.12,2690.05,2540.45,2690.14,2540.45,2690.14,2511.49,2690.95,2510.14,2690.98,2508.99,2691.85,2508.54,2693.11,2502.1,2710.97,2484.77,2709.94,2484.77,2709.94,2484.91,2512.35,2484.94,2505.07,2479.39,2505.54,2479.39,2505.54,2473.97,2505.28,2473.66,2511.65,2473.66,2511.65,2473.32,2709.42,2458.85,2709.56,2452.21,2697.23,2450.14,2692.31,2449.64,2691.11,2448.47,2690.32,2447.17,2690.32,2416.68,2690.32,2399.13,2688.43,2391.91,2664.5,2391.91,2664.5,2338.15,2501.17,2338.78,2500.16,2379.92,2494.52,2380.75,2495.03,2425.26,2619.02,2425.65,2618.95,2426.58,2502.38,2426.65,2494.81,2426.04,2487.25,2424.79,2479.79,2382.92,2231.24,2382.76,2230.26,2383.5,2229.37,2384.49,2229.35,2441.82,2228.7,2443.43,2230.05,2479.01,2439.36,2515.23,2229.53,2517.04,2228.03,2574,2229.33,2575.1,2229.35,2575.92,2230.35,2575.74,2231.43,2533.46,2482.81,2532.27,2489.86,2531.66,2497,2531.66,2504.15,2531.5,2620.48,2531.9,2620.55,2578.24,2494.29,2579.23,2493.71,2620.83,2501.14],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.strokeColor))

        g.transform = (0.75 ,0, 0, 0.75, self.x-(s*2.6),self.y-(s*2.63))
        g.scale(float(float(s)/float(600)), float(float(s)/float(600)))

        return g


class BareCircle(_Symbol):

    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc="x offset"),
        y = AttrMapValue(isNumber,desc="y offset"),
        size = AttrMapValue(isNumber,desc="scale"),
        background = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        fillColor = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        strokeColor = AttrMapValue(isColorOrNone,desc='the color of the stroke'),
        #strokeWidth = AttrMapValue(isNumber,desc="width of stroke"),
        )

    def __init__(self,width=200.0,height=200.0,*args,**kw):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor = PPE_blue
        self.strokeColor = colors.white

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[0,0,4267,0,4267,2835,0,2835],operators=[0,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,3],strokeOpacity=1,strokeLineJoin=0,points=[402.484,2789.71,225.355,2789.71,81.7539,2646.12,81.7539,2468.99,81.7539,2291.85,225.355,2148.26,402.484,2148.26,579.621,2148.26,723.215,2291.85,723.215,2468.99,723.215,2646.12,579.621,2789.71,402.484,2789.71],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=self.fillColor))

        g.transform = (0.75 ,0, 0, 0.75, self.x-(s*0.05),self.y-(s*2.6))
        g.scale(float(float(s)/float(600)), float(float(s)/float(600)))

        return g



def test():
    """
    This function produces a number of pdf files with examples of all
    the signs and symbols from this file.
    """
    labelFontSize = 10


    #PAGE 1

    D = shapes.Drawing(450,650)

    cb = EarProtectionPPE()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))


    tb = GlovesPPE()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    yn = HazmatSuitPPE()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss2 = BareCircle()
    ss2.x = 170
    ss2.y = 400
    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    # Do some in red & black to prove that feeding in strokeColor and fillColor attributes works OK.

    sf = EarProtectionPPE()
    sf.x = 20
    sf.y = 270
    sf.size = 100
    sf.strokeColor = colors.red
    sf.fillColor = colors.black
    D.add(sf)
    D.add(shapes.String(sf.x+(sf.size/2),(sf.y-(1.2*labelFontSize)),
                            sf.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ds = GlovesPPE()
    ds.x = 170
    ds.y = 270
    ds.size = 100
    ds.strokeColor = colors.red
    ds.fillColor = colors.black
    D.add(ds)
    D.add(shapes.String(ds.x+(ds.size/2),(ds.y-(1.2*labelFontSize)),
                            ds.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    na = HazmatSuitPPE()
    na.x = 320
    na.y = 270
    na.size=100
    na.strokeColor = colors.red
    na.fillColor = colors.black
    D.add(na)
    D.add(shapes.String(na.x+(na.size/2),(na.y-(1.2*labelFontSize)),
                            na.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss3 = BareCircle()
    ss3.x = 170
    ss3.y = 140
    ss3.strokeColor = colors.red
    ss3.fillColor = colors.black
    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    D.add(shapes.String(450/2,26,
                        "MANDATORY PPE SYMBOLS",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))

    renderPDF.drawToFile(D, 'protection_ppe_widgets_1.pdf', 'protection_ppe_widgets_1.py')
    print('wrote file: protection_ppe_widgets_1.pdf')


def make_example_signs():
    ppe_list = ["EAR_PROTECTION", "GLOVES", "HAZMAT_SUITS"]

    ppe_warnings_list = ['EAR PROTECTION', # 'EAR PROTECTION MUST BE WORN'
                         "GLOVES", # "GLOVES MUST BE WORN"
                         'CLASS A HAZMAT SUITS' # 'CLASS A HAZMAT SUITS MUST BE WORN'
                         ]

    height = 1080
    width = 720
    margin = 24

    print

    for this_risk in ppe_list:
        risk_filename_stub = this_risk.lower()
        risk_filename_stub = "protection_ppe_sign_%02d_%s" % (ppe_list.index(this_risk)+1, this_risk.lower())
        #risk_fontsize = 72
        #risk_fontsize2 = 72
        risk_fontsize = 52
        risk_fontsize2 = 52

        if this_risk == "HAZMAT_SUITS":
            risk_fontsize1 = 42
        else:
            risk_fontsize1 = 52

        risk_font = "Gill Sans Nova Bold"
        
        #risk_line1_y = height-700
        risk_line1_y = height-750
        risk_line2_y = risk_line1_y - (risk_fontsize * 1.25)

        risk_box_width = width - (margin*6)
        risk_box_height = (risk_fontsize * 2.0) + 100

        risk_box_x1 = margin * 3
        risk_box_y1 = (risk_line1_y - 25)-(risk_box_height/2.0)

        drisk = Drawing(width, height)
        drisk.add(Rect(0, 0, width, height, fillColor=colors.white))
        drisk.add(Rect(risk_box_x1, risk_box_y1, risk_box_width, risk_box_height, fillColor=PPE_blue, strokeColor=PPE_blue))


        if this_risk == "EAR_PROTECTION":
            risk_widget = EarProtectionPPE()
        elif this_risk == "GLOVES":
            risk_widget = GlovesPPE()
        elif this_risk == "HAZMAT_SUITS":
            risk_widget = HazmatSuitPPE()

        else:
            risk_widget = BareCircle()

        drisk.add(risk_widget)

        risk_widget.x = risk_box_x1                     # symbol x coordinate
        risk_widget.y = height - 50 - risk_box_width    # symbol y coordinate
        risk_widget.size = risk_box_width

        risk_line_1 = ppe_warnings_list[ppe_list.index(this_risk)]
        risk_line_2 = "MUST BE WORN"

        risk_line_1_width = stringWidth(risk_line_1, risk_font, risk_fontsize1)
        risk_line_2_width = stringWidth(risk_line_2, risk_font, risk_fontsize2)

        risk_line_1_x = (width - risk_line_1_width)/2.0
        risk_line_1_y = risk_line1_y

        risk_line_2_x = (width - risk_line_2_width)/2.0
        risk_line_2_y = risk_line2_y

        #EAR PROTECTION/GLOVES/CLASS A HAZMAT SUITS
        drisk.add(String(risk_line_1_x, risk_line_1_y, risk_line_1, fontName=risk_font, fontSize=risk_fontsize1, fillColor=colors.white))
        #"MUST BE WORN" line
        drisk.add(String(risk_line_2_x, risk_line_2_y, risk_line_2, fontName=risk_font, fontSize=risk_fontsize2, fillColor=colors.white))

        lgrisk = scp_widgets.SCPLogo()
        lgrisk.size = 80

        lgrisk.x = width - (margin * 3) - lgrisk.size
        lgrisk.y = height-1025
        drisk.add(lgrisk)

        drisk.add(String((lgrisk.x+(lgrisk.size*0.6))-(stringWidth('Secure. Contain. Protect', "Bauhaus Demi", 12)/2.0),
                         lgrisk.y-(lgrisk.size*0.35), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=12, fillColor=colors.black))

        lgrisk = scp_widgets.SCPLogo()
        lgrisk.size = 80

        lgrisk.x = width - (margin * 3) - lgrisk.size
        lgrisk.y = height-1025
        drisk.add(lgrisk)

        drisk.add(String((lgrisk.x+(lgrisk.size*0.6))-(stringWidth('Secure. Contain. Protect', "Bauhaus Demi", 12)/2.0),
                         lgrisk.y-(lgrisk.size*0.35), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=12, fillColor=colors.black))

        renderPM.drawToFile(drisk, '%s.png' % risk_filename_stub, 'PNG')
        print "WROTE '%s.png'" % risk_filename_stub
        if os.path.isdir(os.path.join(os.getcwd(), "images", "signage", "containment")):
            renderPM.drawToFile(drisk, '%s.png' % os.path.join(os.getcwd(), "images", "signage", "containment", risk_filename_stub), 'PNG')
            print "WROTE '%s.png'" % os.path.join(os.getcwd(), "images", "signage", "containment", risk_filename_stub)

        renderPDF.drawToFile(drisk, '%s.pdf' % risk_filename_stub, this_risk)
        print "WROTE '%s.pdf'" % risk_filename_stub
        if os.path.isdir(os.path.join(os.getcwd(), "images", "signage", "containment")):
            renderPDF.drawToFile(drisk, os.path.join(os.getcwd(), "images", "signage", "containment", '%s.pdf' % risk_filename_stub), this_risk)
            print "WROTE '%s.pdf'" % os.path.join(os.getcwd(), "images", "signage", "containment", risk_filename_stub)

        print


def make_elements():

    outputdir = os.path.join(os.getcwd(),"images", "signage", "elements")

    for obj in sys.modules['__main__'].__dict__:
        #print "trying '%s'" % obj
        if type(eval(obj)) == ClassType:
            x = eval(obj)
            if "draw" in x.__dict__:
                fnamestub = os.path.join(outputdir, obj)
                height = 720
                width = 720
                margin = 32
                d = Drawing(width, height)
                item = eval("%s()" % obj)
                #print x
                #print type(x)
                try:
                    item.x = margin
                    #item.y = height - margin
                    item.y = margin
                    item.size = height-(margin*2)
                    #specials...
                    if obj == "SCPLogo":
                        item.x = 0-(margin)
                        item.y = item.y + (margin*2.5)
                        item.size = height-(margin*2.15)
                    d.add(item)
                    renderPDF.drawToFile(d, '%s.pdf' % fnamestub, obj)
                    print "\twrote file '%s'.pdf" % fnamestub
                    renderPM.drawToFile(d, '%s.png' % fnamestub, 'PNG')
                    print "\twrote file '%s'.png" % fnamestub
                except:
                    #we don't care if we can't make something for eg Widget or Drawing
                    pass


if __name__=='__main__':
    test()
    make_example_signs()
    if MAKE_ELEMENTS > 0:
        make_elements()

