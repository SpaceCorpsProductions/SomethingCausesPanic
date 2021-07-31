#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""uses the reportlab toolkit to create door/locker
signs for all known SCPs with a known object class."""

#Unless otherwise stated, SCP logos taken from:
#http://www.scpwiki.com/component:anomaly-class-bar

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.


import os, string, random, copy

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
from reportlab.graphics.shapes import *

from reportlab.graphics import renderPM
from reportlab.graphics import renderPDF   # in case we want PDFs of these things one day...

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

import scp_widgets, hazard_widgets, objects
from objects import KNOWN_SCPS_DICT, GetRisks 

#register fonts
#pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'BAUHS93.TTF')))
pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'Bauhaus_Demi.ttf')))
#pdfmetrics.registerFont(TTFont('Verdana Bold', os.path.join("fonts", 'verdanab.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova', os.path.join("fonts", 'GillSansNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Bold', os.path.join("fonts", 'GillSansBoNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond', os.path.join("fonts", 'GillSansCondNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond Bold', os.path.join("fonts", 'GillSansCondBoNova.ttf')))
pdfmetrics.registerFont(TTFont('OCR A', os.path.join("fonts", 'OCRAEXT.TTF')))

#turn off unicode warnings... ugh.
import warnings
warnings.filterwarnings(action="ignore", category=UnicodeWarning)

MAKE_PDFS = 0
MAKE_PDFS = 1

USE_LOG = 1
USE_LOG = 0

VERBOSE = 1
VERBOSE = 0


THISDIR = os.getcwd()

if not os.path.isdir(os.path.join(THISDIR, "images")):
    os.mkdir(os.path.join(THISDIR, "images"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images")
if not os.path.isdir(os.path.join(THISDIR, "images", "signage")):
    os.mkdir(os.path.join(THISDIR, "images", "signage"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images", "signage")
if not os.path.isdir(os.path.join(THISDIR, "images", "signage", "containment")):
    os.mkdir(os.path.join(THISDIR, "images", "signage", "containment"))
    print "CREATED DIRECTORY '%s'" % os.path.join(THISDIR, "images", "signage", "containment")
os.chdir(os.path.join(THISDIR, "images", "signage", "containment"))


def run(USE_LOG=0):

    print "\nMaking door/locker signs..."
    num_signs_made = 0

    #zero it, get rid of anything from previous runs...
    if USE_LOG == 1:
        logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "w")
        logfile.close()

    #set up some custom colours...

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
    # /EKHI/Danger
    orange_background_colour = colors.Color(255.0/255.0,
                                            233.0/255.0,
                                            217.0/255.0)

    orange_bar_colour = colors.Color(255.0/255.0,
                                     109.0/255.0,
                                     0.0/255.0)


    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24

    #now use a widget rather than a png file.
    #LOGO  = os.path.join(THISDIR, "images", "SCP_Foundation_logo_3000x3000.png")

    LOGOWIDTH = 165
    LOGOHEIGHT = 165

    OUR_SCPS = copy.copy(KNOWN_SCPS_DICT.keys())
    OUR_SCPS.sort()

    for scp in OUR_SCPS:
        if not KNOWN_SCPS_DICT[scp].has_key("object_class"):
            OUR_SCPS.remove(scp)
        if KNOWN_SCPS_DICT[scp]["object_class"] in [None, ""]:
            OUR_SCPS.remove(scp)

    # Make doubly sure these don't get created - they don't have any content (ie have
    # no "object_class", "disruption_class" or "risk_class" attributes), but
    # somehow get missed by the above tests...            
    TO_EXCLUDE = ["SCP-4613", "SCP-4787", "SCP-5678",
                  "SCP-4487" # class is 'Spiritual' - unique, and not one we have a logo for
                  "SCP-4317", "SCP-3682"#, 
                  ]

    for scp in OUR_SCPS:
        if scp in TO_EXCLUDE:
            OUR_SCPS.remove(scp)


    print "%s VALID SCPs found (ie SCPs with a defined class)..." % len(OUR_SCPS)


    #Now make the signs...

    name                = None
    OBJECT_CLASS        = None

    DISRUPTION_CLASS    = None
    RISK_CLASS          = None

    for scp in OUR_SCPS:
        name                = KNOWN_SCPS_DICT[scp]["item_name"]
        OBJECT_CLASS        = KNOWN_SCPS_DICT[scp]["object_class"]

        DISRUPTION_CLASS    = KNOWN_SCPS_DICT[scp]["disruption_class"]
        RISK_CLASS          = KNOWN_SCPS_DICT[scp]["risk_class"]


        if KNOWN_SCPS_DICT[scp].has_key("secondary_class"):
            SECONDARY_CLASS = KNOWN_SCPS_DICT[scp]["secondary_class"]
            SECONDARY_CLASS = string.upper(SECONDARY_CLASS)
            secondary_class_line = "SECONDARY CLASS: %s" % (SECONDARY_CLASS)
        else:
            SECONDARY_CLASS = None
            secondary_class_line = None

        if OBJECT_CLASS in objects.ESOTERIC_CLASSES:
            #print "!!! ESOTERIC OBJECT !!! "
            #print "!!! (CLASS: '%s' !!! )" % OBJECT_CLASS
            #print name
            if USE_LOG == 1:
                logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                logfile.write("!!! ESOTERIC OBJECT !!!\n")
                try:
                    logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS)
                except UnicodeEncodeError:
                    try:
                        logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS.encode("utf-8"))
                    except UnicodeEncodeError:
                        try:
                            logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS.encode("latin-1"))
                        except UnicodeEncodeError:
                            logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS.encode("ASCII", ignore))
                logfile.write("%s\n\n"% name)
                logfile.close()
            else:
                pass

        if OBJECT_CLASS == "EXPLAINED":
            if USE_LOG == 1:
                logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                logfile.write("!!! EXPLAINED OBJECT !!!\n")
                logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS)
                logfile.write("%s\n\n"% name)
                logfile.close()
        if OBJECT_CLASS == "DECOMMISSIONED":
            if USE_LOG == 1:
                logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                logfile.write("!!! DECOMMISSIONED OBJECT !!!\n")
                logfile.write("!!! (CLASS: '%s' !!! )\n" % OBJECT_CLASS)
                logfile.write("%s\n\n"% name)
                logfile.close()

        if SECONDARY_CLASS != None:
            #print "!!! SECONDARY CLASS !!! "
            #print "!!! (CLASS: '%s' !!! )" % SECONDARY_CLASS
            #print name
            if USE_LOG == 1:
                logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                logfile.write("!!! SECONDARY CLASS !!!\n")
                try:
                    logfile.write("!!! (CLASS: '%s' !!! )\n" % SECONDARY_CLASS)
                except UnicodeEncodeError:
                    try:
                        logfile.write("!!! (CLASS: '%s' !!! )\n" % SECONDARY_CLASS.encode("utf-8"))
                    except UnicodeEncodeError:
                        try:
                            logfile.write("!!! (CLASS: '%s' !!! )\n" % SECONDARY_CLASS.encode("latin-1"))
                        except UnicodeEncodeError:
                            logfile.write("!!! (CLASS: '%s' !!! )\n" % SECONDARY_CLASS.encode("ASCII", "ignore"))
                logfile.write("%s\n\n"% name)
                logfile.close()
            else:
                pass

        if OBJECT_CLASS in ["", None]:
            OBJECT_CLASS = ""
        else:
            OBJECT_CLASS = string.upper(OBJECT_CLASS)

        DISRUPTION_CLASS    = KNOWN_SCPS_DICT[scp]["disruption_class"]
        RISK_CLASS          = KNOWN_SCPS_DICT[scp]["risk_class"]

        filename_stub       = string.split(KNOWN_SCPS_DICT[scp]["filename"], ".")[0]
        filename_stub       = "%s_door_sign" % (filename_stub)

        object_class_line = "OBJECT CLASS: %s" % OBJECT_CLASS

        roomnum = random.randint(0,99999)
        BARCODE_LINE = "LOCATION #%05d / %s / %s" % (roomnum, name, OBJECT_CLASS)
        #BARCODE_LINE = BARCODE_LINE.encode("ASCII", ignore)
        try:
            if string.find(BARCODE_LINE, "ö") >-1:
                #BARCODE_LINE = string.replace(BARCODE_LINE, "ö", "o")
                BARCODE_LINE = BARCODE_LINE.encode("utf-8")
            if string.find(BARCODE_LINE, "\xc3\xb6") >-1:
                #BARCODE_LINE = string.replace(BARCODE_LINE, "\xc3\xb6", "O")
                BARCODE_LINE = BARCODE_LINE.encode("utf-8")
        except:
            BARCODE_LINE = BARCODE_LINE.encode("ASCII", "ignore")
        if DISRUPTION_CLASS == None:
            DISRUPTION_CLASS = ""
        if RISK_CLASS == None:
            RISK_CLASS = ""

        d = Drawing(width, height)
        d.add(Rect(0, 0, width, height, fillColor=colors.white, strokeColor=colors.white))
        d.add(Rect(margin, margin, (width-(margin*2)), (height-(margin*2)), fillColor=colors.yellow, strokeColor=colors.yellow))

        #white rectangle
        d.add(Rect(0, height-600, width, 250, fillColor=colors.white, strokeColor=colors.white))

        #d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=180, fillColor=colors.black))
        d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=220, fillColor=colors.black))
        #d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=48, fillColor=colors.black))
        d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=52, fillColor=colors.black))

        lg = scp_widgets.SCPLogo()
        lg.size = LOGOWIDTH
        #lg.x = 425
        #lg.y = height-210
        lg.x = 465
        lg.y = height-190
        d.add(lg)

        #SCP-nnn line
        if string.find(object_class_line, "THAUMIEL") > -1:
            d.add(String(margin*1.45,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "APOLLYON") > -1:
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "KRONECKER") > -1:
            d.add(String(margin*1.45,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "ESOTERIC") > -1:
            d.add(String(margin*1.50,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "DAMBALLAH") > -1:
            #d.add(String(margin*1.45,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
            d.add(String(margin*1.45,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=82, fillColor=colors.black))
        elif string.find(object_class_line, "TICONDEROGA") > -1:
            #d.add(String(margin*1.40,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
            d.add(String(margin*1.40,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=82, fillColor=colors.black))
        elif string.find(object_class_line, "DECLASSIFIED") > -1:
            d.add(String(margin*1.40,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=82, fillColor=colors.black))
        elif string.find(object_class_line, "UNCONTAINED") > -1:
            d.add(String(margin*1.40,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=82, fillColor=colors.black))
        elif string.find(object_class_line, "GEVURAH") > -1:
            d.add(String(margin*1.50,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))

        elif string.find(object_class_line, "PENDING") > -1:
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "NEUTRALIZED") > -1:
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "DECOMMISSIONED") > -1:
            #d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
            #d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=70, fillColor=colors.black))
            d.add(String(margin*1.40,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "UNKNOWN") > -1:
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif string.find(object_class_line, "EXPLAINED") > -1:
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        elif "G\xc3\xb6DEL" in object_class_line.encode("UTF-8", "ignore"):
            d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
        else:
            d.add(String(margin*2,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))

        # MAIN 'OBJECT CLASS' LINE
        if SECONDARY_CLASS == None:
            if string.find(object_class_line, "PENDING") > -1:
                d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=80, fillColor=colors.black))
            elif string.find(object_class_line, "THAUMIEL") > -1:
                d.add(String(margin*1.45,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
            elif string.find(object_class_line, "APOLLYON") > -1:
                d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
            elif string.find(object_class_line, "KRONECKER") > -1:
                d.add(String(margin*1.45,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
            elif string.find(object_class_line, "ESOTERIC") > -1:
                d.add(String(margin*1.50,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=73, fillColor=colors.black))
            elif string.find(object_class_line, "DAMBALLAH") > -1:
                d.add(String(margin*1.45,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
            elif string.find(object_class_line, "TICONDEROGA") > -1:
                d.add(String(margin*1.40,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=68, fillColor=colors.black))
            elif string.find(object_class_line, "DECLASSIFIED") > -1:
                d.add(String(margin*1.40,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=68, fillColor=colors.black))
            elif string.find(object_class_line, "UNCONTAINED") > -1:
                d.add(String(margin*1.40,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=68, fillColor=colors.black))
            elif string.find(object_class_line, "UNKNOWN") > -1:
                d.add(String(margin*1.40,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=68, fillColor=colors.black))
            elif string.find(object_class_line, "GEVURAH") > -1:
                d.add(String(margin*1.50,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=73, fillColor=colors.black))
            elif string.find(object_class_line, "DECOMMISSIONED") > -1:
                #d.add(String(margin*1.50,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=73, fillColor=colors.black))
                #d.add(String(margin*1.50,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
                d.add(String(margin*1.40,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
                if USE_LOG == 1:
                    logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                    logfile.write("!!! DECOMMISSIONED OBJECT !!!\n")
                    logfile.write("%s\n\n"% name)
                    logfile.close()
                else:
                    pass
            elif string.find(object_class_line, "EXPLAINED") > -1:
                d.add(String(margin*1.50,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=73, fillColor=colors.black))
                if USE_LOG == 1:
                    logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                    logfile.write("!!! EXPLAINED OBJECT !!!\n")
                    logfile.write("%s\n\n"% name)
                    logfile.close()
                else:
                    pass

            elif string.find(object_class_line, "NEUTRALIZED") > -1:
                d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
                #print "!!! NEUTRALIZED OBJECT !!! "
                #print name
                #print
                if USE_LOG == 1:
                    logfile = open("make_door_signage_INTERESTING_LOG_FILE.txt", "a")
                    logfile.write("!!! NEUTRALIZED OBJECT !!!\n")
                    logfile.write("%s\n\n"% name)
                    logfile.close()
                else:
                    pass

            else:
                d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=84, fillColor=colors.black))


        #LEFT HAND BOX...

        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

        if OBJECT_CLASS == "SAFE":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=green_background_colour, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=green_bar_colour, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "SAFE", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Safe()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "EUCLID":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=yellow_background_colour, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=yellow_bar_colour, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "EUCLID", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Euclid()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "KETER":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=red_background_colour, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=red_bar_colour, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "KETER", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Keter()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "PENDING":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "PENDING", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Pending()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "THAUMIEL":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "THAUMIEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Thaumiel()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "NEUTRALIZED":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "NEUTRALIZED", fontName="Gill Sans Nova Bold", fontSize=28, fillColor=colors.black))

            cw = scp_widgets.Neutralized()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "ESOTERIC":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "ESOTERIC", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "ARCHON":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "ARCHON", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Archon()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "APOLLYON":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "APOLLYON", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Apollyon()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "ZENO":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "ZENO", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Zeno()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "HIEMAL":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "HIEMAL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Hiemal()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "KRONECKER":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "KRONECKER", fontName="Gill Sans Nova Bold", fontSize=30, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "HERA":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "HERA", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Hera()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "EPARCH":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "EPARCH", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "TICONDEROGA":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), "TICONDEROGA", fontName="Gill Sans Nova Bold", fontSize=32, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.86), "TICONDEROGA", fontName="Gill Sans Nova Bold", fontSize=26, fillColor=colors.black))

            cw = scp_widgets.Ticonderoga()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "DECLASSIFIED":
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.86), "DECLASSIFIED", fontName="Gill Sans Nova Bold", fontSize=26, fillColor=colors.black))

            cw = scp_widgets.Declassified()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if string.find(object_class_line, "DAMBALLAH") > -1:
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), "DAMBALLAH", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "DAMBALLAH", fontName="Gill Sans Nova Bold", fontSize=32, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if string.find(object_class_line, "TIAMAT") > -1:
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "TIAMAT", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Tiamat()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if string.find(object_class_line, "GEVURAH") > -1:
            #d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "GEVURAH", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Gevurah()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "N/A":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "N/A", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Null()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "NULL":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "NULL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Null()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "NONE":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "NONE", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Null()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "UNKNOWN":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "UNKNOWN", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Null()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "UNCONTAINED":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "UNCONTAINED", fontName="Gill Sans Nova Bold", fontSize=26, fillColor=colors.black))

            cw = scp_widgets.Null()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)


        if OBJECT_CLASS == "DECOMMISSIONED":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.86), "DECOMMISSIONED", fontName="Gill Sans Nova Bold", fontSize=21, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.86), "DECOMMISSIONED", fontName="Gill Sans Nova Bold", fontSize=22, fillColor=colors.black))

            cw = scp_widgets.Decommissioned()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "EXPLAINED":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "EXPLAINED", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Explained()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "YESOD":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.85), "YESOD", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS == "G\xc3\xb6DEL":
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"G\xc3\xb6DEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"G\xc3\xb6DEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.83), u"GÖDEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Esoteric()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)

        if OBJECT_CLASS in ["Gödel", u"Gödel", "Godel", u"G\xf6del", "G\xf6del",
                            "GöDEL", "GÖDEL", "GODEL", "GÖDEL",
                            u"GöDEL", u"GÖDEL", u"GODEL", u"GÖDEL"]:
            d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
            #d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))
            d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.black, strokeColor=colors.black))

            d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"G\xc3\xb6DEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL".encode("UTF-8", "ignore"), fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            #d.add(String(margin*4.5,(margin*6.85), u"GÖDEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))
            d.add(String(margin*4.5,(margin*6.83), u"GÖDEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

            cw = scp_widgets.Godel()
            cw.x = margin*5.75
            cw.y = (margin*11.5)
            cw.size = 150
            d.add(cw)


        if SECONDARY_CLASS != None:

##            if string.find(object_class_line, "THAUMIEL") > -1:
##                d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=60, fillColor=colors.black))
##            else:
##                d.add(String(margin*2,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=60, fillColor=colors.black))

            if string.find(object_class_line, "PENDING") > -1:
                d.add(String(margin*2,(height-515), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
            elif string.find(object_class_line, "THAUMIEL") > -1:
                d.add(String(margin*1.55,(height-515), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
            elif string.find(object_class_line, "NEUTRALIZED") > -1:
                d.add(String(margin*1.55,(height-515), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
            else:
                d.add(String(margin*2,(height-515), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))


            ##NEW
            ##SECONDARY CLASS LINE...
            #secondary_class_line = "SECONDARY CLASS: %s" % SECONDARY_CLASS

            if string.find(secondary_class_line, "TICONDEROGA") > -1:
                #d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=45, fillColor=colors.black))

                #different X settings, but all use a fontSize of 50
                if string.find(object_class_line, "PENDING") > -1:
                    d.add(String(margin*2,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=50, fillColor=colors.black))
                elif string.find(object_class_line, "THAUMIEL") > -1:
                    d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=50, fillColor=colors.black))
                elif string.find(object_class_line, "NEUTRALIZED") > -1:
                    d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=50, fillColor=colors.black))
                elif string.find(object_class_line, "TICONDEROGA") > -1:
                    d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=50, fillColor=colors.black))
                else:
                    d.add(String(margin*2,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=50, fillColor=colors.black))
                    #d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))

            elif string.find(object_class_line, "PENDING") > -1:
                d.add(String(margin*2,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
            elif string.find(object_class_line, "THAUMIEL") > -1:
                d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))
            elif string.find(object_class_line, "NEUTRALIZED") > -1:
                d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))

            elif string.find(object_class_line, "TICONDEROGA") > -1:
                d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=45, fillColor=colors.black))

            elif string.find(object_class_line, "UNCONTAINED") > -1:
                d.add(String(margin*1.55,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=45, fillColor=colors.black))

            else:
                d.add(String(margin*2,(height-580), secondary_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=60, fillColor=colors.black))


        #RIGHT HAND BOX...

        #d.add(Rect((width/2.0)+margin, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
        d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

        #DISRUPTION CLASS
        d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
        d.add(String((width/2.0)+margin*2.5,(margin*7.95), "DISRUPTION CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
        d.add(String((width/2.0)+margin*2.5,(margin*6.95), DISRUPTION_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

        bar1FillColour = None

        if DISRUPTION_CLASS == None:
            bar1FillColour = None
        elif DISRUPTION_CLASS == "DARK":
            bar1FillColour = green_bar_colour
            dclass = scp_widgets.DARK()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS == "VLAM":
            bar1FillColour = blue_bar_colour
            dclass = scp_widgets.VLAM()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS == "KENEQ":
            bar1FillColour = yellow_bar_colour
            dclass = scp_widgets.KENEQ()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS == "EKHI":
            bar1FillColour = orange_bar_colour
            dclass = scp_widgets.EKHI()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS == "AMIDA":
            bar1FillColour = red_bar_colour
            dclass = scp_widgets.AMIDA()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS in ["NONE", "None", "NULL", "Null", "N/A", "N/a", "Unknown"]:
            bar1FillColour = colors.lightgrey
            dclass = scp_widgets.Null()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)
        elif DISRUPTION_CLASS == "GEVURAH":
            tmp_pink = colors.Color(215.0/255.0,
                                    6.0/255.0,
                                    111.0/255.0)
            bar1FillColour = tmp_pink
            dclass = scp_widgets.Gevurah()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))-2
            dclass.size = 40
            d.add(dclass)

        if bar1FillColour != None:
            d.add(Rect((width/2.0)+margin, margin*6.35, margin, 65, fillColor=bar1FillColour, strokeColor=None))

        #RISK CLASS
        d.add(Rect((width/2.0)+margin, (margin*6.35)+65, (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
        d.add(String((width/2.0)+margin*2.5,(margin*7.95)+65, "RISK CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
        d.add(String((width/2.0)+margin*2.5,(margin*6.95)+65, RISK_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

        bar2FillColour = None

        if RISK_CLASS == None:
            bar2FillColour = None
        elif RISK_CLASS == "Notice":
            bar2FillColour = green_bar_colour
            dclass = scp_widgets.Notice()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)
        elif RISK_CLASS == "Caution":
            bar2FillColour = blue_bar_colour
            dclass = scp_widgets.Caution()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)
        elif RISK_CLASS == "Warning":
            bar2FillColour = yellow_bar_colour
            dclass = scp_widgets.Warning()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)
        elif RISK_CLASS == "Danger":
            bar2FillColour = orange_bar_colour
            dclass = scp_widgets.Danger()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)
        elif RISK_CLASS == "Critical":
            bar2FillColour = red_bar_colour
            dclass = scp_widgets.Critical()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)

        elif RISK_CLASS in ["NONE", "None", "NULL", "Null", "N/A", "N/a"]:
            bar2FillColour = colors.lightgrey
            dclass = scp_widgets.Null()
            dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
            dclass.y = ((margin*6.95))+65-2
            dclass.size = 40
            d.add(dclass)

        if bar2FillColour != None:
            d.add(Rect((width/2.0)+margin, (margin*6.35)+65, margin, 65, fillColor=bar2FillColour, strokeColor=None))

        #OCTANCT GRAPHIC
        #"Danger Diamond"
        d.add(Rect((width/2.0)+margin, (margin*6.35)+130, (width/2.0)-margin*4, 170, fillColor=colors.white, strokeColor=colors.black))

        dd = scp_widgets.DangerDiamond()
        #dd.x = (width/2.0)+(margin*3.25)+15
        dd.x = (width/2.0)+(margin*3.25)+7
        dd.y = (margin*6.45)+142
        dd.size = 150

        dd.DisruptionClass = DISRUPTION_CLASS
        dd.RiskClass = RISK_CLASS
        dd.ObjectClass = OBJECT_CLASS

        if SECONDARY_CLASS != None:
            dd.SecondaryClass = SECONDARY_CLASS

        d.add(dd)


# moved to scp_widgets.py
##        if SECONDARY_CLASS != None:
##            ##NEW
##            ##SECONDARY CLASS LOGO ON DANGER DIAMOND
##
##            #default logo is Esoteric
##            sscw = scp_widgets.Esoteric()
##
##            if SECONDARY_CLASS == "ARCHON":
##                sscw = scp_widgets.Archon()
##            elif SECONDARY_CLASS == "APOLLYON":
##                sscw = scp_widgets.Apollyon()
##            elif SECONDARY_CLASS in ["CERNUNNOS", "CERNNUNOS"]:
##                sscw = scp_widgets.Cernnunos()
##            elif SECONDARY_CLASS == "THAUMIEL":
##                sscw = scp_widgets.Thaumiel()
##            elif SECONDARY_CLASS == "NEUTRALIZED":
##                sscw = scp_widgets.Neutralized()
##            elif SECONDARY_CLASS == "PENDING":
##                sscw = scp_widgets.Pending()
##            elif SECONDARY_CLASS == "HIEMAL":
##                sscw = scp_widgets.Hiemal()
##            elif SECONDARY_CLASS == "TIAMAT":
##                sscw = scp_widgets.Tiamat()
##            elif SECONDARY_CLASS == "TICONDEROGA":
##                sscw = scp_widgets.Ticonderoga()
##            elif SECONDARY_CLASS in ["N/A", "NULL"]:
##                sscw = scp_widgets.Null()
##            elif SECONDARY_CLASS == "GEVURAH":
##                sscw = scp_widgets.Gevurah()
##            elif SECONDARY_CLASS == "ENOCHIAN":
##                sscw = scp_widgets.Enochian()
##            elif SECONDARY_CLASS == "KETER":
##                sscw = scp_widgets.Keter()
##            elif SECONDARY_CLASS in ["Gödel", u"Gödel", "Godel",
##                                     u"G\xf6del", "G\xf6del",
##                                     u"GöDEL", "GODEL", u"G\xf6del".upper(),
##                                     "G\xf6del".upper()]:
##                sscw = scp_widgets.Godel()
##            elif SECONDARY_CLASS == "HERA":
##                sscw = scp_widgets.Hera()
##            elif SECONDARY_CLASS == "ANOMALOUS":
##                sscw = scp_widgets.Anomalous()
##            elif SECONDARY_CLASS == "TRUCULENT":
##                sscw = scp_widgets.Truculent()
##            elif SECONDARY_CLASS == "NUMEN":
##                sscw = scp_widgets.Numen()
##
##            elif SECONDARY_CLASS in ["ZENO", "KRONECKER", "EPARCH", "DAMBALLAH"]:
##                sscw = scp_widgets.Esoteric()
##
##            sscw.x = (width/2.0)+(margin*5.55)+7
##            sscw.y = (margin*6.45)+157
##            sscw.size = 40
##            d.add(sscw)



        #BARCODE
        from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing, createBarcodeImageInMemory

        dr = createBarcodeDrawing('Code128', humanReadable=1, value=BARCODE_LINE, validate=0)
        dr_width = dr.width

        #white barcode rectangle
        d.add(Rect(margin*3, margin*2, width-margin*6, 80, fillColor=colors.white, strokeColor=None))

        if OBJECT_CLASS == "NEUTRALIZED":
            dr.scale(2.05, 1.35)
            dr_width = dr.width * 2.05
        elif OBJECT_CLASS == "TICONDEROGA":
            dr.scale(2.05, 1.35)
            dr_width = dr.width * 2.05
        elif OBJECT_CLASS == "DECLASSIFIED":
            dr.scale(2.05, 1.35)
            dr_width = dr.width * 2.05
        elif OBJECT_CLASS == "DECOMMISSIONED":
            dr.scale(1.95, 1.35)
            dr_width = dr.width * 1.95
        else:
            dr.scale(2.25, 1.35)
            dr_width = dr.width * 2.25

        #dr_xpos = ((width-dr.width)/2.0)
        dr_xpos = ((width-dr_width)/2.0)
        #dr_xpos = ((dr.width)/2.6)-margin


    ##    if OBJECT_CLASS == "EUCLID":
    ##        dr.translate(margin*2.75,margin*2.55)
    ##    elif OBJECT_CLASS == "SAFE":
    ##        dr.translate(margin*3.05,margin*2.55)
    ##
    ##    elif OBJECT_CLASS == "KETER":
    ##        dr.translate(margin*2.95,margin*2.55)
    ##
    ##    elif OBJECT_CLASS == "NEUTRALIZED":
    ##        dr.translate(margin*2.65,margin*2.55)
    ##    elif OBJECT_CLASS == "APOLLYON":
    ##        dr.translate(margin*2.70,margin*2.55)
    ##
    ##    else:
    ##        dr.translate(margin*2.75,margin*2.55)

        #dr.translate(dr_xpos, margin*2.55)
        dr.translate(dr_xpos/2.25, margin*1.95)

        d.add(dr)

        renderPM.drawToFile(d, '%s.png' % filename_stub, 'PNG')
        num_signs_made = num_signs_made + 1
        if VERBOSE > 0:
            print "WROTE '%s.png'" % filename_stub
        else:
            print ".",
        if MAKE_PDFS == 1:
            renderPDF.drawToFile(d, '%s.pdf' % filename_stub, name)
            num_signs_made = num_signs_made + 1
            if VERBOSE > 0:
                print "WROTE '%s.pdf'" % filename_stub
            else:
                print ".",
        if VERBOSE > 0:
            print


        # CREATE A SEPARATE FILE FOR A WARNING SIGN ("WARNING: RADIACTIVE" etc)

        this_sign_risks = GetRisks(KNOWN_SCPS_DICT[scp]["name"])

        if this_sign_risks in (None, []):
            pass
        else:
            print "-",
            risk_filename_stub = string.split(KNOWN_SCPS_DICT[scp]["filename"], ".")[0]
            risk_filename_stub = "%s_warning_sign" % (risk_filename_stub)
            risk_fontsize = 72
            if this_sign_risks[0] == "COGNITOHAZARD":
                risk_fontsize2 = 52
            else:
                risk_fontsize2 = 72
            risk_font = "Gill Sans Nova Bold"
            
            #risk_line1_y = height-700
            risk_line1_y = height-750
            risk_line2_y = risk_line1_y - (risk_fontsize * 1.25)

            risk_box_width = width - (margin*6)
            risk_box_height = (risk_fontsize * 2.0) + 100

            risk_box_x1 = margin * 3
            risk_box_y1 = (risk_line1_y - 25)-(risk_box_height/2.0)

            if len(this_sign_risks) == 1:
                drisk = Drawing(width, height)
                drisk.add(Rect(0, 0, width, height, fillColor=colors.white))
                drisk.add(Rect(risk_box_x1, risk_box_y1, risk_box_width, risk_box_height, fillColor=colors.yellow, strokeColor=colors.yellow))

                if this_sign_risks[0] == "RADIOACTIVE":
                    risk_widget = hazard_widgets.Radioactive()
                elif this_sign_risks[0] == "BIOHAZARD":
                    risk_widget = hazard_widgets.Biohazard()
                elif this_sign_risks[0] == "COGNITOHAZARD":
                    risk_widget = hazard_widgets.Cognitohazard()
                elif this_sign_risks[0] == "INFOHAZARD":
                    risk_widget = hazard_widgets.Infohazard()
                elif this_sign_risks[0] == "HOSTILE":
                    #risk_widget = hazard_widgets.Hostile()
                    #bodge - fix later
                    risk_widget = hazard_widgets.BareTriangle()

                else:
                    risk_widget = hazard_widgets.BareTriangle()

                drisk.add(risk_widget)

                risk_widget.x = risk_box_x1                     # symbol x coordinate
                risk_widget.y = height - 50 - risk_box_width    # symbol y coordinate
                risk_widget.size = risk_box_width

                if this_sign_risks[0] == "HOSTILE":
                    risk_widget2 = hazard_widgets.Hostile()
                    #bodge - fix later
                    #(Hostile widget doesn't display correctly - remove this once it does)
                    risk_widget2.x = risk_box_x1                     # symbol x coordinate
                    risk_widget2.y = height - 50 - risk_box_width    # symbol y coordinate
                    risk_widget2.size = risk_box_width
                    drisk.add(risk_widget2)

                #do barcode...
                dr2 = createBarcodeDrawing('Code128', humanReadable=1, value=BARCODE_LINE, validate=0)
                dr2_width = dr2.width
                #white barcode rectangle
                drisk.add(Rect(margin*3, margin*2, width-margin*6, 80, fillColor=colors.white, strokeColor=None))
                if OBJECT_CLASS == "NEUTRALIZED":
                    dr2.scale(2.05, 1.35)
                    dr2_width = dr2.width * 2.05
                elif OBJECT_CLASS == "TICONDEROGA":
                    dr2.scale(2.05, 1.35)
                    dr2_width = dr2.width * 2.05
                elif OBJECT_CLASS == "DECLASSIFIED":
                    dr2.scale(2.05, 1.35)
                    dr2_width = dr2.width * 2.05
                elif OBJECT_CLASS == "DECOMMISSIONED":
                    dr2.scale(1.95, 1.35)
                    dr2_width = dr2.width * 1.95
                else:
                    dr2.scale(2.25, 1.35)
                    dr2_width = dr2.width * 2.25
                dr2.scale(0.85, 0.85)
                #dr2_xpos = ((width-dr2_width)/2.0)
                #dr2.translate(dr2_xpos/2.25, margin*1.95)
                #dr2.translate(dr2_xpos/3.25, margin*1.95)
                dr2.translate(margin, margin*1.95)
                drisk.add(dr2)

                risk_line_1 = "WARNING"
                risk_line_2 = this_sign_risks[0]

                risk_line_1_width = stringWidth(risk_line_1, risk_font, risk_fontsize)
                risk_line_2_width = stringWidth(risk_line_2, risk_font, risk_fontsize2)

                risk_line_1_x = (width - risk_line_1_width)/2.0
                risk_line_1_y = risk_line1_y

                risk_line_2_x = (width - risk_line_2_width)/2.0
                risk_line_2_y = risk_line2_y

                #"WARNING" line
                drisk.add(String(risk_line_1_x, risk_line_1_y, risk_line_1, fontName=risk_font, fontSize=risk_fontsize, fillColor=colors.black))
                #"BIOHAZARD", "RADIATION", or whatever
                drisk.add(String(risk_line_2_x, risk_line_2_y, risk_line_2, fontName=risk_font, fontSize=risk_fontsize2, fillColor=colors.black))

                lgrisk = scp_widgets.SCPLogo()
                lgrisk.size = 80
                #lg.x = 425
                #lg.y = height-210
                #lgrisk.x = 525

                lgrisk.x = width - (margin * 3) - lgrisk.size
                #dr2.translate(margin * 3, margin*1.95)
                lgrisk.y = height-1025
                drisk.add(lgrisk)

                drisk.add(String((lgrisk.x+(lgrisk.size*0.6))-(stringWidth('Secure. Contain. Protect', "Bauhaus Demi", 12)/2.0),
                                 lgrisk.y-(lgrisk.size*0.35), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=12, fillColor=colors.black))

                risk_line_1 = "WARNING"
                risk_line_2 = this_sign_risks[0]

                risk_line_1_width = stringWidth(risk_line_1, risk_font, risk_fontsize)
                risk_line_2_width = stringWidth(risk_line_2, risk_font, risk_fontsize2)

                risk_line_1_x = (width - risk_line_1_width)/2.0
                risk_line_1_y = risk_line1_y

                risk_line_2_x = (width - risk_line_2_width)/2.0
                risk_line_2_y = risk_line2_y

                #"WARNING" line
                drisk.add(String(risk_line_1_x, risk_line_1_y, risk_line_1, fontName=risk_font, fontSize=risk_fontsize, fillColor=colors.black))
                #"BIOHAZARD", "RADIATION", or whatever
                drisk.add(String(risk_line_2_x, risk_line_2_y, risk_line_2, fontName=risk_font, fontSize=risk_fontsize2, fillColor=colors.black))


            elif len(this_sign_risks) == 2:
                #change later?
                drisk = Drawing(width, height)
                drisk.add(Rect(0, 0, width, height, fillColor=colors.white))


                # MODIFIED FROM ABOVE ROUTINE...
                for increment in [0,1]:
                    #for this_sub_sign_risks in this_sign_risks:
                    this_sub_sign_risks = this_sign_risks[increment]

                    print "=",
                    #this_risk_fontsize = 52
                    this_risk_fontsize = 37
                    if this_sub_sign_risks == "COGNITOHAZARD":
                        #this_risk_fontsize2 = 42
                        this_risk_fontsize2 = 28
                    else:
                        #this_risk_fontsize2 = 52
                        this_risk_fontsize2 = 37
                    #risk_font = "Gill Sans Nova Bold"

                    this_risk_box_width = (width - (margin*6))/2.0
                    this_risk_box_height = (this_risk_fontsize * 2.0) + 100

                    this_risk_line_1_y = height-600
                    this_risk_line_2_y = this_risk_line_1_y - (this_risk_fontsize * 1.5)

                    this_risk_box_x1 = (margin * 2)+(increment*(width/2.0))
                    if increment == 1:
                        this_risk_box_x1 = this_risk_box_x1 - margin
                    this_risk_box_y1 = (this_risk_line_1_y - 25)-(this_risk_box_height/2.0)

                    this_risk_line_1 = "WARNING"
                    this_risk_line_2 = this_sign_risks[increment]

                    this_risk_line_1_width = stringWidth(this_risk_line_1, risk_font, this_risk_fontsize)
                    this_risk_line_2_width = stringWidth(this_risk_line_2, risk_font, this_risk_fontsize2)

                    #this_risk_line_1_x = ((width - this_risk_line_1_width)/2.0)+((width/2.0)*increment)
                    ##this_risk_line_1_x = ((margin)+ (this_risk_line_1_width/2.0)+((width/2.0)*increment))
                    ###this_risk_line_1_x = (margin + (this_risk_box_width - this_risk_line_1_width)/2.0)+((width/2.0)*increment)
                    this_risk_line_1_x = (this_risk_box_x1 + (this_risk_box_width - this_risk_line_1_width)/2.0)
                    #this_risk_line_1_y = risk_line1_y

                    #this_risk_line_2_x = ((width - this_risk_line_2_width)/2.0)+((width/2.0)*increment)
                    ##this_risk_line_2_x = ((margin)+ (this_risk_line_2_width/2.0)+((width/2.0)*increment))
                    ###this_risk_line_2_x = (margin + (this_risk_box_width - this_risk_line_2_width)/2.0)+((width/2.0)*increment)
                    this_risk_line_2_x = (this_risk_box_x1 + (this_risk_box_width - this_risk_line_2_width)/2.0)
                    #this_risk_line_2_y = risk_line2_y


                    drisk.add(Rect(this_risk_box_x1, this_risk_box_y1, this_risk_box_width, this_risk_box_height, fillColor=colors.yellow, strokeColor=colors.yellow))

                    if this_sub_sign_risks == "RADIOACTIVE":
                        this_risk_widget = hazard_widgets.Radioactive()
                    elif this_sub_sign_risks == "BIOHAZARD":
                        this_risk_widget = hazard_widgets.Biohazard()
                    elif this_sub_sign_risks == "COGNITOHAZARD":
                        this_risk_widget = hazard_widgets.Cognitohazard()
                    elif this_sub_sign_risks == "INFOHAZARD":
                        this_risk_widget = hazard_widgets.Infohazard()
                    elif this_sub_sign_risks == "HOSTILE":
                        #risk_widget = hazard_widgets.Hostile()
                        #bodge - fix later
                        this_risk_widget = hazard_widgets.BareTriangle()

                    else:
                        this_risk_widget = hazard_widgets.BareTriangle()

                    drisk.add(this_risk_widget)

                    this_risk_widget.x = this_risk_box_x1                               # symbol x coordinate
                    this_risk_widget.y = height - 50 - (this_risk_box_width*1.5)        # symbol y coordinate
                    this_risk_widget.size = this_risk_box_width

                    if this_sub_sign_risks == "HOSTILE":
                        this_risk_widget2 = hazard_widgets.Hostile()
                        #bodge - fix later
                        #(Hostile widget doesn't display correctly - remove this once it does)
                        this_risk_widget2.x = this_risk_box_x1                          # symbol x coordinate
                        this_risk_widget2.y = height - 50 - (this_risk_box_width*1.5)   # symbol y coordinate
                        this_risk_widget2.size = this_risk_box_width
                        drisk.add(risk_widget2)

                    #"WARNING" line
                    drisk.add(String(this_risk_line_1_x, this_risk_line_1_y, this_risk_line_1, fontName=risk_font, fontSize=this_risk_fontsize, fillColor=colors.black))
                    #"BIOHAZARD", "RADIATION", or whatever
                    drisk.add(String(this_risk_line_2_x, this_risk_line_2_y, this_risk_line_2, fontName=risk_font, fontSize=this_risk_fontsize2, fillColor=colors.black))

            #do barcode...
            dr2 = createBarcodeDrawing('Code128', humanReadable=1, value=BARCODE_LINE, validate=0)
            dr2_width = dr2.width
            #white barcode rectangle
            drisk.add(Rect(margin*3, margin*2, width-margin*6, 80, fillColor=colors.white, strokeColor=None))
            if OBJECT_CLASS == "NEUTRALIZED":
                dr2.scale(2.05, 1.35)
                dr2_width = dr2.width * 2.05
            elif OBJECT_CLASS == "TICONDEROGA":
                dr2.scale(2.05, 1.35)
                dr2_width = dr2.width * 2.05
            elif OBJECT_CLASS == "DECLASSIFIED":
                dr2.scale(2.05, 1.35)
                dr2_width = dr2.width * 2.05
            elif OBJECT_CLASS == "DECOMMISSIONED":
                dr2.scale(1.95, 1.35)
                dr2_width = dr2.width * 1.95
            else:
                dr2.scale(2.25, 1.35)
                dr2_width = dr2.width * 2.25
            dr2.scale(0.85, 0.85)
            #dr2_xpos = ((width-dr2_width)/2.0)
            #dr2.translate(dr2_xpos/2.25, margin*1.95)
            #dr2.translate(dr2_xpos/3.25, margin*1.95)
            dr2.translate(margin, margin*1.95)
            drisk.add(dr2)

            lgrisk = scp_widgets.SCPLogo()
            lgrisk.size = 80
            #lg.x = 425
            #lg.y = height-210
            #lgrisk.x = 525

            lgrisk.x = width - (margin * 3) - lgrisk.size
            #dr2.translate(margin * 3, margin*1.95)
            lgrisk.y = height-1025
            drisk.add(lgrisk)

            drisk.add(String((lgrisk.x+(lgrisk.size*0.6))-(stringWidth('Secure. Contain. Protect', "Bauhaus Demi", 12)/2.0),
                             lgrisk.y-(lgrisk.size*0.35), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=12, fillColor=colors.black))

            renderPM.drawToFile(drisk, '%s.png' % risk_filename_stub, 'PNG')

            if VERBOSE > 0:
                print "WROTE '%s.png'" % risk_filename_stub
            else:
                print "=",

            if MAKE_PDFS == 1:
                renderPDF.drawToFile(drisk, '%s.pdf' % risk_filename_stub, name)
                #num_signs_made = num_signs_made + 1
                if VERBOSE > 0:
                    print "WROTE '%s.pdf'" % risk_filename_stub
                else:
                    print ".",
            if VERBOSE > 0:
                print



        #end writing this SCP's sign... on to the next one.
    if VERBOSE > 0:
        print
    else:
        print "\n"


    #Now make One last DEMO SIGN
    name = "SCP-0000"
    OBJECT_CLASS = random.choice(("EUCLID", "SAFE", "KETER", "PENDING", "THAUMIEL"))

    object_class_line = u"OBJECT CLASS: %s" % OBJECT_CLASS

    DISRUPTION_CLASS = random.choice(("DARK", "KENEQ", "VLAM", "EKHI", "AMIDA", None))
    RISK_CLASS = random.choice(("Caution", "Warning", "Danger", "Critical", None))

    #BARCODE_LINE = "%s / %s" % (name, OBJECT_CLASS)
    roomnum = random.randint(0,99999)
    BARCODE_LINE = "LOCATION #%05d / %s / %s" % (roomnum, name, OBJECT_CLASS)

    if DISRUPTION_CLASS == None:
        DISRUPTION_CLASS = ""
    if RISK_CLASS == None:
        RISK_CLASS = ""

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.white))
    d.add(Rect(margin, margin, (width-(margin*2)), (height-(margin*2)), fillColor=colors.yellow, strokeColor=colors.yellow))

    #white rectangle
    d.add(Rect(0, height-600, width, 250, fillColor=colors.white, strokeColor=colors.white))

    #d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=180, fillColor=colors.black))
    d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=190, fillColor=colors.black))
    #d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=48, fillColor=colors.black))
    d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=52, fillColor=colors.black))

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.x = 425
    lg.y = height-210
    d.add(lg)

    if string.find(object_class_line, "THAUMIEL") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "PENDING") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "NEUTRALIZED") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "TICONDEROGA") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "DECLASSIFIED") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "UNCONTAINED") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "UNKNOWN") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "EXPLAINED") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif string.find(object_class_line, "DECOMMISSIONED") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    elif "G\xc3\xb6DEL" in object_class_line.encode("UTF-8", "ignore"):
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    else:
        d.add(String(margin*2,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))

    if string.find(object_class_line, "PENDING") > -1:
        d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=80, fillColor=colors.black))
    elif string.find(object_class_line, "THAUMIEL") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=80, fillColor=colors.black))
    elif string.find(object_class_line, "NEUTRALIZED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
    elif string.find(object_class_line, "TICONDEROGA") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
    elif string.find(object_class_line, "DECLASSIFIED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
    elif string.find(object_class_line, "UNCONTAINED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
    elif string.find(object_class_line, "EXPLAINED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
    elif string.find(object_class_line, "DECOMMISSIONED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
    elif string.find(object_class_line, "UNKNOWN") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=70, fillColor=colors.black))
    #elif string.find(object_class_line, "G\xc3\xb6DEL") > -1:
    elif "G\xc3\xb6DEL" in object_class_line.encode("UTF-8", "ignore"):
        d.add(String(margin*2,(height-550), object_class_line.encode("UTF-8", "ignore"), fontName="Gill Sans Nova Cond Bold", fontSize=84, fillColor=colors.black))

    else:
        d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=84, fillColor=colors.black))

    #LEFT HAND BOX...

    d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

    if OBJECT_CLASS == "SAFE":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=green_background_colour, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=green_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "SAFE", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Safe()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "EUCLID":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=yellow_background_colour, strokeColor=colors.black))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=yellow_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "EUCLID", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Euclid()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "KETER":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=red_background_colour, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=red_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "KETER", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Keter()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "PENDING":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "PENDING", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Pending()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "THAUMIEL":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "THAUMIEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Thaumiel()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "NEUTRALIZED":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "NEUTRALIZED", fontName="Gill Sans Nova Bold", fontSize=32, fillColor=colors.black))

        cw = scp_widgets.Neutralized()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "ESOTERIC":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "ESOTERIC", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Esoteric()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "G\xc3\xb6DEL":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "G\xc3\xb6DEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Esoteric()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "EXPLAINED":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "EXPLAINED", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Explained()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "DECOMMISSIONED":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "DECOMMISSIONED", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Decommissioned()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)


    #RIGHT HAND BOX...

    #d.add(Rect((width/2.0)+margin, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
    d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

    #DISRUPTION CLASS
    d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*7.95), "DISRUPTION CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*6.95), DISRUPTION_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

    bar1FillColour = None

    if DISRUPTION_CLASS == None:
        bar1FillColour = None
    elif DISRUPTION_CLASS == "DARK":
        bar1FillColour = green_bar_colour
        dclass = scp_widgets.DARK()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "VLAM":
        bar1FillColour = blue_bar_colour
        dclass = scp_widgets.VLAM()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "KENEQ":
        bar1FillColour = yellow_bar_colour
        dclass = scp_widgets.KENEQ()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "EKHI":
        bar1FillColour = orange_bar_colour
        dclass = scp_widgets.EKHI()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "AMIDA":
        bar1FillColour = red_bar_colour
        dclass = scp_widgets.AMIDA()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)

    if bar1FillColour != None:
        d.add(Rect((width/2.0)+margin, margin*6.35, margin, 65, fillColor=bar1FillColour, strokeColor=None))


    #RISK CLASS
    d.add(Rect((width/2.0)+margin, (margin*6.35)+65, (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*7.95)+65, "RISK CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*6.95)+65, RISK_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

    bar2FillColour = None

    if RISK_CLASS == None:
        bar2FillColour = None
    elif RISK_CLASS == "Notice":
        bar2FillColour = green_bar_colour
        dclass = scp_widgets.Notice()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Caution":
        bar2FillColour = blue_bar_colour
        dclass = scp_widgets.Caution()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Warning":
        bar2FillColour = yellow_bar_colour
        dclass = scp_widgets.Warning()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Danger":
        bar2FillColour = orange_bar_colour
        dclass = scp_widgets.Danger()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Critical":
        bar2FillColour = red_bar_colour
        dclass = scp_widgets.Critical()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)

    if bar2FillColour != None:
        d.add(Rect((width/2.0)+margin, (margin*6.35)+65, margin, 65, fillColor=bar2FillColour, strokeColor=None))

    #OCTANCT GRAPHIC
    #"Danger Diamond"
    d.add(Rect((width/2.0)+margin, (margin*6.35)+130, (width/2.0)-margin*4, 170, fillColor=colors.white, strokeColor=colors.black))

    dd = scp_widgets.DangerDiamond()
    #dd.x = (width/2.0)+(margin*3.25)+15
    dd.x = (width/2.0)+(margin*3.25)+7
    dd.y = (margin*6.45)+142
    dd.size = 150

    dd.DisruptionClass = DISRUPTION_CLASS
    dd.RiskClass = RISK_CLASS
    dd.ObjectClass = OBJECT_CLASS

    d.add(dd)

    #BARCODE
    from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing, createBarcodeImageInMemory

    dr = createBarcodeDrawing('Code128', humanReadable=1, value=BARCODE_LINE, validate=0)

    #white barcode rectangle
    d.add(Rect(margin*3, margin*2, width-margin*6, 80, fillColor=colors.white, strokeColor=None))
    d.add(dr)

    if OBJECT_CLASS == "EUCLID":
        dr.translate(margin*2.75,margin*2.55)
    elif OBJECT_CLASS == "SAFE":
        dr.translate(margin*3.05,margin*2.55)
    else:
        dr.translate(margin*2.75,margin*2.55)

    dr.scale(2.25, 1.35)

    renderPM.drawToFile(d, 'example1.png', 'PNG')
    num_signs_made = num_signs_made + 1

    if MAKE_PDFS == 1:
        renderPDF.drawToFile(d, 'example1.pdf', name)
        num_signs_made = num_signs_made + 1


## ONE LAST, *LAST* EXAMPLE FILE...


    #Now make One last DEMO SIGN
    name = "SCP-0000"
    OBJECT_CLASS = random.choice(("EUCLID", "SAFE", "KETER", "PENDING", "THAUMIEL"))
    SECONDARY_CLASS = random.choice(objects.ESOTERIC_CLASSES)
    SECONDARY_CLASS = string.upper(SECONDARY_CLASS)

    object_class_line = "OBJECT CLASS: %s" % OBJECT_CLASS
    secondary_class_line = "SECONDARY CLASS: %s" % SECONDARY_CLASS

    DISRUPTION_CLASS = random.choice(("DARK", "KENEQ", "VLAM", "EKHI", "AMIDA", None))
    RISK_CLASS = random.choice(("Caution", "Warning", "Danger", "Critical", None))

    #BARCODE_LINE = "%s / %s" % (name, OBJECT_CLASS)
    roomnum = random.randint(0,99999)
    BARCODE_LINE = "LOCATION #%05d / %s / %s" % (roomnum, name, OBJECT_CLASS)

    if DISRUPTION_CLASS == None:
        DISRUPTION_CLASS = ""
    if RISK_CLASS == None:
        RISK_CLASS = ""

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=colors.white))
    d.add(Rect(margin, margin, (width-(margin*2)), (height-(margin*2)), fillColor=colors.yellow, strokeColor=colors.yellow))

    #white rectangle
    d.add(Rect(0, height-600, width, 250, fillColor=colors.white, strokeColor=colors.white))

    #d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=180, fillColor=colors.black))
    d.add(String(100, (height-210), 'SCP', fontName="Bauhaus Demi", fontSize=190, fillColor=colors.black))
    #d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=48, fillColor=colors.black))
    d.add(String(100, (height-290), 'Secure. Contain. Protect', fontName="Bauhaus Demi", fontSize=52, fillColor=colors.black))

    lg = scp_widgets.SCPLogo()
    lg.size = LOGOWIDTH
    lg.x = 425
    lg.y = height-210
    d.add(lg)

    if string.find(object_class_line, "THAUMIEL") > -1:
        d.add(String(margin*1.55,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))
    else:
        d.add(String(margin*2,(height-450), name, fontName="Gill Sans Nova Bold", fontSize=84, fillColor=colors.black))

    if string.find(object_class_line, "PENDING") > -1:
        d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=80, fillColor=colors.black))
    elif string.find(object_class_line, "THAUMIEL") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=80, fillColor=colors.black))
    elif string.find(object_class_line, "NEUTRALIZED") > -1:
        d.add(String(margin*1.55,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=75, fillColor=colors.black))
    else:
        d.add(String(margin*2,(height-550), object_class_line, fontName="Gill Sans Nova Cond Bold", fontSize=84, fillColor=colors.black))

    #LEFT HAND BOX...

    d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

    if OBJECT_CLASS == "SAFE":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=green_background_colour, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=green_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "SAFE", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Safe()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "EUCLID":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=yellow_background_colour, strokeColor=colors.black))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=yellow_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "EUCLID", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Euclid()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "KETER":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=red_background_colour, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=red_bar_colour, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "KETER", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Keter()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "PENDING":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.lightgrey, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.grey, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "PENDING", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Pending()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "THAUMIEL":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "THAUMIEL", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Thaumiel()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "NEUTRALIZED":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "NEUTRALIZED", fontName="Gill Sans Nova Bold", fontSize=32, fillColor=colors.black))

        cw = scp_widgets.Neutralized()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)

    if OBJECT_CLASS == "ESOTERIC":
        d.add(Rect(margin*3, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))
        d.add(Rect(margin*3, margin*6.35, margin, 300, fillColor=colors.white, strokeColor=None))

        d.add(String(margin*4.5,(margin*9.20), "CONTAINMENT", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*8.20), "CLASS:", fontName="Gill Sans Nova", fontSize=24, fillColor=colors.black))
        d.add(String(margin*4.5,(margin*6.85), "ESOTERIC", fontName="Gill Sans Nova Bold", fontSize=36, fillColor=colors.black))

        cw = scp_widgets.Esoteric()
        cw.x = margin*5.75
        cw.y = (margin*11.5)
        cw.size = 150
        d.add(cw)


    #RIGHT HAND BOX...

    #d.add(Rect((width/2.0)+margin, margin*6.35, (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=colors.black))
    d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 300, fillColor=colors.white, strokeColor=None))

    #DISRUPTION CLASS
    d.add(Rect((width/2.0)+margin, (margin*6.35), (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*7.95), "DISRUPTION CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*6.95), DISRUPTION_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

    bar1FillColour = None

    if DISRUPTION_CLASS == None:
        bar1FillColour = None
    elif DISRUPTION_CLASS == "DARK":
        bar1FillColour = green_bar_colour
        dclass = scp_widgets.DARK()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "VLAM":
        bar1FillColour = blue_bar_colour
        dclass = scp_widgets.VLAM()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "KENEQ":
        bar1FillColour = yellow_bar_colour
        dclass = scp_widgets.KENEQ()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "EKHI":
        bar1FillColour = orange_bar_colour
        dclass = scp_widgets.EKHI()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)
    elif DISRUPTION_CLASS == "AMIDA":
        bar1FillColour = red_bar_colour
        dclass = scp_widgets.AMIDA()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))-2
        dclass.size = 40
        d.add(dclass)

    if bar1FillColour != None:
        d.add(Rect((width/2.0)+margin, margin*6.35, margin, 65, fillColor=bar1FillColour, strokeColor=None))


    #RISK CLASS
    d.add(Rect((width/2.0)+margin, (margin*6.35)+65, (width/2.0)-margin*4, 65, fillColor=colors.white, strokeColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*7.95)+65, "RISK CLASS", fontName="Gill Sans Nova", fontSize=18, fillColor=colors.black))
    d.add(String((width/2.0)+margin*2.5,(margin*6.95)+65, RISK_CLASS, fontName="Gill Sans Nova Bold", fontSize=24, fillColor=colors.black))

    bar2FillColour = None

    if RISK_CLASS == None:
        bar2FillColour = None
    elif RISK_CLASS == "Notice":
        bar2FillColour = green_bar_colour
        dclass = scp_widgets.Notice()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Caution":
        bar2FillColour = blue_bar_colour
        dclass = scp_widgets.Caution()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Warning":
        bar2FillColour = yellow_bar_colour
        dclass = scp_widgets.Warning()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Danger":
        bar2FillColour = orange_bar_colour
        dclass = scp_widgets.Danger()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)
    elif RISK_CLASS == "Critical":
        bar2FillColour = red_bar_colour
        dclass = scp_widgets.Critical()
        dclass.x = ((width/2.0)+margin)+((width/2.0)-margin*4)-48
        dclass.y = ((margin*6.95))+65-2
        dclass.size = 40
        d.add(dclass)

    if bar2FillColour != None:
        d.add(Rect((width/2.0)+margin, (margin*6.35)+65, margin, 65, fillColor=bar2FillColour, strokeColor=None))

    #OCTANCT GRAPHIC
    #"Danger Diamond"
    d.add(Rect((width/2.0)+margin, (margin*6.35)+130, (width/2.0)-margin*4, 170, fillColor=colors.white, strokeColor=colors.black))

    dd = scp_widgets.DangerDiamond()
    #dd.x = (width/2.0)+(margin*3.25)+15
    dd.x = (width/2.0)+(margin*3.25)+7
    dd.y = (margin*6.45)+142
    dd.size = 150

    dd.DisruptionClass = DISRUPTION_CLASS
    dd.RiskClass = RISK_CLASS
    dd.ObjectClass = OBJECT_CLASS

    d.add(dd)

    #BARCODE
    from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing, createBarcodeImageInMemory

    dr = createBarcodeDrawing('Code128', humanReadable=1, value=BARCODE_LINE, validate=0)

    #white barcode rectangle
    d.add(Rect(margin*3, margin*2, width-margin*6, 80, fillColor=colors.white, strokeColor=None))
    d.add(dr)

    if OBJECT_CLASS == "EUCLID":
        dr.translate(margin*2.75,margin*2.55)
    elif OBJECT_CLASS == "SAFE":
        dr.translate(margin*3.05,margin*2.55)
    else:
        dr.translate(margin*2.75,margin*2.55)

    dr.scale(2.25, 1.35)

    renderPM.drawToFile(d, 'example2.png', 'PNG')
    num_signs_made = num_signs_made + 1

    if MAKE_PDFS == 1:
        renderPDF.drawToFile(d, 'example2.pdf', name)
        num_signs_made = num_signs_made + 1


    os.chdir(THISDIR)

    print "\nCreated %s door/locker signs in directory '%s'\n\n" % (num_signs_made, os.path.join(THISDIR, "images", "signage", "containment"))

    if USE_LOG == 1:
        print "(see logfile 'make_door_signage_INTERESTING_LOG_FILE.txt' for more info).\n"

    print "\n\nDONE\n\n"



if __name__ == "__main__":
    run(USE_LOG=USE_LOG)