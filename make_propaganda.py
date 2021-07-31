#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""create signage for various offices, containment suites and other
such areas."""

#Unless otherwise stated, SCP logos taken from:
#http://www.scpwiki.com/component:anomaly-class-bar

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.

VERBOSE = 1
VERBOSE = 0

import random, string, os

import base, intercom_messages, scp_widgets


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

from reportlab.graphics.shapes import *
#from reportlab.graphics.shapes import Drawing, Group, Path, Ellipse, Circle, Polygon
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from reportlab.graphics import renderPM
from reportlab.graphics import renderPDF   # in case we want PDFs of these things one day...

#register fonts
#pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'BAUHS93.TTF')))
pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'Bauhaus_Demi.ttf')))
#pdfmetrics.registerFont(TTFont('Verdana Bold', os.path.join("fonts", 'verdanab.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova', os.path.join("fonts", 'GillSansNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Bold', os.path.join("fonts", 'GillSansBoNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond', os.path.join("fonts", 'GillSansCondNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond Bold', os.path.join("fonts", 'GillSansCondBoNova.ttf')))
pdfmetrics.registerFont(TTFont('OCR A', os.path.join("fonts", 'OCRAEXT.TTF')))

MAKE_PDFS = 0
MAKE_PDFS = 1

#default screen size in our game =
#gui.init(1920, 1080)
height = 1080
width = 720
margin = 24

    
THISDIR = os.getcwd()

if not os.path.isdir(os.path.join(THISDIR, "images")):
    os.mkdir(os.path.join(THISDIR, "images"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images")
if not os.path.isdir(os.path.join(THISDIR, "images", "signage")):
    os.mkdir(os.path.join(THISDIR, "images", "signage"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images", "signage")
if not os.path.isdir(os.path.join(THISDIR, "images", "signage", "areas")):
    os.mkdir(os.path.join(THISDIR, "images", "signage", "areas"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images", "signage", "areas")
os.chdir(os.path.join(THISDIR, "images", "signage", "breakrooms"))

OUTDIR = os.path.join(THISDIR, "images", "signage", "breakrooms")



def make_base_sign():
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    #now use a widget rather than a png file.
    #LOGO  = os.path.join(THISDIR, "images", "SCP_Foundation_logo_3000x3000.png")

    LOGOWIDTH = 165
    LOGOHEIGHT = 165

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.white, strokeColor=colors.white))
    d.add(Rect(0, height-350, width, 350, fillColor=colors.yellow, strokeColor=colors.yellow))

    #white rectangle
    #d.add(Rect(0, height-600, width, 250, fillColor=colors.white, strokeColor=colors.white))
    #d.add(Rect(0, 0, width, height-350, fillColor=colors.white, strokeColor=colors.white))

    d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=180, fillColor=colors.black))
    d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=48, fillColor=colors.black))

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.x = 425
    lg.y = height-210
    d.add(lg)

    return d

def make_sign_1(colour):
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    LOGOWIDTH = 125
    LOGOHEIGHT = 125

    #fontSize = 84
    fontSize = 108
    topy = height - 350

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.black, strokeColor=colors.black))

    for word in ["Secure.", "Contain.", "Protect."]:
        d.add(String(width/2.0, topy, word, fontName="Bauhaus Demi", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
#        d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
        topy = topy - (fontSize * 1.5)

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.fillColor = colour
    lg.x = width-LOGOWIDTH-(margin*2)
    lg.y = margin*2
    d.add(lg)

    return d

def make_sign_2(colour):
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    LOGOWIDTH = 125
    LOGOHEIGHT = 125

    #fontSize = 108
    #fontSize = 84
    fontSize = 72
    #topy = height - 350
    topy = height - 390

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.black, strokeColor=colors.black))



    for word in ["We die in the dark", "so you can live", "in the light."]:
        d.add(String(width/2.0, topy, word, fontName="Bauhaus Demi", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
#        d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
        topy = topy - (fontSize * 1.5)

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.fillColor = colour
    lg.x = width-LOGOWIDTH-(margin*2)
    lg.y = margin*2
    d.add(lg)

    return d


def make_sign_3(colour):
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    LOGOWIDTH = 125
    LOGOHEIGHT = 125

    #fontSize = 108
    #fontSize = 84
    fontSize = 72
    #topy = height - 350
    topy = height - 390

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.black, strokeColor=colors.black))

    for word in ["STAY VIGILANT.", "", "STAY SAFE."]:
        d.add(String(width/2.0, topy, word, fontName="Bauhaus Demi", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
#        d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
        topy = topy - (fontSize * 1.5)

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.fillColor = colour
    lg.x = width-LOGOWIDTH-(margin*2)
    lg.y = margin*2
    d.add(lg)

    return d


def make_sign_4(colour):
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    LOGOWIDTH = 125
    LOGOHEIGHT = 125

    #fontSize = 108
    #fontSize = 84
    #fontSize = 72
    fontSize = 50
    #topy = height - 350
    #topy = height - 390
    #topy = height - 250
    topy = height - 300

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.black, strokeColor=colors.black))

    for word in ["LOOSE LIPS LOSE SKIPS", "", "MAINTAIN OPERATIONAL", "SECURITY", "", "YOU NEVER KNOW", "WHO'S LISTENING"]:
        d.add(String(width/2.0, topy, word, fontName="Bauhaus Demi", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
#        d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
        topy = topy - (fontSize * 1.5)

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.fillColor = colour
    lg.x = width-LOGOWIDTH-(margin*2)
    lg.y = margin*2
    d.add(lg)

    return d


def make_sign_0(colour):
    # KEEP CALM AND APOLYON
    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    textcolour = colors.Color(250.0/255.0, 250.0/255.0, 250.0/255.0)

    #LOGOWIDTH = 125
    #LOGOHEIGHT = 125
    LOGOWIDTH = 250
    LOGOHEIGHT = 250

    #fontSize = 108
    #fontSize = 84
    #fontSize = 72
    fontSize = 100
    #topy = height - 350
    #topy = height - 390
    #topy = height - 250
    topy = height - 450

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colour, strokeColor=colors.black))

    for word in ["KEEP", "CALM", "AND", "APOLLYON"]:
        if word == "AND":
            d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize/1.75, fillColor=textcolour, textAnchor='middle'))
        else:
            d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=textcolour, textAnchor='middle'))

#        d.add(String(width/2.0, topy, word, fontName="Gill Sans Nova Bold", fontSize=fontSize, fillColor=colour, textAnchor='middle'))
        topy = topy - (fontSize * 1.5)

    #lg = scp_widgets.ApollyonSymbol()
    lg = scp_widgets.Apollyon()
    lg.size = LOGOWIDTH
    lg.fillColor = textcolour
    lg.x = (width/2)-(LOGOWIDTH/2)
    lg.y = height-(margin*2)-LOGOWIDTH
    d.add(lg)

    return d



def save_sign(d,text):
    filename_stub       = string.lower(string.replace(text, " ", "_"))
    #filename_stub       = "area_sign_%s" % (filename_stub)
    filename_stub       = string.replace(filename_stub, "\n", "")
    outfn = os.path.join(OUTDIR, filename_stub)
    renderPM.drawToFile(d, '%s.png' % outfn, 'PNG')
    if VERBOSE>0:
        print "WROTE '%s.png'" % outfn
    else:
        print ".",

    if MAKE_PDFS == 1:
        renderPDF.drawToFile(d, '%s.pdf' % outfn, text)
        if VERBOSE>0:
            print "WROTE '%s.pdf'" % outfn
        else:
            print ".",
    if VERBOSE >0:
        print


def run():
    print "Creating 'Propaganda' signage..."

    num_signs_made = 0
    d = make_sign_1(colour=colors.white)
    fnstub = "Propaganda_1A"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    fnstub = "Propaganda_1B"
    d = make_sign_1(colour=colors.yellow)
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    d = make_sign_2(colour=colors.white)
    fnstub = "Propaganda_2A"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    fnstub = "Propaganda_2B"
    d = make_sign_2(colour=colors.yellow)
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    d = make_sign_3(colour=colors.white)
    fnstub = "Propaganda_3A"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    fnstub = "Propaganda_3B"
    d = make_sign_3(colour=colors.yellow)
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    d = make_sign_4(colour=colors.white)
    fnstub = "Propaganda_4A"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    fnstub = "Propaganda_4B"
    d = make_sign_4(colour=colors.yellow)
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    calmred = colors.Color(208.0/255.0 ,0, 0)
    calmblack = colors.Color(3/255.0 ,3/255.0 , 3/255.0 )
    calmblue = colors.Color(17.0/255.0, 33.0/255.0, 72.0/255.0)

    d = make_sign_0(colour=calmred)
    fnstub = "Keep_Calm_1"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    d = make_sign_0(colour=calmblack)
    fnstub = "Keep_Calm_2"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1

    d = make_sign_0(colour=calmblue)
    fnstub = "Keep_Calm_3"
    save_sign(d,fnstub)
    num_signs_made = num_signs_made + 1


    if VERBOSE == 0:
        print

    print "Made %s signs in directory '%s'" % (num_signs_made, OUTDIR)


if __name__== "__main__":
    run()
    print "\nDONE.\n\n"