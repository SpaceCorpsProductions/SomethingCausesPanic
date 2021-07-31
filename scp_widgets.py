#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Widgets made using the reportlab toolkit implementing the SCP
warning symbols from the Anomaly Classification System (ACS). """

#Unless otherwise stated, the SCP ACS symbols are taken from:
#http://www.scpwiki.com/component:anomaly-class-bar

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.

import random, string

#hope we have svglib installed...
from svglib.svglib import NoStrokePath, ClippingPath

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
from reportlab.graphics import shapes
from reportlab.graphics.widgetbase import Widget
from reportlab.graphics import renderPDF
from reportlab.graphics import renderPM

from reportlab.graphics.shapes import Drawing, Group, Path, Ellipse, Circle, Polygon
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

from errors import ObjectClassError, DisruptionClassError, RiskClassError


MAKE_ELEMENTS = 1
MAKE_ELEMENTS = 0


#DEFINE OUR CUSTOM COLORS...
#YELLOW
#Object/Disruption/Risk
#Euclid/KENEQ/Warning
yellow_background_colour = colors.Color(253.0/255.0,
                                        246.0/255.0,
                                        214.0/255.0)
yellow_bar_colour = colors.Color(254.0/255.0,
                                 211.0/255.0,
                                 0.0/255.0)

#BLUE
#Object/Disruption/Risk
#-/VLAM/Caution
blue_background_colour = colors.Color(214.0/255.0,
                                        234.0/255.0,
                                        242.0/255.0)
blue_bar_colour = colors.Color(0.0/255.0,
                               135.0/255.0,
                               189.0/255.0)
                                        
#GREEN
#Object/Disruption/Risk
#Safe/DARK/Notice
green_background_colour = colors.Color(215.0/255.0,
                                       230.0/255.0,
                                       231.0/255.0)
green_bar_colour = colors.Color(0.0/255.0,
                                159.0/255.0,
                                107.0/255.0)

#RED
#Object/Disruption/Risk
#Keter/Critical/AMIDA
red_background_colour = colors.Color(246.0/255.0,
                                        217.0/255.0,
                                        224.0/255.0)
red_bar_colour = colors.Color(196.0/255.0,
                              2.0/255.0,
                              51.0/255.0)
                                        
#ORANGE
#Object/Disruption/Risk
#-/EKHI/Danger
orange_background_colour = colors.Color(255.0/255.0,
                                        233.0/255.0,
                                        217.0/255.0)

orange_bar_colour = colors.Color(255.0/255.0,
                                 109.0/255.0,
                                 0.0/255.0)


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


#from: http://scp-wiki.wikidot.com/local--files/component:anomaly-class-bar/safe-icon.svg
#stored ss D:\New_SCP_Game\images\tmp_containment_classes_SVG\safe-icon.svg

class SafeLock(_Symbol):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[117.7,54.5,117.7,50.7,114.7,47.5,110.7,47.5,89.3,47.5,85.5,47.5,82.3,50.5,82.3,54.5,82.3,82,117.7,82,117.7,54.5],operators=[0,2,1,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[137.6,82.5,137.6,82.2,137.6,79.2,137.6,47.5,137.6,36.6,128.8,27.6,117.7,27.6,82.3,27.6,71.3,27.6,62.4,36.4,62.4,47.5,62.4,78.5,62.4,82.3,62.4,82.6,52,84.4,44,93.5,44,104.5,44,142,44,154.3,54,164.2,66.2,164.2,134.1,164.2,146.4,164.2,156.3,154.2,156.3,142,156.3,104.4,156.3,93.2,148.2,84.1,137.6,82.5,82.3,54.5,82.3,50.6,85.5,47.5,89.3,47.5,110.8,47.5,114.7,47.5,117.8,50.7,117.8,54.5,117.8,82,82.3,82,82.3,54.5,99.9,148.8,85.7,148.8,74.1,137.2,74.1,123,74.1,108.8,85.7,97.2,99.9,97.2,114.1,97.2,125.7,108.8,125.7,123,125.7,137.2,114.1,148.8,99.9,148.8],operators=[0,1,1,1,2,1,2,1,1,1,2,1,2,1,2,1,2,3,0,2,1,2,1,1,1,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        v1=g._nn(Group())
        v1.transform = (.3827,-0.9239,.9239,.3827,-51.9271,168.1886)
        v1.add(Ellipse(99.9,123,18,18,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[99.9,97.1,85.7,97.1,74.1,108.7,74.1,122.9,74.1,137.1,85.7,148.7,99.9,148.7,114.1,148.7,125.7,137.1,125.7,122.9,125.7,108.7,114.1,97.1,99.9,97.1,99.9,140.9,90,140.9,81.9,132.9,81.9,122.9,81.9,112.9,89.9,104.9,99.9,104.9,109.9,104.9,117.9,112.9,117.9,122.9,117.9,132.9,109.8,140.9,99.9,140.9],operators=[0,2,2,2,2,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


#from: http://scp-wiki.wikidot.com/local--files/component:anomaly-class-bar/euclid-icon.svg
#stored ss D:\New_SCP_Game\images\tmp_containment_classes_SVG\euclid-icon.svg

class EuclidLock(_Symbol):

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

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[113.7,54.5,113.7,52.7,112.2,51.2,110.4,51.2,89,51.2,87.2,51.2,85.7,52.7,85.7,54.5,85.7,78.4,113.7,78.4,113.7,54.5],operators=[0,2,1,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[136.7,86.1,133.6,85.6,133.6,47.5,133.6,38.6,126.3,31.3,117.4,31.3,82,31.3,73.1,31.3,65.8,38.6,65.8,47.5,65.8,85.7,62.7,86.2,53.8,87.7,47.4,95.4,47.4,104.5,47.4,142,47.4,152.2,55.7,160.5,65.9,160.5,133.8,160.5,144,160.5,152.3,152.2,152.3,142,152.3,104.4,152.3,95.2,145.8,87.5,136.7,86.1,78.3,54.5,78.3,48.6,83.1,43.9,88.9,43.9,110.4,43.9,116.3,43.9,121,48.7,121,54.5,121,85.7,78.3,85.7,78.3,54.5,99.9,148.8,99.9,148.8,99.8,148.8,99.8,148.8,99.8,148.8,99.7,148.8,99.7,148.8,85.5,148.8,73.9,137.2,73.9,123,73.9,108.8,85.5,97.2,99.7,97.2,99.7,97.2,99.8,97.2,99.8,97.2,99.8,97.2,99.9,97.2,99.9,97.2,114.1,97.2,125.7,108.8,125.7,123,125.7,137.2,114.1,148.8,99.9,148.8],operators=[0,1,1,2,1,2,1,1,2,1,2,1,2,1,2,3,0,2,1,2,1,1,1,3,0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Ellipse(99.7,123,17.8,18,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[141,79.5,141,47.5,141,34.5,130.4,23.9,117.4,23.9,82,23.9,69,23.9,58.4,34.5,58.4,47.5,58.4,79.7,47.6,82.9,40,92.9,40,104.5,40,142,40,156.3,51.6,167.9,65.9,167.9,133.8,167.9,148.1,167.9,159.7,156.3,159.7,142,159.7,104.4,159.7,92.6,152,82.6,141,79.5,152.3,142,152.3,152.2,144,160.5,133.8,160.5,65.9,160.5,55.7,160.5,47.4,152.2,47.4,142,47.4,104.6,47.4,95.5,53.9,87.8,62.7,86.3,65.8,85.8,65.8,47.5,65.8,38.6,73.1,31.3,82,31.3,117.4,31.3,126.3,31.3,133.6,38.6,133.6,47.5,133.6,85.6,136.7,86.1,145.7,87.5,152.3,95.1,152.3,104.4,152.3,142],operators=[0,1,2,1,2,1,2,1,2,1,2,1,2,3,0,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[121.1,54.5,121.1,48.6,116.3,43.9,110.5,43.9,89,43.9,83.1,43.9,78.4,48.7,78.4,54.5,78.4,85.7,121.2,85.7,121.2,54.5,85.7,54.5,85.7,52.7,87.2,51.2,89,51.2,110.5,51.2,112.3,51.2,113.8,52.7,113.8,54.5,113.8,78.4,85.8,78.4,85.8,54.5],operators=[0,2,1,2,1,1,1,3,0,2,1,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[99.9,105,99.9,105,99.8,105,99.8,105,109.7,105.1,117.6,113,117.6,123,117.6,133,109.6,140.9,99.8,141,99.8,141,99.9,141,99.9,141,109.8,141,117.9,133,117.9,123,117.9,113,109.9,105,99.9,105],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[74,123,74,108.8,85.5,97.3,99.7,97.2,99.7,97.2,99.6,97.2,99.6,97.2,85.4,97.2,73.8,108.8,73.8,123,73.8,137.2,85.4,148.8,99.6,148.8,99.6,148.8,99.7,148.8,99.7,148.8,85.6,148.7,74,137.1,74,123],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[99.9,97.1,99.9,97.1,99.8,97.1,99.8,97.1,85.6,97.2,74,108.8,74,123,74,137.2,85.5,148.7,99.7,148.8,99.7,148.8,99.8,148.8,99.8,148.8,114,148.8,125.6,137.2,125.6,123,125.6,108.8,114.1,97.1,99.9,97.1,117.8,123,117.8,133,109.7,141,99.8,141,99.8,141,99.7,141,99.7,141,89.9,140.9,81.9,133,81.9,123,81.9,113,89.8,105.1,99.7,105,99.7,105,99.8,105,99.8,105,109.9,105,117.8,112.9,117.8,123],operators=[0,2,2,2,2,2,2,3,0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class KeterLock(_Symbol):

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

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[60.1,96,60.6,95.9,61,95.9,61.5,96,62,96,64.4,95.8,66.6,97.2,67.5,99.4,74,114.8,79.7,125.7,114.8,106.5,115.6,106,116.5,105.8,117.4,105.8,117.9,105.8,118.5,105.9,119,106,120.4,106.4,121.6,107.4,122.3,108.7,133.7,130,153,120.1,149.5,93.7,148.3,84.6,140.9,77.9,131.9,77.6,128.3,78.1,123,38.7,121.8,29.9,113.8,23.7,105,24.8,72.1,33,68.2,34,65.7,37.7,66.2,41.7,68.7,60.4,68.8,61.4,69.8,62.1,70.8,62,76.8,61.2,77.8,61.1,78.5,60.1,78.4,59.1,77.5,52.1,76.9,47.2,80,42.6,84.8,41.5,99.5,38.1,105.3,37.3,110.7,41.4,111.5,47.3,115.8,79.8,57.6,87.6,49.9,88.7,46.7,91,45.9,97.1,58.5,96.2,60.1,96],operators=[0,2,1,2,1,1,1,2,2,2,1,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[119.8,147.1,113.8,124,79.7,134.7,77,135.6,74.1,134.2,73,131.6,61.2,103.5,45.7,104.6,42.2,138.4,41.7,143.3,43.1,148.2,46.3,152,49.4,155.8,53.8,158.2,58.7,158.7,126.2,165.7,131.1,166.2,136,164.8,139.8,161.6,143.6,158.5,146,154.1,146.5,149.2,146.8,146.1,126.5,151,123.6,151.8,120.6,150,119.8,147.1],operators=[0,1,1,2,1,1,1,2,2,1,2,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[160.4,120.4,156.7,92.7,155.1,80.9,146.1,72,134.6,70.5,130.3,37.8,128.6,24.9,116.7,15.8,103.9,17.5,70.4,25.9,62.9,27.8,58,35,59,42.7,61.5,61.4,62.2,66.5,66.8,70,71.9,69.3,77.9,68.5,82.9,67.8,86.5,63.2,85.9,58.2,85,51.2,84.9,50.1,85.6,49,86.7,48.8,100.9,45.5,102.6,45.3,104.2,46.6,104.4,48.3,107.7,73.5,56.8,80.3,43.7,82.2,38.2,88.6,38.5,101.8,38.6,102.5,34.9,137.5,34.2,144.4,36.2,151.2,40.6,156.5,45,161.8,51.1,165.2,58,165.9,125.5,172.9,126.4,173,127.3,173,128.2,173,134.1,173,139.8,171,144.5,167.2,149.8,162.8,153.2,156.7,153.9,149.8,154.5,144.1,154.7,142.3,154,140.5,152.6,139.4,151.2,138.2,149.4,137.8,147.7,138.2,126.6,143.3,120.9,121.6,128,134.9,129,136.8,130.9,137.8,132.9,137.8,133.7,137.8,134.6,137.6,135.4,137.2,157.5,125.9,159.5,125,160.7,122.7,160.4,120.4,126.5,151,146.8,146.1,146.5,149.2,146,154.1,143.6,158.5,139.8,161.6,136,164.7,131.1,166.2,126.2,165.7,58.7,158.7,53.8,158.2,49.4,155.8,46.3,152,43.2,148.2,41.7,143.3,42.2,138.4,45.7,104.6,61.2,103.5,73,131.6,74.1,134.2,77,135.6,79.7,134.7,113.8,124,119.8,147.1,120.6,150,123.6,151.8,126.5,151,133.6,130,122.2,108.7,121.5,107.4,120.3,106.4,118.9,106,118.4,105.8,117.8,105.8,117.3,105.8,116.4,105.8,115.5,106,114.7,106.5,79.6,125.7,73.9,114.8,67.4,99.4,66.5,97.2,64.3,95.9,61.9,96,61.4,96,61,95.9,60.5,95.9,60,96,58.4,96.2,45.8,97.1,46.6,91,49.8,88.7,57.5,87.6,115.7,79.8,111.4,47.3,110.6,41.5,105.3,37.4,99.4,38.1,84.7,41.5,79.9,42.6,76.7,47.2,77.4,52.1,78.3,59.1,78.4,60.1,77.7,61.1,76.7,61.2,70.7,62,69.7,62.1,68.7,61.4,68.6,60.4,66.1,41.7,65.6,37.7,68.1,34,72,33,104.9,24.7,113.7,23.6,121.7,29.9,122.9,38.6,128.1,78,131.7,77.5,140.7,77.8,148.1,84.5,149.3,93.6,152.8,120,133.6,130],operators=[0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,2,2,1,2,2,2,1,2,2,1,1,1,2,2,1,2,3,0,1,1,2,2,1,2,2,1,1,1,2,1,1,2,3,0,1,2,2,2,1,1,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g



#danger-diamond

class DangerDiamond(_Symbol):
    """This widget draws our 'Danger Diamond'.

        possible attributes:
        'x', 'y', 'size', 'fillColor', 'strokeColor', 'strokeWidth',

        ObjectClass: (Safe/Euclid/Keter/Thaumiel/Neutralized/Esoteric)
        DisruptionClass: (DARK/KENEQ/VLAM/EKHI/AMIDA)
        RiskClass: (Notice/Warning/Caution/Danger/Critical)
        SecondaryClass: (Archon/Apollyon/Cernunnos/Thaumiel etc)
    """
    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc="x offset"),
        y = AttrMapValue(isNumber,desc="y offset"),
        size = AttrMapValue(isNumber,desc="scale"),
        contents = AttrMapValue(None,desc="Contained drawable elements"),

        fillColor = AttrMapValue(isColorOrNone,desc='the color of the fill'),
        strokeColor = AttrMapValue(isColorOrNone,desc='the color of the stroke'),
        strokeWidth = AttrMapValue(isNumber,desc="width of stroke"),

        DisruptionClass = AttrMapValue(isNoneOrString, desc="DARK/KENEQ/VLAM/EKHI/AMIDA"),
        RiskClass = AttrMapValue(isNoneOrString,desc="Notice/Warning/Caution/Danger/Critical"),
        ObjectClass = AttrMapValue(isNoneOrString, desc="Safe/Euclid/Keter/Thaumiel/Neutralized/Esoteric"),
        SecondaryClass = AttrMapValue(isNoneOrString, desc="Archon/Apollyon/Cernunnos/Thaumiel etc")#,
        )

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor = None
        self.strokeColor = colors.black
        self.strokeWidth = 4

        self.DisruptionClass = None
        self.RiskClass = None
        self.ObjectClass = None
        self.SecondaryClass = None

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        athird=s/3

        quadrant1Symbol = None
        quadrant2Symbol = None
        quadrant3Symbol = None
        quadrant5Symbol = None

        #SYMBOLSIZE = s * 0.2
        #SYMBOLSIZE = s * 0.4
        #SYMBOLSIZE = s * 0.33
        SYMBOLSIZE = s * 0.32
        #SYMBOLSIZE = s * 0.4

        if self.ObjectClass != None:
            self.ObjectClass = string.capwords(self.ObjectClass)
        if self.RiskClass != None:
            self.RiskClass = string.capwords(self.RiskClass)
        if self.DisruptionClass != None:
            self.DisruptionClass = string.upper(self.DisruptionClass)
        if self.ObjectClass == "Neutralised":
            self.ObjectClass = "Neutralized"

        if self.DisruptionClass in [None, ""]:
            quadrant1FillColour = None
        elif self.DisruptionClass == "DARK":
            quadrant1FillColour = green_background_colour
            quadrant1Symbol = DARK()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            #quadrant1Symbol.size = 38
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass == "VLAM":
            quadrant1FillColour = blue_background_colour
            quadrant1Symbol = VLAM()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass == "KENEQ":
            quadrant1FillColour = yellow_background_colour
            quadrant1Symbol = KENEQ()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass == "EKHI":
            quadrant1FillColour = red_background_colour
            quadrant1Symbol = EKHI()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass == "AMIDA":
            quadrant1FillColour = red_background_colour
            quadrant1Symbol = AMIDA()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass == "GEVURAH":
            tmp_pink = colors.Color(215.0/255.0,
                                        6.0/255.0,
                                        111.0/255.0)
            quadrant1FillColour = tmp_pink
            quadrant1Symbol = Gevurah()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE

        elif self.DisruptionClass in ["NULL", "N/A", "N/a", "NONE"]:
            quadrant1FillColour = colors.lightgrey
            quadrant1Symbol = Null()
            quadrant1Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant1Symbol.y = (self.y+(s/2.0))-20
            quadrant1Symbol.size = SYMBOLSIZE
        else:
            #raise "UNKNOWN DISRUPTIONCLASS '%s'!" % self.DisruptionClass
            raise DisruptionClassError("UNKNOWN DISRUPTIONCLASS '%s'!" % self.DisruptionClass)

        if self.RiskClass in [None, ""]:
            quadrant3FillColour = None
        elif self.RiskClass == "Notice":
            quadrant3FillColour = green_background_colour
            quadrant3Symbol = Notice()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            #quadrant3Symbol.size = 38
            quadrant3Symbol.size = SYMBOLSIZE
        elif self.RiskClass == "Caution":
            quadrant3FillColour = blue_background_colour
            quadrant3Symbol = Caution()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            quadrant3Symbol.size = SYMBOLSIZE
        elif self.RiskClass == "Warning":
            quadrant3FillColour = yellow_background_colour
            quadrant3Symbol = Warning()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            quadrant3Symbol.size = SYMBOLSIZE
        elif self.RiskClass == "Danger":
            quadrant3FillColour = red_background_colour
            quadrant3Symbol = Danger()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            quadrant3Symbol.size = SYMBOLSIZE
        elif self.RiskClass == "Critical":
            quadrant3FillColour = red_background_colour
            quadrant3Symbol = Critical()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            quadrant3Symbol.size = SYMBOLSIZE
        elif self.RiskClass in ["NULL", "Null", "N/A", "N/a", "NONE", "None"]:
            quadrant3FillColour = colors.lightgrey
            quadrant3Symbol = Null()
            quadrant3Symbol.x = ((self.x+(s/2.0)))+(athird)-24
            quadrant3Symbol.y = (self.y+(s/2.0))-20
            quadrant3Symbol.size = SYMBOLSIZE

        else:
            #raise "UNKNOWN RISKCLASS '%s'!" % self.RiskClass
            raise RiskClassError("UNKNOWN RISKCLASS '%s'!" % self.RiskClass)


        if self.ObjectClass in [None, ""]:
            quadrant2FillColour = None
        elif self.ObjectClass == "Safe":
            quadrant2FillColour = green_background_colour
            quadrant2Symbol = Safe()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            #quadrant2Symbol.size = 40
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Euclid":
            quadrant2FillColour = yellow_background_colour
            quadrant2Symbol = Euclid()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Keter":
            quadrant2FillColour = red_background_colour
            quadrant2Symbol = Keter()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Thaumiel":
            quadrant2FillColour = colors.white
            quadrant2Symbol = Thaumiel()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Neutralized":
            #quadrant2FillColour = colors.grey
            quadrant2FillColour = colors.lightgrey
            quadrant2Symbol = Neutralized()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Esoteric":
            quadrant2FillColour = colors.white
            quadrant2Symbol = Esoteric()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Pending":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Pending()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Archon":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Archon()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Apollyon":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Apollyon()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Hiemal":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Hiemal()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Tiamat":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Tiamat()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Ticonderoga":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Ticonderoga()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass in ["N/A", "N/a", "Null", "None", "NONE", "Uncontained", "Unknown"]:
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Null()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Gevurah":
            tmp_pink = colors.Color(215.0/255.0,
                                        6.0/255.0,
                                        111.0/255.0)
            quadrant2FillColour = tmp_pink
            quadrant2Symbol = Gevurah()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass in ["Gödel", u"Gödel", "Godel", u"G\xf6del", "G\xf6del"]:
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Godel()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Hera":
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Hera()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Explained":
            #quadrant2FillColour = colors.grey
            quadrant2FillColour = colors.lightgrey
            quadrant2Symbol = Explained()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Decommissioned":
            #quadrant2FillColour = colors.grey
            quadrant2FillColour = colors.lightgrey
            quadrant2Symbol = Decommissioned()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass == "Declassified":
            #quadrant2FillColour = colors.grey
            quadrant2FillColour = colors.lightgrey
            quadrant2Symbol = Declassified()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        elif self.ObjectClass in ["Zeno", "Kronecker", "Eparch", "Damballah", "Yesod"]:
            #no specific logos for these ones,
            #just use the standard Esoteric class logo
            quadrant2FillColour = colors.grey
            quadrant2Symbol = Esoteric()
            quadrant2Symbol.x = (self.x+(s/2.0))-20
            quadrant2Symbol.y = (self.y+(athird*2.5))-25
            quadrant2Symbol.size = SYMBOLSIZE

        else:
            #raise "UNKNOWN OBJECTCLASS '%s'!" % self.ObjectClass
            if type(self.ObjectClass) == StringType:
                raise ObjectClassError("UNKNOWN OBJECTCLASS '%s'!" % self.ObjectClass)
            else:
                raise ObjectClassError("UNKNOWN OBJECTCLASS '%s'!" % self.ObjectClass.encode("ASCII", "ignore"))

        if self.SecondaryClass != None:
            quadrant2FillColour = colors.grey

        if self.DisruptionClass == None:
            if self.RiskClass == None:
                if self.ObjectClass == None:
                    #plain white DangerDiamond looks BORING...
                    #let's have some shading at least...
                    poss_fill_colours = [yellow_background_colour,
                                         blue_background_colour,
                                         green_background_colour]
                    quadrant1FillColour = random.choice(poss_fill_colours)
                    quadrant2FillColour = random.choice(poss_fill_colours)
                    quadrant3FillColour = random.choice(poss_fill_colours)

        quadrant1 = shapes.Polygon(points = [((self.x+(s/2.0))-(self.strokeWidth/2.0)),
                                             (self.y+(s/2.0)),
                                             self.x+(athird/2.0), (self.y+(athird*2.5))-(self.strokeWidth/2.0),
                                             self.x+(self.strokeWidth/2.0), self.y+(athird*2),
                                             self.x+(self.strokeWidth/2.0), self.y+athird,
                                             self.x+(athird/2.0), (self.y+(athird/2.0))+(self.strokeWidth/2.0)
                                             ],
                                   fillColor = quadrant1FillColour
                                   )
        g.add(quadrant1)
                                             
        quadrant2 = shapes.Polygon(points = [(self.x+(s/2.0)), (self.y+(s/2.0))+(self.strokeWidth/2.0),
                                             ((self.x+(athird*2.5))-(self.strokeWidth/2.0)),
#                                             ((self.x+(athird*2.5))),
                                             (self.y+(athird*2.5))-(self.strokeWidth/2.0),
#                                             (self.y+(athird*2.5)),
                                             (self.x+(athird*2))-(self.strokeWidth/2.0),
                                             (self.y+s)-(self.strokeWidth/2.0),
                                             (self.x+(athird)+(self.strokeWidth/2.0)),
                                             (self.y+s)-(self.strokeWidth/2.0),
                                             (self.x)+(athird*0.5)+(self.strokeWidth/2.0),
                                             self.y+(athird*2.5)-(self.strokeWidth/2.0),
#                                             (self.x+s)-(athird/2.0), (self.y+(athird/2.0))+(self.strokeWidth/2.0)
                                             ],
                                   fillColor = quadrant2FillColour
                                   )

        g.add(quadrant2)

        quadrant3 = shapes.Polygon(points = [((self.x+(s/2.0))+(self.strokeWidth/2.0)),
                                             (self.y+(s/2.0)),
                                             ((self.x+s)-(athird/2.0)),
                                             (self.y+(athird*2.5))-(self.strokeWidth/2.0),
                                             (self.x+s-(self.strokeWidth/2.0)), self.y+(athird*2)-(self.strokeWidth/2.0),
                                             (self.x+s)-(self.strokeWidth/2.0), self.y+athird,
                                             (self.x+s)-(athird/2.0), (self.y+(athird/2.0))+(self.strokeWidth/2.0)
                                             ],
                                   fillColor = quadrant3FillColour
                                   )
        g.add(quadrant3)


        octagon = shapes.Polygon(points=[self.x+athird, self.y,
                                              self.x, self.y+athird,
                                              self.x, self.y+(athird*2),
                                              self.x+athird, self.y+s,
                                              self.x+(athird*2), self.y+s,
                                              self.x+s, self.y+(athird*2),
                                              self.x+s, self.y+athird,
                                              self.x+(athird*2), self.y],
                                      strokeColor = self.strokeColor,
                                      fillColor = self.fillColor,
                                      strokeWidth=self.strokeWidth)
        g.add(octagon)

        g.add(shapes.Line(self.x+1, self.y+1, self.x+self.size-1, (self.y+self.size)-1,
                          strokeColor=colors.black,
                          strokeWidth=self.strokeWidth,
                          fillColor = colors.black
                          ))
        g.add(shapes.Line(self.x+1, (self.y+self.size)-1, (self.x+self.size)-1, (self.y)+1,
                          strokeColor=colors.black,
                          strokeWidth=self.strokeWidth,
                          fillColor = colors.black
                          ))

        triangle1 = shapes.Polygon(points = [
            self.x, self.y,
            self.x, self.y+(s/20),
            self.x+(s/20),self.y],
               fillColor = colors.black,
               strokeColor = colors.black,
               strokeWidth=s/50.)
        g.add(triangle1)

        triangle2 = shapes.Polygon(points = [
            self.x, self.y+s,
            self.x, (self.y+s)-(s/20),
            self.x+(s/20),self.y+s],
               fillColor = colors.black,
               strokeColor = colors.black,
               strokeWidth=s/50.)
        g.add(triangle2)

        triangle3 = shapes.Polygon(points = [
            self.x+s, self.y+s,
            (self.x+s)-(s/20), self.y+s,
            self.x+s,(self.y+s)-(s/20)],
               fillColor = colors.black,
               strokeColor = colors.black,
               strokeWidth=s/50.)
        g.add(triangle3)

        triangle4 = shapes.Polygon(points = [
            self.x+s, self.y,
            self.x+s-(s/20), self.y,
            self.x+s,self.y+(s/20)],
               fillColor = colors.black,
               strokeColor = colors.black,
               strokeWidth=s/50.)
        g.add(triangle4)

        if quadrant1Symbol != None:
            g.add(quadrant1Symbol)
        if quadrant2Symbol != None:
            g.add(quadrant2Symbol)
        if quadrant3Symbol != None:
            g.add(quadrant3Symbol)

        quadrant4Symbol = None
        if self.SecondaryClass != None:
            ##NEW
            ##SECONDARY CLASS LOGO ON DANGER DIAMOND

            #default logo is Esoteric
            quadrant4Symbol = Esoteric()
            SECONDARYCLASS = self.SecondaryClass.upper()

            if SECONDARYCLASS == "ARCHON":
                quadrant4Symbol = Archon()
            elif SECONDARYCLASS == "APOLLYON":
                quadrant4Symbol = Apollyon()
            elif SECONDARYCLASS in ["CERNUNNOS", "CERNNUNOS"]:
                quadrant4Symbol = Cernnunos()
            elif SECONDARYCLASS == "THAUMIEL":
                quadrant4Symbol = Thaumiel()
            elif SECONDARYCLASS == "NEUTRALIZED":
                quadrant4Symbol = Neutralized()
            elif SECONDARYCLASS == "PENDING":
                quadrant4Symbol = Pending()
            elif SECONDARYCLASS == "HIEMAL":
                quadrant4Symbol = Hiemal()
            elif SECONDARYCLASS == "TIAMAT":
                quadrant4Symbol = Tiamat()
            elif SECONDARYCLASS == "TICONDEROGA":
                quadrant4Symbol = Ticonderoga()
            elif SECONDARYCLASS in ["N/A", "NULL"]:
                quadrant4Symbol = Null()
            elif SECONDARYCLASS == "GEVURAH":
                quadrant4Symbol = Gevurah()
            elif SECONDARYCLASS == "ENOCHIAN":
                quadrant4Symbol = Enochian()
            elif SECONDARYCLASS == "KETER":
                quadrant4Symbol = Keter()
            elif SECONDARYCLASS in ["Gödel", u"Gödel", "Godel",
                                         u"G\xf6del", "G\xf6del",
                                         u"GöDEL", "GODEL", u"G\xf6del".upper(),
                                         "G\xf6del".upper()]:
                quadrant4Symbol = Godel()
            elif SECONDARYCLASS == "HERA":
                quadrant4Symbol = Hera()
            elif SECONDARYCLASS == "ANOMALOUS":
                quadrant4Symbol = Anomalous()
            elif SECONDARYCLASS == "TRUCULENT":
                quadrant4Symbol = Truculent()
            elif SECONDARYCLASS == "NUMEN":
                quadrant4Symbol = Numen()
            elif SECONDARYCLASS == "DAASELYON":
                quadrant4Symbol = Daaselyon()
            elif SECONDARYCLASS == "TERMINAL":
                quadrant4Symbol = Terminal()

            elif SECONDARYCLASS in ["ZENO", "KRONECKER", "EPARCH", "DAMBALLAH"]:
                quadrant4Symbol = Esoteric()

            #quadrant4Symbol.x = ((self.x+(s/2.0)))-(athird)-13
            quadrant4Symbol.x = quadrant2Symbol.x
            #quadrant4Symbol.y = quadrant2Symbol.y - (s/2.0)
            quadrant4Symbol.y = self.y + (athird/2.0)

            #quadrant4Symbol.size = 40
            quadrant4Symbol.size = SYMBOLSIZE
            g.add(quadrant4Symbol)

        fiddle = s/50.0

        if quadrant1Symbol != None:
            quadrant1Symbol.x = quadrant1Symbol.x - (fiddle*1.5)
            quadrant1Symbol.y = quadrant1Symbol.y - fiddle

        if quadrant2Symbol != None:
            quadrant2Symbol.x = quadrant2Symbol.x - (fiddle*1.5)
            quadrant2Symbol.y = quadrant2Symbol.y - (fiddle*1.5)

        if quadrant3Symbol != None:
            quadrant3Symbol.x = quadrant3Symbol.x - (fiddle*1.75)
            quadrant3Symbol.y = quadrant3Symbol.y - fiddle

        if quadrant4Symbol != None:
            quadrant4Symbol.x = quadrant4Symbol.x - (fiddle*1.5)
            #quadrant4Symbol.y = quadrant4Symbol.y - (fiddle*5.5)
            quadrant4Symbol.y = quadrant4Symbol.y - (fiddle*6.25)

        return g

class Null(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=None, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        #empty circle - no central design
        return g


class Safe(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=green_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        lockbody = SafeLock()
        lockbody.size = (s/100)*100
        lockbody.x = (self.x+(s/2.0))-(lockbody.size/2.0)
        lockbody.y = self.y
        g.add(lockbody)

        return g

class Euclid(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=yellow_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        lockbody = EuclidLock()
        lockbody.size = (s/100)*100
        lockbody.x = (self.x+(s/2.0))-(lockbody.size/2.0)
        lockbody.y = self.y
        g.add(lockbody)
        
        return g

class Keter(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=red_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        lockbody = KeterLock()
        lockbody.size = (s/100)*100
        lockbody.x = (self.x+(s/2.0))-(lockbody.size/2.0)
        lockbody.y = self.y
        g.add(lockbody)

        return g


#from: http://scp-wiki.wdfiles.com/local--files/component%3Aobject-warning-box-source/scp-logo.svg

class SCPLogo(_Symbol):

    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc='symbol x coordinate'),
        y = AttrMapValue(isNumber,desc='symbol y coordinate'),
        size = AttrMapValue(isNumber),
        fillColor = AttrMapValue(isColorOrNone),
        )

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        #self.fillColor = colors.black
        self.fillColor=Color(0,0,0,1)

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1.25,0,0,-1.25,0,-3000)
        g.transform = (.1,0,0,-0.1,0,-2400)
        #g.add(Path(points=[8816,22953,8813,22937,8743,22536,8660,22060,8578,21584,8507,21189,8503,21182,8498,21175,8430,21143,8350,21111,6801,20486,5406,19446,4364,18140,3284,16786,2577,15172,2325,13490,2311,13394,2294,13304,2289,13291,2269,13242,2229,12858,2210,12526,2197,12296,2197,11718,2210,11475,2222,11257,2241,11053,2272,10792,2294,10608,2254,10571,2171,10493,2060,10391,1950,10290,1887,10232,1804,10156,1765,10120,1681,10041,1666,10028,1243,9636,1060,9468,909,9326,906,9321,903,9317,1028,9093,1183,8824,1338,8555,2064,7299,2795,6033,3526,4766,4129,3730,4135,3730,4141,3730,4220,3757,4311,3791,4401,3824,4597,3896,4745,3950,5625,4272,5841,4350,5849,4350,5855,4350,5885,4328,5918,4301,6101,4148,6550,3832,6845,3648,7345,3336,7996,3018,8605,2790,10059,2245,11668,2053,13210,2240,14033,2340,14864,2548,15605,2840,15704,2879,15794,2912,15805,2914,15859,2923,16179,3069,16495,3228,17008,3488,17457,3766,17928,4117,18121,4260,18173,4244,18202,4235,18239,4224,18255,4218,18302,4203,18758,4061,18825,4041,18941,4006,19475,3839,19500,3830,19514,3825,19572,3807,19630,3790,19688,3772,19777,3745,19828,3728,19879,3712,19925,3700,19930,3702,19942,3706,23162,9281,23158,9290,23155,9297,22963,9459,22160,10128,21959,10296,21787,10441,21776,10450,21758,10468,21758,10471,21778,10617,21889,11399,21902,12173,21819,12990,21627,14879,20903,16651,19714,18142,18952,19098,17989,19922,16920,20533,16585,20724,16119,20953,15783,21090,15737,21108,15698,21131,15696,21139,15693,21148,15600,21558,15490,22050,15379,22542,15286,22953,15284,22963,15279,22979,15116,22980,12050,22980,8822,22980,8816,22953,14744,22443,14752,22416,14979,21444,15060,21090,15099,20917,15135,20762,15139,20745,15146,20717,15157,20711,15336,20642,15730,20490,16200,20272,16525,20090,17585,19498,18498,18728,19245,17800,20409,16353,21108,14598,21259,12745,21292,12344,21298,11633,21270,11300,21244,10980,21195,10605,21138,10287,21126,10220,21170,10177,21195,10154,21256,10101,21305,10060,21355,10019,21400,9980,21407,9974,21413,9968,21464,9925,21521,9879,21577,9833,21666,9759,21719,9715,21772,9670,21943,9527,22100,9396,22482,9076,22455,9101,22443,9081,22438,9072,21831,8022,21096,6748,20292,5355,19752,4430,19744,4430,19736,4430,19656,4452,19567,4479,19478,4506,19389,4533,19370,4538,19328,4549,18921,4672,18835,4699,18802,4710,18735,4730,18685,4745,18636,4760,18586,4776,18575,4780,18564,4785,18535,4794,18510,4800,18485,4806,18456,4815,18445,4820,18434,4825,18394,4838,18355,4848,18317,4859,18230,4885,18163,4905,18042,4942,18041,4942,18016,4924,18003,4913,17927,4853,17848,4789,17606,4593,17159,4270,17131,4270,17126,4270,17081,4244,17033,4213,16566,3912,15984,3614,15451,3403,14549,3046,13654,2844,12635,2768,12412,2752,11668,2752,11445,2768,10142,2865,8996,3178,7880,3741,7302,4032,6698,4420,6245,4790,6207,4822,6170,4849,6163,4851,6157,4853,6108,4893,6055,4939,5958,5022,5911,5012,5866,5002,5801,4980,5480,4860,5389,4826,5169,4745,4990,4680,4811,4615,4591,4534,4500,4501,4410,4467,4331,4440,4325,4440,4319,4440,3708,5491,2966,6776,1617,9112,1651,9142,1670,9159,1759,9243,1850,9329,1941,9414,2044,9512,2080,9545,2116,9579,2188,9647,2240,9697,2292,9747,2359,9809,2389,9836,2419,9863,2460,9901,2481,9920,2549,9984,2742,10165,2769,10189,2783,10202,2825,10241,2861,10276,2928,10340,2914,10412,2864,10672,2809,11146,2805,11340,2804,11420,2799,11636,2795,11820,2783,12353,2815,12859,2895,13385,3285,15956,4736,18242,6895,19685,7526,20108,8234,20465,8915,20705,9030,20746,9035,20749,9043,20781,9053,20821,9118,21186,9241,21895,9291,22181,9334,22425,9337,22438,9342,22460,12040,22460,14602,22460,14739,22459,14744,22443],operators=[0,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,0,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,fillColor=self.fillColor, strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[8816,22953,8813,22937,8743,22536,8660,22060,8578,21584,8507,21189,8503,21182,8498,21175,8430,21143,8350,21111,6801,20486,5406,19446,4364,18140,3284,16786,2577,15172,2325,13490,2311,13394,2294,13304,2289,13291,2269,13242,2229,12858,2210,12526,2197,12296,2197,11718,2210,11475,2222,11257,2241,11053,2272,10792,2294,10608,2254,10571,2171,10493,2060,10391,1950,10290,1887,10232,1804,10156,1765,10120,1681,10041,1666,10028,1243,9636,1060,9468,909,9326,906,9321,903,9317,1028,9093,1183,8824,1338,8555,2064,7299,2795,6033,3526,4766,4129,3730,4135,3730,4141,3730,4220,3757,4311,3791,4401,3824,4597,3896,4745,3950,5625,4272,5841,4350,5849,4350,5855,4350,5885,4328,5918,4301,6101,4148,6550,3832,6845,3648,7345,3336,7996,3018,8605,2790,10059,2245,11668,2053,13210,2240,14033,2340,14864,2548,15605,2840,15704,2879,15794,2912,15805,2914,15859,2923,16179,3069,16495,3228,17008,3488,17457,3766,17928,4117,18121,4260,18173,4244,18202,4235,18239,4224,18255,4218,18302,4203,18758,4061,18825,4041,18941,4006,19475,3839,19500,3830,19514,3825,19572,3807,19630,3790,19688,3772,19777,3745,19828,3728,19879,3712,19925,3700,19930,3702,19942,3706,23162,9281,23158,9290,23155,9297,22963,9459,22160,10128,21959,10296,21787,10441,21776,10450,21758,10468,21758,10471,21778,10617,21889,11399,21902,12173,21819,12990,21627,14879,20903,16651,19714,18142,18952,19098,17989,19922,16920,20533,16585,20724,16119,20953,15783,21090,15737,21108,15698,21131,15696,21139,15693,21148,15600,21558,15490,22050,15379,22542,15286,22953,15284,22963,15279,22979,15116,22980,12050,22980,8822,22980,8816,22953,14744,22443,14752,22416,14979,21444,15060,21090,15099,20917,15135,20762,15139,20745,15146,20717,15157,20711,15336,20642,15730,20490,16200,20272,16525,20090,17585,19498,18498,18728,19245,17800,20409,16353,21108,14598,21259,12745,21292,12344,21298,11633,21270,11300,21244,10980,21195,10605,21138,10287,21126,10220,21170,10177,21195,10154,21256,10101,21305,10060,21355,10019,21400,9980,21407,9974,21413,9968,21464,9925,21521,9879,21577,9833,21666,9759,21719,9715,21772,9670,21943,9527,22100,9396,22482,9076,22455,9101,22443,9081,22438,9072,21831,8022,21096,6748,20292,5355,19752,4430,19744,4430,19736,4430,19656,4452,19567,4479,19478,4506,19389,4533,19370,4538,19328,4549,18921,4672,18835,4699,18802,4710,18735,4730,18685,4745,18636,4760,18586,4776,18575,4780,18564,4785,18535,4794,18510,4800,18485,4806,18456,4815,18445,4820,18434,4825,18394,4838,18355,4848,18317,4859,18230,4885,18163,4905,18042,4942,18041,4942,18016,4924,18003,4913,17927,4853,17848,4789,17606,4593,17159,4270,17131,4270,17126,4270,17081,4244,17033,4213,16566,3912,15984,3614,15451,3403,14549,3046,13654,2844,12635,2768,12412,2752,11668,2752,11445,2768,10142,2865,8996,3178,7880,3741,7302,4032,6698,4420,6245,4790,6207,4822,6170,4849,6163,4851,6157,4853,6108,4893,6055,4939,5958,5022,5911,5012,5866,5002,5801,4980,5480,4860,5389,4826,5169,4745,4990,4680,4811,4615,4591,4534,4500,4501,4410,4467,4331,4440,4325,4440,4319,4440,3708,5491,2966,6776,1617,9112,1651,9142,1670,9159,1759,9243,1850,9329,1941,9414,2044,9512,2080,9545,2116,9579,2188,9647,2240,9697,2292,9747,2359,9809,2389,9836,2419,9863,2460,9901,2481,9920,2549,9984,2742,10165,2769,10189,2783,10202,2825,10241,2861,10276,2928,10340,2914,10412,2864,10672,2809,11146,2805,11340,2804,11420,2799,11636,2795,11820,2783,12353,2815,12859,2895,13385,3285,15956,4736,18242,6895,19685,7526,20108,8234,20465,8915,20705,9030,20746,9035,20749,9043,20781,9053,20821,9118,21186,9241,21895,9291,22181,9334,22425,9337,22438,9342,22460,12040,22460,14602,22460,14739,22459,14744,22443],operators=[0,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,0,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,fillColor=self.fillColor, strokeColor=None,strokeLineCap=0))
        #g.add(Path(points=[11640,19006,11640,18491,11598,18486,11574,18484,11461,18472,11346,18460,10332,18359,9303,17986,8429,17404,7730,16939,7101,16310,6636,15611,6322,15140,6045,14573,5871,14044,5387,12578,5436,11004,6010,9574,6050,9475,6120,9317,6166,9221,6212,9125,6250,9044,6250,9040,6250,9036,6030,8906,5760,8750,5491,8595,5264,8463,5255,8456,5242,8447,5267,8398,5437,8103,5546,7914,5638,7760,5641,7760,5645,7760,5874,7890,6150,8050,6426,8210,6655,8340,6660,8340,6664,8340,6709,8282,6759,8211,7199,7593,7789,7022,8429,6596,8900,6282,9467,6005,9996,5831,11331,5390,12749,5390,14084,5831,14613,6005,15180,6282,15651,6596,16299,7027,16877,7588,17334,8230,17393,8313,17443,8380,17446,8380,17448,8380,17672,8252,17943,8096,18213,7939,18442,7808,18451,7805,18463,7800,18510,7874,18664,8141,18842,8448,18860,8485,18845,8496,18836,8503,18608,8635,18339,8790,18070,8946,17850,9076,17850,9080,17850,9084,17883,9156,17924,9241,18478,10397,18669,11789,18449,13080,18296,13981,17951,14851,17444,15611,17043,16214,16527,16758,15940,17199,15614,17443,15322,17623,14940,17814,14233,18167,13489,18385,12734,18460,12619,18472,12506,18484,12483,18486,12440,18491,12440,19006,12440,19520,12040,19520,11640,19520,11640,19006,11640,16130,11640,14970,11184,14970,10919,14970,10730,14966,10732,14961,10742,14932,12056,12390,12060,12390,12064,12390,13377,14932,13388,14961,13390,14966,13191,14970,12916,14970,12440,14970,12440,16130,12440,17290,12485,17290,12626,17290,13047,17220,13331,17149,13713,17054,14015,16942,14385,16760,14789,16561,15114,16350,15465,16059,15618,15933,16011,15533,16143,15371,16338,15130,16519,14866,16668,14604,16748,14463,16912,14121,16974,13963,17434,12801,17472,11510,17080,10332,16991,10064,16831,9680,16808,9680,16796,9680,14960,10738,14941,10756,14929,10766,14962,10830,15148,11152,15270,11363,15370,11539,15370,11545,15370,11555,15377,11555,15140,11565,15044,11569,14958,11573,14950,11575,14942,11576,14852,11581,14750,11584,14648,11588,14543,11593,14515,11595,14488,11597,14398,11602,14315,11605,14233,11608,14145,11613,14120,11615,14095,11617,13996,11622,13900,11626,13804,11629,13710,11633,13692,11635,13674,11636,13582,11641,13487,11645,13393,11649,13299,11653,13280,11655,13261,11657,13160,11661,13055,11665,12951,11669,12858,11673,12850,11675,12812,11682,12480,11692,12480,11686,12480,11682,12764,11237,13112,10697,13459,10157,13811,9610,13894,9482,14029,9272,14045,9250,14057,9266,14064,9276,14172,9461,14297,9677,14524,10070,14554,10052,14571,10042,14993,9798,15493,9510,15992,9222,16400,8982,16400,8977,16400,8962,16252,8763,16131,8615,16008,8464,15610,8061,15465,7941,15245,7758,15002,7586,14760,7440,14591,7337,14190,7140,14003,7066,12737,6566,11343,6566,10077,7066,9890,7140,9489,7337,9320,7440,9078,7586,8833,7759,8615,7941,8473,8059,8092,8442,7970,8590,7856,8727,7696,8939,7701,8945,7703,8947,8112,9183,8610,9470,9108,9757,9529,10001,9547,10011,9578,10030,9796,9653,9916,9445,10019,9267,10026,9257,10036,9241,10045,9251,10099,9337,10133,9391,10222,9530,10297,9645,10371,9761,10483,9934,10545,10030,10651,10196,10995,10731,11085,10870,11108,10906,11209,11063,11310,11220,11411,11377,11517,11542,11546,11587,11576,11633,11600,11675,11600,11681,11600,11688,11576,11690,11523,11686,11480,11683,11384,11678,11310,11675,11236,11672,11141,11668,11100,11665,11019,11660,10879,11653,10680,11645,10611,11642,10521,11638,10480,11635,10439,11632,10349,11628,10280,11625,10153,11620,10038,11614,9863,11605,9809,11602,9666,11595,9545,11590,9424,11585,9281,11578,9228,11575,9174,11572,9086,11568,9033,11565,8790,11553,8710,11547,8710,11541,8710,11538,8815,11352,8944,11130,9178,10725,9151,10709,9064,10654,7300,9640,7292,9640,7280,9640,7187,9838,7115,10016,6824,10734,6691,11555,6740,12325,6797,13213,7068,14057,7538,14815,7641,14981,7798,15199,7937,15371,8069,15533,8462,15933,8615,16059,8966,16350,9291,16561,9695,16760,10065,16942,10367,17054,10749,17149,11037,17221,11428,17287,11583,17289,11640,17290,11640,16130],operators=[0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,3,0,1,1,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,fillColor=self.fillColor,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[11640,19006,11640,18491,11598,18486,11574,18484,11461,18472,11346,18460,10332,18359,9303,17986,8429,17404,7730,16939,7101,16310,6636,15611,6322,15140,6045,14573,5871,14044,5387,12578,5436,11004,6010,9574,6050,9475,6120,9317,6166,9221,6212,9125,6250,9044,6250,9040,6250,9036,6030,8906,5760,8750,5491,8595,5264,8463,5255,8456,5242,8447,5267,8398,5437,8103,5546,7914,5638,7760,5641,7760,5645,7760,5874,7890,6150,8050,6426,8210,6655,8340,6660,8340,6664,8340,6709,8282,6759,8211,7199,7593,7789,7022,8429,6596,8900,6282,9467,6005,9996,5831,11331,5390,12749,5390,14084,5831,14613,6005,15180,6282,15651,6596,16299,7027,16877,7588,17334,8230,17393,8313,17443,8380,17446,8380,17448,8380,17672,8252,17943,8096,18213,7939,18442,7808,18451,7805,18463,7800,18510,7874,18664,8141,18842,8448,18860,8485,18845,8496,18836,8503,18608,8635,18339,8790,18070,8946,17850,9076,17850,9080,17850,9084,17883,9156,17924,9241,18478,10397,18669,11789,18449,13080,18296,13981,17951,14851,17444,15611,17043,16214,16527,16758,15940,17199,15614,17443,15322,17623,14940,17814,14233,18167,13489,18385,12734,18460,12619,18472,12506,18484,12483,18486,12440,18491,12440,19006,12440,19520,12040,19520,11640,19520,11640,19006,11640,16130,11640,14970,11184,14970,10919,14970,10730,14966,10732,14961,10742,14932,12056,12390,12060,12390,12064,12390,13377,14932,13388,14961,13390,14966,13191,14970,12916,14970,12440,14970,12440,16130,12440,17290,12485,17290,12626,17290,13047,17220,13331,17149,13713,17054,14015,16942,14385,16760,14789,16561,15114,16350,15465,16059,15618,15933,16011,15533,16143,15371,16338,15130,16519,14866,16668,14604,16748,14463,16912,14121,16974,13963,17434,12801,17472,11510,17080,10332,16991,10064,16831,9680,16808,9680,16796,9680,14960,10738,14941,10756,14929,10766,14962,10830,15148,11152,15270,11363,15370,11539,15370,11545,15370,11555,15377,11555,15140,11565,15044,11569,14958,11573,14950,11575,14942,11576,14852,11581,14750,11584,14648,11588,14543,11593,14515,11595,14488,11597,14398,11602,14315,11605,14233,11608,14145,11613,14120,11615,14095,11617,13996,11622,13900,11626,13804,11629,13710,11633,13692,11635,13674,11636,13582,11641,13487,11645,13393,11649,13299,11653,13280,11655,13261,11657,13160,11661,13055,11665,12951,11669,12858,11673,12850,11675,12812,11682,12480,11692,12480,11686,12480,11682,12764,11237,13112,10697,13459,10157,13811,9610,13894,9482,14029,9272,14045,9250,14057,9266,14064,9276,14172,9461,14297,9677,14524,10070,14554,10052,14571,10042,14993,9798,15493,9510,15992,9222,16400,8982,16400,8977,16400,8962,16252,8763,16131,8615,16008,8464,15610,8061,15465,7941,15245,7758,15002,7586,14760,7440,14591,7337,14190,7140,14003,7066,12737,6566,11343,6566,10077,7066,9890,7140,9489,7337,9320,7440,9078,7586,8833,7759,8615,7941,8473,8059,8092,8442,7970,8590,7856,8727,7696,8939,7701,8945,7703,8947,8112,9183,8610,9470,9108,9757,9529,10001,9547,10011,9578,10030,9796,9653,9916,9445,10019,9267,10026,9257,10036,9241,10045,9251,10099,9337,10133,9391,10222,9530,10297,9645,10371,9761,10483,9934,10545,10030,10651,10196,10995,10731,11085,10870,11108,10906,11209,11063,11310,11220,11411,11377,11517,11542,11546,11587,11576,11633,11600,11675,11600,11681,11600,11688,11576,11690,11523,11686,11480,11683,11384,11678,11310,11675,11236,11672,11141,11668,11100,11665,11019,11660,10879,11653,10680,11645,10611,11642,10521,11638,10480,11635,10439,11632,10349,11628,10280,11625,10153,11620,10038,11614,9863,11605,9809,11602,9666,11595,9545,11590,9424,11585,9281,11578,9228,11575,9174,11572,9086,11568,9033,11565,8790,11553,8710,11547,8710,11541,8710,11538,8815,11352,8944,11130,9178,10725,9151,10709,9064,10654,7300,9640,7292,9640,7280,9640,7187,9838,7115,10016,6824,10734,6691,11555,6740,12325,6797,13213,7068,14057,7538,14815,7641,14981,7798,15199,7937,15371,8069,15533,8462,15933,8615,16059,8966,16350,9291,16561,9695,16760,10065,16942,10367,17054,10749,17149,11037,17221,11428,17287,11583,17289,11640,17290,11640,16130],operators=[0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,3,0,1,1,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,fillColor=self.fillColor,strokeColor=None,strokeLineCap=0))

        g.transform = (1,0,0,-1, self.x, self.y+s)
        #g.scale(float(float(s)/float(3000)), float(float(s)/float(3000)))
        g.scale(float(float(s)/float(20000)), float(float(s)/float(20000)))

        return g


class DARKSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[175.6,89.7,168.4,83.4,140.1,59.9,97.2,59.5,59,59.2,32.5,77.4,24.2,83.6,21.2,85.8,21.2,89.3,21.2,89.7,21.2,93.4,23.9,95.5,24.2,95.8,30.4,100.4,39.5,106.3,51.3,111.4,60.5,115.4,76,121.9,97.2,122.3,128.2,122.8,150.2,109.7,155.1,106.6,164.3,100.8,171.1,94.5,175.6,89.7],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[39,114,33.1,111.1,31.4,110.3,29.4,110.9,28.6,112.6,21.9,126,21.1,127.7,21.7,129.7,23.4,130.5,29.3,133.4,31,134.2,33,133.6,33.8,131.9,40.5,118.5,41.3,116.8,40.7,114.8,39,114],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[69.8,126.4,63.4,124.8,61.6,124.4,59.8,125.4,59.3,127.2,55.7,141.8,55.3,143.6,56.3,145.4,58.1,145.9,64.5,147.5,66.3,147.9,68.1,146.9,68.6,145.1,72.2,130.5,72.7,128.7,71.6,126.9,69.8,126.4],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[103.4,129.5,96.8,129.5,95,129.5,93.5,131,93.5,132.8,93.5,147.8,93.5,149.6,95,151.1,96.8,151.1,103.4,151.1,105.2,151.1,106.7,149.6,106.7,147.8,106.7,132.8,106.8,131,105.3,129.5,103.4,129.5],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[142.3,127.3,141.9,125.5,140,124.4,138.2,124.9,131.8,126.5,130,126.9,128.9,128.8,129.4,130.6,133,145.2,133.4,147,135.3,148.1,137.1,147.6,143.5,146,145.3,145.6,146.4,143.7,145.9,141.9,142.3,127.3],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[180,122.8,170.6,111,169.4,109.6,167.3,109.3,165.9,110.5,160.7,114.6,159.3,115.8,159,117.9,160.2,119.3,169.6,131.1,170.8,132.5,172.9,132.8,174.3,131.6,179.5,127.5,180.9,126.4,181.1,124.3,180,122.8],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g

class VLAMSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[91,110.1,91,110.1,88,106.9,87.6,102.1,87,95.6,93.6,88,104.3,83.9,103.7,86.2,103.2,89.6,104.7,93,106,96.1,107.9,96.4,109.3,99.8,109.8,101,111.4,105.1,109.3,108.9,107.3,112.5,103.2,113.3,102.5,113.5,102.5,121.7,112.2,121.8,126.6,120.9,142.4,113.5,151,109.4,157.5,104.7,161.8,101,157.7,97.4,151.7,92.7,143.6,88.5,139.5,86.4,120.9,77.1,95.8,78.2,65.6,79.6,44.8,95.1,37.7,101,47.6,107.8,68.5,120.1,96.9,121.5,96.9,113.5,95.4,113.1,93,112.2,91,110.1],operators=[0,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[143.4,80.4,119.5,69,97.8,70.5,88.7,71.3,58.3,73.9,36.9,88.2,27.8,95.2,27.5,95.4,24.9,97.4,24.9,100.9,24.9,104.4,27.5,106.4,27.8,106.6,40.4,116.6,52.2,121.9,60.2,124.8,68,127.6,111.5,142.3,150.2,119.1,160.4,113,167.5,105.9,171.8,100.9,166.2,95.1,156.8,86.9,143.4,80.4,142.2,113.5,126.5,120.9,112,121.8,102.3,121.7,102.3,113.5,103.1,113.4,107.1,112.5,109.1,108.9,111.2,105.1,109.6,101,109.1,99.8,107.7,96.4,105.9,96.1,104.5,93,103.1,89.6,103.5,86.1,104.1,83.9,93.6,88,87,95.6,87.6,102.1,88,106.9,91,110.1,91,110.1,93.1,112.3,95.5,113.2,96.7,113.5,96.7,121.5,68.3,120.1,47.4,107.8,37.5,101,44.6,95.1,65.3,79.6,95.6,78.2,120.8,77.1,139.4,86.3,143.4,88.5,151.5,92.7,157.5,97.4,161.6,101,157.3,104.6,150.8,109.4,142.2,113.5],operators=[0,2,2,2,2,2,2,2,2,3,0,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class KENEQSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[96.7,82.4,63.6,83.8,42.7,103.7,38,108.5,43,112.8,54.3,121.5,70.7,127,68.8,124,67,119.8,67.4,114.6,68.4,102.4,81.1,96.2,82.2,95.7,79.4,98.3,78.9,101.9,80.9,104.6,83,107.5,87.1,107.9,87.6,107.9,87.7,105.4,88.2,101.8,90.3,97.9,94.5,90,102.1,86,105.1,84.6,104.2,86.1,102.7,88.8,102.4,92.4,102.1,95.9,103.1,98.6,103.7,100.2,104.1,99.4,104.9,98.1,106.4,96.9,107.1,96.3,108.5,95.3,110.4,94.7,109.9,96,109.3,97.9,109.1,100.3,108.9,102.1,108.7,103.3,109.1,104.7,109.4,105.7,110.2,108,113.1,110.3,113.9,110.1,117.7,109.1,119.8,105.9,122.6,101.7,120,97.4,119.8,97,121.8,98.8,126.5,103.3,127.9,110.3,129.6,119.4,124.5,126.5,122.2,129.2,144.4,123.8,159.2,111.8,163.1,108.6,159.1,104.6,134.6,80.8,96.7,82.4],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[94.6,72.7,78.1,72.9,64.6,78.2,63.4,78.7,45.8,85.6,35,97,29.9,103.1,29.6,103.3,27.2,105.2,27.2,108.6,27.2,111.9,29.7,113.9,29.9,114.1,36.4,120.2,48.9,130.4,67.6,136.1,68.7,136.4,80.6,140,94.6,140.1,132.5,140.5,164.1,115.9,172.9,108.6,166.1,101.9,134.8,72.1,94.6,72.7,127.9,110.2,126.6,103.2,121.9,98.6,119.8,96.9,120,97.3,122.6,101.5,119.8,105.8,117.7,109,113.9,110,113.1,110.2,110.1,107.9,109.3,105.7,109.1,104.6,108.7,103.2,108.9,101.9,109.1,100.2,109.4,97.8,110,95.9,110.4,94.6,108.4,95.3,107.1,96.2,106.4,96.8,104.9,98,104.1,99.3,103.7,100.1,103,98.6,102.1,95.8,102.4,92.3,102.7,88.7,104.1,86,105.1,84.5,102.1,86,94.4,90,90.3,98,88.2,101.9,87.7,105.5,87.6,108,87.1,108,83,107.6,80.9,104.7,78.9,102,79.4,98.4,82.2,95.8,81.1,96.3,68.5,102.5,67.4,114.7,67,119.9,68.8,124.1,70.7,127.1,54.3,121.6,43.1,112.9,38,108.6,42.7,103.8,63.6,83.9,96.7,82.5,134.5,80.9,159,104.6,163,108.6,159.2,111.8,144.3,123.8,122.1,129.2,124.5,126.4,129.6,119.3,127.9,110.2],operators=[0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[155.9,81.4,160.6,83.8,162.3,84.6,164.3,84,165.1,82.3,170.9,70.8,171.7,69.1,171.1,67.1,169.4,66.3,164.7,63.9,163,63.1,161,63.7,160.2,65.4,154.4,76.9,153.6,78.5,154.2,80.5,155.9,81.4],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[127.1,66.8,132.2,68.1,134,68.5,135.8,67.5,136.3,65.7,139.4,53.2,139.8,51.4,138.8,49.6,137,49.1,131.9,47.8,130.1,47.4,128.3,48.4,127.8,50.2,124.7,62.7,124.2,64.6,125.3,66.4,127.1,66.8],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[96.8,62.9,102.1,62.9,103.9,62.9,105.4,61.4,105.4,59.6,105.4,46.7,105.4,44.9,103.9,43.4,102.1,43.4,96.8,43.4,95,43.4,93.5,44.9,93.5,46.7,93.5,59.6,93.5,61.4,95,62.9,96.8,62.9],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[62.2,66.1,62.8,67.8,64.7,68.7,66.5,68.1,71.5,66.3,73.2,65.7,74.1,63.8,73.5,62,69.1,49.9,68.5,48.2,66.6,47.3,64.8,47.9,59.8,49.7,58.1,50.3,57.2,52.2,57.8,54,62.2,66.1],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[35.7,81.4,36.9,82.8,39,83.1,40.4,81.9,44.5,78.6,45.9,77.4,46.2,75.3,45,73.9,37,63.8,35.8,62.4,33.7,62.1,32.3,63.3,28.2,66.6,26.8,67.8,26.5,69.9,27.7,71.3,35.7,81.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class EKHISymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[61.9,73.1,56.7,76.6,44.6,84.9,44.3,97.3,44.1,104.7,48.3,110.3,50.9,113.8,67.2,135.2,98.9,134.8,102.5,134.7,109.7,134.5,130.3,133.9,145.4,118.2,151.4,111.9,154.7,105.2,156.4,100.6,155.2,95.6,152.6,88,146.5,80.8,131.8,63.5,108.6,63.3,99.3,63.2,91.7,63.1,76.3,63.2,61.9,73.1,101.4,77.7,107.8,74.6,115.2,73.8,122.1,75.4,119.2,78.3,117,81.8,115.5,85.6,122.2,87.9,128,92.6,131.8,98.6,127.7,98.6,123.7,99.5,119.9,101.1,123,107.5,123.8,114.9,122.2,121.8,119.3,118.9,115.8,116.7,112,115.2,109.7,121.9,105,127.7,99,131.5,99,127.4,98.1,123.4,96.5,119.6,90.1,122.7,82.7,123.5,75.8,121.9,78.7,119,80.9,115.5,82.4,111.7,75.7,109.4,69.9,104.7,66.1,98.7,70.2,98.7,74.2,97.8,78,96.2,74.9,89.8,74.1,82.4,75.7,75.5,78.6,78.4,82.1,80.6,85.9,82.1,88.2,75.4,92.9,69.6,98.9,65.8,98.8,69.9,99.7,73.8,101.4,77.7],operators=[0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[42.8,131.3,38,128.9,36.3,128.1,34.3,128.7,33.5,130.4,27.6,142.1,26.8,143.8,27.4,145.8,29.1,146.6,33.9,149,35.6,149.8,37.6,149.2,38.4,147.5,44.3,135.8,45.1,134.2,44.4,132.2,42.8,131.3],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[70.8,142.7,65.6,141.4,63.8,141,62,142,61.5,143.8,58.3,156.5,57.9,158.3,58.9,160.1,60.7,160.6,65.9,161.9,67.7,162.3,69.5,161.3,70,159.5,73.2,146.8,73.7,145,72.6,143.2,70.8,142.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[101.4,145.6,96,145.6,94.2,145.6,92.7,147.1,92.7,148.9,92.7,162,92.7,163.8,94.2,165.3,96,165.3,101.4,165.3,103.2,165.3,104.7,163.8,104.7,162,104.7,149,104.7,147.1,103.2,145.6,101.4,145.6],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[137.2,143.9,136.8,142.1,134.9,141,133.1,141.5,127.9,142.8,126.1,143.2,125,145.1,125.5,146.9,128.7,159.6,129.1,161.4,131,162.5,132.8,162,138,160.7,139.8,160.3,140.9,158.4,140.4,156.6,137.2,143.9],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[171.2,139.3,163.1,129.1,161.9,127.7,159.8,127.4,158.4,128.6,154.2,132,152.8,133.2,152.5,135.3,153.7,136.7,161.8,146.9,163,148.3,165.1,148.6,166.5,147.4,170.7,144,172.1,142.9,172.4,140.8,171.2,139.3],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[33.3,98.4,33.3,120.4,67,138.8,94.8,140.2,126.3,141.7,163.7,122.1,164,99.5,164.4,77.3,128.8,56.6,98.1,56.6,68.6,56.7,33.3,75.9,33.3,98.4,146.5,80.8,152.6,87.9,155.2,95.6,156.4,100.6,154.7,105.2,151.5,111.9,145.4,118.2,130.3,133.9,109.8,134.5,102.5,134.7,98.8,134.8,67.2,135.3,50.9,113.8,48.3,110.3,44.1,104.8,44.3,97.3,44.6,84.9,56.7,76.7,61.9,73.1,76.4,63.2,91.7,63.1,99.3,63.2,108.6,63.3,131.8,63.5,146.5,80.8],operators=[0,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[155.7,68.7,160.5,71.1,162.2,71.9,164.2,71.3,165,69.6,170.9,57.9,171.7,56.2,171.1,54.2,169.4,53.4,164.6,51,162.9,50.2,160.9,50.8,160.1,52.5,154.2,64.2,153.4,65.8,154.1,67.9,155.7,68.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[126.6,54,131.8,55.3,133.6,55.7,135.4,54.7,135.9,52.9,139.1,40.2,139.5,38.4,138.5,36.6,136.7,36.1,131.5,34.8,129.7,34.4,127.9,35.4,127.4,37.2,124.2,49.9,123.7,51.7,124.8,53.6,126.6,54],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[96,50,101.4,50,103.2,50,104.7,48.5,104.7,46.7,104.7,33.6,104.7,31.8,103.2,30.3,101.4,30.3,96,30.3,94.2,30.3,92.7,31.8,92.7,33.6,92.7,46.7,92.7,48.5,94.2,50,96,50],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[61.1,53.3,61.7,55,63.6,55.9,65.4,55.3,70.5,53.5,72.2,52.9,73.1,51,72.5,49.2,68,36.9,67.4,35.2,65.5,34.3,63.7,34.9,58.6,36.7,56.9,37.3,56,39.2,56.6,41,61.1,53.3],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[39,69.3,43.2,65.9,44.6,64.7,44.9,62.6,43.7,61.2,35.6,51,34.4,49.6,32.3,49.3,30.9,50.5,26.7,53.9,25.3,55.1,25,57.2,26.2,58.6,34.3,68.8,35.5,70.2,37.6,70.5,39,69.3],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[85.8,82,81.9,80.5,78.5,78.3,75.6,75.4,74,82.3,74.8,89.7,77.9,96.1,74.1,97.8,70.1,98.6,66,98.6,69.8,104.6,75.5,109.3,82.3,111.6,80.8,115.5,78.6,118.9,75.7,121.8,82.6,123.4,90,122.6,96.4,119.5,98.1,123.3,98.9,127.3,98.9,131.4,104.9,127.6,109.6,121.9,111.9,115.1,115.8,116.6,119.2,118.8,122.1,121.7,123.7,114.8,122.9,107.4,119.8,101,123.6,99.3,127.6,98.5,131.7,98.5,127.9,92.5,122.2,87.8,115.4,85.5,116.9,81.6,119.1,78.2,122,75.3,115.1,73.7,107.7,74.5,101.3,77.6,99.6,73.8,98.8,69.8,98.8,65.7,92.8,69.5,88.1,75.3,85.8,82],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class AMIDASymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[153,99.5,153,99.8,153,100.1,153,100.4,153,100.6,153,100.8,153,101.1,153.1,100.9,153.1,100.6,153.2,100.4,153.1,100.1,153,99.8,153,99.5],operators=[0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[153,99.5,151.8,93.6,149.7,88.1,146.8,83.1,146.2,84.1,144.5,83.4,143.6,83.2,142.1,82.9,140.6,82.7,139,82.5,131,81.8,122.8,83.2,115.7,86.8,114.8,87.2,114,87.7,113.1,88.2,112.1,88.8,111.5,88.5,110.5,88.4,108.6,88.2,106.6,88.7,104.9,89.6,102,91.2,100.2,94.3,100,97.6,100,94.2,101,90.7,102.9,87.9,103.9,86.5,105.1,85.4,106.4,84.2,107.3,83.4,107,82,105.7,82,104.9,82,104.4,81.2,104.6,80.5,104.8,79.7,105.8,78.8,106.4,78.1,107.8,76.6,109.3,75.3,110.9,74.1,114.2,71.9,118,70.4,121.9,69.9,128.5,69.1,135.3,70.9,140.6,74.9,141.2,75.4,141.9,75.9,142.4,76.4,135.9,68.1,127,61.9,116.9,58.5,116.3,59,115.7,59.4,115.1,59.9,109.1,64.9,104.5,71.6,101.9,79,101.6,80,101.3,81,101,82,100.7,83,100.5,83.2,99.7,83.8,98.2,84.9,97,86.5,96.4,88.3,95.2,91.7,96,95.5,98.4,98.1,96.2,95.9,94.6,93.2,93.8,90.2,93.4,88.4,93.2,86.5,93.4,84.7,93.5,84.1,93.6,83.4,93.1,83,92.6,82.6,91.9,82.6,91.5,83.1,91,83.6,90.2,83.7,89.7,83.1,89.1,82.4,89.2,80.8,89.2,80,89.1,77.7,89.3,75.4,89.8,73.2,90.7,69.1,92.7,65.2,95.5,62,97.7,59.4,100.5,57.4,103.5,55.9,102.2,55.8,101,55.8,99.7,55.8,93.9,55.8,88.3,56.8,83,58.6,82.9,59.3,82.8,60,82.7,60.7,82,68.7,83.4,76.9,87,84,87.4,84.9,87.9,85.7,88.4,86.6,89,87.6,88.7,88.2,88.6,89.2,88.4,91.1,88.9,93.1,89.8,94.8,91.4,97.7,94.5,99.5,97.8,99.7,94.4,99.7,90.9,98.7,88.1,96.8,86.7,95.8,85.6,94.6,84.4,93.3,83.6,92.4,82.2,92.7,82.2,94,82.2,94.8,81.4,95.3,80.7,95.1,79.9,94.9,79,93.9,78.3,93.3,76.8,91.9,75.5,90.4,74.3,88.8,72.1,85.5,70.6,81.7,70.1,77.8,69.5,72.8,70.4,67.7,72.6,63.2,66,67.1,60.3,72.4,55.8,78.6,56.3,78.9,56.7,79.7,57,80.2,57.6,81.1,58.3,82.1,59,83,60.7,85.2,62.6,87.2,64.7,89.1,67.3,91.4,70.1,93.4,73.2,95,76.3,96.6,79.5,97.7,82.9,98.7,83.7,98.9,83.9,99.6,84.4,100.2,84.9,100.8,85.4,101.3,86,101.7,87.3,102.7,88.7,103.3,90.3,103.6,93.2,104.1,96.3,103.2,98.5,101.2,96.8,103,94.7,104.4,92.4,105.2,89.9,106.1,87.3,106.4,84.7,106.1,83.8,106,82.8,106.5,83.1,107.6,83.3,108.4,84.3,108.8,83.6,109.7,83,110.5,81,110.4,80.1,110.4,78.7,110.5,77.3,110.4,75.9,110.2,73.1,109.9,70.4,109.1,67.8,107.8,62.1,105,57.6,100,55.3,94.1,54.3,91.5,53.7,88.7,53.6,85.9,53.5,84.5,53.6,83.2,53.7,81.9,50.4,87.3,48,93.4,46.8,99.9,48.1,105.7,50.4,111.2,53.4,116.1,54.1,115.4,55.6,116,56.4,116.2,57.9,116.5,59.4,116.7,61,116.9,69,117.6,77.2,116.2,84.3,112.6,85.2,112.2,86,111.7,86.9,111.2,87.9,110.6,88.5,110.9,89.5,111,91.4,111.2,93.4,110.7,95.1,109.8,98,108.2,99.8,105.1,100,101.8,100,105.2,99,108.7,97.1,111.5,96.1,112.9,94.9,114,93.6,115.2,92.7,116,93,117.4,94.3,117.4,95.1,117.4,95.6,118.2,95.4,118.9,95.2,119.7,94.2,120.6,93.6,121.3,92.2,122.8,90.7,124.1,89.1,125.3,85.8,127.5,82,129,78.1,129.5,71.5,130.3,64.7,128.5,59.4,124.5,59.4,124.5,59.4,124.5,59.4,124.5,66,131.8,74.4,137.3,83.8,140.2,84.1,139.9,84.5,139.7,84.8,139.4,90.8,134.4,95.4,127.7,98,120.3,98.3,119.3,98.6,118.3,98.9,117.3,99.2,116.3,99.4,116.1,100.2,115.5,101.7,114.4,102.9,112.8,103.5,111,104.7,107.6,103.9,103.8,101.5,101.2,103.7,103.4,105.3,106.1,106.1,109.1,106.5,110.9,106.7,112.8,106.5,114.6,106.4,115.2,106.3,115.9,106.9,116.3,107.4,116.7,108.1,116.7,108.5,116.2,109,115.7,109.8,115.6,110.3,116.2,110.9,116.9,110.8,118.5,110.8,119.3,110.9,121.6,110.7,123.9,110.2,126.1,109.3,130.2,107.3,134.1,104.5,137.3,102.6,139.4,100.4,141.2,98,142.6,98.7,142.6,99.5,142.6,100.2,142.6,106,142.6,111.7,141.6,117,139.8,117,139.4,117.1,139,117.1,138.6,117.8,130.6,116.4,122.4,112.8,115.3,112.4,114.4,111.9,113.6,111.4,112.7,110.8,111.7,111.1,111.1,111.2,110.1,111.4,108.2,110.9,106.2,110,104.5,108.4,101.6,105.3,99.8,102,99.6,105.4,99.6,108.9,100.6,111.7,102.5,113.1,103.5,114.2,104.7,115.4,106,116.2,106.9,117.6,106.6,117.6,105.3,117.6,104.5,118.4,104,119.1,104.2,119.9,104.4,120.8,105.4,121.5,106,123,107.4,124.3,108.9,125.5,110.5,127.7,113.8,129.2,117.6,129.7,121.5,130.3,126.1,129.6,130.7,127.7,134.9,133.9,131.2,139.3,126.3,143.6,120.4,143.2,120,142.9,119.4,142.7,119,142.1,118.1,141.4,117.1,140.7,116.2,139,114,137.1,112,135,110.1,132.4,107.8,129.6,105.8,126.5,104.2,123.4,102.6,120.2,101.5,116.8,100.5,116,100.3,115.8,99.6,115.3,99,114.8,98.4,114.3,97.9,113.7,97.5,112.4,96.5,111,95.9,109.4,95.6,106.5,95.1,103.4,96,101.2,98,102.9,96.2,105,94.8,107.3,94,109.8,93.1,112.4,92.8,115,93.1,115.9,93.2,116.9,92.7,116.6,91.6,116.4,90.8,115.4,90.4,116.1,89.5,116.7,88.7,118.7,88.8,119.6,88.8,121,88.7,122.4,88.8,123.8,89,126.6,89.3,129.3,90.1,131.9,91.4,137.6,94.2,142.1,99.2,144.4,105.1,145.4,107.7,146,110.5,146.1,113.3,146.2,114.5,146.1,115.6,146,116.8,149,112,151.3,106.7,152.6,100.9,152.6,100.7,152.6,100.5,152.6,100.2,153,100.1,153,99.8,153,99.5],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[98.3,38.7,101.7,38.7,103.5,38.7,105,37.2,105,35.4,105,25.5,105,23.7,103.5,22.2,101.7,22.2,98.3,22.2,96.5,22.2,95,23.7,95,25.5,95,35.4,94.9,37.2,96.4,38.7,98.3,38.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[101.7,161.3,98.3,161.3,96.5,161.3,95,162.8,95,164.6,95,174.5,95,176.3,96.5,177.8,98.3,177.8,101.7,177.8,103.5,177.8,105,176.3,105,174.5,105,164.6,105.1,162.8,103.6,161.3,101.7,161.3],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[174.5,94.9,164.6,94.9,162.8,94.9,161.3,96.4,161.3,98.2,161.3,101.6,161.3,103.4,162.8,104.9,164.6,104.9,174.5,104.9,176.3,104.9,177.8,103.4,177.8,101.6,177.8,98.2,177.9,96.4,176.4,94.9,174.5,94.9],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[38.7,101.7,38.7,98.3,38.7,96.5,37.2,95,35.4,95,25.5,95,23.7,95,22.2,96.5,22.2,98.3,22.2,101.7,22.2,103.5,23.7,105,25.5,105,35.4,105,37.2,105.1,38.7,103.6,38.7,101.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[149.3,142.1,148,140.8,145.9,140.8,144.6,142.1,142.2,144.5,140.9,145.8,140.9,147.9,142.2,149.2,149.2,156.2,150.5,157.5,152.6,157.5,153.9,156.2,156.3,153.8,157.6,152.5,157.6,150.4,156.3,149.1,149.3,142.1],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[50.7,57.9,52,59.2,54.1,59.2,55.4,57.9,57.8,55.5,59.1,54.2,59.1,52.1,57.8,50.8,50.8,43.8,49.5,42.5,47.4,42.5,46.1,43.8,43.7,46.2,42.4,47.5,42.4,49.6,43.7,50.9,50.7,57.9],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[55.4,142.1,54.1,140.8,52,140.8,50.7,142.1,43.7,149.1,42.4,150.4,42.4,152.5,43.7,153.8,46.1,156.2,47.4,157.5,49.5,157.5,50.8,156.2,57.8,149.2,59.1,147.9,59.1,145.8,57.8,144.5,55.4,142.1],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[77.6,157.1,74.4,155.8,72.7,155.1,70.7,155.9,70,157.6,66.1,166.7,65.4,168.4,66.2,170.4,67.9,171.1,71.1,172.4,72.8,173.1,74.8,172.3,75.5,170.6,79.4,161.5,80.1,159.8,79.3,157.8,77.6,157.1],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.6,57.9,145.9,59.2,148,59.2,149.3,57.9,156.3,50.9,157.6,49.6,157.6,47.5,156.3,46.2,153.9,43.8,152.6,42.5,150.5,42.5,149.2,43.8,142.2,50.8,140.9,52.1,140.9,54.2,142.2,55.5,144.6,57.9],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[122.4,42.9,125.6,44.2,127.3,44.9,129.3,44.1,130,42.4,133.9,33.3,134.6,31.6,133.8,29.6,132.1,28.9,128.9,27.6,127.2,26.9,125.2,27.7,124.5,29.4,120.6,38.5,119.9,40.2,120.7,42.2,122.4,42.9],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[29.4,75.5,38.5,79.4,40.2,80.1,42.2,79.3,42.9,77.6,44.2,74.4,44.9,72.7,44.1,70.7,42.4,70,33.3,66.1,31.6,65.4,29.6,66.2,28.9,67.9,27.6,71.1,26.9,72.9,27.7,74.8,29.4,75.5],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[170.6,124.5,161.5,120.6,159.8,119.9,157.8,120.7,157.1,122.4,155.8,125.6,155.1,127.3,155.9,129.3,157.6,130,166.7,133.9,168.4,134.6,170.4,133.8,171.1,132.1,172.4,128.9,173.1,127.1,172.3,125.2,170.6,124.5],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[71.1,42,71.8,43.7,73.7,44.5,75.5,43.8,78.7,42.5,80.4,41.8,81.2,39.9,80.5,38.1,76.8,29,76.1,27.3,74.2,26.5,72.4,27.2,69.2,28.5,67.5,29.2,66.7,31.1,67.4,32.9,71.1,42],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[128.9,158,128.2,156.3,126.3,155.5,124.5,156.2,121.3,157.5,119.6,158.2,118.8,160.1,119.5,161.9,123.2,171.1,123.9,172.8,125.8,173.6,127.6,172.9,130.8,171.6,132.5,170.9,133.3,169,132.6,167.2,128.9,158],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[156.2,75.4,157.5,78.6,158.2,80.3,160.1,81.1,161.9,80.4,171.1,76.7,172.8,76,173.6,74.1,172.9,72.3,171.6,69.1,170.9,67.4,169,66.6,167.2,67.3,158,71,156.3,71.8,155.5,73.7,156.2,75.4],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[43.8,124.6,42.5,121.4,41.8,119.7,39.9,118.9,38.1,119.6,28.9,123.3,27.2,124,26.4,125.9,27.1,127.7,28.4,130.9,29.1,132.6,31,133.4,32.8,132.7,42,129,43.7,128.2,44.5,126.3,43.8,124.6],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[100.2,44.7,69.7,44.7,44.9,69.5,44.9,100,44.9,130.5,69.7,155.3,100.2,155.3,130.7,155.3,155.5,130.5,155.5,100,155.5,69.5,130.7,44.7,100.2,44.7,146.3,117,146.4,115.8,146.5,114.7,146.4,113.5,146.3,110.7,145.7,107.9,144.7,105.3,142.4,99.4,137.9,94.4,132.2,91.6,129.7,90.4,126.9,89.5,124.1,89.2,122.7,89,121.3,89,119.9,89,118.9,89,117,88.9,116.4,89.7,115.7,90.6,116.7,91,116.9,91.8,117.2,92.9,116.2,93.3,115.3,93.3,112.7,93.1,110.1,93.3,107.6,94.2,105.3,95.1,103.2,96.5,101.5,98.2,103.7,96.2,106.8,95.3,109.7,95.8,111.3,96.1,112.8,96.7,114,97.7,114.6,98.1,115.1,98.7,115.6,99.2,116.1,99.8,116.3,100.4,117.1,100.7,120.4,101.7,123.7,102.7,126.8,104.4,129.9,106,132.7,108,135.3,110.3,137.4,112.1,139.3,114.2,141,116.4,141.7,117.3,142.3,118.2,143,119.2,143.3,119.6,143.6,120.2,143.9,120.6,139.6,126.4,134.2,131.4,128,135.1,129.8,130.9,130.5,126.2,130,121.7,129.5,117.8,128.1,114,125.8,110.7,124.7,109,123.3,107.5,121.8,106.2,121.2,105.6,120.3,104.6,119.4,104.4,118.6,104.2,117.9,104.7,117.9,105.5,117.9,106.8,116.5,107.1,115.7,106.2,114.6,104.9,113.5,103.7,112,102.7,109.2,100.7,105.7,99.8,102.3,99.8,105.6,100,108.7,101.8,110.3,104.7,111.3,106.4,111.7,108.3,111.5,110.3,111.4,111.4,111.2,112,111.7,112.9,112.2,113.7,112.7,114.6,113.1,115.5,116.7,122.7,118.2,130.8,117.4,138.8,117.4,139.2,117.3,139.6,117.3,140,112,141.8,106.3,142.8,100.5,142.8,99.8,142.8,99,142.8,98.3,142.8,100.7,141.4,102.9,139.6,104.8,137.5,107.6,134.3,109.6,130.5,110.5,126.3,111,124.1,111.2,121.8,111.1,119.5,111.1,118.6,111.2,117.1,110.6,116.4,110.1,115.8,109.3,115.8,108.8,116.4,108.4,116.8,107.7,116.9,107.2,116.5,106.7,116,106.8,115.4,106.8,114.8,107,113,106.8,111.1,106.4,109.3,105.7,106.3,104,103.5,101.8,101.4,104.2,104,105,107.9,103.8,111.2,103.2,113,102,114.6,100.5,115.7,99.7,116.3,99.5,116.6,99.2,117.5,98.9,118.5,98.6,119.5,98.3,120.5,95.8,127.9,91.2,134.6,85.1,139.6,84.8,139.9,84.4,140.1,84.1,140.4,74.7,137.5,66.2,132,59.7,124.7,59.7,124.7,59.7,124.7,59.7,124.7,65,128.7,71.8,130.6,78.4,129.7,82.3,129.2,86.1,127.8,89.4,125.5,91.1,124.4,92.6,123,93.9,121.5,94.5,120.9,95.5,120,95.7,119.1,95.9,118.3,95.4,117.6,94.6,117.6,93.3,117.6,93,116.2,93.9,115.4,95.2,114.3,96.4,113.2,97.4,111.7,99.4,108.9,100.3,105.4,100.3,102,100.1,105.3,98.3,108.4,95.4,110,93.7,111,91.8,111.4,89.8,111.2,88.7,111.1,88.1,110.9,87.2,111.4,86.4,111.9,85.5,112.4,84.6,112.8,77.4,116.4,69.3,117.9,61.3,117.1,59.8,117,58.2,116.7,56.7,116.4,55.9,116.2,54.3,115.6,53.7,116.3,50.7,111.4,48.5,106,47.1,100.1,48.3,93.6,50.7,87.5,54,82.1,53.8,83.4,53.8,84.8,53.9,86.1,54,88.9,54.6,91.7,55.6,94.3,57.9,100.2,62.4,105.2,68.1,108,70.6,109.2,73.4,110.1,76.2,110.4,77.6,110.6,79,110.6,80.4,110.6,81.4,110.6,83.3,110.7,83.9,109.9,84.6,109,83.6,108.6,83.4,107.8,83.1,106.7,84.1,106.3,85,106.3,87.6,106.5,90.2,106.3,92.7,105.4,95,104.5,97.1,103.1,98.8,101.4,96.6,103.4,93.5,104.3,90.6,103.8,89,103.5,87.5,102.9,86.3,101.9,85.7,101.5,85.2,100.9,84.7,100.4,84.2,99.8,84,99.2,83.2,98.9,79.9,97.9,76.6,96.9,73.5,95.2,70.4,93.6,67.6,91.6,65,89.3,62.9,87.5,61,85.4,59.3,83.2,58.6,82.3,58,81.4,57.3,80.4,57,79.9,56.6,79.1,56.1,78.8,60.5,72.5,66.3,67.3,72.9,63.4,70.7,67.9,69.8,73,70.4,78,70.9,81.9,72.3,85.7,74.6,89,75.7,90.7,77.1,92.2,78.6,93.5,79.2,94.1,80.1,95.1,81,95.3,81.8,95.5,82.5,95,82.5,94.2,82.5,92.9,83.9,92.6,84.7,93.5,85.8,94.8,86.9,96,88.4,97,91.2,99,94.7,99.9,98.1,99.9,94.8,99.7,91.7,97.9,90.1,95,89.1,93.3,88.7,91.4,88.9,89.4,89,88.3,89.2,87.7,88.7,86.8,88.2,86,87.7,85.1,87.3,84.2,83.7,77,82.2,68.9,83,60.9,83.1,60.2,83.2,59.5,83.3,58.8,88.6,57,94.2,56,100,56,101.3,56,102.5,56,103.8,56.1,100.8,57.6,98,59.6,95.8,62.2,93,65.4,91,69.2,90.1,73.4,89.6,75.6,89.4,77.9,89.5,80.2,89.5,81.1,89.4,82.6,90,83.3,90.5,83.9,91.3,83.9,91.8,83.3,92.2,82.9,92.9,82.8,93.4,83.2,93.9,83.7,93.8,84.3,93.7,84.9,93.5,86.7,93.7,88.6,94.1,90.4,94.8,93.4,96.5,96.2,98.7,98.3,96.3,95.7,95.5,91.8,96.7,88.5,97.3,86.7,98.5,85.1,100,84,100.8,83.4,101,83.1,101.3,82.2,101.6,81.2,101.9,80.2,102.2,79.2,104.7,71.8,109.3,65.1,115.4,60.1,116,59.6,116.6,59.1,117.2,58.7,127.3,62,136.1,68.3,142.7,76.6,142.1,76.1,141.5,75.5,140.9,75.1,135.6,71.1,128.8,69.2,122.2,70.1,118.3,70.6,114.5,72,111.2,74.3,109.5,75.4,108,76.8,106.7,78.3,106.1,78.9,105.1,79.8,104.9,80.7,104.7,81.5,105.2,82.2,106,82.2,107.3,82.2,107.6,83.6,106.7,84.4,105.4,85.5,104.2,86.6,103.2,88.1,101.2,90.9,100.3,94.4,100.3,97.8,100.5,94.5,102.3,91.4,105.2,89.8,106.9,88.8,108.8,88.4,110.8,88.6,111.9,88.7,112.5,88.9,113.4,88.4,114.2,87.9,115.1,87.4,116,87,123.2,83.4,131.3,81.9,139.3,82.7,140.8,82.8,142.4,83.1,143.9,83.4,144.8,83.6,146.5,84.3,147.1,83.3,150,88.3,152.1,93.8,153.3,99.7,153.4,100,153.4,100.3,153.5,100.6,153.4,100.8,153.4,101.1,153.3,101.3,151.6,106.9,149.3,112.2,146.3,117],operators=[0,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class NoticeSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Circle(100,100,41.9,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[100,50.7,72.8,50.7,50.7,72.8,50.7,100,50.7,127.2,72.8,149.3,100,149.3,127.2,149.3,149.3,127.2,149.3,100,149.3,72.8,127.2,50.7,100,50.7,100,141.9,76.8,141.9,58.1,123.1,58.1,100,58.1,76.9,76.8,58.1,100,58.1,123.2,58.1,141.9,76.9,141.9,100,141.9,123.1,123.2,141.9,100,141.9],operators=[0,2,2,2,2,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class CautionSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #g.transform = (1,0,0,-1,0,200)
        g.transform = (.7071,-0.7071,.7071,.7071,-41.5334,99.7292)
        g.add(Ellipse(99.6,100,32.3,15.2,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[83.7,84,94,73.7,107.7,69,121.1,69.7,119.2,63,115.7,56.7,110.4,51.5,94,35.1,67.5,35.1,51.1,51.5,34.7,67.9,34.7,94.4,51.1,110.8,56.4,116.1,62.7,119.6,69.3,121.5,68.6,108,73.4,94.3,83.7,84],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[115.6,116,105.3,126.3,91.6,131,78.2,130.3,80.1,137,83.6,143.3,88.9,148.5,105.3,164.9,131.8,164.9,148.2,148.5,164.6,132.1,164.6,105.6,148.2,89.2,142.9,83.9,136.6,80.4,130,78.5,130.6,92,125.8,105.7,115.6,116],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[153.4,84,146.4,77,137.9,72.6,128.9,70.7,127,61.7,122.6,53.2,115.6,46.2,96.4,27,65.1,27,45.9,46.2,26.7,65.4,26.7,96.7,45.9,115.9,52.9,122.9,61.4,127.3,70.4,129.2,72.3,138.2,76.7,146.7,83.7,153.7,102.9,172.9,134.2,172.9,153.4,153.7,172.6,134.5,172.6,103.3,153.4,84,110.4,110.8,101.2,120,88.8,124,76.8,122.9,75.7,110.9,79.7,98.5,88.9,89.3,98.1,80.1,110.5,76.1,122.5,77.2,123.6,89.2,119.6,101.6,110.4,110.8,51.1,110.8,34.7,94.4,34.7,67.9,51.1,51.5,67.5,35.1,94,35.1,110.4,51.5,115.7,56.8,119.2,63.1,121.1,69.7,107.6,69,93.9,73.8,83.7,84,73.4,94.3,68.7,108,69.4,121.4,62.6,119.6,56.3,116,51.1,110.8,148.2,148.6,131.8,165,105.3,165,88.9,148.6,83.6,143.3,80.1,137,78.2,130.4,91.7,131.1,105.4,126.3,115.6,116.1,125.8,105.9,130.6,92.1,129.9,78.7,136.6,80.6,142.9,84.1,148.1,89.4,164.5,105.6,164.5,132.2,148.2,148.6],operators=[0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,3,0,2,2,2,2,2,2,3,0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class WarningSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[100,108.8,103.9,108.8,107.6,108.3,111.2,107.3,109.3,99.8,105.4,93.1,100,87.8,94.7,93.1,90.7,99.8,88.8,107.3,92.4,108.2,96.1,108.8,100,108.8],operators=[0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[100,78,108.2,71.8,118.4,68.2,129.5,68.2,133.8,68.2,137.9,68.7,141.8,69.8,141.9,68.8,141.9,67.8,141.9,66.9,141.9,43.7,123.1,25,100,25,76.9,25,58.1,43.7,58.1,66.8,58.1,67.8,58.1,68.8,58.2,69.7,58.4,72.2,58.8,74.7,59.4,77,62.5,89.2,70.9,99.2,82,104.6,84.1,96.4,88.5,89,94.3,83,96.1,81.2,98,79.5,100,78],operators=[0,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[87.7,114.6,85.2,114,82.8,113.1,80.5,112.1,66.8,106.2,56.4,94.3,52.4,79.7,38.3,86.5,28.6,100.9,28.6,117.5,28.6,140.7,47.4,159.4,70.5,159.4,79.3,159.4,87.5,156.7,94.3,152,96.3,150.6,98.2,149,100,147.3,107.7,139.7,112.4,129.2,112.4,117.5,112.4,116.5,112.4,115.5,112.3,114.6,108.4,115.6,104.2,116.2,100,116.2,95.8,116.2,91.6,115.6,87.7,114.6],operators=[0,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[129.5,75.6,120.7,75.6,112.5,78.3,105.7,83,111.5,89,115.9,96.4,118.1,104.7,118.8,107.1,119.2,109.6,119.5,112.1,119.7,113.9,119.8,115.7,119.8,117.5,119.8,130.9,114.4,143.1,105.7,152,112.5,156.7,120.7,159.4,129.5,159.4,152.7,159.4,171.4,140.6,171.4,117.5,171.4,100.8,161.7,86.4,147.6,79.7,145.4,78.6,143.1,77.8,140.7,77.1,137.1,76.1,133.4,75.6,129.5,75.6],operators=[0,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[149,72.2,149.2,70.4,149.3,68.6,149.3,66.8,149.3,39.6,127.2,17.5,100,17.5,72.8,17.5,50.7,39.6,50.7,66.8,50.7,68.6,50.8,70.4,51,72.2,33.5,79.8,21.2,97.2,21.2,117.5,21.2,144.7,43.3,166.8,70.5,166.8,81.5,166.8,91.8,163.1,100,157,108.2,163.2,118.4,166.8,129.5,166.8,156.7,166.8,178.8,144.7,178.8,117.5,178.8,97.3,166.5,79.8,149,72.2,100,24.9,123.2,24.9,141.9,43.7,141.9,66.8,141.9,67.8,141.9,68.8,141.8,69.7,137.9,68.7,133.7,68.1,129.5,68.1,118.5,68.1,108.2,71.8,100,77.9,98,79.4,96.1,81.1,94.3,82.9,88.5,88.9,84.1,96.3,81.9,104.6,70.8,99.3,62.4,89.2,59.3,77,58.7,74.6,58.3,72.2,58.1,69.7,58,68.7,58,67.7,58,66.8,58.1,43.7,76.8,24.9,100,24.9,100,87.7,105.3,93,109.3,99.7,111.2,107.2,107.6,108.2,103.9,108.7,100,108.7,96.1,108.7,92.4,108.2,88.8,107.2,90.7,99.7,94.7,93,100,87.7,94.3,152,87.5,156.7,79.3,159.4,70.5,159.4,47.3,159.4,28.6,140.6,28.6,117.5,28.6,100.8,38.3,86.4,52.4,79.7,56.3,94.3,66.8,106.2,80.5,112.1,82.8,113.1,85.2,113.9,87.7,114.6,91.6,115.6,95.8,116.2,100,116.2,104.2,116.2,108.4,115.7,112.3,114.6,112.4,115.6,112.4,116.6,112.4,117.5,112.4,129.2,107.6,139.7,100,147.3,98.3,149,96.4,150.6,94.3,152,129.5,159.4,120.7,159.4,112.5,156.7,105.7,152,114.4,143.1,119.8,130.9,119.8,117.5,119.8,115.7,119.7,113.9,119.5,112.1,119.2,109.6,118.7,107.1,118.1,104.7,115.9,96.4,111.5,89,105.7,83,112.5,78.3,120.7,75.6,129.5,75.6,133.4,75.6,137.1,76.1,140.7,77.1,143.1,77.8,145.4,78.6,147.6,79.7,161.7,86.5,171.4,100.9,171.4,117.5,171.4,140.7,152.7,159.4,129.5,159.4],operators=[0,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class DangerSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Ellipse(99.7,101,20.3,21.1,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[69.5,133.6,68.7,130.9,68.2,128.1,67.9,125.2,67.7,123.3,67.6,121.4,67.6,119.5,67.6,113,68.8,106.7,71,101,72.4,97.4,74.1,94,76.2,90.9,80,85.2,84.8,80.3,90.4,76.5,87,75.7,83.4,75.2,79.8,75.2,78.5,75.2,77.2,75.3,76,75.4,73.2,75.6,70.5,76.1,67.9,76.8,55.2,80.3,44.9,89.3,39.4,101,37.9,104.2,36.8,107.6,36.1,111.1,35.6,113.8,35.3,116.6,35.3,119.5,35.3,144,55.2,163.9,79.7,163.9,83.4,163.9,86.9,163.4,90.3,162.6,80.3,155.8,72.8,145.6,69.5,133.6],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[129.9,133.6,127.1,134.2,124.3,134.5,121.4,134.6,120.8,134.6,120.2,134.6,119.6,134.6,112.5,134.6,105.8,133.2,99.6,130.6,96.3,129.2,93.1,127.5,90.2,125.5,84.6,121.7,79.8,116.7,76,111.1,75.5,113.8,75.2,116.6,75.2,119.5,75.2,121.9,75.4,124.3,75.8,126.6,76.2,129.3,76.9,132,77.9,134.5,81.8,145.2,89.6,154,99.7,159,102.7,160.5,105.8,161.7,109.1,162.5,112.5,163.3,116.1,163.8,119.7,163.8,144.2,163.8,164.1,143.9,164.1,119.4,164.1,116.5,163.8,113.7,163.3,111,155.7,122.5,143.8,130.8,129.9,133.6],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[119.7,38,116,38,112.5,38.5,109.1,39.3,119.1,46.1,126.6,56.4,129.9,68.3,130.7,71,131.2,73.8,131.5,76.7,131.7,78.6,131.8,80.5,131.8,82.4,131.8,88.9,130.6,95.2,128.4,100.9,127,104.5,125.3,107.9,123.2,111,119.4,116.7,114.6,121.6,109,125.4,112.4,126.2,116,126.7,119.6,126.7,120.9,126.7,122.2,126.6,123.4,126.5,126.2,126.3,128.9,125.8,131.5,125.1,144.2,121.6,154.5,112.6,160,100.9,161.5,97.7,162.6,94.3,163.3,90.8,163.8,88.1,164.1,85.3,164.1,82.4,164.1,57.9,144.2,38,119.7,38],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[69.5,68.3,72.3,67.7,75.1,67.4,78,67.3,78.6,67.3,79.2,67.3,79.8,67.3,86.9,67.3,93.6,68.7,99.8,71.3,103.1,72.7,106.3,74.4,109.2,76.4,114.8,80.2,119.6,85.2,123.4,90.8,123.9,88.1,124.2,85.3,124.2,82.4,124.2,80,124,77.6,123.6,75.3,123.2,72.6,122.5,69.9,121.5,67.4,117.6,56.7,109.8,47.9,99.7,42.9,96.7,41.4,93.6,40.2,90.3,39.4,86.9,38.6,83.3,38.1,79.7,38.1,55.2,38.1,35.3,58,35.3,82.5,35.3,85.4,35.6,88.2,36.1,90.9,43.7,79.4,55.6,71.1,69.5,68.3],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[171.9,82.4,171.9,53.6,148.5,30.2,119.7,30.2,112.6,30.2,105.9,31.6,99.7,34.2,93.5,31.6,86.8,30.2,79.7,30.2,50.9,30.2,27.5,53.6,27.5,82.4,27.5,88.9,28.7,95.2,30.9,100.9,28.7,106.7,27.5,112.9,27.5,119.4,27.5,148.2,50.9,171.6,79.7,171.6,86.8,171.6,93.5,170.2,99.7,167.6,105.9,170.2,112.6,171.6,119.7,171.6,148.5,171.6,171.9,148.2,171.9,119.4,171.9,112.9,170.7,106.6,168.5,100.9,170.7,95.2,171.9,89,171.9,82.4,79.7,38,83.4,38,86.9,38.5,90.3,39.3,93.6,40.1,96.7,41.3,99.7,42.8,109.7,47.9,117.6,56.7,121.5,67.3,122.4,69.8,123.1,72.5,123.6,75.2,124,77.5,124.2,79.9,124.2,82.3,124.2,85.2,123.9,88,123.4,90.7,119.6,85,114.8,80.1,109.2,76.3,106.3,74.3,103.1,72.6,99.8,71.2,93.6,68.6,86.9,67.2,79.8,67.2,79.2,67.2,78.6,67.2,78,67.2,75.1,67.3,72.3,67.6,69.5,68.2,55.6,71,43.7,79.3,36.2,90.7,35.7,88,35.4,85.2,35.4,82.3,35.3,57.9,55.2,38,79.7,38,120,101,115.8,110.1,108.6,117.6,99.7,122.1,90.8,117.6,83.6,110.1,79.4,101,83.6,91.9,90.8,84.4,99.7,79.9,108.6,84.4,115.8,91.9,120,101,79.7,163.9,55.2,163.9,35.3,144,35.3,119.5,35.3,116.6,35.6,113.8,36.1,111.1,36.8,107.6,37.9,104.2,39.4,101,44.8,89.3,55.2,80.3,67.9,76.8,70.5,76.1,73.2,75.6,76,75.4,77.3,75.3,78.5,75.2,79.8,75.2,83.5,75.2,87,75.7,90.4,76.5,84.8,80.3,80,85.3,76.2,90.9,74,94,72.3,97.4,70.9,101,68.7,106.8,67.5,113,67.5,119.5,67.5,121.4,67.6,123.3,67.8,125.2,68.1,128.1,68.7,130.9,69.4,133.6,72.8,145.5,80.3,155.8,90.2,162.6,86.9,163.5,83.4,163.9,79.7,163.9,119.7,163.9,116,163.9,112.5,163.4,109.1,162.6,105.8,161.8,102.7,160.6,99.7,159.1,89.7,154,81.8,145.2,77.9,134.6,77,132.1,76.3,129.4,75.8,126.7,75.4,124.4,75.2,122,75.2,119.6,75.2,116.7,75.5,113.9,76,111.2,79.8,116.9,84.6,121.8,90.2,125.6,93.1,127.6,96.3,129.3,99.6,130.7,105.8,133.3,112.5,134.7,119.6,134.7,120.2,134.7,120.8,134.7,121.4,134.7,124.3,134.6,127.1,134.3,129.9,133.7,143.8,130.9,155.7,122.6,163.2,111.2,163.7,113.9,164,116.7,164,119.6,164.1,144,144.2,163.9,119.7,163.9,163.3,90.8,162.6,94.3,161.5,97.7,160,100.9,154.6,112.6,144.2,121.6,131.5,125.1,128.9,125.8,126.2,126.3,123.4,126.5,122.1,126.6,120.9,126.7,119.6,126.7,115.9,126.7,112.4,126.2,109,125.4,114.6,121.6,119.4,116.6,123.2,111,125.3,107.8,127,104.4,128.4,100.9,130.6,95.1,131.8,88.9,131.8,82.4,131.8,80.5,131.7,78.6,131.5,76.7,131.2,73.8,130.6,71,129.9,68.3,126.5,56.4,119,46.1,109.1,39.3,112.5,38.5,116.1,38,119.7,38,144.2,38,164.1,57.9,164.1,82.4,164.1,85.3,163.8,88.1,163.3,90.8],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class CriticalSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[74.8,62.3,78.6,54.4,84.4,47.6,91.6,42.6,88.4,41.8,85,41.4,81.6,41.4,58.4,41.4,39.7,60.2,39.7,83.3,39.7,86,40,88.7,40.5,91.2,41.1,94.6,42.2,97.8,43.6,100.8,46.6,107.4,51.3,113,57.1,117.2,55.2,112.1,54.1,106.6,54.1,100.8,53.9,84.8,62.2,70.6,74.8,62.3],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[119.4,41.5,115.9,41.5,112.6,41.9,109.4,42.7,106.3,43.5,103.3,44.6,100.5,46,95.3,48.6,90.8,52.3,87.1,56.7,91.2,55.5,95.5,54.8,100,54.8,114.5,54.8,127.4,61.5,135.8,72,146,75.6,154.6,82.5,160.5,91.4,161,88.8,161.3,86.2,161.3,83.5,161.3,60.2,142.5,41.5,119.4,41.5],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[126.5,138.6,122.8,146.9,116.8,154.1,109.3,159.2,112.5,160,115.9,160.4,119.3,160.4,142.5,160.4,161.2,141.6,161.2,118.5,161.2,115.8,160.9,113.1,160.4,110.6,159.8,107.2,158.7,104,157.3,101,154.1,94,148.9,88,142.6,83.7,144.8,89,146,94.9,146,101,146.1,116.5,138.4,130.2,126.5,138.6],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[63.8,129.4,54.2,125.7,46,119,40.4,110.5,39.9,113.1,39.6,115.7,39.6,118.4,39.6,141.6,58.4,160.3,81.5,160.3,85,160.3,88.3,159.9,91.5,159.1,94.6,158.3,97.6,157.2,100.4,155.8,105.7,153.1,110.4,149.3,114.1,144.7,109.6,146.1,104.9,146.9,99.9,146.9,85.3,147,72.2,140.1,63.8,129.4],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Circle(100,100.9,24,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[168.7,83.4,168.7,56.2,146.6,34.1,119.4,34.1,112.7,34.1,106.3,35.4,100.5,37.9,94.7,35.5,88.3,34.1,81.6,34.1,54.4,34.1,32.3,56.2,32.3,83.4,32.3,89.6,33.4,95.5,35.5,100.9,33.4,106.3,32.3,112.2,32.3,118.4,32.3,145.6,54.4,167.7,81.6,167.7,88.3,167.7,94.7,166.4,100.5,163.9,106.3,166.3,112.7,167.7,119.4,167.7,146.6,167.7,168.7,145.6,168.7,118.4,168.7,112.2,167.6,106.3,165.5,100.9,167.5,95.5,168.7,89.6,168.7,83.4,81.6,41.5,85.1,41.5,88.4,41.9,91.6,42.7,84.4,47.6,78.6,54.4,74.8,62.4,62.2,70.6,53.9,84.8,53.9,101,53.9,106.8,55,112.3,56.9,117.4,51.1,113.2,46.5,107.6,43.4,101,42,98,41,94.8,40.3,91.4,39.8,88.8,39.5,86.2,39.5,83.5,39.6,60.2,58.4,41.5,81.6,41.5,100,62.2,121.4,62.2,138.7,79.6,138.7,100.9,138.7,122.3,121.3,139.6,100,139.6,78.7,139.6,61.3,122.2,61.3,100.9,61.3,79.6,78.6,62.2,100,62.2,91.6,159.2,88.4,160,85,160.4,81.6,160.4,58.4,160.4,39.7,141.6,39.7,118.5,39.7,115.8,40,113.1,40.5,110.6,46.1,119.1,54.3,125.7,63.9,129.5,72.2,140.1,85.3,147,100,147,104.9,147,109.7,146.2,114.2,144.8,110.5,149.4,105.8,153.2,100.5,155.9,97.7,157.3,94.7,158.4,91.6,159.2,119.4,160.4,115.9,160.4,112.6,160,109.4,159.2,116.9,154.1,122.9,147,126.6,138.6,138.4,130.2,146.2,116.5,146.2,100.9,146.2,94.8,145,89,142.8,83.6,149.2,87.9,154.3,93.9,157.5,100.9,158.9,103.9,159.9,107.1,160.6,110.5,161.1,113.1,161.4,115.7,161.4,118.4,161.3,141.6,142.5,160.4,119.4,160.4,135.8,72,127.3,61.5,114.4,54.8,100,54.8,95.5,54.8,91.2,55.5,87.1,56.7,90.8,52.3,95.3,48.6,100.5,46,103.3,44.6,106.3,43.5,109.4,42.7,112.6,41.9,116,41.5,119.4,41.5,142.6,41.5,161.3,60.3,161.3,83.4,161.3,86.1,161,88.8,160.5,91.3,154.7,82.5,146,75.6,135.8,72],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[100,132.3,117.3,132.3,131.4,118.3,131.4,100.9,131.4,83.6,117.4,69.5,100,69.5,82.6,69.5,68.6,83.5,68.6,100.9,68.6,118.2,82.7,132.3,100,132.3,100,76.9,113.2,76.9,124,87.7,124,100.9,124,114.1,113.2,124.9,100,124.9,86.8,124.9,76,114.1,76,100.9,76,87.7,86.8,76.9,100,76.9],operators=[0,2,2,2,2,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class ThaumielSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[94.7,112.4,105.8,112.4,106.5,112.4,107,111.6,106.5,110.9,104.6,108.3,102.8,105.8,100.9,103.2,100.5,102.7,99.8,102.7,99.4,103.2,97.5,105.8,95.7,108.3,93.8,110.9,93.5,111.6,94,112.4,94.7,112.4],operators=[0,1,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[111.2,108.8,112.3,105.3,113.5,101.7,114.6,98.2,114.8,97.5,114.2,96.8,113.4,97,110.4,98,107.4,98.9,104.4,99.9,103.8,100.1,103.6,100.8,103.9,101.3,105.8,103.9,107.6,106.4,109.5,109,110,109.7,110.9,109.6,111.2,108.8],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[32.6,94.4,34,97.2,35.9,99.7,38.3,101.7,38.3,101.7,39.2,102.5,42.1,104.7,46.1,106.1,48.2,106.8,51.1,107.2,55,107.2,55.5,107.2,56,107.2,56.5,107.2,62.6,107.1,68.6,106,74.4,104.1,81.3,101.8,82.3,101.5,82.8,100.4,82.5,99.5,82.1,98.3,81.7,97,81.3,95.8,80.9,94.6,80.3,93.3,81.5,92.3,82.2,91.7,84.3,90.2,85.9,89.1,86.7,88.5,86.9,87.3,86.3,86.5,82,80.5,78.3,75.4,73.9,70.8,68.8,67,65.4,64.5,62.6,62.9,60.4,62.2,58.3,61.6,55.9,60.9,53,60.9,49.6,60.9,46.1,61.9,42.4,63.9,41.9,64.1,41.5,64.4,41.2,64.6,41.1,64.7,41,64.8,40.9,64.9,38.8,66.5,38.7,66.6,38.6,66.7,35.3,69.5,32.9,73.1,31.6,77.2,30.5,80.6,30.2,84.3,30.7,87.8,30.8,88.3,31,88.9,31.1,89.4,32.6,94.4],operators=[0,2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,1,2,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[73.1,162.2,73.3,162.2,73.7,162.2,74.2,162.1,74.7,162.1,77.9,161.7,80.9,160.6,83.6,158.9,84,158.7,87.3,156.6,90.1,152.9,91.3,151.3,92.5,148.7,93.7,145.4,95.8,139.1,96.8,132.4,96.8,125.7,96.8,118,96.8,117,96,116.2,95,116.2,90.8,116.2,89.5,116.2,88.4,116.2,87.9,114.8,87.5,113.8,86.8,111.5,86.2,109.8,85.9,108.8,84.8,108.3,83.9,108.6,78.2,110.4,73.1,112.1,68.2,114.4,63.6,117.3,58.5,120.6,54.8,123.6,53.1,126.1,50.6,129.7,47.4,134.3,49.2,143.6,49.3,144.1,49.4,144.6,49.5,145,49.5,145.2,49.5,145.3,49.5,145.4,50.3,147.9,50.3,148,50.4,148.1,52,152,54.7,155.4,58.1,158,61.6,160.5,65.6,162,69.9,162.3,70,162.3,70.1,162.3,72,162.3,73,162.3,73.1,162.2],operators=[0,1,2,2,2,2,2,1,2,1,2,2,2,1,2,2,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[84.9,32.6,84.7,32.7,84.6,32.9,84.4,33,82,35.3,80.2,38,79,40.9,78.8,41.3,77.4,45,77.3,49.6,77.2,52.2,78.1,56.1,79.8,60.8,81.8,66.3,84.6,71.5,88.1,76.3,92.3,82,92.9,82.9,94.1,83,95,82.3,95.9,81.7,96.7,81.1,97.6,80.4,98.6,79.7,99.8,78.3,101.3,79,102.1,79.4,104.3,81.1,105.9,82.3,106.7,82.9,107.9,82.8,108.5,81.9,112.6,76.2,116.1,71.4,118.9,66.2,120.9,60.7,122.6,56,123.5,52.1,123.4,49.5,123.3,45,123.2,39.5,116.2,32.9,116,32.7,115.9,32.6,115.7,32.5,112.3,30,112.1,29.9,111.9,29.7,111.7,29.6,108.2,27.6,104.3,26.6,100.3,26.6,100.3,26.6,96.3,26.6,92.4,27.7,88.9,29.6,88.7,29.7,88.5,29.9,88.3,30,84.9,32.6],operators=[0,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,1,2,2,1,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[85.9,98.3,87,101.8,88.2,105.4,89.3,108.9,89.5,109.6,90.5,109.8,90.9,109.2,92.8,106.6,94.6,104.1,96.5,101.5,96.9,101,96.6,100.3,96,100.1,87,97.2,86.4,96.9,85.7,97.6,85.9,98.3],operators=[0,2,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[97.4,96.5,98,96.7,98.6,96.3,98.6,95.6,98.6,92.4,98.6,89.3,98.6,86.1,98.6,85.4,97.8,84.9,97.2,85.4,88.2,91.9,87.6,92.3,87.7,93.3,88.5,93.5,91.4,94.6,94.4,95.6,97.4,96.5],operators=[0,2,2,2,1,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[103.5,96.5,112.5,93.6,113.2,93.4,113.4,92.4,112.8,92,109.8,89.8,106.8,87.6,103.8,85.5,103.2,85.1,102.4,85.5,102.3,86.2,102.3,89.4,102.3,92.5,102.3,95.7,102.3,96.3,102.9,96.7,103.5,96.5],operators=[0,1,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[150.6,148,152.6,141.8,152.8,139.4,152.6,137.1,152,134.7,151.9,134.3,150.9,130.4,148.3,126.6,145.9,123.1,139.4,118.4,130.3,113.4,129.9,113.2,129.6,113,129.2,112.9,115.6,108.5,115.5,108.5,115.4,108.5,115.4,108.6,115.1,109.4,114,112.9,113.4,114.7,113,115.8,112.5,116.6,111.2,116.7,108.9,116.8,106.6,116.8,104.3,116.8,104.2,116.8,104.1,116.9,104.1,117,104.1,132.6,104.1,133,104.1,133.5,104.2,133.9,106.1,143.4,108.5,150.5,111,153.8,113.3,156.8,116.1,160.4,122.7,162.2,131.1,162.2,140,162.2,147.9,156.5,150.6,148],operators=[0,1,2,2,2,2,1,2,2,2,2,2,1,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[170.5,84.3,170.5,81.9,170.2,79.4,169.4,77.1,168.1,73,165.6,69.4,162.4,66.6,162.3,66.5,162.2,66.4,160.1,64.8,160,64.7,159.9,64.6,159.8,64.5,159.4,64.3,159,64,158.6,63.8,155.7,62.3,152.7,61.3,149.5,61.1,149.4,61.1,148.9,61.1,148.2,61.1,146.4,61.1,143.6,61.3,140.6,62.2,138.1,63,134.6,65.1,130.6,68.2,126,71.8,121.9,76.1,118.5,80.8,114.5,86.3,113.9,87.1,114.1,88.3,114.9,88.9,115.7,89.5,116.5,90,117.3,90.6,118.2,91.2,119.8,92.1,120.1,93.3,120.2,93.8,120,94.2,119.9,94.7,119.4,96.3,118.9,97.8,118.4,99.4,118.1,100.4,118.6,101.4,119.6,101.7,126.6,104,132.4,105.9,138.5,107,144.6,107.1,145.1,107.1,145.6,107.1,146.1,107.1,150,107.1,152.9,106.7,155,106,158.9,104.6,163.8,102.9,167.7,95.7,169.8,89.1,170.1,87.6,170.4,86,170.5,84.3],operators=[0,2,2,1,1,1,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[166.5,60.4,166.5,60.4,116.7,24.2,106.9,17.1,93.8,17.1,84,24.2,34,60.4,24.2,67.5,20.2,80,23.9,91.4,42.9,150.2,46.6,161.7,57.3,169.5,69.4,169.5,131.1,169.5,143.2,169.5,153.8,161.8,157.6,150.2,176.6,91.3,180.3,80,176.2,67.5,166.5,60.4,169.6,89.2,167.5,95.8,163.5,103,158.7,104.7,154.8,106.1,152.7,106.8,149.8,107.2,145.9,107.2,145.4,107.2,144.9,107.2,144.4,107.2,138.3,107.1,132.3,106,126.4,104.1,119.4,101.8,118.4,101.5,117.9,100.4,118.2,99.5,118.7,97.9,119.2,96.4,119.7,94.8,119.8,94.3,120,93.9,119.9,93.4,119.7,92.2,118,91.4,117.1,90.7,116.3,90.1,115.5,89.6,114.7,89,113.9,88.4,113.7,87.2,114.3,86.4,118.3,80.9,121.7,76.2,125.8,71.9,130.4,68.3,134.5,65.1,137.9,63,140.4,62.3,143.4,61.4,146.2,61.2,148,61.2,148.7,61.2,149.2,61.2,149.3,61.2,152.5,61.5,155.6,62.4,158.4,63.9,158.9,64.1,159.2,64.4,159.6,64.6,159.7,64.7,159.8,64.8,159.9,64.9,162,66.5,162.1,66.6,162.2,66.7,165.5,69.5,167.9,73.1,169.2,77.2,170,79.6,170.3,82,170.3,84.4,170.4,86,170.1,87.6,169.6,89.2,50.5,148,50.4,147.9,50.4,147.8,49.6,145.3,49.6,145.2,49.6,145.1,49.6,144.9,49.5,144.5,49.4,144,49.3,143.5,47.6,134.2,50.7,129.6,53.2,126,54.9,123.5,58.6,120.5,63.7,117.2,68.2,114.3,73.1,112,78.3,110.3,84,108.5,85,108.2,86,108.7,86.3,109.7,86.8,111.4,87.6,113.7,88,114.7,88.6,116.1,89.7,116.1,90.9,116.1,95.1,116.1,96.1,116.1,96.9,116.9,96.9,117.9,96.9,125.6,96.9,132.3,95.9,139,93.8,145.3,92.7,148.6,91.5,151.2,90.2,152.8,87.4,156.5,84.1,158.6,83.7,158.8,81,160.5,78,161.5,74.8,162,74.3,162.1,73.8,162.1,73.4,162.1,73.2,162.1,73.1,162.1,72.2,162.1,70.3,162.1,70.2,162.1,70.1,162.1,65.9,161.8,61.8,160.3,58.3,157.8,54.7,155.4,52.1,152,50.5,148,38.3,101.7,38.3,101.7,35.9,99.7,34,97.2,32.6,94.4,30.9,89.3,30.7,88.8,30.6,88.2,30.5,87.7,30,84.2,30.2,80.5,31.4,77.1,32.7,73,35.2,69.4,38.4,66.6,38.5,66.5,38.6,66.4,40.7,64.8,40.8,64.7,40.9,64.6,41,64.5,41.4,64.3,41.8,64,42.2,63.8,45.9,61.8,49.4,60.8,52.8,60.8,55.7,60.8,58.1,61.5,60.2,62.1,62.4,62.8,65.3,64.4,68.6,66.9,73.7,70.7,78.1,75.3,81.8,80.4,86.1,86.3,86.7,87.1,86.5,88.3,85.7,88.9,84.2,90,82.1,91.5,81.3,92.1,80.1,93.1,80.7,94.4,81.1,95.6,81.5,96.8,81.9,98.1,82.3,99.3,82.6,100.3,82.1,101.3,81.1,101.6,74.2,103.9,68.4,105.8,62.4,106.9,56.3,107,55.8,107,55.3,107,54.8,107,50.9,107,48,106.6,45.9,105.9,42.1,104.7,39.2,102.5,38.3,101.7,111.7,29.8,111.9,29.9,112.1,30.1,112.3,30.2,115.7,32.7,115.9,32.8,116,33,116.2,33.1,123.1,39.7,123.2,45.2,123.4,49.7,123.5,52.3,122.6,56.2,120.9,60.9,118.9,66.4,116.1,71.6,112.6,76.4,108.5,82.1,107.9,82.9,106.7,83.1,105.9,82.5,104.3,81.3,102,79.6,101.3,79.2,99.9,78.6,98.7,79.9,97.6,80.6,96.7,81.2,95.9,81.8,95,82.5,94.2,83.2,93,83,92.3,82.2,88.1,76.5,84.6,71.7,81.8,66.5,79.8,61,78.1,56.3,77.2,52.4,77.3,49.8,77.4,45.2,78.9,41.5,79,41.1,80.2,38.1,82,35.5,84.4,33.2,84.6,33,84.7,32.9,84.9,32.8,88.3,30.3,88.5,30.2,88.7,30,88.9,29.9,92.4,27.9,96.3,26.9,100.3,26.9,100.3,26.9,104.3,26.7,108.2,27.8,111.7,29.8,96.1,100,96.7,100.2,96.9,100.9,96.6,101.4,94.7,104,92.9,106.5,91,109.1,90.6,109.7,89.6,109.6,89.4,108.8,88.3,105.3,87.1,101.7,86,98.2,85.8,97.5,86.4,96.8,87.2,97,96.1,100,88.2,92,97.2,85.5,97.8,85.1,98.7,85.5,98.6,86.2,98.6,89.4,98.6,92.5,98.6,95.7,98.6,96.3,98,96.8,97.4,96.6,94.4,95.6,91.4,94.7,88.4,93.7,87.7,93.4,87.6,92.4,88.2,92,94,111,95.9,108.4,97.7,105.9,99.6,103.3,100,102.8,100.7,102.8,101.1,103.3,103,105.9,104.8,108.4,106.7,111,107.1,111.6,106.7,112.5,106,112.5,94.7,112.5,94,112.4,93.5,111.6,94,111,102.3,95.7,102.3,92.5,102.3,89.4,102.3,86.2,102.3,85.5,103.1,85,103.8,85.5,106.8,87.7,109.8,89.9,112.8,92,113.4,92.4,113.3,93.4,112.5,93.6,103.5,96.5,102.9,96.7,102.3,96.3,102.3,95.7,104,101.4,103.6,100.9,103.9,100.2,104.5,100,107.5,99,110.5,98.1,113.5,97.1,114.2,96.9,114.9,97.5,114.7,98.3,113.6,101.8,112.4,105.4,111.3,108.9,111.1,109.6,110.1,109.8,109.7,109.2,107.7,106.5,105.8,104,104,101.4,152.6,141.8,150.6,148,147.9,156.5,140.1,162.2,131.2,162.2,122.8,162.2,116.2,160.4,113.4,156.8,111.1,153.8,108.6,150.5,106.3,143.4,104.3,133.9,104.2,133.5,104.2,133,104.2,132.6,104.2,117,104.2,116.9,104.3,116.8,104.4,116.8,106.7,116.8,109,116.8,111.3,116.7,112.6,116.6,113.1,115.9,113.5,114.7,114.1,112.9,115.2,109.5,115.5,108.6,115.5,108.5,115.6,108.5,115.7,108.5,129.3,112.9,129.7,113,130.1,113.2,130.4,113.4,139.5,118.4,145.9,123.1,148.4,126.6,151,130.4,152,134.3,152.1,134.7,152.6,137.1,152.8,139.5,152.6,141.8],operators=[0,1,1,2,1,2,1,2,1,2,1,2,3,0,1,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,3,0,1,1,1,1,1,1,2,2,2,2,1,2,2,2,1,2,1,2,2,2,2,2,1,1,1,1,1,1,2,2,3,0,1,2,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,3,0,2,1,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,3,0,2,2,2,2,2,1,3,0,1,2,2,2,2,2,3,0,2,2,2,2,1,2,3,0,2,2,2,2,1,2,3,0,2,2,2,2,2,2,3,0,1,2,1,2,2,2,1,2,2,2,2,2,1,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))


        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class PendingSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[114.3,54.5,114.3,52.7,112.8,51.2,111,51.2,89.5,51.2,87.7,51.2,86.2,52.7,86.2,54.5,86.2,78.4,114.2,78.4,114.2,54.5],operators=[0,2,1,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[137.3,86.1,134.2,85.6,134.2,47.5,134.2,38.6,126.9,31.3,118,31.3,82.5,31.3,73.6,31.3,66.3,38.6,66.3,47.5,66.3,85.7,63.2,86.2,54.3,87.7,47.9,95.4,47.9,104.5,47.9,142,47.9,152.2,56.2,160.5,66.4,160.5,134.3,160.5,144.5,160.5,152.8,152.2,152.8,142,152.8,104.4,152.8,95.2,146.3,87.5,137.3,86.1,104.9,152.4,103.3,153.8,101.1,154.4,98.4,154.4,95.8,154.4,93.6,153.7,92,152.4,90.4,151,89.5,149.1,89.5,146.4,89.5,143.8,90.3,141.9,92,140.5,93.6,139.1,95.8,138.5,98.4,138.5,101.1,138.5,103.3,139.2,104.9,140.5,106.5,141.9,107.4,143.8,107.4,146.4,107.3,149.1,106.5,151.1,104.9,152.4,117,115.5,116.4,116.9,115.6,118.2,114.6,119.2,113.6,120.3,112.4,121.2,111.1,121.9,109.8,122.6,108.4,123.2,106.9,123.7,105,124.3,103.5,124.8,102.3,125.3,101.1,125.8,100.4,126.4,100.1,127.2,100.1,127.5,100.3,127.8,100.8,128.3,101.2,128.8,101.8,129.3,102.4,129.9,102.4,129.9,102.5,130,102.5,130,103.7,131,103.1,133,101.6,133.2,100,133.5,98.4,133.7,98,133.8,97.4,133.9,97,134,96.7,134,96.4,134,96,134,95.7,133.9,93.5,132.9,91.7,131.4,90.4,129.5,89,127.5,88.3,125.5,88.3,123.4,88.3,120.9,89.1,119,90.8,117.5,92.5,116,94.8,114.9,97.7,114,100,113.3,101.8,112.7,102.9,112.2,104,111.8,104.7,110.8,104.8,109.6,104.8,108,104,106.7,102.3,105.8,100.6,104.9,98.4,104.5,95.5,104.5,94,104.5,92.3,104.7,90.5,105,89.7,105.2,89,105.3,88.3,105.5,87.1,105.8,85.9,104.9,86,103.6,86.4,95.3,86.4,94.5,86.9,93.9,87.7,93.6,88.7,93.3,89.7,93,90.9,92.8,92.6,92.5,94.5,92.3,96.8,92.3,99.9,92.3,102.8,92.8,105.4,93.7,108,94.6,110.3,95.9,112.1,97.5,114,99.1,115.4,101,116.5,103.2,117.5,105.4,118.1,107.8,118.1,110.3,117.8,112.4,117.5,114.1,117,115.5,121.6,85.7,78.9,85.7,78.9,54.5,78.9,48.6,83.7,43.9,89.5,43.9,111,43.9,116.9,43.9,121.6,48.7,121.6,54.5,121.6,85.7],operators=[0,1,1,2,1,2,1,1,2,1,2,1,2,1,2,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,3,0,1,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[141.5,79.5,141.5,47.5,141.5,34.5,130.9,23.9,117.9,23.9,82.5,23.9,69.6,24,59,34.5,59,47.5,59,79.7,48.2,82.9,40.6,92.9,40.6,104.5,40.6,142,40.6,156.3,52.2,167.9,66.5,167.9,134.4,167.9,148.7,167.9,160.3,156.3,160.3,142,160.3,104.4,160.2,92.6,152.5,82.6,141.5,79.5,152.8,142,152.8,152.2,144.5,160.5,134.3,160.5,66.4,160.5,56.2,160.5,47.9,152.2,47.9,142,47.9,104.6,47.9,95.5,54.4,87.8,63.2,86.3,66.3,85.8,66.3,47.5,66.3,38.6,73.6,31.3,82.5,31.3,117.9,31.3,126.8,31.3,134.1,38.6,134.1,47.5,134.1,85.6,137.2,86.1,146.2,87.5,152.8,95.1,152.8,104.4,152.8,142],operators=[0,1,2,1,2,1,2,1,2,1,2,1,2,3,0,2,1,2,1,2,1,1,2,1,2,1,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[111,43.8,89.5,43.8,83.6,43.8,78.9,48.6,78.9,54.4,78.9,85.6,121.7,85.6,121.7,54.5,121.6,48.6,116.8,43.8,111,43.8,114.3,78.4,86.3,78.4,86.3,54.5,86.3,52.7,87.8,51.2,89.6,51.2,111,51.2,112.8,51.2,114.3,52.7,114.3,54.5,114.3,78.4],operators=[0,1,2,1,1,1,2,3,0,1,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[104.9,140.5,103.3,139.1,101.1,138.5,98.4,138.5,95.8,138.5,93.6,139.2,92,140.5,90.4,141.9,89.5,143.8,89.5,146.4,89.5,149,90.3,151,92,152.4,93.6,153.8,95.8,154.4,98.4,154.4,101.1,154.4,103.3,153.7,104.9,152.4,106.5,151,107.4,149.1,107.4,146.4,107.3,143.8,106.5,141.9,104.9,140.5],operators=[0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[111.9,97.8,110,96.2,107.8,94.9,105.2,94,102.6,93.1,99.7,92.6,96.6,92.6,94.4,92.6,92.4,92.8,90.7,93.1,89.5,93.3,88.4,93.6,87.5,93.9,86.8,94.1,86.3,94.8,86.2,95.6,85.8,103.9,85.7,105.1,86.9,106.1,88.1,105.8,88.8,105.6,89.5,105.4,90.3,105.3,92.2,104.9,93.8,104.8,95.3,104.8,98.2,104.8,100.5,105.2,102.1,106.1,103.8,107,104.6,108.2,104.6,109.9,104.6,111,103.8,112,102.7,112.5,101.5,113,99.8,113.6,97.5,114.3,94.5,115.1,92.2,116.3,90.6,117.8,88.9,119.3,88.1,121.3,88.1,123.7,88.1,125.7,88.8,127.7,90.2,129.8,91.5,131.7,93.3,133.1,95.5,134.2,95.8,134.3,96.1,134.4,96.5,134.3,96.8,134.3,97.3,134.2,97.8,134.1,98.2,134,99.8,133.8,101.4,133.5,102.9,133.3,103.5,131.3,102.3,130.3,102.3,130.3,102.2,130.2,102.2,130.2,101.6,129.7,101.1,129.1,100.6,128.6,100.2,128.1,99.9,127.7,99.9,127.5,100.2,126.7,101,126,102.1,125.6,103.3,125.1,104.8,124.6,106.7,124,108.2,123.5,109.6,122.9,110.9,122.2,112.2,121.5,113.4,120.6,114.4,119.5,115.4,118.4,116.2,117.2,116.8,115.8,117.4,114.4,117.6,112.7,117.6,110.8,117.6,108.3,117.1,105.9,116,103.7,115.2,101.3,113.7,99.4,111.9,97.8],operators=[0,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class NeutralizedSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[110.6,49.3,88.3,49.3,86.4,49.3,84.9,50.8,84.9,52.7,84.9,62.1,100.3,77.5,101,77.5,114,64.5,114,52.7,114,50.9,112.5,49.3,110.6,49.3],operators=[0,1,2,1,1,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[117.9,28.7,81.1,28.7,73.1,28.7,66.4,34.4,64.7,41.9,77.3,54.5,77.3,52.8,77.3,46.7,82.3,41.7,88.4,41.7,110.7,41.7,116.8,41.7,121.8,46.7,121.8,52.8,121.8,56.9,134.6,44,133.8,35.4,126.6,28.7,117.9,28.7],operators=[0,1,2,1,1,2,1,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[137.9,85.6,136.4,85.4,122.3,99.5,154.1,131.3,154.1,104.6,154.1,95,147.3,87,137.9,85.6],operators=[0,1,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[61.1,85.7,51.9,87.2,45.2,95.2,45.2,104.7,45.2,133.4,79,99.5,64.3,84.8,64.3,85.2,61.1,85.7],operators=[0,2,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[134.9,162.8,137.1,162.8,139.2,162.4,141.2,161.7,100.7,121.2,59.7,162.2,61.2,162.6,62.8,162.8,64.4,162.8,134.9,162.8],operators=[0,2,1,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Polygon(points=[100.7,110.3,160.2,169.9,171,159.1,111.5,99.5,170.1,40.9,159.3,30.1,100.7,88.7,41.1,29.1,30.3,40,89.8,99.5,30.3,159.1,41.1,169.9],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[161.7,138.9,161.7,104.5,161.7,92.5,154,82.3,142.9,78.9,180.9,40.9,159.2,19.2,141,37.6,137.7,28,128.6,21.1,117.9,21.1,81.1,21.1,71,21.1,62.4,27.2,58.6,35.9,41.1,18.3,19.5,40,56.7,77.2,56.7,79,45.4,82.3,37.6,92.7,37.6,104.8,37.6,141,19.5,159.1,41.2,180.8,53.7,168.3,57,169.7,60.6,170.5,64.4,170.5,134.9,170.5,139.3,170.5,143.4,169.4,147,167.6,160.2,180.8,181.9,159.1,161.7,138.9,137.9,85.6,147.3,87,154.1,95,154.1,104.6,154.1,131.3,122.3,99.5,136.4,85.4,137.9,85.6,81.1,28.7,117.8,28.7,126.5,28.7,133.7,35.4,134.5,43.9,121.6,56.8,121.6,52.7,121.6,46.6,116.6,41.6,110.5,41.6,88.3,41.6,82.2,41.6,77.2,46.6,77.2,52.7,77.2,54.4,64.7,41.9,66.4,34.4,73.1,28.7,81.1,28.7,100.3,77.5,84.9,62.1,84.9,52.7,84.9,50.8,86.4,49.3,88.3,49.3,110.6,49.3,112.5,49.3,114,50.8,114,52.7,114,64.5,101,77.5,100.3,77.5,45.2,104.7,45.2,95.2,51.9,87.3,61.1,85.7,64.3,85.2,64.3,84.8,79,99.5,45.2,133.3,45.2,104.7,134.9,162.8,64.4,162.8,62.8,162.8,61.2,162.6,59.7,162.2,100.7,121.2,141.2,161.7,139.2,162.4,137.1,162.8,134.9,162.8,100.7,110.3,41.2,169.8,30.4,159,89.9,99.5,30.3,40,41.1,29.2,100.6,88.7,159.2,30.1,170,40.9,111.4,99.5,170.9,159,160.1,169.8,100.7,110.3],operators=[0,1,2,1,1,1,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,3,0,2,1,1,1,1,3,0,1,2,1,1,2,1,2,1,1,2,3,0,1,1,2,1,2,1,1,1,3,0,2,1,1,1,1,1,3,0,1,2,1,1,2,3,0,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g



class EsotericSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        #self.transform = (1,0,0,1,0,0)
        #v0=self._nn(Group())
        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[97.4,70.4,96.7,69.8,95.6,69.8,94.9,70.4,43.7,118.1,46.8,117.7,47.8,117.6,48.7,118.3,48.8,119.3,48.8,119.3,48.9,120.3,48.2,121.2,47.2,121.3,42.5,121.9,41.6,122,41,121.5,40.6,120.9,39.2,122.2,38.4,122.9,38.4,124.2,39.2,124.9,96.6,176.9,96.7,176.8,97.3,176,98.5,175.9,99.3,176.5,99.3,176.5,99.5,176.6,99.6,176.8,99.7,177,103.1,173.9,102.6,174,102,173.9,101.5,173.6,101.5,173.6,100.7,173,100.6,171.8,101.2,171,103.5,168.1,104.1,167.3,105.3,167.2,106.1,167.8,106.1,167.8,106.9,168.4,107,169.6,106.4,170.4,104.9,172.4,157.3,125,158.1,124.3,158.1,123,157.3,122.2,97.4,70.4,58.2,120.7,54.6,120.8,53.7,120.8,52.9,120.1,52.8,119.2,52.6,117.3,52.6,117.3,52.6,117.2,52.6,117.1,52.6,117.1,52.4,114,52.3,113,53.1,112.1,54.1,112.1,54.1,112.1,55.1,112.1,55.9,112.8,56,113.8,56.1,115.3,56.2,116.3,57,117,57.9,117,58.1,117,59.1,117,59.9,117.8,59.9,118.8,60,119.9,59.2,120.7,58.2,120.7,71,118.9,71,119.9,70.2,120.7,69.2,120.7,65.5,120.7,64.5,120.7,63.7,119.9,63.7,118.9,63.7,118.9,63.7,117.9,64.5,117.1,65.5,117.1,69.2,117.1,70.1,117.1,71,117.9,71,118.9,71,118.9,82,118.9,82,119.9,81.2,120.7,80.2,120.7,76.5,120.7,75.5,120.7,74.7,119.9,74.7,118.9,74.7,118.9,74.7,117.9,75.5,117.1,76.5,117.1,80.2,117.1,81.2,117.1,82,117.9,82,118.9,82,118.9,93.1,118.9,93.1,119.9,92.3,120.7,91.3,120.7,87.6,120.7,86.6,120.7,85.8,119.9,85.8,118.9,85.8,118.9,85.8,117.9,86.6,117.1,87.6,117.1,91.3,117.1,92.3,117.1,93.1,117.9,93.1,118.9,93.1,118.9,105.1,118.9,105.1,119.9,104.3,120.7,103.3,120.7,99.6,120.7,98.6,120.7,97.8,119.9,97.8,118.9,97.8,118.9,97.8,117.9,98.6,117.1,99.6,117.1,103.3,117.1,104.2,117.1,105.1,117.9,105.1,118.9,105.1,118.9,130.9,118.9,130.9,117.9,131.7,117.1,132.7,117.1,136.4,117.1,137.4,117.1,138.2,117.9,138.2,118.9,138.2,118.9,138.2,119.9,137.4,120.7,136.4,120.7,132.7,120.7,131.7,120.7,130.9,119.9,130.9,118.9,130.9,118.9,119.8,118.9,119.8,117.9,120.6,117.1,121.6,117.1,125.3,117.1,126.3,117.1,127.1,117.9,127.1,118.9,127.1,118.9,127.1,119.9,126.3,120.7,125.3,120.7,121.6,120.7,120.6,120.7,119.8,119.9,119.8,118.9,119.8,118.9,113.3,161.8,111,164.7,110.4,165.5,109.2,165.6,108.4,165,108.4,165,107.6,164.4,107.5,163.2,108.1,162.4,110.4,159.5,111,158.7,112.2,158.6,113,159.2,113.8,159.9,113.9,161,113.3,161.8,110.6,120.7,109.6,120.7,108.8,119.9,108.8,118.9,108.8,118.9,108.8,117.9,109.6,117.1,110.6,117.1,114.3,117.1,115.3,117.1,116.1,117.9,116.1,118.9,116.1,118.9,116.1,119.9,115.3,120.7,114.3,120.7,110.6,120.7,120.1,153.1,117.8,156,117.2,156.8,116,156.9,115.2,156.3,115.2,156.3,114.4,155.7,114.3,154.5,114.9,153.7,117.2,150.8,117.8,150,119,149.9,119.8,150.5,119.8,150.5,120.6,151.2,120.8,152.3,120.1,153.1,127,144.4,124.7,147.3,124.1,148.1,122.9,148.2,122.1,147.6,122.1,147.6,121.3,147,121.2,145.8,121.8,145,124.1,142.1,124.7,141.3,125.9,141.2,126.7,141.8,127.4,142.5,127.6,143.6,127,144.4,133.8,135.7,131.5,138.6,130.9,139.4,129.7,139.5,128.9,138.9,128.1,138.3,128,137.1,128.6,136.3,130.9,133.4,131.5,132.6,132.7,132.5,133.5,133.1,133.5,133.1,134.3,133.8,134.4,134.9,133.8,135.7,140.6,127,138.3,129.9,137.7,130.7,136.5,130.8,135.7,130.2,135.7,130.2,134.9,129.6,134.8,128.4,135.4,127.6,137.7,124.7,138.3,123.9,139.5,123.8,140.3,124.4,140.3,124.4,141.1,125.1,141.2,126.2,140.6,127,146.5,118.9,146.5,119.3,146.4,119.7,146.1,120,145.2,121.2,144.6,122,143.4,122.1,142.6,121.5,141.8,120.9,141.7,119.7,142.3,118.9,142.5,118.7,142.8,118.4,142.9,118,142.9,117.6,142.9,116.1,142.9,115.1,143.7,114.3,144.7,114.3,144.7,114.3,145.7,114.3,146.5,115.1,146.5,116.1,146.5,118.9],operators=[0,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,3,0,1,2,1,1,1,1,1,1,2,1,2,1,2,1,2,2,3,0,2,1,2,1,2,1,2,1,3,0,2,1,2,1,2,1,2,1,3,0,2,1,2,1,2,1,2,1,3,0,2,1,2,1,2,1,2,1,3,0,2,1,2,1,2,1,2,1,3,0,2,1,2,1,2,1,2,1,3,0,1,2,1,2,1,2,2,3,0,2,1,2,1,2,1,2,1,3,0,1,2,1,2,1,2,1,2,3,0,1,2,1,2,1,2,2,3,0,1,2,2,1,2,1,2,3,0,1,2,1,2,1,2,1,2,3,0,2,1,2,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[64.3,39.3,98,60.8,98,60.8,98,60.8,98,60.8,98.2,60.9,98.3,61,98.4,61.1,122.8,82.2,123.8,83.1,125.3,82.6,125.8,81.4,140,38.4,140.4,37.2,139.5,36,138.2,36,65.2,36,63.4,35.9,62.7,38.4,64.3,39.3],operators=[0,1,2,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[43.7,108.2,51.7,100.8,51.7,100.7,51.6,100.5,51.6,100.4,51.4,96.7,51.4,95.7,52.1,94.8,53.2,94.8,53.2,94.8,54.2,94.8,55.1,95.5,55.1,96.6,55.1,97.6,73.3,80.7,74.1,80,73.2,78.8,72.3,79.2,54.6,87,54.7,89.5,54.7,90.5,54,91.4,52.9,91.4,52.9,91.4,51.9,91.4,51,90.7,51,89.7,42.2,107.1,41.8,108,42.9,108.8,43.7,108.2],operators=[0,1,2,1,2,1,2,1,1,2,1,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[147.5,50.6,147.4,50,147,49.6,146.5,49.3,146.4,50.2,145.6,51,144.7,51,144.4,51,144.1,50.9,143.8,50.7,131.3,88.5,131.1,89.2,131.3,90,131.8,90.5,156.3,111.7,157.6,112.9,159.7,111.7,159.3,109.9,147.5,50.6,146.5,96.6,146.5,97.6,145.7,98.4,144.7,98.4,143.7,98.4,142.9,97.6,142.9,96.6,142.9,92.4,142.9,91.4,143.7,90.6,144.7,90.6,145.7,90.6,146.5,91.4,146.5,92.4,146.5,96.6,146.5,84.8,146.5,85.8,145.7,86.6,144.7,86.6,143.7,86.6,142.9,85.8,142.9,84.8,142.9,80.6,142.9,79.6,143.7,78.8,144.7,78.8,145.7,78.8,146.5,79.6,146.5,80.6,146.5,84.8,146.5,72.9,146.5,73.9,145.7,74.7,144.7,74.7,143.7,74.7,142.9,73.9,142.9,72.9,142.9,68.7,142.9,67.7,143.7,66.9,144.7,66.9,145.7,66.9,146.5,67.7,146.5,68.7,146.5,72.9,146.5,61,146.5,62,145.7,62.8,144.7,62.8,143.7,62.8,142.9,62,142.9,61,142.9,56.8,142.9,55.8,143.7,55,144.7,55,145.7,55,146.5,55.8,146.5,56.8,146.5,61],operators=[0,2,2,2,1,2,1,2,1,3,0,2,2,1,2,2,1,3,0,2,2,1,2,2,1,3,0,2,2,1,2,2,1,3,0,2,2,1,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[54.2,78.9,84.7,65.2,86,64.6,86.2,62.8,84.9,62,54.4,42.6,53.2,41.8,51.6,42.7,51.6,44.2,51.6,77.3,51.6,78.5,53,79.4,54.2,78.9],operators=[0,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[168.2,118.2,151.8,36,150.9,31.7,147.1,28.5,142.7,28.5,53.5,28.5,48.4,28.5,44.2,32.7,44.2,37.8,44.2,85.4,28.7,116,26.8,119.7,27.7,124.3,30.8,127.1,91.6,182.2,92.5,183,93.4,183.6,94.5,184,97.9,185.3,101.6,184.5,104.2,182.2,165.4,126.8,167.7,124.8,168.8,121.4,168.2,118.2,65.2,35.9,138.2,35.9,139.5,35.9,140.3,37.1,140,38.3,125.8,81.4,125.4,82.7,123.8,83.1,122.8,82.2,98.5,61.1,98.4,61,98.2,60.9,98.1,60.8,98.1,60.8,98.1,60.8,98.1,60.8,64.3,39.3,62.7,38.4,63.4,35.9,65.2,35.9,51.6,44.1,51.6,42.6,53.2,41.8,54.4,42.5,85,62,86.2,62.8,86.1,64.6,84.8,65.2,54.2,78.9,53,79.4,51.6,78.6,51.6,77.2,51.6,44.1,42.2,107.1,51,89.7,51.1,90.7,51.9,91.5,52.9,91.4,52.9,91.4,53.9,91.4,54.7,90.5,54.7,89.5,54.6,87,72.3,79,73.2,78.6,74,79.8,73.3,80.5,55.1,97.5,55.1,96.5,55.1,95.5,54.2,94.7,53.2,94.7,53.2,94.7,52.2,94.7,51.4,95.6,51.4,96.6,51.6,100.3,51.6,100.4,51.6,100.6,51.7,100.7,43.7,108.1,42.9,108.8,41.8,108,42.2,107.1,157.3,125.1,104.9,172.5,106.4,170.5,107,169.7,106.9,168.5,106.1,167.9,106.1,167.9,105.3,167.3,104.1,167.4,103.5,168.2,101.2,171.1,100.6,171.9,100.7,173.1,101.5,173.7,101.5,173.7,102,174.1,102.5,174.2,103.1,174,99.7,177.1,99.6,176.9,99.4,176.7,99.3,176.6,99.3,176.6,98.5,176,97.3,176.1,96.7,176.9,96.6,177,39.2,125,38.4,124.3,38.4,123,39.2,122.3,40.6,121,40.9,121.7,41.6,122.1,42.5,122,47.2,121.4,48.2,121.3,48.9,120.4,48.8,119.4,48.8,119.4,48.7,118.4,47.8,117.7,46.8,117.8,43.7,118.2,94.9,70.5,95.6,69.9,96.7,69.8,97.4,70.5,157.3,122.4,158.1,123.1,158.1,124.4,157.3,125.1,156.3,111.8,131.8,90.6,131.2,90.1,131,89.3,131.3,88.6,143.8,50.8,144.1,51,144.4,51.1,144.7,51.1,145.7,51.1,146.4,50.4,146.5,49.4,147,49.6,147.3,50,147.5,50.7,159.4,110.1,159.7,111.7,157.7,112.9,156.3,111.8],operators=[0,1,2,1,2,1,1,2,1,2,2,1,2,3,0,1,2,1,2,1,2,2,1,2,3,0,2,1,2,1,2,1,3,0,1,2,1,2,1,1,2,1,1,2,1,2,1,2,1,2,3,0,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,1,2,1,2,3,0,1,2,1,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.7,78.7,143.7,78.7,142.9,79.5,142.9,80.5,142.9,84.7,142.9,85.7,143.7,86.5,144.7,86.5,145.7,86.5,146.5,85.7,146.5,84.7,146.5,80.5,146.5,79.5,145.7,78.7,144.7,78.7],operators=[0,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.7,66.8,143.7,66.8,142.9,67.6,142.9,68.6,142.9,72.8,142.9,73.8,143.7,74.6,144.7,74.6,145.7,74.6,146.5,73.8,146.5,72.8,146.5,68.6,146.5,67.7,145.7,66.8,144.7,66.8],operators=[0,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.7,55,143.7,55,142.9,55.8,142.9,56.8,142.9,61,142.9,62,143.7,62.8,144.7,62.8,145.7,62.8,146.5,62,146.5,61,146.5,56.8,146.5,55.8,145.7,55,144.7,55],operators=[0,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.7,90.6,143.7,90.6,142.9,91.4,142.9,92.4,142.9,96.6,142.9,97.6,143.7,98.4,144.7,98.4,145.7,98.4,146.5,97.6,146.5,96.6,146.5,92.4,146.5,91.4,145.7,90.6,144.7,90.6],operators=[0,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[144.7,114.3,144.7,114.3,143.7,114.3,142.9,115.1,142.9,116.1,142.9,117.6,142.9,118,142.8,118.4,142.5,118.7,142.3,118.9,141.7,119.7,141.8,120.9,142.6,121.5,143.4,122.1,144.6,122,145.2,121.2,146.1,120,146.4,119.7,146.5,119.3,146.5,118.9,146.5,116.1,146.5,115.1,145.7,114.3,144.7,114.3],operators=[0,1,2,1,2,1,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[113,159.3,112.2,158.7,111,158.8,110.4,159.6,108.1,162.5,107.5,163.3,107.6,164.5,108.4,165.1,108.4,165.1,109.2,165.7,110.4,165.6,111,164.8,113.3,161.9,113.9,161,113.8,159.9,113,159.3],operators=[0,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[133.5,133.1,133.5,133.1,132.7,132.5,131.5,132.6,130.9,133.4,128.6,136.3,128,137.1,128.1,138.3,128.9,138.9,129.7,139.5,130.9,139.4,131.5,138.6,133.8,135.7,134.4,134.9,134.3,133.8,133.5,133.1],operators=[0,1,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[119.8,150.6,119.8,150.6,119,150,117.8,150.1,117.2,150.9,114.9,153.8,114.3,154.6,114.4,155.8,115.2,156.4,115.2,156.4,116,157,117.2,156.9,117.8,156.1,120.1,153.2,120.8,152.3,120.6,151.2,119.8,150.6],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[140.3,124.4,140.3,124.4,139.5,123.8,138.3,123.9,137.7,124.7,135.4,127.6,134.8,128.4,134.9,129.6,135.7,130.2,135.7,130.2,136.5,130.8,137.7,130.7,138.3,129.9,140.6,127,141.2,126.2,141.1,125.1,140.3,124.4],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[126.6,141.8,125.8,141.2,124.6,141.3,124,142.1,121.7,145,121.1,145.8,121.2,147,122,147.6,122,147.6,122.8,148.2,124,148.1,124.6,147.3,126.9,144.4,127.6,143.6,127.4,142.5,126.6,141.8],operators=[0,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[80.2,117.1,76.5,117.1,75.5,117.1,74.7,117.9,74.7,118.9,74.7,118.9,74.7,119.9,75.5,120.7,76.5,120.7,80.2,120.7,81.2,120.7,82,119.9,82,118.9,82,118.9,82,117.9,81.2,117.1,80.2,117.1],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[69.1,117.1,65.4,117.1,64.4,117.1,63.6,117.9,63.6,118.9,63.6,118.9,63.6,119.9,64.4,120.7,65.4,120.7,69.1,120.7,70.1,120.7,70.9,119.9,70.9,118.9,70.9,118.9,71,117.9,70.1,117.1,69.1,117.1],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[91.2,117.1,87.5,117.1,86.5,117.1,85.7,117.9,85.7,118.9,85.7,118.9,85.7,119.9,86.5,120.7,87.5,120.7,91.2,120.7,92.2,120.7,93,119.9,93,118.9,93,118.9,93.1,117.9,92.3,117.1,91.2,117.1],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[132.7,120.7,136.4,120.7,137.4,120.7,138.2,119.9,138.2,118.9,138.2,118.9,138.2,117.9,137.4,117.1,136.4,117.1,132.7,117.1,131.7,117.1,130.9,117.9,130.9,118.9,130.9,118.9,130.9,119.9,131.7,120.7,132.7,120.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[121.7,120.7,125.4,120.7,126.4,120.7,127.2,119.9,127.2,118.9,127.2,118.9,127.2,117.9,126.4,117.1,125.4,117.1,121.7,117.1,120.7,117.1,119.9,117.9,119.9,118.9,119.9,118.9,119.8,119.9,120.6,120.7,121.7,120.7],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[103.2,117.1,99.5,117.1,98.5,117.1,97.7,117.9,97.7,118.9,97.7,118.9,97.7,119.9,98.5,120.7,99.5,120.7,103.2,120.7,104.2,120.7,105,119.9,105,118.9,105,118.9,105.1,117.9,104.2,117.1,103.2,117.1],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[116.1,118.9,116.1,118.9,116.1,117.9,115.3,117.1,114.3,117.1,110.6,117.1,109.6,117.1,108.8,117.9,108.8,118.9,108.8,118.9,108.8,119.9,109.6,120.7,110.6,120.7,114.3,120.7,115.3,120.7,116.1,119.9,116.1,118.9],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[58.1,117.1,57.9,117.1,56.9,117.1,56.1,116.4,56.1,115.4,56,113.9,55.9,112.9,55.1,112.2,54.1,112.2,54.1,112.2,53.1,112.2,52.3,113.1,52.4,114.1,52.6,117.2,52.6,117.2,52.6,117.3,52.6,117.4,52.6,117.4,52.8,119.3,52.9,120.2,53.7,120.9,54.6,120.9,58.2,120.8,59.2,120.8,60,120,60,119,60,117.9,59.1,117,58.1,117.1],operators=[0,1,2,1,2,1,2,1,1,1,1,1,1,2,1,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class ArchonSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        #self.transform = (1,0,0,1,0,0)
        #v0=self._nn(Group())
        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[66.6,89.4,66.6,94.4,67.2,99.3,68.4,104,96.4,85.5,97.9,88.9,69.4,107.7,69.4,107.7,121.1,73.6,85,45.4,73.3,57,66.6,73,66.6,89.4],operators=[0,2,1,1,1,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Polygon(points=[47.7,122,58.2,115.1,58.2,115.1],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Polygon(points=[63.8,126.8,54.8,132.8,63.8,126.8],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[103.1,101,104.6,104.4,76.5,122.9,87.5,139.9,106.6,151.2,128.3,151.2,128.7,151.2,129.1,151.2,129.5,151.2,127,85.2,74.6,119.7,74.6,119.7,103.1,101],operators=[0,1,1,2,2,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[66.6,89.4,66.6,73,73.3,57,85.1,45.4,121.2,73.6,131.9,66.6,95.7,37.4,95.6,37.2,95.7,37,95.9,36.9,98.9,35,102.1,33.4,105.4,32.1,107.9,31.1,109.2,28.2,108.3,25.7,107.4,23.1,106.7,21.1,104.7,19.7,102.6,19.7,102.6,19.7,101.9,19.7,101.3,19.8,100.7,20.1,86.9,25.6,75.1,35.1,66.7,47.6,58.1,60,53.7,74.5,53.7,89.4,53.7,97.1,54.9,104.5,57,111.5,68.3,104,67.2,99.3,66.6,94.4,66.6,89.4],operators=[0,2,1,1,1,2,2,2,1,2,1,2,2,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Polygon(points=[58.2,115.1,58.2,115.1,69.4,107.7,69.4,107.7],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Polygon(points=[74.6,119.7,74.6,119.7,63.8,126.8,63.8,126.8],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[129.6,151.1,129.2,151.1,128.8,151.1,128.4,151.1,106.7,151.1,87.6,139.8,76.6,122.8,65.7,130,79,150.5,102.1,164.1,128.3,164.1,138.8,164.1,149,162,158.5,157.7,159.8,157.1,160.8,156.1,161.2,154.8,161.7,153.5,161.6,152.1,161,150.8,159.8,148.3,159,146.6,157.2,145.4,155.2,145.4,154.5,145.4,153.8,145.5,153.2,145.8,150,147.2,146.6,148.4,143.1,149.2,143.1,149.2,143,149.2,143,149.2,142.9,149.2,142.7,149.1,142.6,148.9,138.3,77.5,127,85.2,129.6,151.1],operators=[0,2,2,1,2,2,2,2,1,2,2,2,2,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[165.1,54.1,163.5,51.7,162.6,50.3,161,49.4,159.3,49.4,158.3,49.4,157.4,49.7,156.6,50.2,131.8,66.5,121.1,73.5,69.4,107.6,58.3,114.9,47.7,122,45.6,118.8,44.8,117.6,43.5,116.9,42.1,116.9,40.5,116.9,39,117.8,38.3,119.2,29,137.6,28.3,138.9,28.4,140.5,29.2,141.7,30,143,31.3,143.7,32.8,143.7,32.9,143.7,33,143.7,33,143.7,53.6,142.5,55.1,142.4,56.5,141.5,57.1,140.2,57.8,138.9,57.7,137.2,56.9,136,54.8,132.8,63.8,126.9,74.6,119.8,127,85.2,138.4,77.7,163.6,61.1,164.7,60.4,165.5,59.2,165.8,57.9,166.1,56.6,165.8,55.3,165.1,54.1],operators=[0,1,2,2,1,1,1,1,1,1,2,2,1,2,2,2,1,2,2,1,1,1,1,1,1,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g

class ZenoSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #use the generic 'Esoteric' symbol, sincce I can't find a specialised one for Zeno
        es = EsotericSymbol()
        es.size = self.size
        es.x = self.x#+(s/2)
        es.y = self.y#+(s/2)
        g.add(es)

        #g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g

class ApollyonSymbol(_Symbol):

    _attrMap = AttrMap(
        x = AttrMapValue(isNumber,desc='symbol x coordinate'),
        y = AttrMapValue(isNumber,desc='symbol y coordinate'),
        size = AttrMapValue(isNumber),
        fillColor = AttrMapValue(isColorOrNone),
        )

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.fillColor=Color(0,0,0,1)

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        #self.transform = (1,0,0,1,0,0)
        #v0=self._nn(Group())
        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[84,128.1,83.9,126.9,84.2,125.6,85,124.6,89.8,118.8,72.6,121.3,56.9,130.2,45.9,143.9,85.9,143.9,93.2,137,85.7,131.3,84.8,130.5,84.2,129.4,84,128.1],operators=[0,2,1,2,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[106.9,118.4,100.5,126.2,108.9,132.7,110,133.5,110.6,134.8,110.7,136.1,110.8,137.5,110.2,138.8,109.2,139.7,104.8,143.8,154.1,143.8,142.2,129.2,125.6,120.3,106.9,118.4],operators=[0,1,1,2,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[166.2,138.5,153.2,121.1,134.6,109.8,113.7,106.4,112.5,108.5,109.9,113,105.2,115.7,100,115.7,94.8,115.7,90.1,113,87.5,108.5,86.3,106.4,65.4,109.8,46.8,121.1,33.8,138.5,31.2,142,30.8,146.6,32.7,150.5,34.7,154.4,38.6,156.8,42.9,156.8,156.9,156.8,161.3,156.8,165.2,154.4,167.1,150.5,169.2,146.6,168.8,142,166.2,138.5,85.9,143.9,45.9,143.9,57,130.2,72.6,121.3,89.8,118.8,85,124.6,84.2,125.6,83.8,126.8,84,128.1,84.1,129.3,84.8,130.5,85.8,131.2,93.3,136.9,85.9,143.9,104.8,143.9,109.2,139.8,110.2,138.9,110.7,137.6,110.7,136.2,110.6,134.8,110,133.6,108.9,132.8,100.5,126.3,106.9,118.5,125.6,120.3,142.2,129.3,154.1,144,104.8,144],operators=[0,2,1,2,2,1,2,2,2,1,2,2,3,0,1,2,1,2,2,1,1,3,0,1,2,2,1,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[90.7,106.6,92.6,110,96.1,112,100,112,103.9,112,107.3,110,109.3,106.6,141.8,50.3,143.7,46.9,143.7,42.9,141.8,39.6,139.9,36.2,136.4,34.2,132.5,34.2,67.5,34.2,63.6,34.2,60.2,36.2,58.2,39.6,56.3,43,56.3,47,58.2,50.3,90.7,106.6,94.2,86.8,105.8,86.8,100,96.9,94.2,86.8,85.8,72.3,71.3,47.1,128.8,47.1,114.3,72.2,113.7,73.2,112.6,73.8,111.4,73.8,88.6,73.8,87.5,73.9,86.4,73.3,85.8,72.3],operators=[0,2,2,1,2,2,1,2,2,1,3,0,1,1,1,3,0,1,1,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g



class HiemalSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,1,1,2,2,2,2,2,1,1,2,2,1,2,1,1,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,1,2,2,2,2,2,1,1,2,2,1,2,1,1,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,1,2,3,0,1,1,2,1,1,2,1,3,0,1,1,2,1,1,2,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[154.4,147.6,149.3,147.6,149.3,128.3,149.3,115.1,144.2,107.1,137.1,102.2,135.6,103.1,134,103.9,132.2,104.6,129,105.9,125.7,106.8,122.4,107.5,123.6,107.8,124.8,108.2,125.9,108.6,131.3,110.7,134.8,114,136.7,118.7,69.4,116,64.9,115.8,66.9,112.7,70,110.3,74.1,108.7,82.1,105.6,92.5,105.6,100.2,105.6,100.2,105.6,116.4,105.6,149.3,105.3,149.3,71.8,149.3,52.4,154.4,52.4,155.8,52.4,156.7,50.9,156,49.6,145.4,31.3,145,30.7,144.4,30.4,143.8,30.4,143.2,30.4,142.6,30.7,142.2,31.3,131.6,49.6,130.9,50.8,131.8,52.4,133.2,52.4,138.3,52.4,138.3,61.7,134.6,61.5,61.8,58.4,61.8,52.3,66.9,52.3,68.3,52.3,69.2,50.8,68.5,49.5,57.8,31.3,57.1,30.1,55.3,30.1,54.6,31.3,44,49.7,43.3,50.9,44.2,52.5,45.6,52.5,50.7,52.5,50.7,71.8,50.7,85,55.8,93,62.9,97.9,64.4,97,66,96.2,67.8,95.5,71,94.2,74.3,93.3,77.6,92.6,76.4,92.3,75.2,91.9,74.1,91.5,69,89.5,65.6,86.4,63.6,82,129.9,84.8,134.6,85,132.6,87.8,129.7,89.9,125.8,91.5,117.8,94.6,107.4,94.6,99.7,94.6,99.7,94.6,83.5,94.6,50.6,94.9,50.6,128.4,50.6,147.7,45.5,147.7,44.1,147.7,43.2,149.2,43.9,150.5,54.5,168.8,54.9,169.4,55.5,169.7,56.1,169.7,56.7,169.7,57.3,169.4,57.7,168.8,68.3,150.5,69,149.3,68.1,147.7,66.7,147.7,61.6,147.7,61.6,138,65.3,138.2,138.1,141.3,138.1,147.6,133,147.6,131.6,147.6,130.7,149.1,131.4,150.4,142,168.7,142.7,169.9,144.5,169.9,145.2,168.7,155.8,150.4,156.7,149.1,155.8,147.6,154.4,147.6,134.6,69,138.3,69.2,138.3,71.8,138.3,73.9,138.1,75.9,137.7,77.7,134,77.5,61.9,74.5,61.8,73.6,61.8,72.7,61.8,71.8,61.8,66,65.4,130.8,61.7,130.6,61.7,128.3,61.7,126.4,61.8,124.7,62.1,123,65.8,123.2,138.1,126.3,138.1,127,138.2,127.6,138.2,128.3,138.2,133.9,65.4,130.8],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[154.4,147.6,149.3,147.6,149.3,128.3,149.3,115.1,144.2,107.1,137.1,102.2,135.6,103.1,134,103.9,132.2,104.6,129,105.9,125.7,106.8,122.4,107.5,123.6,107.8,124.8,108.2,125.9,108.6,131.3,110.7,134.8,114,136.7,118.7,69.4,116,64.9,115.8,66.9,112.7,70,110.3,74.1,108.7,82.1,105.6,92.5,105.6,100.2,105.6,100.2,105.6,116.4,105.6,149.3,105.3,149.3,71.8,149.3,52.4,154.4,52.4,155.8,52.4,156.7,50.9,156,49.6,145.4,31.3,145,30.7,144.4,30.4,143.8,30.4,143.2,30.4,142.6,30.7,142.2,31.3,131.6,49.6,130.9,50.8,131.8,52.4,133.2,52.4,138.3,52.4,138.3,61.7,134.6,61.5,61.8,58.4,61.8,52.3,66.9,52.3,68.3,52.3,69.2,50.8,68.5,49.5,57.8,31.3,57.1,30.1,55.3,30.1,54.6,31.3,44,49.7,43.3,50.9,44.2,52.5,45.6,52.5,50.7,52.5,50.7,71.8,50.7,85,55.8,93,62.9,97.9,64.4,97,66,96.2,67.8,95.5,71,94.2,74.3,93.3,77.6,92.6,76.4,92.3,75.2,91.9,74.1,91.5,69,89.5,65.6,86.4,63.6,82,129.9,84.8,134.6,85,132.6,87.8,129.7,89.9,125.8,91.5,117.8,94.6,107.4,94.6,99.7,94.6,99.7,94.6,83.5,94.6,50.6,94.9,50.6,128.4,50.6,147.7,45.5,147.7,44.1,147.7,43.2,149.2,43.9,150.5,54.5,168.8,54.9,169.4,55.5,169.7,56.1,169.7,56.7,169.7,57.3,169.4,57.7,168.8,68.3,150.5,69,149.3,68.1,147.7,66.7,147.7,61.6,147.7,61.6,138,65.3,138.2,138.1,141.3,138.1,147.6,133,147.6,131.6,147.6,130.7,149.1,131.4,150.4,142,168.7,142.7,169.9,144.5,169.9,145.2,168.7,155.8,150.4,156.7,149.1,155.8,147.6,154.4,147.6,134.6,69,138.3,69.2,138.3,71.8,138.3,73.9,138.1,75.9,137.7,77.7,134,77.5,61.9,74.5,61.8,73.6,61.8,72.7,61.8,71.8,61.8,66,65.4,130.8,61.7,130.6,61.7,128.3,61.7,126.4,61.8,124.7,62.1,123,65.8,123.2,138.1,126.3,138.1,127,138.2,127.6,138.2,128.3,138.2,133.9,65.4,130.8],operators=[0,1,1,2,2,2,2,2,1,1,2,2,1,2,1,1,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,1,2,1,1,2,2,2,2,2,1,1,2,2,1,2,1,1,2,1,2,2,1,2,1,1,1,1,1,1,2,1,2,1,2,3,0,1,1,2,1,1,2,1,0,1,1,2,1,1,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class TiamatSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[64,56.5,66.4,55.2,69.2,54.4,72.2,54.4,100,54.4,127.8,54.4,130.8,54.4,133.6,55.2,136,56.5,143,49.4,100,49.4,57,49.4,64,56.5],operators=[0,2,1,1,2,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[49.3,113,49.3,114.2,49.7,115.5,50.5,116.4,54.8,121.8,54.8,71.8,54.8,69.2,55.4,66.7,56.4,64.5,49.2,57.2,49.2,113],operators=[0,2,1,1,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[69.9,78.2,69.5,79.6,69.2,81.1,69.2,82.7,69.2,121.6,92.5,101.3,69.9,78.2],operators=[0,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[76.8,69.6,82.1,75,83.2,75,100,75,116.8,75,117.9,75,123.2,69.6,121,68.3,118.4,67.6,115.7,67.6,100,67.6,84.3,67.6,81.6,67.7,79,68.4,76.8,69.6],operators=[0,1,1,1,1,1,1,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[63.8,126.5,63.8,126.5,63.8,126.5,63.8,126.5,63.8,126.5,63.8,79.5,63.8,77.3,64.2,75.2,65,73.2,59.7,67.8,59,69.6,58.6,71.5,58.6,73.5,58.6,126.4,81.3,154.6,94.6,154.6,94.6,113,70,134.2,63.8,126.5],operators=[0,1,1,1,1,1,2,1,2,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[67.1,59.7,72,64.7,74.6,63.1,77.7,62.1,81,62.1,100,62.1,119,62.1,122.3,62.1,125.4,63,128,64.7,132.9,59.7,130.9,58.7,128.6,58.1,126.2,58.1,100,58.1,73.8,58.1,71.4,58.1,69.1,58.7,67.1,59.7],operators=[0,1,2,1,1,2,1,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[135.1,73.2,135.9,75.2,136.3,77.3,136.3,79.5,136.3,126.4,136.3,126.4,136.3,126.4,136.3,126.4,136.3,126.4,130.1,134.1,105.6,112.8,105.6,154.4,118.9,154.4,141.6,126.2,141.6,73.4,141.6,71.4,141.2,69.5,140.5,67.7,135.1,73.2],operators=[0,2,1,1,1,1,1,1,1,1,1,1,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[145.2,71.8,145.2,121.7,149.5,116.3,150.3,115.3,150.7,114.1,150.7,112.9,150.7,57.2,143.5,64.5,144.6,66.8,145.2,69.2,145.2,71.8],operators=[0,1,1,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[130.8,82.7,130.8,81.1,130.6,79.6,130.1,78.2,107.4,101.3,130.7,121.6,130.7,82.7],operators=[0,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Polygon(points=[49.4,138.9,44,143.6,39.1,137.9,31,161.5,55.5,156.7,50.6,151.1,55.7,146.7],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Polygon(points=[169,161.5,160.9,137.9,156,143.6,150.6,138.9,144.3,146.7,149.4,151.1,144.5,156.7],strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[160.8,119.8,161.3,119.2,161.6,118.3,161.6,117.5,161.6,114.9,161.6,49.4,161.6,43.9,161.6,40.9,159.1,38.4,156.1,38.4,150.6,38.4,100,38.4,49.3,38.4,43.8,38.4,40.8,38.4,38.3,40.9,38.3,43.9,38.3,49.4,38.3,114.9,38.3,117.5,38.3,118.3,38.6,119.1,39.1,119.8,40.7,121.8,72.6,161.4,74.8,164.1,75.5,165,76.5,165.5,77.6,165.5,81.1,165.5,100,165.5,118.8,165.5,122.3,165.5,123.4,165.5,124.5,165,125.1,164.1,127.3,161.4,159.2,121.8,160.8,119.8,54.8,71.8,54.8,121.7,50.5,116.3,49.7,115.3,49.3,114.1,49.3,112.9,49.3,57.2,56.5,64.5,55.4,66.8,54.8,69.2,54.8,71.8,94.5,154.5,81.2,154.5,58.5,126.3,58.5,73.4,58.5,71.4,58.9,69.5,59.6,67.7,64.9,73.1,64.1,75.1,63.7,77.2,63.7,79.4,63.7,126.3,63.7,126.3,63.7,126.3,63.7,126.3,63.7,126.3,69.9,134,94.4,112.7,94.4,154.5,128,64.7,125.4,63.1,122.3,62.1,119,62.1,100,62.1,81,62.1,77.7,62.1,74.6,63,72,64.7,67.1,59.7,69.1,58.7,71.4,58.1,73.8,58.1,100,58.1,126.2,58.1,128.6,58.1,130.9,58.7,132.9,59.7,128,64.7,130.8,82.7,130.8,121.6,107.5,101.3,130.2,78.2,130.5,79.7,130.8,81.2,130.8,82.7,92.6,101.4,69.3,121.7,69.3,82.7,69.3,81.1,69.5,79.6,70,78.2,92.6,101.4,83.2,75,82.1,75,76.8,69.6,79,68.3,81.6,67.6,84.3,67.6,100,67.6,115.7,67.6,118.4,67.6,121,68.3,123.2,69.6,117.9,75,116.8,75,100,75,83.2,75,141.5,126.3,118.8,154.5,105.5,154.5,105.5,112.9,130,134.2,136.2,126.5,136.2,126.5,136.2,126.5,136.2,126.5,136.2,126.5,136.2,79.5,136.2,77.3,135.8,75.2,135,73.2,140.3,67.8,141,69.6,141.4,71.5,141.4,73.5,141.4,126.3,136,56.5,133.6,55.2,130.8,54.4,127.8,54.4,100,54.4,72.2,54.4,69.2,54.4,66.4,55.2,64,56.5,57,49.4,100,49.4,143,49.4,136,56.5,150.7,113,150.7,114.2,150.3,115.5,149.5,116.4,145.2,121.8,145.2,71.8,145.2,69.2,144.6,66.7,143.6,64.5,150.8,57.2,150.8,113],operators=[0,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,3,0,1,1,2,1,1,2,3,0,1,1,1,2,1,2,1,1,1,1,1,1,1,1,3,0,2,1,1,2,1,2,1,1,2,1,3,0,1,1,1,2,3,0,1,1,2,1,3,0,1,1,2,1,1,2,1,1,1,1,3,0,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,0,2,1,1,2,1,1,1,1,3,0,2,1,1,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class TiconderogaSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[84.5,131.5,88.5,123.1,87.4,115.3,86.1,106.3,85,98.3,83.7,89.4,86,79.2,88.3,68.7,94.1,58.8,103.2,49.7,87.5,55.7,77.9,63.4,74.5,73,71.4,81.7,73.4,92.1,75.5,103,77.9,115.2,80.4,128.7,76.3,142.2,79.9,139,82.6,135.4,84.5,131.5],operators=[0,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[121.2,82.6,117.8,75.7,114.3,68.6,115.1,57.9,115.2,56.3,115.4,54.7,115.7,53.1,105.3,61.9,98.9,71.5,96.7,81.6,94.9,89.8,95.9,97,97,104.7,98.4,114.6,99.9,124.8,94.4,136.3,90.9,143.6,85.3,149.9,77.7,155,88.2,155.5,102.1,153.7,112.8,143.6,126.5,130.7,129.5,110.2,126.5,96.6,125.4,91.1,123.4,87,121.2,82.6],operators=[0,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[131.1,77.7,128,71.4,125.6,66.4,126.1,58.7,126.6,52.4,128.9,46.2,133,40.2,138.1,32.8,139,31.4,137.8,29.6,136.2,30,127.4,31.7,91.2,38.7,70.5,51,64,69.3,59.9,80.8,62.3,93.2,64.6,105.1,67.5,120,70.2,134,61.8,147.2,60.3,149.6,58.5,151.8,56.5,153.8,52.2,158.1,51.2,159.1,51.6,160.7,52.9,161.2,58.6,163,59.3,163.2,68.5,166.1,80.6,166.1,92.8,166.1,108,163.2,120.3,151.6,137.3,135.7,141,111.3,137.3,94.2,135.9,87.5,133.4,82.3,131.1,77.7,74.5,73,77.9,63.5,87.5,55.7,103.2,49.7,94.1,58.8,88.3,68.7,86,79.2,83.7,89.4,85,98.4,86.2,106.3,87.5,115.3,88.6,123.1,84.6,131.5,82.7,135.5,79.9,139,76.3,142.2,80.5,128.8,77.9,115.3,75.5,103,73.4,92.1,71.4,81.7,74.5,73,112.9,143.6,102.2,153.7,88.3,155.5,77.8,155,85.4,149.9,91,143.6,94.5,136.3,100,124.8,98.5,114.6,97.1,104.7,96,97,94.9,89.8,96.8,81.6,99.1,71.5,105.5,61.9,115.8,53.1,115.5,54.7,115.3,56.3,115.2,57.9,114.4,68.7,117.9,75.8,121.3,82.6,123.5,87,125.5,91.1,126.7,96.6,129.6,110.2,126.6,130.7,112.9,143.6],operators=[0,2,2,1,2,1,2,2,2,2,1,2,1,2,2,2,2,3,0,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[49.7,98.9,47.7,95.8,45.4,92.8,42.7,90.1,45.5,85.8,46.3,84.6,45.5,83,44.1,83,22.9,81.8,21.5,81.7,20.5,83.2,21.2,84.5,30.8,103.4,31.4,104.7,33.2,104.8,34,103.6,36.5,99.7,37.9,101.3,39.3,103.1,40.4,104.9,50,119.9,48.2,130.6,45.1,136.9,43.3,140.4,40.7,143.6,37.2,146.4,36.4,147,36.3,148.1,36.9,148.9,41.3,154.9,41.9,155.8,43.1,155.9,44,155.2,48.8,151.4,52.5,146.9,55.1,141.8,59.4,132.9,62.1,118.3,49.7,98.9],operators=[0,2,1,2,1,2,1,2,1,2,2,2,2,1,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[180.6,100.4,167.4,83.8,166.5,82.7,164.8,83,164.2,84.3,162.5,88.6,160.8,87.3,159.2,85.9,157.7,84.4,145.3,71.6,144.9,60.8,146.7,54,147.7,50.2,149.7,46.5,152.5,43,153.1,42.2,153,41.1,152.3,40.5,146.8,35.6,146,34.9,144.8,35,144.1,35.8,140.1,40.5,137.4,45.7,135.9,51.2,133.3,60.8,133.6,75.7,149.6,92.2,152.2,94.9,155.1,97.2,158.2,99.3,156.3,104.1,155.8,105.4,156.9,106.8,158.3,106.6,179.3,103.5,180.8,103.2,181.5,101.5,180.6,100.4],operators=[0,1,2,1,2,2,2,2,1,2,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class GevurahSymbol(_Symbol):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[2647,4794,2643,4790,2640,4671,2640,4529,2640,4271,2590,4268,2541,4265,2633,4103,2683,4014,2728,3941,2731,3940,2736,3940,2920,4254,2920,4265,2920,4268,2900,4270,2875,4270,2830,4270,2828,4533,2825,4795,2740,4798,2693,4799,2651,4798,2647,4794],operators=[0,2,1,1,1,1,2,2,2,1,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[1080,4403,1039,4384,1004,4367,1002,4365,1000,4364,1049,4255,1109,4125,1170,3994,1220,3887,1220,3885,1220,3884,1202,3875,1180,3865,1158,3855,1140,3843,1140,3839,1140,3824,1445,3619,1447,3632,1454,3673,1480,3994,1476,3997,1474,4000,1458,3994,1441,3986,1425,3977,1405,3970,1398,3970,1391,3970,1336,4076,1276,4205,1217,4334,1165,4440,1161,4439,1158,4439,1121,4423,1080,4403],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[4277,4328,4259,4288,4208,4180,4165,4088,4087,3921,4048,3941,4026,3952,4006,3959,4003,3956,3997,3950,4019,3647,4029,3609,4035,3582,4036,3583,4187,3689,4271,3747,4340,3798,4340,3801,4340,3805,4322,3815,4300,3824,4278,3833,4260,3843,4260,3846,4260,3849,4308,3954,4366,4078,4424,4203,4472,4309,4473,4314,4475,4322,4337,4398,4318,4399,4314,4400,4295,4367,4277,4328],operators=[0,2,1,1,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2530,3839,2240,3814,1944,3733,1711,3616,1537,3528,1335,3362,1230,3220,1168,3137,1106,3006,1084,2914,1059,2812,1061,2645,1088,2548,1116,2448,1151,2371,1202,2296,1420,1975,1807,1755,2320,1663,2452,1639,2489,1636,2730,1636,3012,1635,3095,1643,3315,1695,3840,1819,4247,2125,4373,2491,4439,2682,4422,2908,4328,3093,4216,3315,3949,3544,3661,3665,3474,3744,3247,3804,3042,3829,2917,3845,2649,3850,2530,3839,3096,3646,3350,3609,3564,3548,3748,3460,4028,3326,4215,3145,4301,2925,4321,2874,4324,2847,4324,2745,4324,2610,4311,2565,4237,2435,4187,2347,4053,2213,3945,2141,3522,1862,2866,1755,2260,1866,1967,1920,1747,2003,1545,2138,1383,2245,1284,2351,1211,2497,1094,2731,1150,2989,1365,3205,1469,3309,1570,3379,1725,3455,1952,3565,2246,3639,2555,3664,2652,3672,2996,3660,3096,3646],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2615,3551,2391,3515,2185,3380,2056,3186,2005,3109,1973,3032,1948,2931,1919,2808,1926,2610,1964,2495,2051,2229,2272,2018,2535,1949,2650,1919,2834,1919,2950,1949,3090,1986,3199,2049,3311,2160,3497,2344,3570,2533,3557,2790,3545,3023,3452,3208,3267,3368,3188,3436,3052,3509,2955,3535,2886,3553,2688,3563,2615,3551,2922,3310,2988,3290,3108,3223,3124,3198,3130,3187,3108,3141,3042,3027,2951,2870,3135,2870,3266,2870,3321,2867,3326,2858,3330,2852,3335,2812,3338,2771,3349,2571,3253,2374,3088,2257,3027,2214,2960,2180,2936,2180,2929,2180,2883,2250,2834,2335,2786,2420,2742,2489,2737,2487,2732,2486,2689,2416,2641,2333,2594,2249,2550,2181,2544,2180,2538,2180,2504,2194,2469,2212,2381,2256,2256,2382,2213,2471,2171,2555,2150,2646,2150,2740,2150,2870,2133,2859,2345,2862,2528,2865,2438,3020,2372,3134,2350,3179,2357,3190,2387,3238,2561,3321,2660,3334,2725,3342,2857,3330,2922,3310],operators=[0,2,2,2,2,2,2,2,2,2,2,3,0,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2673,2904,2608,2871,2560,2802,2560,2739,2560,2693,2596,2624,2637,2593,2689,2553,2774,2549,2832,2583,2895,2619,2923,2675,2918,2750,2913,2821,2881,2868,2817,2899,2766,2924,2717,2925,2673,2904],operators=[0,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[1293,1752,1209,1693,1141,1642,1140,1639,1140,1636,1158,1625,1180,1615,1202,1605,1220,1596,1220,1595,1220,1594,1171,1486,1110,1356,1050,1226,1000,1118,1000,1116,1000,1113,1156,1040,1163,1040,1165,1040,1216,1145,1275,1273,1335,1400,1385,1507,1387,1509,1388,1511,1408,1505,1431,1496,1454,1487,1475,1481,1477,1484,1481,1488,1451,1852,1447,1856,1446,1857,1377,1810,1293,1752],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[4027,1813,4016,1740,3997,1489,4003,1484,4006,1481,4022,1486,4039,1494,4055,1503,4073,1510,4078,1510,4083,1510,4136,1405,4195,1278,4255,1150,4305,1043,4307,1041,4312,1034,4462,1104,4467,1116,4469,1122,4424,1230,4366,1354,4308,1479,4260,1585,4260,1589,4260,1593,4278,1605,4300,1615,4322,1625,4337,1637,4334,1641,4332,1646,4279,1684,4217,1726,4155,1769,4092,1814,4077,1827,4039,1858,4034,1856,4027,1813],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2642,1411,2591,1324,2550,1248,2550,1241,2550,1235,2568,1230,2595,1230,2640,1230,2640,970,2640,710,2735,710,2830,710,2830,970,2830,1230,2875,1230,2900,1230,2920,1234,2920,1239,2920,1246,2750,1548,2735,1567,2735,1569,2692,1498,2642,1411],operators=[0,2,2,1,1,1,1,1,1,1,1,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (.001,0,0,-0.001,0,0)
        #g.transform = (0.035,0,0,0.035,self.x+(s/25.0), self.y+(s/20.0))
        g.transform = (0.035,0,0,0.035,self.x+(s/50.0), self.y+(s/50.0))

        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class EnochianSymbol(_Symbol):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(Path(points=[812,1650,715,1624,667,1602,593,1547,490,1471,416,1362,385,1243,367,1176,365,1043,381,968,416,801,551,651,721,589,777,568,780,566,780,534,780,500,627,500,544,500,460,504,441,510,395,523,362,556,354,597,344,652,320,639,320,578,320,525,233,476,135,420,134,427,247,365,308,330,585,330,861,330,855,412,840,630,843,615,799,636,701,680,632,789,605,944,576,1113,593,1261,657,1382,840,1731,1292,1662,1397,1267,1409,1225,1414,1165,1414,1080,1414,844,1351,707,1212,636,1163,611,1156,508,1152,451,1146,388,1143,367,1137,330,1414,330,1691,330,1770,376,1814,401,1850,423,1850,425,1850,427,1812,450,1765,477,1681,525,1680,578,1680,639,1656,652,1646,597,1638,556,1605,523,1559,510,1540,504,1456,500,1373,500,1208,500,1209,500,1230,554,1235,568,1246,580,1253,580,1283,580,1411,653,1461,698,1577,802,1634,935,1634,1105,1634,1274,1584,1396,1471,1503,1343,1623,1211,1670,1006,1669,921,1669,864,1663,812,1650],operators=[0,2,2,2,2,2,1,1,2,2,2,1,1,2,1,1,1,1,2,2,2,2,2,2,1,1,2,1,1,1,1,2,2,1,1,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[853,1005,931,871,997,761,1000,761,1003,761,1069,871,1147,1005,1288,1250,1000,1250,712,1250,853,1005,1200,1194,1200,1184,1006,850,1000,850,994,850,800,1184,800,1194,800,1197,890,1200,1000,1200,1110,1200,1200,1197,1200,1194],operators=[0,2,2,1,1,1,1,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.transform = (.001,0,0,-0.001,0,0)

        g.transform = (0.085,0,0,0.085,self.x+(s/15.0), self.y+(s/8.0))
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class CernnunosSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)

        g.add(Path(points=[133.95,65.87,69.65,1.57,46.11,89.41,22.57,177.25,110.41,153.71,198.25,130.17,133.95,65.87,179.39,125.12,143.13,134.84,124.94,90.52,111.12,56.84,127.05,72.77,179.39,125.12,78.41,86.87,104.14,53.56,115.4,80.99,92.98,86.36,75.6,90.52,78.41,86.87,114.17,84.63,108.19,104.78,102.21,124.93,87.75,109.68,73.29,94.42,93.73,89.53,114.17,84.63,85.39,111.91,99.16,126.44,94.39,125.8,52.68,120.17,70.88,96.61,85.39,111.91,104.92,127.22,111.31,105.7,117.28,85.58,120.12,92.49,136.1,131.42,104.92,127.22,74.7,20.43,102.04,47.77,74.29,83.69,67.52,92.46,67.05,92.57,67.26,92.79,48.96,116.48,55.54,91.94,74.7,20.43,107.89,144.28,36.38,163.44,46.78,124.63,93.7,130.96,136.19,136.69,107.89,144.28],operators=[0,1,1,1,1,1,1,3,0,1,1,1,1,1,3,0,1,1,1,1,1,3,0,1,1,1,1,1,1,3,0,1,1,1,1,1,3,0,1,1,1,1,1,3,0,1,1,1,1,1,1,1,1,3,0,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[93.26,104.34,95.29,106.37,98.59,106.37,100.62,104.34,102.65,102.31,102.65,99.01,100.62,96.98,98.59,94.95,95.29,94.95,93.26,96.98,91.23,99.01,91.23,102.31,93.26,104.34,99.24,98.36,100.51,99.63,100.51,101.69,99.24,102.96,97.97,104.23,95.91,104.23,94.64,102.96,93.37,101.69,93.37,99.63,94.64,98.36,95.91,97.09,97.97,97.09,99.24,98.36],operators=[0,2,2,2,2,3,0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


#from http://www.scpwiki.com/itsdenalis-personnel-file
class GodelSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (0.1,0,0,-0.1,0,200)

        g.add(Path(points=[225.4,41.7,104.2,100,87.4,108.1,75.1,123.4,71,141.7,41,272.8,36.8,291,41.2,310.1,52.9,324.7,136.7,430,148.4,444.6,166,453.1,184.7,453.1,319.2,453.1,337.9,453.1,355.6,444.6,367.2,430,451.1,324.8,462.8,310.2,467.1,291.1,463,272.9,433.1,141.7,428.9,123.5,416.7,108.2,399.9,100,278.6,41.7,261.8,33.5,242.2,33.5,225.4,41.7],operators=[0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=20,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=1,fillOpacity=1,strokeColor=Color(0,0,0,1),strokeLineCap=1,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[269,440.8,426.2,326.6,436.4,319.2,440.6,306.2,436.7,294.2,376.6,109.3,372.7,97.4,361.6,89.3,349.1,89.3,154.8,89.3,142.3,89.3,131.1,97.4,127.3,109.3,67.2,294.1,63.3,306,67.6,319.1,77.7,326.5,235,440.8,245.1,448.1,258.9,448.1,269,440.8],operators=[0,1,2,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=20,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=Color(0,0,0,1),strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[239.8,110.3,116.5,323.9,111.1,333.3,117.9,345,128.7,345,375.3,345,386.1,345,392.9,333.3,387.5,323.9,264.2,110.3,258.8,100.9,245.2,100.9,239.8,110.3],operators=[0,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=20,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=1,fillOpacity=1,strokeColor=Color(0,0,0,1),strokeLineCap=1,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[252,182.6,209.7,182.6,175.5,217,175.5,259.4,175.5,301.8,209.8,336.2,252,336.2,294.2,336.2,328.5,301.8,328.5,259.4,328.5,217,294.3,182.6,252,182.6,192.8,288.7,185,289.3,179.7,267.5,184.7,245,193.5,205.5,250.4,180.5,260.7,195.5,272.7,212.8,214.7,287,192.8,288.7],operators=[0,2,2,2,2,3,0,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[265.6,458.9,238.4,458.9,231.8,458.9,226.4,453.5,226.4,446.9,226.4,332.9,226.4,326.3,231.8,320.9,238.4,320.9,265.6,320.9,272.2,320.9,277.6,326.3,277.6,332.9,277.6,446.9,277.6,453.5,272.2,458.9,265.6,458.9],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[436.6,143,439.7,166.2,443,171.9,441,179.3,435.3,182.6,315.6,253.4,309.9,256.7,302.5,254.7,299.2,249,285.6,225.5,282.3,219.8,284.3,212.4,290,209.1,425.4,130.9,431.1,127.6,433.3,137.3,436.6,143],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[66.3,141.5,63.2,164.7,59.9,170.4,61.9,177.8,67.6,181.1,179.5,249.5,180.9,250.7,184,237.9,187.3,232.2,201.3,209.1,204.6,203.4,221.4,201.7,215.7,198.4,77.5,129.4,71.8,126.1,69.6,135.8,66.3,141.5],operators=[0,1,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (1,0,0,-1,self.x+(s/12.5), self.y+s-(s/12.5))
        g.scale(float(float(s)/float(600)), float(float(s)/float(600)))
#        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g



#from http://www.scpwiki.com/itsdenalis-personnel-file
class HeraSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (.1,0,0,-0.1,0,500)
        g.add(Path(points=[1633,4355,1432,4262,1220,4111,1054,3946,453,3345,287,2447,632,1664,819,1239,1173,873,1594,665,1687,620,1715,610,1759,610,1822,610,1860,628,1897,677,1925,713,1928,1172,1931,1630,2500,1630,3069,1630,3072,1172,3075,713,3103,677,3182,573,3283,587,3534,734,4035,1029,4390,1526,4505,2094,4689,3003,4243,3915,3410,4332,3313,4381,3287,4390,3242,4390,3178,4390,3140,4372,3103,4323,3075,4287,3072,3828,3069,3370,2500,3370,1931,3370,1928,3828,1925,4287,1897,4323,1838,4401,1753,4411,1633,4355,1590,3655,1590,3370,1315,3370,1164,3370,1040,3372,1040,3375,1040,3404,1201,3610,1302,3711,1371,3779,1570,3940,1585,3940,1588,3940,1590,3812,1590,3655,3538,3852,3678,3748,3894,3507,3956,3389,3971,3360,3728,3360,3594,3360,3468,3363,3448,3366,3410,3373,3410,3657,3410,3942,3438,3925,3453,3915,3498,3882,3538,3852,1262,2978,1246,2949,1185,2843,1127,2742,1069,2642,1019,2545,1016,2526,1006,2475,1024,2435,1158,2203,1225,2087,1280,1990,1280,1986,1280,1983,1254,1980,1222,1980,1164,1980,1017,2234,937,2374,869,2493,868,2498,866,2504,932,2626,1015,2769,1165,3030,1228,3030,1292,3030,1262,2978,1880,3016,1880,3014,1817,2902,1740,2769,1660,2629,1600,2514,1600,2500,1600,2485,1659,2371,1740,2232,1817,2099,1880,1987,1880,1985,1880,1982,1835,1980,1781,1980,1682,1980,1532,2240,1382,2500,1532,2760,1682,3020,1781,3020,1835,3020,1880,3018,1880,3016,3043,2758,3192,2500,3043,2243,2894,1985,2500,1985,2106,1985,1957,2243,1808,2500,1951,2748,2029,2884,2097,3001,2103,3008,2110,3017,2198,3020,2503,3018,2894,3015,3043,2758,3468,2760,3618,2500,3468,2240,3318,1980,3219,1980,3165,1980,3120,1982,3120,1984,3120,1986,3183,2098,3260,2231,3339,2369,3400,2486,3400,2500,3400,2514,3339,2631,3260,2769,3183,2902,3120,3014,3120,3016,3120,3018,3165,3020,3219,3020,3318,3020,3468,2760,3983,2766,4063,2626,4131,2507,4132,2502,4134,2496,4068,2374,3985,2231,3835,1970,3772,1970,3708,1970,3738,2023,3754,2051,3815,2157,3873,2258,3931,2358,3981,2455,3984,2474,3994,2524,3977,2563,3842,2797,3775,2914,3720,3011,3720,3014,3720,3018,3746,3020,3778,3020,3836,3020,3983,2766,1584,1629,1588,1626,1589,1496,1588,1340,1585,1057,1485,1132,1430,1173,1346,1245,1299,1292,1215,1376,1076,1550,1044,1611,1029,1641,1304,1638,1455,1636,1581,1632,1584,1629,3960,1625,3960,1597,3802,1393,3704,1296,3634,1225,3504,1118,3438,1075,3410,1058,3410,1344,3410,1630,3685,1630,3836,1630,3960,1628,3960,1625],operators=[0,2,2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,2,3,0,1,1,2,2,2,2,3,0,2,1,1,2,1,1,1,1,2,3,0,2,2,2,2,2,1,1,2,2,1,1,1,1,3,0,2,2,2,2,2,1,1,1,1,1,1,2,3,0,1,1,1,1,1,1,1,1,2,2,1,1,3,0,1,1,1,1,2,2,2,2,2,2,1,1,3,0,2,2,1,1,1,1,2,2,2,2,2,1,1,3,0,2,1,1,2,2,1,1,2,3,0,2,2,1,1,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2235,2991,2224,2986,2208,2974,2199,2964,2162,2922,1940,2524,1940,2500,1940,2471,2167,2070,2206,2030,2230,2005,2500,2005,2770,2005,2794,2030,2833,2070,3060,2471,3060,2500,3060,2529,2833,2930,2794,2970,2770,2995,2512,2997,2371,2998,2246,2995,2235,2991,2605,2667,2695,2614,2695,2500,2695,2386,2605,2333,2556,2304,2508,2280,2500,2280,2492,2280,2445,2304,2395,2333,2305,2386,2305,2500,2305,2614,2395,2667,2445,2696,2492,2720,2500,2720,2508,2720,2556,2696,2605,2667],operators=[0,2,2,2,1,1,1,1,2,2,1,1,2,3,0,1,1,1,1,2,2,1,1,1,1,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2445,2621,2434,2616,2414,2600,2400,2585,2379,2563,2375,2548,2375,2499,2375,2446,2378,2437,2408,2408,2437,2378,2446,2375,2500,2375,2554,2375,2563,2378,2592,2408,2622,2437,2625,2446,2625,2500,2625,2554,2622,2563,2593,2591,2568,2616,2552,2623,2513,2626,2487,2628,2456,2626,2445,2621,2550,2595,2582,2578,2610,2534,2610,2500,2610,2447,2553,2390,2500,2390,2466,2390,2422,2418,2405,2450,2386,2487,2386,2513,2405,2550,2433,2604,2495,2623,2550,2595],operators=[0,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (0.1,0,0,-0.1,self.x, self.y+s)
        g.scale(float(float(s)/float(500)), float(float(s)/float(500)))

        return g


#from http://scp-wiki.wdfiles.com/local--files/component%3Aanomaly-class-bar/explained-icon.svg

class ExplainedSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[138.9,87.5,139.4,87.7,140.1,87,140.5,86,141.7,82.5,142,81.5,142.1,80.7,141.9,80.6,141.7,80.5,141.2,80.2,141.2,80,141.2,79.8,140.4,79.6,139.4,79.6,135.7,79.6,134.7,79.6,133.9,80.4,133.9,81.4,133.9,84.6,133.9,85.6,134.6,86.5,135.5,86.7,136.4,86.9,138.3,87.4,138.9,87.5],operators=[0,2,1,2,2,2,1,2,1,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[133.7,51.8,133.7,52.8,134.5,53.6,135.5,53.6,139.2,53.6,140.2,53.6,141,52.8,141,51.8,141,50.3,141,49.3,141,48,141,47.5,141,47,140,45.8,139,45.9,135.3,46.3,134.3,46.4,133.5,46.8,133.5,47.1,133.5,47.4,133.6,49.2,133.6,50.2,133.6,51.8],operators=[0,2,1,2,1,2,2,1,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[58.6,68.7,58.6,69.7,59.4,70.5,60.4,70.5,64.1,70.5,65.1,70.5,65.9,69.7,65.9,68.7,65.9,64.9,65.9,63.9,65.1,63.1,64.1,63.1,60.4,63.1,59.4,63.1,58.6,63.9,58.6,64.9,58.6,68.7],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[132.4,30.4,131.6,29.7,130.5,29.9,129.9,30.7,127.8,33.7,127.2,34.5,127.4,35.7,128.1,36.4,129.8,38.1,130.4,38.9,131.7,39.1,132.5,38.5,135.6,36.5,136.4,35.9,136.6,34.8,136,34,132.4,30.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[133.7,68.6,133.7,69.6,134.5,70.4,135.5,70.4,139.2,70.4,140.2,70.4,141,69.6,141,68.6,141,64.8,141,63.8,140.2,63,139.2,63,135.5,63,134.5,63,133.7,63.8,133.7,64.8,133.7,68.6],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[69.6,30.7,69,29.9,67.9,29.7,67.1,30.4,63.5,34.1,63,34.9,63.1,36,64,36.6,67.1,38.6,67.9,39.2,69.2,39,69.8,38.2,71.4,36.5,72.2,35.8,72.3,34.6,71.7,33.8,69.6,30.7],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[103.5,26.8,103.5,25.8,102.7,25,101.7,25,97.9,25,96.9,25,96.1,25.8,96.1,26.8,96.1,30.5,96.1,31.5,96.9,32.3,97.9,32.3,101.7,32.3,102.7,32.3,103.5,31.5,103.5,30.5,103.5,26.8],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[58.6,47.6,58.6,48.1,58.6,49.3,58.6,50.3,58.6,51.9,58.6,52.9,59.4,53.7,60.4,53.7,64.1,53.7,65.1,53.7,65.9,52.9,65.9,51.9,65.9,50.3,65.9,49.3,65.9,48.2,65.9,47.8,65.9,47.5,65.2,46.5,64.1,46.4,60.4,46,59.6,46,58.6,47.1,58.6,47.6],operators=[0,2,1,2,1,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[119.1,32.4,119.5,32.4,120,31.7,120.1,30.7,120.6,27,120.7,26,120.4,25.1,119.8,25.1,119.2,25,116.8,25,115.8,25,114.8,25,113.8,25,113,25.8,113,26.8,113,30.5,113,31.5,113.8,32.3,114.8,32.3,115.8,32.3,116.7,32.3,118.6,32.3,119.1,32.4],operators=[0,2,1,2,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[81.4,32.3,81.8,32.3,83,32.3,84,32.3,84.9,32.3,85.9,32.3,86.7,31.5,86.7,30.5,86.7,26.8,86.7,25.8,85.9,25,84.9,25,84,25,83,25,81.6,25,81,25,80.4,25,78.8,26,79,27,79.5,30.6,79.7,31.7,80.9,32.4,81.4,32.3],operators=[0,2,1,2,1,2,1,2,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[58.6,80.3,58.6,80.5,58.4,80.7,58.2,80.8,58,80.9,57.7,81.8,58.1,82.8,59.3,86.3,59.6,87.3,60.3,87.9,60.9,87.7,61.4,87.5,63.6,87.1,64.4,87,65.2,86.9,65.9,85.9,65.9,84.9,65.9,81.8,65.9,80.8,65.1,80,64.1,80,60.4,80,59.4,79.9,58.6,80.1,58.6,80.3],operators=[0,2,2,1,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[55.7,164.6,55.3,165.5,55.7,166.6,56.6,166.9,61.1,168.2,62.1,168.4,63,167.7,63.1,166.7,63.5,163,63.6,162,62.9,161,61.9,160.8,59.7,160.2,58.8,159.8,57.6,160.3,57.2,161.2,55.7,164.6],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[47.5,137.4,47.5,136.4,46.7,135.6,45.7,135.6,42,135.6,41,135.6,40.2,136.4,40.2,137.4,40.2,140.9,40.2,141.9,41,142.7,42,142.7,45.7,142.7,46.7,142.7,47.5,141.9,47.5,140.9,47.5,137.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[72.3,167,72.3,168,73.1,168.8,74.1,168.8,77.6,168.8,78.6,168.8,79.4,168,79.4,167,79.4,163.3,79.4,162.3,78.6,161.5,77.6,161.5,74.1,161.5,73.1,161.5,72.3,162.3,72.3,163.3,72.3,167],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[47.5,107.3,47.5,106.3,47.5,105.2,47.5,104.8,47.5,104.4,46.8,103.5,45.7,103.3,42,102.9,41,102.8,40.1,103.1,40.1,103.6,40.1,104.1,40,106.2,40,107.2,40,108.4,40,109.4,40.8,110.2,41.8,110.2,45.5,110.2,46.5,110.2,47.3,109.4,47.3,108.4,47.3,107.3],operators=[0,2,2,1,2,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[44.4,91.4,43.8,92.2,44.1,93.3,45,93.8,48.2,95.6,49.1,96.1,50.3,95.8,50.8,95,52.2,93.2,52.9,92.5,52.9,91.2,52.2,90.5,49.7,87.8,49,87.1,47.9,87.1,47.2,87.8,44.4,91.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[43.9,152.2,43,152.6,42.6,153.6,43,154.5,45.5,158.5,46.1,159.3,47.2,159.4,48,158.8,50.8,156.4,51.6,155.7,51.7,154.5,51.1,153.7,49.9,151.8,49.4,150.9,48.3,150.5,47.4,150.9,43.9,152.2],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[47.5,121.2,47.5,120.2,46.7,119.4,45.7,119.4,42,119.4,41,119.4,40.2,120.2,40.2,121.2,40.2,124.7,40.2,125.7,41,126.5,42,126.5,45.7,126.5,46.7,126.5,47.5,125.7,47.5,124.7,47.5,121.2],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[152.4,124.4,152.4,125.4,153.2,126.2,154.2,126.2,157.9,126.2,158.9,126.2,159.7,125.4,159.7,124.4,159.7,120.9,159.7,119.9,158.9,119.1,157.9,119.1,154.2,119.1,153.2,119.1,152.4,119.9,152.4,120.9,152.4,124.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[120.8,167,120.8,168,121.6,168.8,122.6,168.8,126.1,168.8,127.1,168.8,127.9,168,127.9,167,127.9,163.3,127.9,162.3,127.1,161.5,126.1,161.5,122.6,161.5,121.6,161.5,120.8,162.3,120.8,163.3,120.8,167],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[149.1,153.4,148.5,154.2,148.7,155.4,149.4,156.1,152.2,158.5,153,159.2,154.1,159,154.7,158.2,157.1,154.2,157.6,153.3,157.2,152.2,156.2,151.9,152.8,150.5,151.9,150.1,150.7,150.6,150.3,151.5,149.1,153.4],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[138.3,160.9,137.3,161.1,136.6,162.1,136.8,163.1,137.3,166.8,137.4,167.8,138.4,168.4,139.4,168.2,143.9,166.8,144.8,166.4,145.2,165.4,144.8,164.5,143.2,161.2,142.7,160.3,141.6,159.9,140.7,160.2,138.3,160.9],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[154.9,93.5,155.8,93,156,91.9,155.5,91.1,152.6,87.5,151.9,86.8,150.8,86.8,150.1,87.5,147.6,90.2,146.9,91,146.9,92.2,147.6,92.9,149,94.7,149.6,95.5,150.8,95.8,151.6,95.3,154.9,93.5],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[159.7,103.4,159.7,102.9,158.8,102.5,157.8,102.6,154.1,103,153.1,103.1,152.3,103.5,152.3,103.9,152.3,104.3,152.4,106.1,152.4,107.1,152.4,108.1,152.4,109.1,153.2,109.9,154.2,109.9,157.9,109.9,158.9,109.9,159.7,109.1,159.7,108.1,159.7,107.1,159.8,106.2,159.8,104,159.7,103.4],operators=[0,2,1,2,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[152.4,140.6,152.4,141.6,153.2,142.4,154.2,142.4,157.9,142.4,158.9,142.4,159.7,141.6,159.7,140.6,159.7,137.1,159.7,136.1,158.9,135.3,157.9,135.3,154.2,135.3,153.2,135.3,152.4,136.1,152.4,137.1,152.4,140.6],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[104.7,167,104.7,168,105.5,168.8,106.5,168.8,110,168.8,111,168.8,111.8,168,111.8,167,111.8,163.3,111.8,162.3,111,161.5,110,161.5,106.5,161.5,105.5,161.5,104.7,162.3,104.7,163.3,104.7,167],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[88.5,167,88.5,168,89.3,168.8,90.3,168.8,93.8,168.8,94.8,168.8,95.6,168,95.6,167,95.6,163.3,95.6,162.3,94.8,161.5,93.8,161.5,90.3,161.5,89.3,161.5,88.5,162.3,88.5,163.3,88.5,167],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[113.9,84.9,113.9,85.9,114.7,86.7,115.7,86.7,119.4,86.7,120.4,86.7,121.2,85.9,121.2,84.9,121.2,81.2,121.2,80.2,120.4,79.4,119.4,79.4,115.7,79.4,114.7,79.4,113.9,80.2,113.9,81.2,113.9,84.9],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[103.9,81.2,103.9,80.2,103.1,79.4,102.1,79.4,97.8,79.4,96.8,79.4,96,80.2,96,81.2,96,84.9,96,85.9,96.8,86.7,97.8,86.7,102.1,86.7,103.1,86.7,103.9,85.9,103.9,84.9,103.9,81.2],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[85.8,81.2,85.8,80.2,85,79.4,84,79.4,80.3,79.4,79.3,79.4,78.5,80.2,78.5,81.2,78.5,84.9,78.5,85.9,79.3,86.7,80.3,86.7,84,86.7,85,86.7,85.8,85.9,85.8,84.9,85.8,81.2],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[121.2,64.8,121.2,63.8,120.4,63,119.4,63,115.7,63,114.7,63,113.9,63.8,113.9,64.8,113.9,68.4,113.9,69.4,114.7,70.2,115.7,70.2,119.4,70.2,120.4,70.2,121.2,69.4,121.2,68.4,121.2,64.8],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[101.6,52.2,102.6,52.2,103.4,51.4,103.4,50.4,103.4,46.7,103.4,45.7,102.6,44.9,101.6,44.9,98,44.9,97,44.9,96.2,45.7,96.2,46.7,96.2,50.4,96.2,51.4,97,52.2,98,52.2,101.6,52.2],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[113.2,53.7,113.5,54.3,114.6,54.5,115.6,54.3,119.2,53.4,120.2,53.2,120.6,52.2,120.1,51.4,115.2,46.3,114.3,45.8,113.4,46.1,113.1,47.1,112.1,50.6,111.8,51.5,112.9,53.1,113.2,53.7],operators=[0,2,1,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[85.8,64.8,85.8,63.8,85,63,84,63,80.3,63,79.3,63,78.5,63.8,78.5,64.8,78.5,68.4,78.5,69.4,79.3,70.2,80.3,70.2,84,70.2,85,70.2,85.8,69.4,85.8,68.4,85.8,64.8],operators=[0,2,1,2,1,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[79.6,51.4,79.1,52.3,79.5,53.2,80.5,53.4,84.1,54.2,85.1,54.4,86.1,54.2,86.5,53.6,86.9,53,87.9,51.4,87.7,50.5,86.6,47,86.3,46,85.4,45.7,84.5,46.2,79.6,51.4],operators=[0,2,1,2,2,1,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[98.3,144.4,98,148.7,97.9,149.6,98.7,150.5,99.6,150.5,99.6,150.5,99.6,150.5,99.6,150.5,102.3,150.5,105,150.1,107.6,149.2,108.5,148.9,109,147.9,108.6,147,106.9,143,106.6,142.3,105.9,141.9,105.1,142,99.6,142.9,99,143,98.4,143.7,98.3,144.4],operators=[0,1,2,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[91.1,107.9,89.2,103.9,88.8,103,89.2,102,90.1,101.6,93.1,100.4,96.4,99.7,99.7,99.7,100.3,99.7,100.8,99.7,101.4,99.8,102.4,99.9,103.1,100.7,102.9,101.7,102.3,106.1,102.2,106.8,101.6,107.4,100.9,107.5,92.8,108.8,92.2,108.9,91.4,108.6,91.1,107.9],operators=[0,1,2,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[117.4,117.5,121.4,115.8,122.3,115.4,122.7,114.4,122.2,113.5,121,111.1,119.3,108.9,117.4,107,116.7,106.3,115.6,106.4,115,107.1,112.2,110.4,111.7,111,111.7,111.8,112.1,112.5,115.4,117,115.9,117.6,116.7,117.8,117.4,117.5],operators=[0,1,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[83.2,115.1,79.5,112.9,78.7,112.4,77.6,112.7,77.1,113.6,75.9,116,75,118.6,74.6,121.3,74.5,122.3,75.2,123.1,76.1,123.2,80.4,123.6,81.2,123.7,81.9,123.2,82.1,122.5,83.8,117.2,84.1,116.3,83.8,115.5,83.2,115.1],operators=[0,1,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[82.6,134.1,81.5,134.6,79.9,135.4,78.7,136,77.8,136.4,77.5,137.5,78,138.4,79.4,140.7,81.2,142.8,83.2,144.5,83.9,145.1,85.1,145,85.6,144.2,88.2,140.7,88.7,140.1,88.6,139.2,88.1,138.6,84.5,134.4,84.1,133.9,83.3,133.8,82.6,134.1],operators=[0,2,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))
        g.add(Path(points=[115.4,136.3,118.9,138.8,119.7,139.4,120.8,139.1,121.3,138.3,122.7,136,123.7,133.4,124.3,130.8,124.5,129.9,123.9,128.9,122.9,128.8,118.6,128.1,117.8,128,117.1,128.4,116.8,129.1,114.7,134.3,114.6,135,114.8,135.9,115.4,136.3],operators=[0,1,2,2,2,1,2,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(.003922,.003922,.003922,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


#from https://usercontent.irccloud-cdn.com/file/hOzaeSei/Anomalous.png

class AnomalousSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[950,3889,884,3876,804,3832,753,3779,691,3715,673,3685,650,3610,630,3546,630,3521,632,2265,635,985,667,917,730,785,847,699,990,680,1088,668,3399,667,3497,680,3678,703,3820,841,3849,1021,3864,1109,3864,3461,3849,3550,3827,3690,3750,3794,3622,3857,3546,3895,2271,3897,1565,3897,975,3894,950,3889,3495,3609,3519,3593,3546,3562,3563,3532,3590,3482,3590,2289,3590,1095,3559,1042,3535,999,3519,984,3477,964,3425,940,2240,940,1055,940,1003,964,961,984,945,999,921,1042,890,1095,893,2300,895,3505,924,3548,952,3589,988,3616,1035,3632,1046,3635,1595,3637,2255,3637,3455,3635,3495,3609],operators=[0,2,2,2,1,1,2,2,2,2,2,1,1,2,3,0,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2135,3064,1878,3022,1654,2859,1545,2635,1489,2520,1470,2449,1463,2325,1442,1957,1686,1624,2051,1524,2140,1499,2350,1499,2439,1524,2716,1600,2930,1814,3006,2091,3031,2180,3031,2390,3006,2479,2965,2631,2892,2748,2771,2862,2683,2945,2558,3015,2445,3045,2385,3061,2191,3073,2135,3064,2330,2769,2428,2753,2514,2708,2591,2631,2927,2295,2643,1733,2170,1800,1973,1828,1802,1990,1761,2188,1700,2483,1928,2768,2235,2779,2252,2779,2294,2775,2330,2769],operators=[0,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (1,0,0,-1,self.x+(s/20.0), (self.y+s)-(s/20.0))
        g.scale(float(float(s)/float(5000)), float(float(s)/float(5000)))

        return g


class TruculentSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[99.991,52.85,108.859,53.937,122.365,31.531,130.745,34.635,139.124,37.739,131.004,62.424,135.681,70.038,140.361,77.651,166.299,74.242,169.097,82.728,171.898,91.215,147.535,100.253,144.497,108.66,141.457,117.061,160.3,135.218,155.411,142.695,150.518,150.176,127.848,135.752,119.798,139.628,111.747,143.508,108.888,170.223,99.991,169.385,91.095,168.546,88.649,142.496,80.185,139.628,71.72,136.763,49.462,150.177,44.572,142.695,39.68,135.217,58.518,117.061,55.485,108.66,52.451,100.253,28.201,91.251,30.884,82.728,33.566,74.204,58.728,77.025,64.3,70.038,69.872,63.051,61.522,39.147,69.235,34.635,76.948,30.124,91.121,51.763,99.991,52.85],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=6.5027,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=Color(.137255,.121569,.12549,1),strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3],strokeOpacity=1,strokeLineJoin=0,points=[99.981,26.325,114.957,26.322,92.993,79.377,106.485,85.872,107.309,86.269,108.188,86.454,109.112,86.454,121.717,86.454,142.855,52.035,153.57,52.035,154.92,52.035,156.103,52.581,157.085,53.81,166.424,65.515,111.249,81.423,114.585,96.023,117.922,110.621,174.528,100.99,171.2,115.59,170.579,118.311,168.447,119.372,165.329,119.372,154.312,119.372,130.975,106.133,118.449,106.131,115.496,106.13,113.147,106.865,111.698,108.683,102.364,120.395,145.189,158.648,131.696,165.147,130.972,165.496,130.278,165.661,129.61,165.661,117.827,165.661,114.17,114.319,100,114.319,99.999,114.319,100,114.319,99.999,114.319,85.827,114.324,82.192,165.674,70.407,165.674,69.739,165.674,69.047,165.51,68.323,165.161,54.829,158.665,97.637,120.394,88.299,108.688,86.851,106.873,84.501,106.138,81.553,106.138,69.025,106.139,45.681,119.4,34.664,119.4,31.55,119.4,29.421,118.34,28.8,115.622,25.465,101.021,82.077,110.629,85.406,96.029,88.736,81.428,33.554,65.544,42.89,53.833,43.87,52.603,45.055,52.057,46.405,52.057,57.118,52.055,78.267,86.458,90.872,86.458,91.797,86.458,92.676,86.273,93.501,85.875,106.99,79.374,85.006,26.328,99.981,26.325,99.983,16.325,99.983,16.325,99.98,16.325,95.657,16.326,91.757,18.069,89.001,21.232,82.63,28.542,84.266,40.418,86.337,55.453,87.065,60.736,87.817,66.199,88.038,70.752,88.115,72.327,88.116,73.598,88.076,74.614,87.256,74.011,86.263,73.218,85.079,72.177,81.656,69.167,77.852,65.174,74.174,61.313,63.924,50.554,55.83,42.057,46.405,42.057,41.944,42.057,37.919,44.026,35.07,47.6,32.375,50.981,31.306,55.116,32.061,59.244,33.804,68.783,44.109,74.908,57.155,82.663,61.739,85.388,66.479,88.205,70.176,90.871,71.455,91.794,72.449,92.585,73.219,93.25,72.237,93.515,70.998,93.797,69.446,94.074,64.958,94.874,59.466,95.358,54.154,95.826,39.035,97.159,27.093,98.211,21.387,106.052,18.917,109.445,18.088,113.634,19.051,117.85,20.996,126.366,28.392,129.401,34.664,129.401,41.822,129.401,50.764,126.022,60.23,122.444,66.283,120.157,73.541,117.415,78.532,116.475,78.127,117.41,77.574,118.558,76.819,119.95,74.646,123.957,71.6,128.554,68.654,132.998,60.27,145.649,53.647,155.642,56.219,164.991,57.332,169.037,60.09,172.298,63.986,174.174,66.058,175.171,68.218,175.676,70.408,175.676,80.453,175.676,85.167,165.863,86.717,162.637,89.149,157.575,91.143,151.39,93.255,144.841,94.892,139.765,96.584,134.516,98.361,130.318,98.976,128.866,99.527,127.72,100.003,126.821,100.481,127.72,101.031,128.865,101.647,130.317,103.425,134.514,105.12,139.762,106.758,144.838,108.872,151.385,110.869,157.569,113.303,162.63,114.853,165.854,119.571,175.663,129.612,175.663,131.804,175.663,133.966,175.157,136.04,174.158,139.934,172.282,142.69,169.02,143.803,164.973,146.371,155.623,139.745,145.634,131.356,132.987,128.408,128.543,125.36,123.948,123.185,119.941,122.43,118.55,121.876,117.403,121.471,116.468,126.463,117.406,133.718,120.145,139.768,122.428,149.234,125.999,158.175,129.374,165.331,129.374,171.608,129.374,179.008,126.337,180.952,117.815,181.913,113.599,181.081,109.41,178.61,106.018,172.901,98.181,160.959,97.133,145.839,95.807,140.527,95.341,135.033,94.859,130.546,94.061,128.993,93.785,127.754,93.503,126.772,93.239,127.543,92.573,128.536,91.781,129.815,90.858,133.511,88.19,138.252,85.37,142.835,82.643,155.877,74.883,166.179,68.754,167.918,59.215,168.67,55.087,167.6,50.953,164.903,47.573,162.054,44.001,158.03,42.034,153.572,42.034,144.144,42.034,136.051,50.537,125.805,61.302,122.128,65.165,118.326,69.159,114.905,72.171,113.72,73.213,112.728,74.006,111.909,74.609,111.869,73.592,111.869,72.321,111.945,70.746,112.164,66.193,112.914,60.729,113.639,55.446,115.703,40.411,117.334,28.535,110.962,21.228,108.204,18.066,104.305,16.325,99.983,16.325,99.983,16.325],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[99.981,26.325,114.957,26.322,92.993,79.377,106.485,85.872,107.309,86.269,108.188,86.454,109.112,86.454,121.717,86.454,142.855,52.035,153.57,52.035,154.92,52.035,156.103,52.581,157.085,53.81,166.424,65.515,111.249,81.423,114.585,96.023,117.922,110.621,174.528,100.99,171.2,115.59,170.579,118.311,168.447,119.372,165.329,119.372,154.312,119.372,130.975,106.133,118.449,106.131,115.496,106.13,113.147,106.865,111.698,108.683,102.364,120.395,145.189,158.648,131.696,165.147,130.972,165.496,130.278,165.661,129.61,165.661,117.827,165.661,114.17,114.319,100,114.319,99.999,114.319,100,114.319,99.999,114.319,85.827,114.324,82.192,165.674,70.407,165.674,69.739,165.674,69.047,165.51,68.323,165.161,54.829,158.665,97.637,120.394,88.299,108.688,86.851,106.873,84.501,106.138,81.553,106.138,69.025,106.139,45.681,119.4,34.664,119.4,31.55,119.4,29.421,118.34,28.8,115.622,25.465,101.021,82.077,110.629,85.406,96.029,88.736,81.428,33.554,65.544,42.89,53.833,43.87,52.603,45.055,52.057,46.405,52.057,57.118,52.055,78.267,86.458,90.872,86.458,91.797,86.458,92.676,86.273,93.501,85.875,106.99,79.374,85.006,26.328,99.981,26.325,99.983,16.325,99.983,16.325,99.98,16.325,95.657,16.326,91.757,18.069,89.001,21.232,82.63,28.542,84.266,40.418,86.337,55.453,87.065,60.736,87.817,66.199,88.038,70.752,88.115,72.327,88.116,73.598,88.076,74.614,87.256,74.011,86.263,73.218,85.079,72.177,81.656,69.167,77.852,65.174,74.174,61.313,63.924,50.554,55.83,42.057,46.405,42.057,41.944,42.057,37.919,44.026,35.07,47.6,32.375,50.981,31.306,55.116,32.061,59.244,33.804,68.783,44.109,74.908,57.155,82.663,61.739,85.388,66.479,88.205,70.176,90.871,71.455,91.794,72.449,92.585,73.219,93.25,72.237,93.515,70.998,93.797,69.446,94.074,64.958,94.874,59.466,95.358,54.154,95.826,39.035,97.159,27.093,98.211,21.387,106.052,18.917,109.445,18.088,113.634,19.051,117.85,20.996,126.366,28.392,129.401,34.664,129.401,41.822,129.401,50.764,126.022,60.23,122.444,66.283,120.157,73.541,117.415,78.532,116.475,78.127,117.41,77.574,118.558,76.819,119.95,74.646,123.957,71.6,128.554,68.654,132.998,60.27,145.649,53.647,155.642,56.219,164.991,57.332,169.037,60.09,172.298,63.986,174.174,66.058,175.171,68.218,175.676,70.408,175.676,80.453,175.676,85.167,165.863,86.717,162.637,89.149,157.575,91.143,151.39,93.255,144.841,94.892,139.765,96.584,134.516,98.361,130.318,98.976,128.866,99.527,127.72,100.003,126.821,100.481,127.72,101.031,128.865,101.647,130.317,103.425,134.514,105.12,139.762,106.758,144.838,108.872,151.385,110.869,157.569,113.303,162.63,114.853,165.854,119.571,175.663,129.612,175.663,131.804,175.663,133.966,175.157,136.04,174.158,139.934,172.282,142.69,169.02,143.803,164.973,146.371,155.623,139.745,145.634,131.356,132.987,128.408,128.543,125.36,123.948,123.185,119.941,122.43,118.55,121.876,117.403,121.471,116.468,126.463,117.406,133.718,120.145,139.768,122.428,149.234,125.999,158.175,129.374,165.331,129.374,171.608,129.374,179.008,126.337,180.952,117.815,181.913,113.599,181.081,109.41,178.61,106.018,172.901,98.181,160.959,97.133,145.839,95.807,140.527,95.341,135.033,94.859,130.546,94.061,128.993,93.785,127.754,93.503,126.772,93.239,127.543,92.573,128.536,91.781,129.815,90.858,133.511,88.19,138.252,85.37,142.835,82.643,155.877,74.883,166.179,68.754,167.918,59.215,168.67,55.087,167.6,50.953,164.903,47.573,162.054,44.001,158.03,42.034,153.572,42.034,144.144,42.034,136.051,50.537,125.805,61.302,122.128,65.165,118.326,69.159,114.905,72.171,113.72,73.213,112.728,74.006,111.909,74.609,111.869,73.592,111.869,72.321,111.945,70.746,112.164,66.193,112.914,60.729,113.639,55.446,115.703,40.411,117.334,28.535,110.962,21.228,108.204,18.066,104.305,16.325,99.983,16.325,99.983,16.325],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[100.399,176.903,100.031,176.903,99.66,176.885,99.284,176.849,90.097,175.984,86.131,166.015,82.632,157.22,79.747,149.965,78.325,147.475,77.627,146.728,77.544,146.723,77.43,146.718,77.289,146.718,74.687,146.718,70.031,148.081,65.921,149.284,60.53,150.861,54.955,152.493,50.105,152.493,43.422,152.493,39.995,149.395,38.296,146.797,33.244,139.074,38.564,129.757,43.258,121.535,47.192,114.648,48.223,112.01,48.345,111.036,47.357,109.366,41.577,105.295,39.059,103.52,30.393,97.416,20.576,90.5,23.732,80.474,26.55,71.515,37.339,69.724,46.857,68.143,49.645,67.68,56.947,66.467,58.426,65.351,59.186,63.66,58.742,56.267,58.573,53.453,57.995,43.821,57.34,32.904,65.448,28.161,67.314,27.07,69.376,26.517,71.576,26.517,78.593,26.517,84.777,32.082,91.325,37.975,93.598,40.021,98.784,44.686,100.68,45.344,102.591,44.711,108.003,39.737,109.824,38.063,116.103,32.291,122.034,26.839,129.052,26.839,130.538,26.839,131.984,27.095,133.35,27.601,143.288,31.284,142.562,43.341,141.921,53.978,141.735,57.054,141.31,64.104,141.996,65.94,142.837,66.452,145.546,67.29,153.372,68.508,162.729,69.964,173.329,71.613,176.22,80.379,179.541,90.444,169.661,97.393,160.945,103.525,158.424,105.298,152.644,109.363,151.638,111.044,151.761,112.02,152.795,114.661,156.725,121.542,161.419,129.76,166.74,139.075,161.689,146.8,160.022,149.347,156.679,152.383,150.211,152.383,145.458,152.383,139.993,150.722,134.708,149.114,130.597,147.864,125.956,146.453,123.35,146.453,123.215,146.453,123.107,146.457,123.021,146.463,122.061,147.48,120.349,151.08,117.925,157.181,114.25,166.43,110.091,176.902,100.399,176.903,100.399,176.903,77.288,131.719,79.257,131.719,80.991,131.982,82.59,132.523,89.94,135.014,93.16,143.106,96.569,151.673,98.275,155.961,99.463,158.57,100.29,160.134,101.214,158.344,102.45,155.508,103.98,151.654,107.195,143.558,110.232,135.912,116.542,132.872,118.523,131.917,120.75,131.453,123.35,131.453,128.188,131.453,133.714,133.134,139.06,134.76,142.105,135.686,145.455,136.704,148.001,137.152,147.288,135.535,145.986,132.985,143.699,128.983,139.123,120.969,134.804,113.405,137.445,106.109,139.572,100.22,145.757,95.869,152.306,91.262,156.119,88.58,158.82,86.528,160.383,85.123,158.459,84.596,155.348,83.997,151.078,83.332,141.959,81.913,133.352,80.574,129.29,73.965,126.011,68.626,126.465,61.077,126.946,53.085,127.227,48.421,127.305,45.027,127.181,42.929,124.83,44.642,121.358,47.834,119.977,49.104,113.662,54.909,107.7,60.389,100.628,60.389,100.112,60.389,99.59,60.357,99.079,60.295,92.855,59.533,87.238,54.479,81.291,49.128,79.77,47.759,75.887,44.264,73.343,42.518,73.222,44.274,73.231,47.325,73.545,52.556,74.059,61.125,74.545,69.22,70.163,74.715,65.782,80.209,57.783,81.537,49.315,82.943,44.144,83.801,41.168,84.475,39.482,84.987,41.024,86.397,43.77,88.495,47.692,91.258,54.233,95.866,60.411,100.218,62.539,106.114,65.172,113.407,60.854,120.968,56.282,128.974,53.903,133.14,52.594,135.737,51.907,137.346,54.635,136.957,58.345,135.872,61.697,134.892,67.035,133.33,72.541,131.719,77.288,131.719],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3],strokeOpacity=1,strokeLineJoin=0,points=[71.576,29.017,77.633,29.017,83.472,34.271,89.653,39.833,93.298,43.112,98.288,47.604,100.6,47.887,102.83,47.887,108.268,42.889,111.517,39.903,117.427,34.47,123.009,29.34,129.052,29.34,130.241,29.34,131.395,29.544,132.482,29.946,140.682,32.985,140.044,43.581,139.426,53.83,139.13,58.73,138.726,65.442,139.942,67.421,140.98,69.11,149.093,70.372,152.993,70.979,162.059,72.39,171.434,73.848,173.847,81.162,176.587,89.466,167.904,95.574,159.506,101.48,155.49,104.304,149.99,108.172,149.2,110.358,148.525,112.223,152.597,119.354,154.554,122.781,159.105,130.748,163.81,138.986,159.596,145.43,158.268,147.46,155.563,149.881,150.211,149.881,150.21,149.881,150.208,149.881,150.207,149.881,145.826,149.881,140.538,148.273,135.423,146.717,130.952,145.358,126.328,143.951,123.35,143.951,122.369,143.951,122.005,144.112,121.967,144.131,120.05,145.055,117.154,152.349,115.597,156.267,112.056,165.182,108.394,174.402,100.399,174.403,100.109,174.403,99.818,174.389,99.523,174.361,91.855,173.638,88.347,164.822,84.955,156.296,83.497,152.629,80.461,144.999,78.581,144.362,78.455,144.319,78.072,144.218,77.289,144.218,74.332,144.218,69.699,145.573,65.219,146.885,59.996,148.413,54.596,149.993,50.105,149.993,44.54,149.993,41.75,147.511,40.389,145.429,36.173,138.986,40.879,130.744,45.43,122.775,47.387,119.349,51.457,112.22,50.784,110.357,49.993,108.166,44.505,104.299,40.497,101.476,32.145,95.593,23.51,89.51,26.118,81.226,28.476,73.73,38.031,72.144,47.27,70.61,51.942,69.834,59.003,68.662,60.393,66.92,61.783,65.178,61.354,58.032,61.07,53.304,60.509,43.955,59.929,34.287,66.712,30.319,68.188,29.455,69.825,29.017,71.576,29.017,50.104,139.994,53.162,139.994,57.863,138.618,62.41,137.288,67.566,135.779,72.898,134.219,77.288,134.219,78.98,134.219,80.452,134.439,81.788,134.891,88.043,137.011,91.056,144.583,94.246,152.599,95.637,156.095,98.481,163.244,100.336,164.328,102.139,163.058,104.831,156.282,106.302,152.576,109.332,144.946,112.195,137.74,117.626,135.123,119.262,134.335,121.134,133.952,123.349,133.952,127.815,133.952,133.161,135.578,138.331,137.15,142.747,138.493,147.314,139.881,150.209,139.881,150.742,139.881,151.076,139.831,151.266,139.788,151.586,137.749,147.745,131.021,145.87,127.74,141.591,120.246,137.548,113.168,139.796,106.957,141.656,101.807,147.532,97.675,153.752,93.3,157.24,90.846,163.661,86.331,164.288,84.211,163.028,82.66,155.234,81.447,151.455,80.859,142.931,79.533,134.879,78.28,131.421,72.655,128.554,67.987,128.986,60.818,129.443,53.227,129.699,48.975,130.171,41.154,128.911,39.326,126.745,39.487,121.461,44.344,118.284,47.264,112.341,52.727,106.726,57.888,100.63,57.888,100.211,57.888,99.792,57.862,99.383,57.812,93.943,57.145,88.61,52.347,82.964,47.266,79.592,44.231,73.986,39.187,71.69,39.02,70.321,40.547,70.813,48.735,71.051,52.704,71.536,60.781,71.993,68.41,68.21,73.154,64.427,77.898,56.888,79.149,48.906,80.474,44.993,81.123,36.929,82.462,35.705,84.158,36.284,86.277,42.747,90.829,46.254,93.3,52.463,97.674,58.328,101.806,60.189,106.961,62.43,113.168,58.39,120.243,54.113,127.733,52.235,131.021,48.384,137.766,48.747,139.849,48.948,139.91,49.364,139.994,50.104,139.994,71.576,24.017,68.926,24.017,66.44,24.685,64.187,26.002,54.753,31.522,55.487,43.765,56.078,53.603,56.21,55.798,56.532,61.164,56.245,63.613,53.923,64.437,48.624,65.317,46.456,65.677,36.726,67.293,24.626,69.302,21.347,79.726,17.642,91.494,28.717,99.295,37.615,105.564,39.574,106.944,43.767,109.897,45.559,111.642,45.045,112.983,43.814,115.521,41.087,120.296,36.287,128.703,30.313,139.164,36.204,148.167,37.87,150.716,41.892,154.994,50.104,154.994,55.312,154.994,61.062,153.311,66.623,151.684,69.91,150.722,73.9,149.553,76.347,149.279,77.077,150.528,78.292,153.074,80.308,158.143,83.887,167.137,88.34,178.33,99.053,179.338,99.494,179.381,99.949,179.402,100.399,179.402,111.788,179.401,116.477,167.596,120.243,158.112,122.038,153.596,123.394,150.55,124.295,149.014,126.733,149.299,130.697,150.505,133.965,151.498,139.44,153.163,145.085,154.88,150.207,154.88,158.195,154.88,162.14,150.674,163.78,148.166,169.669,139.16,163.695,128.702,158.895,120.299,156.168,115.527,154.938,112.987,154.423,111.646,156.221,109.901,160.42,106.948,162.38,105.569,171.343,99.265,182.495,91.42,178.593,79.594,175.224,69.377,163.322,67.525,153.761,66.037,148.328,65.191,145.575,64.571,144.205,64.137,143.962,61.643,144.271,56.521,144.416,54.13,145.074,43.192,145.894,29.583,134.218,25.256,132.572,24.647,130.834,24.338,129.051,24.338,121.059,24.338,114.488,30.379,108.132,36.22,106.716,37.521,102.823,41.099,100.681,42.501,98.58,41.139,94.777,37.717,93,36.118,86.387,30.168,79.552,24.017,71.576,24.017,71.576,24.017,45.029,86.248,46.321,85.996,47.869,85.716,49.724,85.409,58.286,83.988,67.139,82.518,72.119,76.274,77.099,70.028,76.562,61.07,76.042,52.406,75.929,50.527,75.856,48.954,75.814,47.637,77.369,48.959,78.843,50.285,79.619,50.984,85.869,56.608,91.77,61.918,98.775,62.776,99.39,62.851,100.013,62.889,100.63,62.889,108.675,62.889,115.279,56.818,121.667,50.948,122.302,50.365,123.437,49.322,124.685,48.223,124.636,49.592,124.559,51.158,124.454,52.918,123.947,61.332,123.47,69.263,127.161,75.273,131.83,82.867,141.416,84.358,150.687,85.801,152.173,86.032,153.509,86.254,154.693,86.465,153.592,87.28,152.321,88.196,150.881,89.209,143.989,94.057,137.49,98.628,135.095,105.261,132.061,113.641,136.873,122.068,141.527,130.217,142.216,131.424,142.811,132.488,143.322,133.424,142.123,133.077,140.914,132.71,139.789,132.367,134.268,130.689,128.561,128.953,123.351,128.953,120.368,128.953,117.786,129.498,115.458,130.619,108.269,134.084,104.907,142.547,101.657,150.731,101.161,151.979,100.7,153.113,100.273,154.131,99.861,153.154,99.403,152.034,98.893,150.751,95.423,142.031,91.836,133.017,83.394,130.155,81.53,129.524,79.534,129.218,77.289,129.218,72.184,129.218,66.503,130.88,61.011,132.488,59.522,132.924,57.961,133.38,56.467,133.782,57.019,132.761,57.675,131.58,58.456,130.214,63.108,122.068,67.919,113.644,64.893,105.264,62.498,98.627,56.007,94.055,49.136,89.214,47.564,88.107,46.195,87.118,45.029,86.248,45.029,86.248],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[71.576,29.017,77.633,29.017,83.472,34.271,89.653,39.833,93.298,43.112,98.288,47.604,100.6,47.887,102.83,47.887,108.268,42.889,111.517,39.903,117.427,34.47,123.009,29.34,129.052,29.34,130.241,29.34,131.395,29.544,132.482,29.946,140.682,32.985,140.044,43.581,139.426,53.83,139.13,58.73,138.726,65.442,139.942,67.421,140.98,69.11,149.093,70.372,152.993,70.979,162.059,72.39,171.434,73.848,173.847,81.162,176.587,89.466,167.904,95.574,159.506,101.48,155.49,104.304,149.99,108.172,149.2,110.358,148.525,112.223,152.597,119.354,154.554,122.781,159.105,130.748,163.81,138.986,159.596,145.43,158.268,147.46,155.563,149.881,150.211,149.881,150.21,149.881,150.208,149.881,150.207,149.881,145.826,149.881,140.538,148.273,135.423,146.717,130.952,145.358,126.328,143.951,123.35,143.951,122.369,143.951,122.005,144.112,121.967,144.131,120.05,145.055,117.154,152.349,115.597,156.267,112.056,165.182,108.394,174.402,100.399,174.403,100.109,174.403,99.818,174.389,99.523,174.361,91.855,173.638,88.347,164.822,84.955,156.296,83.497,152.629,80.461,144.999,78.581,144.362,78.455,144.319,78.072,144.218,77.289,144.218,74.332,144.218,69.699,145.573,65.219,146.885,59.996,148.413,54.596,149.993,50.105,149.993,44.54,149.993,41.75,147.511,40.389,145.429,36.173,138.986,40.879,130.744,45.43,122.775,47.387,119.349,51.457,112.22,50.784,110.357,49.993,108.166,44.505,104.299,40.497,101.476,32.145,95.593,23.51,89.51,26.118,81.226,28.476,73.73,38.031,72.144,47.27,70.61,51.942,69.834,59.003,68.662,60.393,66.92,61.783,65.178,61.354,58.032,61.07,53.304,60.509,43.955,59.929,34.287,66.712,30.319,68.188,29.455,69.825,29.017,71.576,29.017,50.104,139.994,53.162,139.994,57.863,138.618,62.41,137.288,67.566,135.779,72.898,134.219,77.288,134.219,78.98,134.219,80.452,134.439,81.788,134.891,88.043,137.011,91.056,144.583,94.246,152.599,95.637,156.095,98.481,163.244,100.336,164.328,102.139,163.058,104.831,156.282,106.302,152.576,109.332,144.946,112.195,137.74,117.626,135.123,119.262,134.335,121.134,133.952,123.349,133.952,127.815,133.952,133.161,135.578,138.331,137.15,142.747,138.493,147.314,139.881,150.209,139.881,150.742,139.881,151.076,139.831,151.266,139.788,151.586,137.749,147.745,131.021,145.87,127.74,141.591,120.246,137.548,113.168,139.796,106.957,141.656,101.807,147.532,97.675,153.752,93.3,157.24,90.846,163.661,86.331,164.288,84.211,163.028,82.66,155.234,81.447,151.455,80.859,142.931,79.533,134.879,78.28,131.421,72.655,128.554,67.987,128.986,60.818,129.443,53.227,129.699,48.975,130.171,41.154,128.911,39.326,126.745,39.487,121.461,44.344,118.284,47.264,112.341,52.727,106.726,57.888,100.63,57.888,100.211,57.888,99.792,57.862,99.383,57.812,93.943,57.145,88.61,52.347,82.964,47.266,79.592,44.231,73.986,39.187,71.69,39.02,70.321,40.547,70.813,48.735,71.051,52.704,71.536,60.781,71.993,68.41,68.21,73.154,64.427,77.898,56.888,79.149,48.906,80.474,44.993,81.123,36.929,82.462,35.705,84.158,36.284,86.277,42.747,90.829,46.254,93.3,52.463,97.674,58.328,101.806,60.189,106.961,62.43,113.168,58.39,120.243,54.113,127.733,52.235,131.021,48.384,137.766,48.747,139.849,48.948,139.91,49.364,139.994,50.104,139.994,71.576,24.017,68.926,24.017,66.44,24.685,64.187,26.002,54.753,31.522,55.487,43.765,56.078,53.603,56.21,55.798,56.532,61.164,56.245,63.613,53.923,64.437,48.624,65.317,46.456,65.677,36.726,67.293,24.626,69.302,21.347,79.726,17.642,91.494,28.717,99.295,37.615,105.564,39.574,106.944,43.767,109.897,45.559,111.642,45.045,112.983,43.814,115.521,41.087,120.296,36.287,128.703,30.313,139.164,36.204,148.167,37.87,150.716,41.892,154.994,50.104,154.994,55.312,154.994,61.062,153.311,66.623,151.684,69.91,150.722,73.9,149.553,76.347,149.279,77.077,150.528,78.292,153.074,80.308,158.143,83.887,167.137,88.34,178.33,99.053,179.338,99.494,179.381,99.949,179.402,100.399,179.402,111.788,179.401,116.477,167.596,120.243,158.112,122.038,153.596,123.394,150.55,124.295,149.014,126.733,149.299,130.697,150.505,133.965,151.498,139.44,153.163,145.085,154.88,150.207,154.88,158.195,154.88,162.14,150.674,163.78,148.166,169.669,139.16,163.695,128.702,158.895,120.299,156.168,115.527,154.938,112.987,154.423,111.646,156.221,109.901,160.42,106.948,162.38,105.569,171.343,99.265,182.495,91.42,178.593,79.594,175.224,69.377,163.322,67.525,153.761,66.037,148.328,65.191,145.575,64.571,144.205,64.137,143.962,61.643,144.271,56.521,144.416,54.13,145.074,43.192,145.894,29.583,134.218,25.256,132.572,24.647,130.834,24.338,129.051,24.338,121.059,24.338,114.488,30.379,108.132,36.22,106.716,37.521,102.823,41.099,100.681,42.501,98.58,41.139,94.777,37.717,93,36.118,86.387,30.168,79.552,24.017,71.576,24.017,71.576,24.017,45.029,86.248,46.321,85.996,47.869,85.716,49.724,85.409,58.286,83.988,67.139,82.518,72.119,76.274,77.099,70.028,76.562,61.07,76.042,52.406,75.929,50.527,75.856,48.954,75.814,47.637,77.369,48.959,78.843,50.285,79.619,50.984,85.869,56.608,91.77,61.918,98.775,62.776,99.39,62.851,100.013,62.889,100.63,62.889,108.675,62.889,115.279,56.818,121.667,50.948,122.302,50.365,123.437,49.322,124.685,48.223,124.636,49.592,124.559,51.158,124.454,52.918,123.947,61.332,123.47,69.263,127.161,75.273,131.83,82.867,141.416,84.358,150.687,85.801,152.173,86.032,153.509,86.254,154.693,86.465,153.592,87.28,152.321,88.196,150.881,89.209,143.989,94.057,137.49,98.628,135.095,105.261,132.061,113.641,136.873,122.068,141.527,130.217,142.216,131.424,142.811,132.488,143.322,133.424,142.123,133.077,140.914,132.71,139.789,132.367,134.268,130.689,128.561,128.953,123.351,128.953,120.368,128.953,117.786,129.498,115.458,130.619,108.269,134.084,104.907,142.547,101.657,150.731,101.161,151.979,100.7,153.113,100.273,154.131,99.861,153.154,99.403,152.034,98.893,150.751,95.423,142.031,91.836,133.017,83.394,130.155,81.53,129.524,79.534,129.218,77.289,129.218,72.184,129.218,66.503,130.88,61.011,132.488,59.522,132.924,57.961,133.38,56.467,133.782,57.019,132.761,57.675,131.58,58.456,130.214,63.108,122.068,67.919,113.644,64.893,105.264,62.498,98.627,56.007,94.055,49.136,89.214,47.564,88.107,46.195,87.118,45.029,86.248,45.029,86.248],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(Path(points=[70.873,91.384,71.82,92.089,72.597,92.713,73.219,93.25,72.237,93.515,70.998,93.797,69.446,94.074,64.958,94.874,59.466,95.358,54.154,95.826,39.035,97.159,27.093,98.211,21.387,106.052,18.917,109.445,18.088,113.634,19.051,117.85,20.996,126.366,28.392,129.401,34.664,129.401,41.822,129.401,50.764,126.022,60.23,122.444,66.283,120.157,73.541,117.415,78.532,116.475,78.217,117.203,77.807,118.065,77.287,119.065,81.233,116.059,84.636,112.058,88.676,109.227,88.561,109.042,88.436,108.863,88.298,108.69,86.85,106.875,84.5,106.14,81.552,106.14,69.025,106.139,45.681,119.4,34.664,119.4,31.55,119.4,29.421,118.34,28.8,115.622,25.465,101.021,82.077,110.629,85.406,96.029,85.804,94.285,85.359,92.522,84.297,90.751,79.908,90.758,75.206,91.395,70.873,91.384],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[178.608,106.018,172.899,98.181,160.957,97.133,145.837,95.807,140.525,95.341,135.031,94.859,130.544,94.061,128.991,93.785,127.752,93.503,126.77,93.239,127.152,92.909,127.589,92.548,128.088,92.156,123.783,92.025,119.413,91.748,115.083,91.9,114.473,93.283,114.272,94.66,114.584,96.025,117.921,110.623,174.527,100.992,171.199,115.592,170.578,118.313,168.446,119.374,165.328,119.374,154.311,119.374,130.974,106.135,118.448,106.133,115.495,106.132,113.146,106.867,111.697,108.685,111.409,109.047,111.171,109.435,110.979,109.845,114.317,112.481,117.911,114.728,121.633,116.839,121.578,116.715,121.518,116.585,121.467,116.468,126.459,117.406,133.714,120.145,139.764,122.428,149.23,125.999,158.171,129.374,165.327,129.374,171.604,129.374,179.004,126.337,180.948,117.815,181.911,113.599,181.079,109.409,178.608,106.018],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[89.152,86.241,89.738,86.368,90.316,86.457,90.871,86.457,91.796,86.457,92.675,86.272,93.5,85.874,106.99,79.374,85.005,26.327,99.981,26.324,114.957,26.321,92.993,79.376,106.485,85.871,107.309,86.268,108.188,86.453,109.112,86.453,109.209,86.453,109.311,86.432,109.41,86.429,112.366,81.333,116.866,76.721,116.494,70.723,115.957,71.223,115.425,71.711,114.903,72.17,113.718,73.212,112.726,74.005,111.907,74.608,111.867,73.591,111.867,72.32,111.943,70.745,112.162,66.192,112.912,60.728,113.637,55.445,115.701,40.41,117.332,28.534,110.96,21.227,108.203,18.065,104.304,16.324,99.982,16.324,99.981,16.324,99.979,16.324,95.656,16.325,91.756,18.068,89,21.231,82.629,28.541,84.265,40.417,86.336,55.452,87.064,60.735,87.816,66.198,88.037,70.751,88.114,72.326,88.115,73.597,88.075,74.613,87.996,74.555,87.908,74.487,87.825,74.425,87.36,78.646,87.979,82.51,89.152,86.241],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (1,0,0,-1,self.x, self.y+s)
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))

        return g


class NumenSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,200)
        g.add(Polygon(points=[150.8,155.9,100,155.9,49.199,155.9,99.424,25.099],strokeDashArray=None,strokeWidth=10,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=Color(.137255,.121569,.12549,1),strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,1,1,1,1,1,3,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[67.999,51.542,110.829,151.693,55.833,151.9,60.338,136.9,30.915,136.9,67.999,51.542,68.057,31.332,60.661,48.354,23.577,133.713,18.717,144.901,30.915,144.901,49.583,144.901,48.171,149.6,45.065,159.942,55.863,159.901,110.859,159.693,122.931,159.647,118.184,148.547,75.354,48.396,68.057,31.332,68.057,31.332],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=Color(.137255,.121569,.12549,1)))
        g.add(Path(points=[67.999,51.542,110.829,151.693,55.833,151.9,60.338,136.9,30.915,136.9,67.999,51.542,68.057,31.332,60.661,48.354,23.577,133.713,18.717,144.901,30.915,144.901,49.583,144.901,48.171,149.6,45.065,159.942,55.863,159.901,110.859,159.693,122.931,159.647,118.184,148.547,75.354,48.396,68.057,31.332,68.057,31.332],operators=[0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))
        g.add(NoStrokePath(strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,operators=[0,1,1,1,1,1,3,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[130.127,51.542,169.085,136.901,140.826,136.901,144.8,151.901,89.639,151.621,130.127,51.542,129.685,31.304,122.711,48.541,82.223,148.62,77.797,159.559,89.599,159.62,144.759,159.9,155.209,159.953,152.533,149.851,151.221,144.9,169.084,144.9,181.529,144.9,176.362,133.579,137.405,48.22,129.685,31.304,129.685,31.304],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=0,fillColor=Color(.137255,.121569,.12549,1)))
        g.add(Path(points=[130.127,51.542,169.085,136.901,140.826,136.901,144.8,151.901,89.639,151.621,130.127,51.542,129.685,31.304,122.711,48.541,82.223,148.62,77.797,159.559,89.599,159.62,144.759,159.9,155.209,159.953,152.533,149.851,151.221,144.9,169.084,144.9,181.529,144.9,176.362,133.579,137.405,48.22,129.685,31.304,129.685,31.304],operators=[0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=None))

        g.transform = (1,0,0,-1,self.x+(s/20.0), (self.y+s)-(s/20.0))
        g.scale(float(float(s)/float(220)), float(float(s)/float(220)))

        return g


class DecommissionedSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (-1,0,0,-1,0,200)
        g.add(Path(points=[2425,6373,2364,6365,2243,6330,2186,6305,1986,6216,1799,6025,1727,5834,1664,5669,1666,5693,1662,5097,1659,4549,1687,4556,1770,4576,2576,4783,2658,4806,2680,4812,2680,4812,2680,5042,2680,5294,2684,5316,2740,5345,2782,5367,3616,5368,3659,5346,3722,5313,3720,5326,3720,4817,3720,4352,2848,4347,2027,4343,1965,4341,1815,4321,1624,4295,1612,4292,1489,4228,1234,4096,1055,3857,994,3567,983,3511,980,3355,980,2677,980,1791,980,1806,1034,1650,1126,1388,1365,1154,1631,1066,1777,1018,1739,1019,3240,1022,4645,1025,4733,1053,5091,1165,5340,1436,5414,1793,5428,1859,5430,1982,5430,2682,5430,3436,5428,3502,5411,3585,5345,3905,5099,4186,4795,4290,4745,4307,4740,4971,4734,5612,4733,5638,4713,5712,4624,6027,4408,6249,4093,6347,4005,6375,3230,6376,2804,6377,2442,6376,2425,6373,4050,6074,4235,6003,4367,5869,4432,5690,4455,5625,4458,4853,4461,4082,4533,4070,4795,4030,4982,3900,5090,3682,5147,3567,5152,3529,5157,3223,5162,2940,4643,2940,4124,2940,4107,3009,4084,3096,4022,3225,3965,3306,3869,3440,3714,3554,3547,3611,3391,3665,3328,3670,2859,3670,2430,3670,2430,3305,2430,2940,1839,2940,1248,2940,1252,3218,1257,3526,1262,3560,1326,3685,1377,3787,1449,3872,1538,3934,1638,4005,1714,4035,1852,4060,1959,4079,2005,4080,2982,4080,4000,4080,4000,4663,4000,5043,3996,5267,3989,5306,3966,5432,3880,5543,3763,5598,3705,5625,3200,5625,2695,5625,2638,5598,2558,5561,2486,5491,2447,5411,2416,5347,2415,5342,2410,5176,2405,5006,2355,4991,2328,4984,2223,4956,2123,4930,1940,4882,1940,5234,1940,5519,1943,5597,1955,5645,2001,5821,2115,5962,2273,6039,2399,6101,2371,6099,3220,6097,3983,6095,3996,6095,4050,6074,3374,3336,3520,3295,3647,3187,3714,3047,3734,3006,3750,2965,3750,2956,3750,2941,3708,2940,3260,2940,2770,2940,2770,3151,2770,3362,3043,3357,3256,3354,3328,3349,3374,3336,2430,2099,2430,1708,2893,1712,3351,1716,3356,1717,3450,1742,3584,1778,3659,1811,3755,1875,3934,1994,4070,2196,4117,2413,4133,2490,4647,2490,5160,2490,5160,2211,5160,1907,5152,1833,5106,1719,5031,1535,4873,1390,4673,1322,4595,1295,3205,1295,1815,1295,1735,1322,1517,1396,1355,1559,1283,1775,1256,1854,1256,1860,1252,2173,1249,2490,1839,2490,2430,2490,2430,2099,3754,2438,3712,2291,3594,2141,3478,2087,3365,2034,3324,2028,3038,2023,2770,2018,2770,2254,2770,2490,3269,2490,3769,2490,3754,2438],operators=[0,2,2,2,1,1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,1,1,2,3,0,2,1,1,1,1,2,2,1,1,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,1,1,2,1,1,2,2,2,2,3,0,2,2,2,1,1,1,1,2,3,0,1,1,2,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,3,0,2,2,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[570,4648,570,4325,786,4540,904,4658,1047,4803,1102,4863,1202,4970,886,4970,570,4970,570,4648],operators=[0,1,1,2,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[5458,4773,5563,4664,5705,4519,5774,4450,5900,4325,5900,4648,5900,4970,5584,4970,5268,4970,5458,4773],operators=[0,2,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[2973,323,3200,95,3427,323,3655,550,3200,550,2745,550,2973,323],operators=[0,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        g.transform = (1,0,0,1,self.x+(s/10.0), self.y+(s/15.0))
        g.scale(float(float(s)/float(8000)), float(float(s)/float(8000)))

        return g


#from http://smlt.wdfiles.com/local--files/shineshadowd%3Agyd4/%E8%A7%A3%E9%99%A4%E5%88%86%E7%BA%A7.svg

class DeclassifiedSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        #g.transform = (-1,0,0,-1,0,200)
        g.transform = (-1,0,0,-1,0,200)
        g.add(Path(points=[262.063,413.0795,250.5026,398.4833,252.1939,381.0037,266.3205,369.0773,275.1248,361.6443,294.42,348.8702,302.5648,345.0823,322.6032,335.7632,330.3655,330.2887,338.9152,319.4455,349.202,306.3994,348.0774,298.2683,335.7238,296.3705,332.5,295.8753,323.7697,311.1876,318.968,319.6094,314.6471,327.0938,314.1677,327.8195,313.4696,328.8763,310.9656,328.4325,301.5916,325.5908,289.8872,322.0426,284.9115,325.9757,278.3724,331.1446,263.8183,339.3028,254.7466,342.8845,212.6384,359.5097,166.4101,353.1803,130.2951,325.8449,123.6463,320.8125,112.6369,324.9139,104.2195,328.0497,101.4353,328.7192,100.811,327.7577,96.38922,320.9467,64.99448,265.7909,64.97718,264.8032,64.96463,264.0864,68.78347,259.9,73.46349,255.5,81.97261,247.5,80.79566,236.6709,76.74885,199.4365,91.84558,159.1833,119.7676,132.758,123.1046,129.5999,125.4311,126.7664,124.9377,126.4615,124.4442,126.1565,120.3591,120.4154,115.8595,113.7035,98.93868,88.46282,90.33292,64.65712,89.58056,41.00917,89.39629,35.21749,88.65868,30.03748,87.69377,27.75893,85.57043,22.74486,82.27694,10.61603,81.44587,4.75,80.77291,0,90.8674,0,100.9619,0,101.5482,2.75,113.0118,56.51478,166.9012,108.1124,247.4806,142.476,269.5424,151.8844,321.0648,167.3969,323.1179,165.249,323.5117,164.8371,326.1262,160.7875,328.9278,156.25,333.3063,149.1587,333.7487,148,332.0775,148,328.647,148,302.9021,143.0222,290,139.8644,273.2071,135.7542,247.1109,127.1894,230.8263,120.4435,211.5395,112.4539,190.9588,101.8254,188.564,98.61786,186.7023,96.12428,186.6615,95.69283,188.0521,93.20417,190.6286,88.59318,193.4805,89.17066,211.2065,97.89269,246.1343,115.0788,281.738,126.7495,319.5,133.3907,342.293,137.3993,339.9109,137.6325,344.2572,130.9665,350.5253,121.3528,374,75.64113,374,73.04905,374,72.68388,366.2033,72.57819,356.6739,72.8142,327.0752,73.54725,289.023,70.29395,258.8429,64.45003,212.7739,55.52949,168.3548,39.0305,138,19.56423,134.425,17.27161,130.8303,14.98898,130.0118,14.49171,127.9415,13.23389,133.7332,20.96142,142.0351,30.53367,149.249,38.85139,162.4198,50.90624,174.4092,60.16462,182.504,66.41561,183.5198,67.79266,182.6355,71.31636,181.8504,74.44411,178.6714,76.38532,175.5976,75.61384,168.5832,73.85334,137.3024,45.64647,125.5674,30.5,117.6598,20.2936,107,3.093091,107,.539838,107,.242927,115.5421,0,125.9824,0,144.9648,0,151.5101,4.006194,168.4276,14.36084,197.4883,27.10956,219.5,33.83285,266.7374,48.26114,318.4171,54.4362,370.765,51.90706,395.8694,50.69417,399.7462,50.95709,402.5572,54.06321,404.3356,56.02827,404.2478,58.25156,399.5474,130.2937,396.8845,171.1071,394.2095,205.5835,393.6029,206.9078,392.0909,210.2087,389.811,211.4204,386.6194,210.6193,382.1721,209.5031,381.8909,206.9432,383.5739,182.8991,384.4229,170.7713,384.9786,160.1736,384.8087,159.3486,384.6389,158.5236,379.8226,187.7918,374.1059,224.3891,364.0574,288.7164,363.7545,291.1311,364.998,296.9908,366.7753,305.3657,365.7611,314.3654,362.1399,322.3517,359.8322,327.4412,357.1655,330.8361,349.8871,337.95,344.7704,342.9511,338.2768,348.632,335.4569,350.5741,330.3297,354.1053,328.5699,364.3027,323.5041,393.6571,322.677,396,317.3803,396,311.4804,396,310.9141,391.7446,314.361,373.3117,316.6402,361.1235,313.0701,362.6143,305.0921,365.9457,286.4814,378.1816,279.25,384.8499,275.5846,388.2299,275,389.3303,275,392.8497,275,400.6824,284.7943,407.8918,301,411.9876,305.675,413.1692,310.1589,414.7803,310.9643,415.568,312.2359,416.8116,309.3197,417,288.7983,417,265.1681,417,219.7249,312.9912,241.1885,310.1382,262.918,298.0122,276.1449,281.5065,279.0126,277.9279,281.6959,275,282.1078,275,282.5197,275,285.5675,276.6148,288.8807,278.5885,294.5469,281.9638,298.4955,282.5069,296.0633,279.5763,295.4947,278.8911,293.3167,275.2147,291.2233,271.4063,287.6124,264.8372,287.4231,264.0465,287.5325,255.991,287.6695,245.8987,290.2439,232.8075,293.7251,224.5,295.8104,219.5238,296.1439,217.4742,295.6795,212.4877,294.8216,203.2749,294.9198,203.3761,285.6961,202.1986,281.1952,201.624,277.3695,201.2972,277.1943,201.4724,277.0192,201.6475,277.6102,205.3254,278.5078,209.6454,280.3734,218.6251,280.5863,229.9908,279.0388,238,277.5051,245.9376,274.0105,256,272.7874,256,272.2102,256,266.1834,252.8228,259.3945,248.9396,247.051,241.8793,250.0595,236.5485,253.0681,231.2177,244.284,230.634,216.714,228.8019,213.7315,228.753,214.5102,230.1453,217.1805,234.9201,234.5922,261.9785,235,261.9873,235.275,261.9933,236.7635,259.7484,238.3077,256.999,239.8519,254.2495,241.4947,252,241.9583,252,243.0292,252,264.0593,263.8969,265.805,265.4903,266.8601,266.4533,266.3276,267.671,263.0242,271.8502,254.8946,282.1348,240.8242,291.0915,226.4549,295.1287,209.8975,299.7806,189.4748,297.5679,174.0451,289.4503,161.6447,282.9265,146.3498,268.5929,149.2556,266.219,150.5828,265.1347,173.0448,252,173.5719,252,173.7439,252,175.1481,254.2495,176.6923,256.999,178.2365,259.7484,179.725,261.9932,180,261.9873,180.4874,261.9769,200.1326,231.6035,200.8719,229.7173,201.1,229.1355,197.8109,228.9969,192.3719,229.359,187.4924,229.6839,178.6447,230.2305,172.7104,230.5738,161.9208,231.1979,164.9081,236.4912,167.6898,241.4201,167.7786,241.8843,166.1978,243.232,164.4889,244.689,143.1782,257,142.3651,257,141.4235,257,138.1733,248.0627,136.536,240.9717,131.2216,217.9547,137.9213,192.924,154.0065,175.7001,157.876,171.5567,163.5381,166.5098,166.589,164.4847,169.6399,162.4596,171.993,160.6875,171.8181,160.5467,170.5923,159.5596,154.1544,151.4634,154.3069,151.9219,154.4127,152.2398,152.2786,154.525,149.5646,157,138.6005,166.9983,133.1585,174.2909,126.9157,187.3508,120.7877,200.1707,118.7841,209.2604,118.7272,224.5,118.6663,240.796,119.9466,246.56,127.6407,264.6299,127.9053,265.2513,125.1694,267.4108,121.5609,269.4288,117.9524,271.4468,115,273.5852,115,274.1809,115,275.8759,119.0486,282,120.1691,282,120.7224,282,123.9769,280.4331,127.4013,278.5181,133.6276,275.0361,138.5638,281.2267,148.4922,293.6781,164.551,304.4945,181.1838,309.9334,187.7496,312.0804,205.571,314.857,209.5,314.345,210.6,314.2017,215.2012,313.5925,219.7249,312.9912,353.4069,276.25,354.4393,271.2321,379.0002,113.5804,378.9916,112.0259,378.9866,111.1867,375.1184,117.7,370.3946,126.5,365.6708,135.3,361.0104,143.4,360.0383,144.5,359.0661,145.6,356.9918,148.75,355.4287,151.5,353.8657,154.25,348.679,162.8199,343.9028,170.5441,329.7583,193.419,312.5861,229.1687,309.5447,242.072,306.2117,256.2122,308.2093,264.8749,315.5261,268.0112,324.3961,271.8133,346.2108,278.3794,351.6705,278.8904,352.3143,278.9507,353.0957,277.7625,353.4069,276.25,216.4134,202.5231,221.136,193.4608,225,185.5858,225,185.0231,225,184.4604,222.8051,184,220.1224,184,214.2022,184,212.6498,182.47,213.1584,177.1364,213.5304,173.2351,208.6889,172.1175,201.8561,170.5403,202,170.4504,202,176.3,202,179.215,201.46,182.14,200.8,182.8,200.14,183.46,197.4025,184,194.7167,184,192.0308,184,189.9833,184.4316,190.1667,184.959,190.5928,186.185,207.4452,218.953,207.6634,218.9799,207.7533,218.991,211.6908,211.5854,216.4134,202.5231,310.3576,188.3762,311.3081,186.3831,311.9539,184.6412,311.7929,184.5053,311.6318,184.3695,305.875,182.8314,299,181.0875,273.4128,174.5969,237.3738,161.2493,214.8257,149.9124,210.4077,147.6911,206.6203,146.0464,206.4091,146.2575,205.4354,147.2313,217.6148,160.3511,224.914,166.1912,242.7137,180.4327,266.1836,188.4765,297,190.897,302.775,191.3506,307.7541,191.7843,308.0648,191.8609,308.3754,191.9374,309.4072,190.3693,310.3576,188.3762,194.9859,151.4796,193.2754,148.9933,190.5001,144.0193,188.8186,140.4261,185.8831,134.1531,185.3129,133.5943,174.493,126.3886,150.5249,110.4264,126.7441,88.95012,112.2218,70.1518,108.2498,65.01029,105,61.3347,105,61.98383,105,67.83568,118.6875,97.10696,124.8831,104.5046,126.8724,106.8798,129.625,110.7651,131,113.1386,137.0589,123.5972,154.6787,137.9151,171.5241,146.0688,180.0826,150.2113,194.5467,155.8671,196.798,155.9514,197.5775,155.9806,196.8535,154.1941,194.9859,151.4796,368.5405,409.75,368.8837,405.7625,371.767,363.9022,374.9479,316.7271,380.0717,240.7387,380.9355,230.7287,382.5207,228.9771,384.8549,226.3979,388.4629,226.4629,391.1323,229.1323,392.9908,230.9908,393.1946,232.0498,392.7201,237.3823,392.4208,240.747,389.5614,282.5375,386.366,330.25,380.5562,417,374.2364,417,367.9166,417],operators=[0,2,2,2,2,1,1,2,2,1,1,2,2,1,1,2,2,2,1,1,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,2,2,2,2,2,1,3,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,3,0,2,2,2,2,2,2,2,2,2,3,0,2,2,2,1,1,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))

        #g.transform = (1,0,0,1,self.x+(s/9.0), self.y+(s/29.0))
        g.transform = (1,0,0,-1,self.x+(s/9.0), (self.y+self.size)-(s/12.0))
        #g.scale(float(float(s)/float(517)), float(float(s)/float(467)))
        g.scale(float(float(s)/float(517)), float(float(s)/float(517)))

        return g


#from http://topia.wdfiles.com/local--files/peppo-wowow/daasElyon2.svg
#as used by https://scp-wiki.wikidot.com/scp-5338    

#Bit messed up, but only used once, so it's probably not worth spending too much time on.

class DaaselyonSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,-1,0,640)
        g.add(Path(points=[336.81,516.24,344.37,516.83,351.85,517.65,359.23,518.69,366.5,519.95,373.67,521.43,380.72,523.11,387.65,525.01,394.45,527.1,401.11,529.38,407.64,531.86,414.02,534.53,420.25,537.37,426.32,540.4,432.23,543.59,437.97,546.96,443.53,550.48,448.91,554.17,454.1,558.01,459.1,562,463.9,566.13,468.49,570.4,472.87,574.81,477.03,579.35,480.96,584.01,483.94,587.85,472.89,593.86,461.42,599.52,449.71,604.75,437.76,609.54,425.59,613.86,413.2,617.72,400.62,621.09,387.84,623.98,374.88,626.36,361.74,628.23,348.45,629.59,335.01,630.4,321.43,630.68,307.85,630.4,294.4,629.59,281.11,628.23,267.98,626.36,255.02,623.98,242.24,621.09,229.65,617.72,217.27,613.86,205.1,609.54,193.15,604.75,181.44,599.52,169.97,593.86,158.92,587.85,161.89,584.01,165.82,579.35,169.98,574.81,174.36,570.4,178.95,566.13,183.75,562,188.75,558.01,193.94,554.17,199.32,550.48,204.88,546.96,210.62,543.59,216.53,540.4,222.6,537.37,228.83,534.53,235.21,531.86,241.74,529.38,248.4,527.1,255.2,525.01,262.13,523.11,269.18,521.43,276.35,519.95,283.62,518.69,291,517.65,298.48,516.83,306.04,516.24,313.69,515.88,321.43,515.76,329.16,515.88,336.81,516.24],operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[372.85,247.93,443.62,183.28,507.82,124.63,414.8,286.96,321.42,449.92,228.04,286.96,135.03,124.64,199.22,183.28,269.99,247.94,289.51,158.51,321.42,12.23,353.34,158.51,372.85,247.93],operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=0,strokeColor=None,strokeLineCap=0,fillColor=Color(.113725,.243137,.529412,0)))
        #g.add(ClippingPath(strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[372.85,247.93,443.62,183.28,507.82,124.63,414.8,286.96,321.42,449.92,228.04,286.96,135.03,124.64,199.22,183.28,269.99,247.94,289.51,158.51,321.42,12.23,353.34,158.51,372.85,247.93],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=1,fillColor=None))
        g.add(Path(points=[372.85,247.93,443.62,183.28,507.82,124.63,414.8,286.96,321.42,449.92,228.04,286.96,135.03,124.64,199.22,183.28,269.99,247.94,289.51,158.51,321.42,12.23,353.34,158.51,372.85,247.93],operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=40,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=0,strokeColor=Color(0,0,0,1),strokeLineCap=0,fillColor=Color(0,0,0,0)))
        g.add(Path(points=[449.91,87.54,460.37,133.9,422.04,173.32,383.71,212.73,369.23,102.9,439.44,41.18,449.91,87.54],operators=[0,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=.99,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,.99)))
        g.add(Path(points=[449.91,87.54,460.37,133.9,422.04,173.32,383.71,212.73,369.23,102.9,439.44,41.18,449.91,87.54],operators=[0,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=0,strokeColor=Color(.207843,.713725,.12549,1),strokeLineCap=0,fillColor=Color(0,0,0,0)))
        g.add(Path(points=[434.76,325.5,437.17,329.93,439.41,334.46,441.47,339.09,443.36,343.81,445.07,348.62,446.6,353.52,447.93,358.49,449.07,363.54,450.01,368.66,450.75,373.85,451.29,379.11,451.61,384.42,451.72,389.79,451.61,395.15,451.29,400.47,450.75,405.72,450.01,410.91,449.07,416.03,447.93,421.08,446.6,426.06,445.07,430.95,443.36,435.76,441.47,440.48,439.41,445.11,437.17,449.64,434.76,454.07,432.19,458.4,429.46,462.61,426.57,466.71,423.53,470.7,420.34,474.56,417.01,478.29,413.54,481.9,409.94,485.37,406.2,488.7,402.34,491.89,398.36,494.93,394.25,497.81,390.04,500.55,385.71,503.12,381.28,505.53,376.75,507.77,372.12,509.83,367.4,511.72,362.59,513.43,357.7,514.96,352.72,516.29,347.67,517.43,342.55,518.37,337.36,519.11,332.11,519.65,326.79,519.97,321.43,520.08,316.06,519.97,310.75,519.65,305.49,519.11,300.3,518.37,295.18,517.43,290.13,516.29,285.16,514.96,280.26,513.43,275.45,511.72,270.73,509.83,266.1,507.77,261.57,505.53,257.14,503.12,252.81,500.55,248.6,497.81,244.5,494.93,240.51,491.89,236.65,488.7,232.92,485.37,229.31,481.9,225.84,478.29,222.51,474.56,219.32,470.7,216.29,466.71,213.4,462.61,210.66,458.4,208.09,454.07,205.68,449.64,203.44,445.11,201.38,440.48,199.49,435.76,197.78,430.95,196.26,426.06,194.92,421.08,193.78,416.03,192.84,410.91,192.1,405.72,191.56,400.47,191.24,395.15,191.13,389.79,191.19,385.84,191.37,381.91,191.66,378.02,192.06,374.17,192.58,370.34,193.2,366.55,193.93,362.8,194.77,359.09,195.72,355.42,196.77,351.79,197.92,348.21,199.17,344.67,200.51,341.18,201.96,337.74,203.5,334.35,205.13,331.01,206.86,327.72,208.67,324.49,210.57,321.32,212.56,318.21,213.19,317.29,228.04,343.21,321.42,506.17,414.8,343.21,429.66,317.28,432.19,321.17,434.76,325.5],operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=.99,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,.99)))
        g.add(Path(points=[190.23,87.54,200.7,41.18,270.91,102.9,256.43,212.73,218.1,173.32,179.77,133.9,190.23,87.54],operators=[0,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=.99,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,.99)))
        g.add(Path(points=[190.23,87.54,200.7,41.18,270.91,102.9,256.43,212.73,218.1,173.32,179.77,133.9,190.23,87.54],operators=[0,1,1,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=0,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=0,strokeColor=Color(.207843,.713725,.12549,1),strokeLineCap=0,fillColor=Color(0,0,0,0)))
        ##g.add(Path(points=[575.54,766.58,575.54,906.82,461.67,1020.68,321.43,1020.68,181.18,1020.68,67.32,906.82,67.32,766.58,67.32,626.33,181.18,512.47,321.43,512.47,461.67,512.47,575.54,626.33,575.54,766.58],operators=[0,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=.99,strokeColor=None,strokeLineCap=0,fillColor=Color(.011765,.039216,.098039,.99)))
        g.add(ClippingPath(strokeDashArray=None,strokeWidth=2.9,strokeMiterLimit=0,operators=[0,1,1,1,1,1,1,1,1,1,1,1,1,3],strokeOpacity=1,strokeLineJoin=0,points=[372.85,247.93,443.62,183.28,507.82,124.63,414.8,286.96,321.42,449.92,228.04,286.96,135.03,124.64,199.22,183.28,269.99,247.94,289.51,158.51,321.42,12.23,353.34,158.51,372.85,247.93],fillOpacity=1,autoclose=None,strokeColor=None,strokeLineCap=0,isClipPath=1,fillColor=None))

        #g.transform = (1,0,0,-1,self.x, (self.y+(self.size/2)))
        g.transform = (0.8,0,0,-0.8, self.x+(s*0.1), (self.y+(s*0.8)))
        g.scale(float(float(s)/float(640)), float(float(s)/float(640)))
        return g


#from https://scp-wiki.wdfiles.com/local--files/calibri-s-mega-cool-art-page-it-s-mostly-just-icons-but-what/Terminal.svg
#https://scp-wiki.wikidot.com/scp-5523

class TerminalSymbol(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.transform = (1,0,0,1,0,0)
        g.transform = (1,0,0,-1,0,200)
        g.add(Path(points=[94,184.5,94,179.4,93.7,178,92.5,178,90.1,178,90.7,171.8,93.6,166.6,95.9,162.4,96.5,162,99.8,162,103.2,162,103.7,162.4,106.3,167,109.3,172.5,109.9,178,107.5,178,106.5,178,106,179.6,105.8,184.3,105.5,190.5,99.8,190.8,94,191.1,94,184.5],operators=[0,2,2,2,2,2,2,1,1,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[78.5,146.8,74.8,144.7,74.1,142.7,74,134.9,74,128.1,73.8,127.1,71.4,124.9,63.3,117.4,59,106.5,59,93.6,59,74.8,67.9,60.9,83.7,55,88.7,53.1,91.1,52.9,101.5,53.2,112.3,53.5,114.1,53.8,119.2,56.3,126.9,60.1,133.6,67,137.4,75,140.3,81.1,140.5,82.2,140.5,93.5,140.5,104.9,140.3,105.8,137.3,112.2,135.6,115.8,132.4,120.6,130.1,122.9,126,127,126,127,126,134.6,126,141.6,125.8,142.4,123.1,145.1,120.2,148,100.3,148,87.3,147.9,79.8,147.5,78.5,146.8,91,121.1,91,119.4,91.5,117.8,92,117.5,94.2,116.2,92.8,115.5,88.4,115.9,85.1,116.1,84.1,116.5,84.9,117.3,85.5,117.9,86,119.7,86,121.2,86,123.5,86.4,124,88.5,124,90.6,124,91,123.5,91,121.1,114,120.6,114,118.7,114.6,117,115.3,116.7,115.9,116.5,114.4,116.1,111.8,115.9,107.2,115.5,105.8,116.1,108,117.5,108.6,117.8,109,119.4,109,121.1,109,123.5,109.4,124,111.5,124,113.7,124,114,123.6,114,120.6,101.2,104.4,100.5,94.1,104.3,90,114.3,90,120.5,90,124.3,92.3,126.4,97.4,127.7,100.5,128.4,96,130.6,82.1,114.7,64.8,99.8,64.8,93,64.8,83.2,69.7,78.5,75.5,72.3,83,69.5,93.6,72,99.5,72.8,101.3,72.9,101.3,72.9,99.7,73,96.6,76.2,92.2,79.2,90.9,80.8,90.3,84.5,90,87.6,90.2,91.9,90.6,93.7,91.3,95.8,93.4,98.2,95.8,98.5,96.8,98.5,103,98.5,108.6,98.8,110,100,110,101.2,110,101.4,108.9,101.2,104.4],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,3,0,2,2,2,2,2,2,3,0,2,2,2,2,2,2,3,0,2,2,1,1,2,2,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[30,70.8,30,69.1,28.7,67.8,25,65.7,20.6,63.2,20,62.5,20,59.7,20.1,55,22,53,26.6,53,28.7,53,31.4,53.7,32.4,54.5,33.5,55.3,36.1,56,38.1,56,41.5,56,42.1,56.4,45,61.1,47.1,64.6,48,67.2,47.8,69.4,47.5,72.5,38.8,72.8,30.2,73.1,30,73,30,70.8],operators=[0,2,2,2,2,2,2,2,1,1,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        g.add(Path(points=[152,69,152,66.5,153,63.5,154.7,60.5,157.1,56.6,157.9,56,161,56,162.9,55.9,165.6,55.3,167,54.5,168.4,53.7,171.2,53.1,173.2,53,177.4,53,179,54.9,179,59.9,179,62.4,178.3,63.3,174.5,65.6,171.1,67.5,170,68.8,170,70.6,170,73,169.8,73,161,73,152,73,152,69],operators=[0,2,2,2,2,2,2,2,2,1,1,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(0,0,0,1)))
        #g.add(Path(points=[0,100,0,0,100,0,200,0,200,100,200,200,100,200,0,200,0,100,102.8,181.3,103,176.6,103.5,175,104.5,175,105.6,175,105.3,173.8,103.2,170,101.7,167.3,100.2,165,99.8,165,99.3,165,94,173.7,94,174.6,94,174.8,94.7,175,95.5,175,96.7,175,97,176.4,97,181.6,97,188.1,99.8,187.8,102.4,187.5,102.5,187.2,102.8,181.3,120.1,142.1,122.8,139.4,123,138.6,123,131.6,123,124,123,124,127.1,119.9,129.4,117.6,132.6,112.8,134.3,109.2,137.1,103.2,137.5,101.5,137.5,93.5,137.5,85.5,137.1,83.8,134.4,78,130.6,70,123.9,63.1,116.2,59.3,108.3,55.4,95.2,54.8,86.7,58,67.8,65.1,57.8,85.5,63.8,104.8,65.8,111,70,117.8,74.4,121.9,76.8,124.1,77,125.1,77,131.9,77.1,144.3,78.2,144.9,100.3,145,117.2,145,120.1,142.1,44.7,69.1,44.9,69.1,43.6,66.7,41.8,63.9,39.3,59.8,38.5,59.1,37.8,60.4,37.1,61.7,36.3,61.5,31.9,59,26,55.5,25.8,55.4,24.3,57.9,23.2,59.7,23.6,60.2,28.6,63,32.6,65.4,33.9,66.6,33.5,67.9,33.1,69.3,33.8,69.5,38.8,69.4,41.9,69.3,44.6,69.2,44.7,69.1,166,68.1,165.2,66.4,165.7,65.8,170.5,63.1,175.4,60.3,175.9,59.7,175,58,173.6,55.5,173.6,55.5,167.4,59,162.8,61.6,162.1,61.7,161.5,60.2,161,58.9,160.2,59.6,157.9,63.3,156.3,65.9,155,68.4,155,69,155,69.6,157.7,70,161,70,166.7,70,167,69.9,166,68.1],operators=[0,1,1,1,1,1,1,1,1,3,0,2,2,2,2,2,2,1,1,2,3,0,2,2,2,2,2,2,2,2,2,2,2,1,1,3,0,2,2,2,2,2,2,2,2,3,0,2,2,2,2,2,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))
        g.add(Path(points=[93.5,137.8,93.3,137.1,92.9,134.5,92.8,132,92.5,127.7,92.3,127.5,89.3,127.2,87.5,127,86,127.2,85.9,127.7,85.9,128.1,85.8,130.4,85.7,132.8,85.7,135.1,85.3,137,84.9,137,83.6,137,83,133.9,83,127.8,83,121.9,82.9,121.6,78.1,116.9,71.4,110.4,68.6,104.3,68.2,95.3,67.4,81.5,73.6,70.8,85.7,64.8,91.5,62,93.4,61.5,100,61.6,109.8,61.6,116.2,64.4,122.8,71.4,135.2,84.5,134.8,104.4,121.9,116.5,117.1,121,117,121.2,117,127.1,117,130.4,116.4,134.1,115.8,135.3,114.6,137.3,114.5,137.1,114,132.5,113.5,127.5,113.5,127.5,110,127.5,106.5,127.5,106.2,133.3,106,136.4,105.5,139,105,139,104.5,139,104,136.4,103.8,133.3,103.5,127.5,100,127.5,96.5,127.5,96.2,133.3,95.9,138.5,94.6,140.8,93.5,137.8,105.2,122.4,105.9,121.8,101.2,113,100.2,113,99.1,113,94.1,121.7,94.7,122.4,95.5,123.2,104.5,123.2,105.2,122.4,92.2,110.1,96.4,106.4,96.8,100.5,93.1,96.6,85.1,88.1,71.8,97.7,77.4,107.9,80.5,113.5,87.3,114.5,92.2,110.1,120.9,109.5,124.8,105.7,124.5,99.7,120.2,95.9,115.3,91.5,108.3,92.5,105.4,98.1,100.1,108.5,112.7,117.8,120.9,109.5],operators=[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,1,1,2,3,0,2,2,2,3,0,2,2,2,3,0,2,2,2,3],isClipPath=0,autoclose=None,strokeDashArray=None,strokeWidth=1,strokeMiterLimit=0,strokeOpacity=1,strokeLineJoin=0,fillOpacity=1,strokeColor=None,strokeLineCap=0,fillColor=Color(1,1,1,1)))

        #g.transform = (0.8,0,0,-0.8, self.x+(s*0.1), (self.y+(s*0.9)))
        #g.transform = (0.95,0,0,-0.95, self.x+(s*0.05), (self.y+(s*0.95)))
        g.transform = (1.05,0,0,-1.05, self.x-(s*0.02), self.y+(s*1.03))
        g.scale(float(float(s)/float(200)), float(float(s)/float(200)))
        return g


class DARK(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()
        
        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=green_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = DARKSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class VLAM(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=blue_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = VLAMSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class KENEQ(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=yellow_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = KENEQSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class EKHI(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=orange_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = EKHISymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class AMIDA(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=red_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = AMIDASymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

#RiskClass

class Notice(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=green_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = NoticeSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Caution(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=blue_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = CautionSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Warning(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=yellow_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = WarningSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Danger(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=orange_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = DangerSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Critical(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=red_bar_colour, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = CriticalSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#ObjectClass (The less common ones)
        
class Thaumiel(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = ThaumielSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Esoteric(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = EsotericSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Pending(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.black, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = PendingSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Neutralized(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.grey, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = NeutralizedSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Archon(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = ArchonSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Zeno(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = ZenoSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Apollyon(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = ApollyonSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Hiemal(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = HiemalSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Tiamat(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = TiamatSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Ticonderoga(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = TiconderogaSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Enochian(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = EnochianSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Gevurah(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = GevurahSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Cernnunos(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = CernnunosSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g

class Godel(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = GodelSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Hera(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = HeraSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Anomalous(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = AnomalousSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#from http://scp-wiki.wdfiles.com/local--files/component%3Aacs-peppo-lite/truculent-icon3.svg

class Truculent(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = TruculentSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#from http://scp-wiki.wdfiles.com/local--files/scp-3906/numen.svg

class Numen(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = NumenSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#from http://www.scp-wiki.net/local--files/calibri-s-mega-cool-art-page-it-s-mostly-just-icons-but-what/Decommissioned%20Icon

class Decommissioned(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = DecommissionedSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#from http://smlt.wdfiles.com/local--files/shineshadowd%3Agyd4/%E8%A7%A3%E9%99%A4%E5%88%86%E7%BA%A7.svg

class Declassified(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = DeclassifiedSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


class Explained(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = ExplainedSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g



#from http://topia.wdfiles.com/local--files/peppo-wowow/daasElyon2.svg
#as used by https://scp-wiki.wikidot.com/scp-5338    

class Daaselyon(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=colors.white, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        symbol = DaaselyonSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        return g


#from https://scp-wiki.wdfiles.com/local--files/calibri-s-mega-cool-art-page-it-s-mostly-just-icons-but-what/Terminal.svg
#https://scp-wiki.wikidot.com/scp-5523

class Terminal(_Symbol):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 100
        self.strokeWidth = 6

    def draw(self):
        # general widget bits
        s = float(self.size)  # abbreviate as we will use this a lot
        g = shapes.Group()

        symbol = TerminalSymbol()
        symbol.size = (s/100)*100
        symbol.x = (self.x+(s/2.0))-(symbol.size/2.0)
        symbol.y = self.y
        g.add(symbol)

        g.add(shapes.Circle(cx=self.x+(s/2), cy=self.y+(s/2), r=s/2,
                fillColor=None, strokeColor=colors.black,
                strokeWidth=max(s/38.,self.strokeWidth)))

        return g



def test():
    """
    This function produces a number of pdf files with examples of all
    the signs and symbols from this file.
    """
    labelFontSize = 10


    #PAGE 1

    #DangerDiamonds are a bit messed up - they work fine on our door signage though.

    D = shapes.Drawing(450,650)

    cb = Safe()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Euclid()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Keter()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss1 = DangerDiamond()
    ss1.x = 20
    ss1.y = 400
    D.add(ss1)
    D.add(shapes.String(ss1.x+(ss1.size/2), ss1.y-(1.2*labelFontSize),
                            ss1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss2 = DangerDiamond()
    ss2.x = 170
    ss2.y = 400

    ss2.DisruptionClass = "DARK"
    ss2.RiskClass = "Notice"
    ss2.ObjectClass = "Safe"

    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss3 = DangerDiamond()
    ss3.x = 320
    ss3.y = 400

    ss3.DisruptionClass = "AMIDA"
    ss3.RiskClass       = "Critical"
    ss3.ObjectClass     = "Keter"
    ss3.SecondaryClass  = "Hera"

    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ne = SafeLock()
    ne.x = 20
    ne.y = 270
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    sf = EuclidLock()
    sf.x = 170
    sf.y = 270
    D.add(sf)
    D.add(shapes.String(sf.x+(sf.size/2),(sf.y-(1.2*labelFontSize)),
                            sf.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ds = KeterLock()
    ds.x = 320
    ds.y = 270
    D.add(ds)
    D.add(shapes.String(ds.x+(ds.size/2),(ds.y-(1.2*labelFontSize)),
                            ds.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    na = Thaumiel()
    na.x = 20
    na.y = 140
    D.add(na)
    D.add(shapes.String(na.x+(na.size/2),(na.y-(1.2*labelFontSize)),
                            na.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ns = Pending()
    ns.x = 170
    ns.y = 140
    D.add(ns)
    D.add(shapes.String(ns.x+(ns.size/2),(ns.y-(1.2*labelFontSize)),
                            ns.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fd = SCPLogo()
    fd.x = 320
    fd.y = 140
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (and other common symbols)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))


    renderPDF.drawToFile(D, 'SCP_widgets_1.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1.pdf')


    #PAGE 1B
    D = shapes.Drawing(450,650)

    cb = Thaumiel()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Pending()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Neutralized()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss1 = ThaumielSymbol()
    ss1.x = 20
    ss1.y = 400
    D.add(ss1)
    D.add(shapes.String(ss1.x+(ss1.size/2), ss1.y-(1.2*labelFontSize),
                            ss1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss2 = PendingSymbol()
    ss2.x = 170
    ss2.y = 400

    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss3 = NeutralizedSymbol()
    ss3.x = 320
    ss3.y = 400

    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ne = Esoteric()
    ne.x = 20
    ne.y = 270
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    nx = Archon()
    nx.x = 170
    nx.y = 270
    D.add(nx)
    D.add(shapes.String(nx.x+(nx.size/2),(nx.y-(1.2*labelFontSize)),
                            nx.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    fx = Zeno()
    fx.x = 320
    fx.y = 270
    D.add(fx)
    D.add(shapes.String(fx.x+(fx.size/2),(fx.y-(1.2*labelFontSize)),
                            fx.__class__.__name__+" *", fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    sf = EsotericSymbol()
    sf.x = 20
    sf.y = 140
    D.add(sf)
    D.add(shapes.String(sf.x+(sf.size/2),(sf.y-(1.2*labelFontSize)),
                            sf.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    sq = ArchonSymbol()
    sq.x = 170
    sq.y = 140
    D.add(sq)
    D.add(shapes.String(sq.x+(sq.size/2),(sq.y-(1.2*labelFontSize)),
                            sq.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fq = ZenoSymbol()
    fq.x = 320
    fq.y = 140
    D.add(fq)
    D.add(shapes.String(fq.x+(fq.size/2),(fq.y-(1.2*labelFontSize)),
                            fq.__class__.__name__+" *", fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    D.add(shapes.String(450/2,26+(labelFontSize*6),
                        "* Uses standard 'Esoteric' class symbol, since no specific class symbol could be found.",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*0.75))

    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (continued)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))


    renderPDF.drawToFile(D, 'SCP_widgets_1B.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1B.pdf')


    #PAGE 1C
    D = shapes.Drawing(450,650)

    cb = Apollyon()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Hiemal()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Tiamat()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss1 = ApollyonSymbol()
    ss1.x = 20
    ss1.y = 400
    D.add(ss1)
    D.add(shapes.String(ss1.x+(ss1.size/2), ss1.y-(1.2*labelFontSize),
                            ss1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss2 = HiemalSymbol()
    ss2.x = 170
    ss2.y = 400

    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss3 = TiamatSymbol()
    ss3.x = 320
    ss3.y = 400

    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ne = Ticonderoga()
    ne.x = 20
    ne.y = 270
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a2 = Gevurah()
    a2.x = 320
    a2.y = 270
    D.add(a2)
    D.add(shapes.String(a2.x+(a2.size/2),(a2.y-(1.2*labelFontSize)),
                            a2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    nx = Enochian()
    nx.x = 170
    nx.y = 270
    D.add(nx)
    D.add(shapes.String(nx.x+(nx.size/2),(nx.y-(1.2*labelFontSize)),
                            nx.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    na = TiconderogaSymbol()
    na.x = 20
    na.y = 140
    D.add(na)
    D.add(shapes.String(na.x+(na.size/2),(na.y-(1.2*labelFontSize)),
                            na.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fd = EnochianSymbol()
    fd.x = 170
    fd.y = 140
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fd = GevurahSymbol()
    fd.x = 320
    fd.y = 140
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (continued/2)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))

    renderPDF.drawToFile(D, 'SCP_widgets_1C.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1C.pdf')



    #PAGE 1D

    D = shapes.Drawing(450,650)

    cb = Cernnunos()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Godel()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Hera()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss1 = CernnunosSymbol()
    ss1.x = 20
    ss1.y = 400
    D.add(ss1)
    D.add(shapes.String(ss1.x+(ss1.size/2), ss1.y-(1.2*labelFontSize),
                            ss1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss2 = GodelSymbol()
    ss2.x = 170
    ss2.y = 400

    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss3 = HeraSymbol()
    ss3.x = 320
    ss3.y = 400

    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a2 = Null()
    a2.x = 320
    a2.y = 270
    D.add(a2)
    D.add(shapes.String(a2.x+(a2.size/2),(a2.y-(1.2*labelFontSize)),
                            a2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    sf = ExplainedSymbol()
    sf.x = 20
    sf.y = 270
    D.add(sf)
    D.add(shapes.String(sf.x+(sf.size/2),(sf.y-(1.2*labelFontSize)),
                            sf.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    nx = Explained()
    nx.x = 170
    nx.y = 270
    D.add(nx)
    D.add(shapes.String(nx.x+(nx.size/2),(nx.y-(1.2*labelFontSize)),
                            nx.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    fd = SCPLogo()
    fd.x = 20
    fd.y = 140
    fd.fillColor = colors.red
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fd = SCPLogo()
    fd.x = 170
    fd.y = 140
    fd.fillColor = colors.green
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    fd = SCPLogo()
    fd.x = 320
    fd.y = 140
    fd.fillColor = colors.blue
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (continued/3)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))


    renderPDF.drawToFile(D, 'SCP_widgets_1D.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1D.pdf')




    #PAGE 1E

    D = shapes.Drawing(450,650)

    cb = Anomalous()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Truculent()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Numen()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss1 = AnomalousSymbol()
    ss1.x = 20
    ss1.y = 400
    D.add(ss1)
    D.add(shapes.String(ss1.x+(ss1.size/2), ss1.y-(1.2*labelFontSize),
                            ss1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss2 = TruculentSymbol()
    ss2.x = 170
    ss2.y = 400

    D.add(ss2)
    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss3 = NumenSymbol()
    ss3.x = 320
    ss3.y = 400

    D.add(ss3)
    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ne = Decommissioned()
    ne.x = 20
    ne.y = 270
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    fd = DecommissionedSymbol()
    fd.x = 20
    fd.y = 140
    D.add(fd)
    D.add(shapes.String(fd.x+(fd.size/2),(fd.y-(1.2*labelFontSize)),
                            fd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    dde = Declassified()
    dde.x = 170
    dde.y = 270
    D.add(dde)
    D.add(shapes.String(dde.x+(dde.size/2),(dde.y-(1.2*labelFontSize)),
                            dde.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ddd = DeclassifiedSymbol()
    ddd.x = 170
    ddd.y = 140
    D.add(ddd)
    D.add(shapes.String(ddd.x+(ddd.size/2),(ddd.y-(1.2*labelFontSize)),
                            ddd.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ddg = Daaselyon()
    ddg.x = 320
    ddg.y = 270
    D.add(ddg)
    D.add(shapes.String(ddg.x+(ddg.size/2),(ddg.y-(1.2*labelFontSize)),
                            ddg.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ddf = DaaselyonSymbol()
    ddf.x = 320
    ddf.y = 140
    D.add(ddf)
    D.add(shapes.String(ddf.x+(ddf.size/2),(ddf.y-(1.2*labelFontSize)),
                            ddf.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (continued/4)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))

    renderPDF.drawToFile(D, 'SCP_widgets_1E.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1E.pdf')




    #PAGE 1F

    D = shapes.Drawing(450,650)

    txb = Terminal()
    txb.x = 20
    txb.y = 530
    D.add(txb)
    D.add(shapes.String(txb.x+(txb.size/2),(txb.y-(1.2*labelFontSize)),
                           txb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

##    tb = Truculent()
##    tb.x = 170
##    tb.y = 530
##    D.add(tb)
##    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
##                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
##                            fontSize=labelFontSize))
##
##
##    yn = Numen()
##    yn.x = 320
##    yn.y = 530
##    D.add(yn)
##    tempstring = yn.__class__.__name__
##    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
##                            tempstring, fillColor=colors.black, textAnchor='middle',
##                            fontSize=labelFontSize))


    st1 = TerminalSymbol()
    st1.x = 20
    st1.y = 400
    D.add(st1)
    D.add(shapes.String(st1.x+(st1.size/2), st1.y-(1.2*labelFontSize),
                            st1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

##    ss2 = TruculentSymbol()
##    ss2.x = 170
##    ss2.y = 400
##
##    D.add(ss2)
##    D.add(shapes.String(ss2.x+(ss2.size/2), ss2.y-(1.2*labelFontSize),
##                            ss2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
##                            fontSize=labelFontSize))
##
##    ss3 = NumenSymbol()
##    ss3.x = 320
##    ss3.y = 400
##
##    D.add(ss3)
##    D.add(shapes.String(ss3.x+(ss3.size/2), ss3.y-(1.2*labelFontSize),
##                            ss3.__class__.__name__, fillColor=colors.black, textAnchor='middle',
##                            fontSize=labelFontSize))

    D.add(shapes.String(450/2,26,
                        "OBJECT CLASSES (continued/5)",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))

    renderPDF.drawToFile(D, 'SCP_widgets_1F.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_1F.pdf')




    #PAGE 2
    D = shapes.Drawing(450,650)

    cb = DARK()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = VLAM()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    yn = KENEQ()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ss = EKHI()
    ss.x = 20
    ss.y = 400
    D.add(ss)
    D.add(shapes.String(ss.x+(ss.size/2), ss.y-(1.2*labelFontSize),
                            ss.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ne = AMIDA()
    ne.x = 170
    ne.y = 400
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ds = DARKSymbol()
    ds.x = 20
    ds.y = 270
    D.add(ds)
    D.add(shapes.String(ds.x+(ds.size/2),(ds.y-(1.2*labelFontSize)),
                            ds.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    na = VLAMSymbol()
    na.x = 170
    na.y = 270
    D.add(na)
    D.add(shapes.String(na.x+(na.size/2),(na.y-(1.2*labelFontSize)),
                            na.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ns = KENEQSymbol()
    ns.x = 320
    ns.y = 270
    D.add(ns)
    D.add(shapes.String(ns.x+(ns.size/2),(ns.y-(1.2*labelFontSize)),
                            ns.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a1 = EKHISymbol()
    a1.x = 20
    a1.y = 140
    D.add(a1)
    D.add(shapes.String(a1.x+(a1.size/2),(a1.y-(1.2*labelFontSize)),
                            a1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a2 = AMIDASymbol()
    a2.x = 170
    a2.y = 140
    D.add(a2)
    D.add(shapes.String(a2.x+(a2.size/2),(a2.y-(1.2*labelFontSize)),
                            a2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    D.add(shapes.String(450/2,26,
                        "DISRUPTION CLASS SYMBOLS",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))


    renderPDF.drawToFile(D, 'SCP_widgets_2.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_2.pdf')


    #PAGE 3
    D = shapes.Drawing(450,650)

    cb = Notice()
    cb.x = 20
    cb.y = 530
    D.add(cb)
    D.add(shapes.String(cb.x+(cb.size/2),(cb.y-(1.2*labelFontSize)),
                           cb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                           fontSize=labelFontSize))

    tb = Caution()
    tb.x = 170
    tb.y = 530
    D.add(tb)
    D.add(shapes.String(tb.x+(tb.size/2),(tb.y-(1.2*labelFontSize)),
                            tb.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    yn = Warning()
    yn.x = 320
    yn.y = 530
    D.add(yn)
    tempstring = yn.__class__.__name__
    D.add(shapes.String(yn.x+(tb.size/2),(yn.y-(1.2*labelFontSize)),
                            tempstring, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ss = Danger()
    ss.x = 20
    ss.y = 400
    D.add(ss)
    D.add(shapes.String(ss.x+(ss.size/2), ss.y-(1.2*labelFontSize),
                            ss.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ne = Critical()
    ne.x = 170
    ne.y = 400
    D.add(ne)
    D.add(shapes.String(ne.x+(ne.size/2),(ne.y-(1.2*labelFontSize)),
                            ne.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))


    ds = NoticeSymbol()
    ds.x = 20
    ds.y = 270
    D.add(ds)
    D.add(shapes.String(ds.x+(ds.size/2),(ds.y-(1.2*labelFontSize)),
                            ds.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    na = CautionSymbol()
    na.x = 170
    na.y = 270
    D.add(na)
    D.add(shapes.String(na.x+(na.size/2),(na.y-(1.2*labelFontSize)),
                            na.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    ns = WarningSymbol()
    ns.x = 320
    ns.y = 270
    D.add(ns)
    D.add(shapes.String(ns.x+(ns.size/2),(ns.y-(1.2*labelFontSize)),
                            ns.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a1 = DangerSymbol()
    a1.x = 20
    a1.y = 140
    D.add(a1)
    D.add(shapes.String(a1.x+(a1.size/2),(a1.y-(1.2*labelFontSize)),
                            a1.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    a2 = CriticalSymbol()
    a2.x = 170
    a2.y = 140
    D.add(a2)
    D.add(shapes.String(a2.x+(a2.size/2),(a2.y-(1.2*labelFontSize)),
                            a2.__class__.__name__, fillColor=colors.black, textAnchor='middle',
                            fontSize=labelFontSize))

    D.add(shapes.String(450/2,26,
                        "RISK CLASS SYMBOLS",
                        fillColor=colors.black, textAnchor='middle',
                        fontSize=labelFontSize*2))

    renderPDF.drawToFile(D, 'SCP_widgets_3.pdf', 'scp_widgets.py')
    print('wrote file: SCP_widgets_3.pdf')


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
    if MAKE_ELEMENTS > 0:
        make_elements()

