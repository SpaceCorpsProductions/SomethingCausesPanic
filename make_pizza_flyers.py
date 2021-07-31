import os, random, string
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

from reportlab.lib import colors
from reportlab.graphics import renderPM
from reportlab.graphics import renderPDF   # in case we want PDFs of these things one day...

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

import scp_widgets

MAKE_PDFS = 0
MAKE_PDFS = 1

VERBOSE = 1
VERBOSE = 0

THISDIR = os.getcwd()

#register fonts
#pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'BAUHS93.TTF')))
pdfmetrics.registerFont(TTFont('Bauhaus Demi', os.path.join("fonts", 'Bauhaus_Demi.ttf')))
pdfmetrics.registerFont(TTFont('Verdana Bold', os.path.join("fonts", 'verdanab.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova', os.path.join("fonts", 'GillSansNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Bold', os.path.join("fonts", 'GillSansBoNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond', os.path.join("fonts", 'GillSansCondNova.ttf')))
pdfmetrics.registerFont(TTFont('Gill Sans Nova Cond Bold', os.path.join("fonts", 'GillSansCondBoNova.ttf')))

pdfmetrics.registerFont(TTFont('Dock 51', os.path.join("fonts", 'dock_0.ttf')))
pdfmetrics.registerFont(TTFont('Press Start 2P Regular', os.path.join("fonts", 'PressStart2P-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Trebuchet MS', os.path.join("fonts", 'trebuc.ttf')))
pdfmetrics.registerFont(TTFont('Trebuchet MS Bold', os.path.join("fonts", 'trebucbd.ttf')))
pdfmetrics.registerFont(TTFont('Trebuchet MS Bold Italic', os.path.join("fonts", 'trebucbi.ttf')))
pdfmetrics.registerFont(TTFont('Trebuchet MS Italic', os.path.join("fonts", 'trebucit.ttf')))

picsdir = os.path.join(".", "images", "misc_pics")
outdir = os.path.join(".", "images", "signage", "breakrooms")

pizza_pics = ["30344707120_93ae518b1a_b.jpg",   #"Mmm... white pizza" by jeffreyw is licensed under CC BY 2.0
              "4342076816_2ae2a0f94d_b.jpg",    #"Pizza! (serving suggestion)" by jeffreyw is licensed under CC BY 2.0
              "6921934437_52fbaa46ea_b.jpg",    #"Mmm... leftovers" by jeffreyw is licensed under CC BY 2.0
              "8580196624_9778f9fd39_b.jpg",    #"pizza" by Gonmi is licensed under CC BY 2.0
              "3495871394_b779997772_b.jpg",    #"Pizza" by rdpeyton is licensed under CC BY-NC-SA 2.0
              "2529856456_368530c5ab_b.jpg",    #"Pizza: Grilled chicken, artichoke hearts, and arugula" by ecospc is licensed under CC BY-NC 2.0
              "8608411604_8e36b8af06_b.jpg",    #"homemade pizza" by plasticrevolver is licensed under CC BY-SA 2.0
              "2368472328_d0be0cdcbc_b.jpg",    #"Pizza filetti" by sfllaw is licensed under CC BY-SA 2.0
              "387142241_6d4a83f7c8_b.jpg",     #"Take-Out @ Singas Famous Pizza" by wEnDaLicious is licensed under CC BY-ND 2.0
              "3889314870_a3331db73d_b.jpg",    #"Pizza @ Home" by code_martial is licensed under CC BY-NC-ND 2.0
              ]

fontnames = ['Bauhaus Demi',
             'Verdana Bold',
             'Gill Sans Nova',
             'Gill Sans Nova Bold',
             #'Gill Sans Nova Cond',
             #'Gill Sans Nova Cond Bold',
             'Dock 51',
             'Press Start 2P Regular',
             'Trebuchet MS',
             'Trebuchet MS Bold',
             'Trebuchet MS Bold Italic',
             'Trebuchet MS Italic'
             ]


def run():

    #default screen size in our game =
    #gui.init(1920, 1080)
    height = 1080
    width = 720
    margin = 24


    #Don't forget, Wednesday is pizza day! So head on down to the cafeteria and grab yourself a hot slice! [different voice, faster] The SCP Foundation holds no liabilities for illnesses or injuries sustained or contracted through attendance of Pizza Day.
    #When dining in the facility cafeteria, always remember to check your rations for the deadly seven: Strychnine, Arsenic Trioxide, Nitrobenzine, Mercury, Epichlorohydrine, Acetone Thiosemicarbazone,  and spiders. Stay Healthy! Stay vigilant!

    NUMPOSTERS = 30
    print "Making %s pizza flyers..." % NUMPOSTERS

    for f in range(0,NUMPOSTERS):

        pizza_pic = os.path.join(picsdir, random.choice(pizza_pics))
        usecaps = random.choice((0,1,2,2))
        alignment = random.choice(("left", "middle"))
        useborder = random.choice((0,1,2))
        #usestroke = random.choice((1,0))
        usestroke = 1
        
        usedropshadow = random.choice((1,0))
        if useborder == 0:
            usedropshadow = 1
        dropshadow_offset = 3
        line1 = random.choice(("", "Don't forget!"))
        line2 = random.choice(("Today is", "Wednesday is", "Every day is"))
        line3 = random.choice(("Pizza Day!", "PIZZA DAY!", "Pizza Day", "PIZZA DAY"))


        if useborder == 0:

            textcolor = random.choice((colors.white,
                                      colors.yellow,
                                      colors.lightgrey#,
                                       ))
            
    #                              colors.darksalmon))

            if usestroke == 1:
                strokecol = colors.black
            else:
                strokecol = None


        else:

            textcolor = random.choice((colors.red,
                                      colors.blue,
                                      colors.dodgerblue,
                                      colors.fidblue,
                                      #colors.fidlightblue,
                                      colors.fidred,
                                      colors.firebrick,
                                      colors.darkred,
                                      colors.black,
                                      colors.darkgrey,
                                       ))
            
    #                              colors.darksalmon))

            if usestroke == 1:
                strokecol = colors.white
            else:
                strokecol = None


        fontname = random.choice(fontnames)

        if useborder == 0:
            fontsize = random.choice((72, 84, 96))
        else:
            fontsize = random.choice((48,72,96))

        line4 = random.choice(("Grab yourself a hot slice!",
                               "The SCP Foundation holds no liabilities for illnesses or injuries sustained or contracted through attendance of Pizza Day"))


        if usecaps == 1:
            line1 = string.capwords(line1)
            line2 = string.capwords(line2)
            line3 = string.capwords(line3)
        if usecaps == 2:
            line1 = string.upper(line1)
            line2 = string.upper(line2)
            line3 = string.upper(line3)

        if VERBOSE == 1:
            print line1
            print line2
            print line3
        else:
            print ".",


        fname = "Pizza_Flyer_%02d" % f
        ##Canvas used only for stringwidth function
        ##c = canvas.Canvas("DUMMY", pagesize=reportlab.lib.pagesizes.A4)

        d = Drawing(width, height)
        d.add(Rect(0, 0, width, height, fillColor=colors.white))

        #d.add(Rect(0, 0, width, height, fillColor=colors.white))
        if VERBOSE == 1:
            print "pizza pic:", pizza_pic

        if useborder == 0:
            d.add(Image(0, 0, width=width, height=height, path=pizza_pic))
   
        newfontsize = fontsize
        for ln in line1, line2, line3:
            linewidth = stringWidth(ln, fontname, newfontsize)
            TOTALMARGINWIDTH = 200
            while linewidth > (width - TOTALMARGINWIDTH):
                newfontsize = newfontsize - 1
                linewidth = stringWidth(ln, fontname, newfontsize)

        topline = height-margin
        if topline > (height - (newfontsize * 1.5)):
            topline = (height - (newfontsize * 1.5))
 

        if alignment == "left":
            if usedropshadow == 1:
                d.add(String(100+dropshadow_offset, topline-dropshadow_offset, line1, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(100, topline, line1, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol))
            x = String(100, topline, line1, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25)
                
            topline = topline - newfontsize * 1.25
            if usedropshadow == 1:
                d.add(String(100+dropshadow_offset, topline-dropshadow_offset, line2, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(100, topline, line2, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25))
                
            topline = topline - newfontsize * 1.25
            if usedropshadow == 1:
                d.add(String(100+dropshadow_offset, topline-dropshadow_offset, line3, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(100, topline, line3, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25))
                
            topline = topline - newfontsize * 1.25

        elif alignment == "middle":
            linewidth = stringWidth(line1, fontname, newfontsize)
            xpos = (width - linewidth) /2.0
            if usedropshadow == 1:
                d.add(String(xpos+dropshadow_offset, topline-dropshadow_offset, line1, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(xpos, topline, line1, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25))

            topline = topline - newfontsize * 1.25

            linewidth = stringWidth(line2, fontname, newfontsize)
            xpos = (width - linewidth) /2.0
            if usedropshadow == 1:
                d.add(String(xpos+dropshadow_offset, topline-dropshadow_offset, line2, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(xpos, topline, line2, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25))
                
            topline = topline - newfontsize * 1.25

            linewidth = stringWidth(line3, fontname, newfontsize)
            xpos = (width - linewidth) /2.0
            if usedropshadow == 1:
                d.add(String(xpos+dropshadow_offset, topline-dropshadow_offset, line3, fontName=fontname, fontSize=newfontsize, fillColor=colors.grey, strokeColor=strokecol))
            d.add(String(xpos, topline, line3, fontName=fontname, fontSize=newfontsize, fillColor=textcolor, strokeColor=strokecol, strokeWidth=25))
                
            topline = topline - newfontsize * 1.25


        if useborder == 1:
            #d.add(Image(margin*2, margin*2, width=width-(margin*4), height=height-(margin*4), path=pizza_pic))
            d.add(Image(margin*2, margin*2, width=width-(margin*4), height=height-((newfontsize*1.25)*4.0)-margin*2, path=pizza_pic))
        elif useborder == 2:
            #d.add(Image(margin*4, margin*4, width=width-(margin*8), height=height-(margin*8), path=pizza_pic))
            d.add(Image(margin*4, margin*4, width=width-(margin*8), height=height-((newfontsize*1.25)*4.0)-margin*4, path=pizza_pic))

        renderPM.drawToFile(d, os.path.join(outdir, '%s.png' % fname), 'PNG')
        if VERBOSE == 1:
            print "Wrote file '%s'" % os.path.join(outdir, '%s.png' % fname)
        else:
            print ".",

        if MAKE_PDFS == 1:
            renderPDF.drawToFile(d, os.path.join(outdir, '%s.pdf' % fname), fname)
            if VERBOSE == 1:
                print "Wrote file '%s'" % os.path.join(outdir, '%s.pdf' % fname)
            else:
                print ".",

    if VERBOSE == 0:
        print
    print "DONE.\n"

if __name__ == "__main__":
    run()
