#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Creates various handwritten and printed notices for break rooms.

Texts inspired from various sources includng the Foundation After Midnight
Radio shows (available on Youtube), the original SCP documents (fron the
SCP Wiki) and others.

"""

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from {a}http://www.scpwiki.com{/a} and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.


import os, random, string, copy

from base import NOTABLE_STAFF_DICT

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
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
#from reportlab.pdfgen import canvas

MAKE_PDFS = 0
MAKE_PDFS = 1
    
THISDIR = os.getcwd()

VERBOSE = 1
VERBOSE = 0


handwritten_fonts = [#A Sensible Armadillo by Brittney Murphy Design 
                     ## Free for personal use ONLY.
                     ## For commercial use, please purchase a license:
                     ## http://brittneymurphydesign.com/downloads/alphabetized-cassette-tapes/
                     ["A Sensible Armadillo", "A Sensible Armadillo.ttf"],
                     #Alphabetized Cassette Tapes by Brittney Murphy Design 
                     ## Free for personal use ONLY.
                     ## For commercial use, please purchase a license:
                     ## http://brittneymurphydesign.com/downloads/alphabetized-cassette-tapes/
                     ["Alphabetized Cassette Tapes", "alphabetized cassette tapes.ttf"],
                     #CatholicSchoolGirls BB font by Blambot (http://www.blambot.com)
                     ["CatholicSchoolGirls", "CATHSGBR.TTF"],
                     #Ink Free Font is a sweet handwritten typeface by Steve Matteson.
                     ["Ink Free Font", "Inkfree.ttf"]
                     ]

typed_fonts = [
                     ["Gill Sans Nova", "GillSansNova.ttf"],
                     ["Gill Sans Nova Bold", "GillSansBoNova.ttf"],
                     ["Trebuchet", "trebuc.ttf"],
                     ["Trebuchet Italic", "trebucit.ttf"],
                     ["Verdana", "verdana.ttf"],
                     ["Verdana Italic", "verdanai.ttf"],
                     ]

possible_fonts = []
handwritten_font_names = []
typed_font_names = []

#register fonts
for t in handwritten_fonts:
    name, ttf = t
    pdfmetrics.registerFont(TTFont(name, os.path.join("fonts", ttf)))
    possible_fonts.append(name)
    handwritten_font_names.append(name)
for t in typed_fonts:
    name, ttf = t
    pdfmetrics.registerFont(TTFont(name, os.path.join("fonts", ttf)))
    possible_fonts.append(name)
    typed_font_names.append(name)

ink_colours = [
    #(almost) black
    colors.Color(5.0/255,
                 5.0/255,
                 5.0/255,
                 0.9),
    #black(-ish)
    colors.Color(15.0/255,
                 15.0/255,
                 15.0/255,
                 0.9),
    #dark grey(-ish)
    colors.Color(55.0/255,
                 55.0/255,
                 55.0/255,
                 0.9),
    #dark blue(-ish)
    colors.Color(5.0/255,
                 5.0/255,
                 75.0/255,
                 0.9),
    #Bright blue(-ish)
    colors.Color(5.0/255,
                 5.0/255,
                 175.0/255,
                 0.9),
    #dark red(-ish)
    colors.Color(75.0/255,
                 5.0/255,
                 5.0/255,
                 0.9),
    #Bright red(-ish)
    colors.Color(175.0/255,
                 15.0/255,
                 15.0/255,
                 0.9)#,
    ]


#So we can keep "DAYS SINCE CONTAINMENT BREACH" signs consistent..
DAYS_SINCE_CONTAINMENT_BREACH = random.randint(1,5),


NOTE_TEXTS = [

# These texts taken from/inspired by
# FAM Radio Ep 00 "Intro To The Foundation" [Full Episode] 
# Foundation After Midnight Radio - #SCP
# https://youtu.be/142L9k8hAsI

"""
All personnel are invited to join the inter-site, intramural softball 
league.

Hope to see you on the field!
""",

"""
Welcome to the Foundation family.

It only gets stranger from here.
""",

"""
Welcome to the Foundation family.

It only gets stranger from here.
(But in a good way. Except for Containment Breaches.)
""",


# These texts taken from/inspired by
# Foundation After Midnight Radio, Episode #01 "Pilot"
# https://youtu.be/jnRn1boqaW0

"""
DAYS SINCE CONTAINMENT BREACH: %s
""" % DAYS_SINCE_CONTAINMENT_BREACH,

"""
DAYS SINCE LAST CONTAINMENT BREACH: %s
""" % DAYS_SINCE_CONTAINMENT_BREACH,

"""
Days since containment breach: %s
""" % DAYS_SINCE_CONTAINMENT_BREACH,

"""
Days since last containment breach: %s
""" % DAYS_SINCE_CONTAINMENT_BREACH,

"""
Venturing off-facility during research hours is not permitted. Even if 
it's just to run to that smoothie place at the strip-mall. More so if 
said persons do not bring back smoothies for the rest of the 
department staff.
""",

"""
Note for female personnel:

If a dog enters the female showers and/or locker room, simply steal 
his glasses. He's not allowed in there, and he should know better.
""",

"""
The Overseers wish to remind all staff that Site-78 does not exist, 
nor has it ever existed. There is no Site-78.

Anyone who says otherwise is a liar, and should be reported to the 
relevant department head.
""",

"""
To whoever has been putting up flyers about the "Official Foundation 
Bring Your Daughter To Work Day" - please stop it.

No such event is scheduled. It would only end in disaster.
""",

"""
To whoever has been putting up flyers about the "Official Foundation 
Bring Your Daughter To Work Day" - please stop it.

No such event is scheduled.""",

"""
The Official Foundation BRING YOUR DAUGHTER TO WORK DAY!

THIS FRIDAY.
""",

"""
The official SCP Foundation BRING YOUR DAUGHTER TO WORK DAY!

THIS FRIDAY.
""",

# These texts taken from/inspired by
# FAM Radio Ep 02 "Space Is Falling" [Full Episode] 
# Foundation After Midnight Radio - #SCP
# https://youtu.be/_IE4IRRM6M0

#"""
#DVD copies of the test recordings from SCP-630 are available for $50.
#
#Contact the IT Department for details.
#""",


# These texts taken from/inspired by
# FAM Radio Ep 03 "The End Is Night" [Full Episode] 
# Foundation After Midnight Radio - #SCP
# https://youtu.be/4ipvSOOsGnc

## Nope, got nothing from that episode.

# These texts taken from/inspired by
# FAM Radio 04 "Universe Pending" [Full Episode]
# Foundation After Midnight Radio - #SCP
# https://youtu.be/coT535OPC9Q

"""
PLEASE REPORT ANY OVERLAPS OR DIMENSIONAL DIFFERENCES IMMEDIATELY TO
THE DEPARTMENT OF EXTRA-UNIVERSAL AFFAIRS.
""",

"""
Please report any time and space based anomalies and paradoxes to

THE TEMPORAL ANOMALY RESEARCH AND INTEGRATION STATION

as soon as you are able (even if they haven't happened yet).
""",

"""
Keep on

SECURING,

CONTAINING,

and

PROTECTING.
""",


# These texts taken from/inspired by
# FAM Radio Ep 05 "Sports Related Tension" [Full Episode]
# Foundation After Midnight Radio - #SCP
# https://youtu.be/HXqBoTTt0aw

"""
A reminder to all researchers - it's still not too late to sign up 
your team for the Global Test-a-thon. Collaborate with your fellow 
researchers and compete to complete the most experiments on an 
anomalous item in 48 hours.

Expand our knowledge of anomalous objects and win prizes for new 
discoveries and the most creative experiments!
""",

"""
If you come across any D-Class personnel wandering around your 
facility, call security and maintain a safe distance.

You never know what they might have been exposed to, and you don't 
know what you'll be exposed to by engaging them.

Be safe and secure yourself first.
""",

"""
The Annual SCP-682 Rodeo Championship has been cancelled.
""",

"""
SCP vs GOC Inter-Agency Charity Ice Hockey Game

Date:  FRIDAY

Venue: Sloth's Pit Ice Rink.

All proceeds go to the Foundation Widows and Orphans' Relief and the 
United Nations' International Children's Emergency Fund. 
""",

"""
The SCP Foundation - Global Occult Coalition Inter-Agency Charity Ice 
Hockey Game is on FRIDAY. 

Venue: Sloth's Pit Ice Rink. 

All proceeds go to benefit The Foundation Widows and Orphans' Relief 
and the United Nations' International Children's Emergency Fund. 
""",

"""
"REALITY BENDERS AND YOU: 
How to Survive When Existence Doesn't".

Speaker: Dr Cleff

Venue: Seminar Room %s

Date: %s
""" % (random.choice(("A", "B", "C", "D")),
       random.choice(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))),


# These texts taken from/inspired by
# FAM Radio Ep 06 "Happy Holiday Skipper" [Full Episode]
# Foundation After Midnight Radio - #SCP
# https://youtu.be/0Y1xklcnjOM

## Nothing relevant from that episode... very Christmas-y.

# These texts taken from/inspired by
# FAM Radio Ep 07 "Better Later" [Full Episode]
# Foundation After Midnight Radio - #SCP
# https://www.youtube.com/watch?v=UTACqGRTrN8

## Nothing relevant from that episode... 

# These texts taken from/inspired by
# FAM Radio Ep 08 "The Radio Show Must Go On" [Full Episode]
# Foundation After Midnight Radio - #SCP
# https://www.youtube.com/watch?v=4MfOb0mWSN0

"""
The first annual 5K Labcoat Fun Run

RUNNING FOR SCIENCE

Everyone welcome!

Funds raised go towards The Manna Charitable Foundation and their
unnatural disaster relief efforts.
""",

"""
The first annual 5K Labcoat Fun Run

RUNNING FOR SCIENCE

Everyone welcome!
""",

"""
REMINDER:

Pumpkin Spice flavor beverages are strictly prohibited 
in light of the recent containment of E-8820.

For details see Site-87's mail "Re: Subcutaneous Ginger".
""",

"""
STAY VIGILANT.

STAY SAFE.
""",


# These texts taken from/inspired by
# FAM Radio Ep 09 "I've Missed You, Listeners" [Full Episode]
# Foundation After Midnight Radio #SCP 👁️
# https://www.youtube.com/watch?v=e4T_RU2PCq4&t=22s

"""
Anomalous Animals Anonymous

A small monthly meet-up for personnel who find themselves transformed,
evolved, devolved, swapped with or physically changed into an animal or
otherwise non-human form.

Next meeting is on %s. 
""" % (random.choice(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))),


# These texts taken from/inspired by
# FAM Radio Ep 10 "Hand Over The DJ And No One Gets Hurt" 
# [Full Episode]- Foundation After Midnight
# https://www.youtube.com/watch?v=7AqAcWsTSYA

"""
A request from Dr Cleff:

Dr Cleff has requested that any personnel who write steamy fan fiction 
involving him to "keep it to to themselves, deep in the secret corners 
of their heart, where true love blooms and I don't have to see it."
""",

"""
Don't forget! Wednesday is Pizza Day!

So head on down to the cafeteria and grab yourself a hot slice!
""",

"""
LOOSE LIPS LOSE SKIPS.

MAINTAIN OPERATIONAL SECURITY.

YOU NEVER KNOW WHO'S LISTENING.
""",

#FROM SCP Documents:
#- http://www.scpwiki.com/scp-080
##"""
##All personnel are requested to stop referring to SCP-080 as 
##"The Boogieman".
##
##- Dr. ██████
##""",
"""
All personnel are requested to stop referring to SCP-080 as 
"The Boogieman".
""",

#- http://www.scpwiki.com/scp-529
"""
Staff are not permitted to feed cheese to SCP-529.

"Josie" will become distressed if not given sufficient cheese.
""",

"""
PLEASE DO NOT FEED CHEESE TO SCP-529.
""",

#http://www.scpwiki.com/scp-5056
"""
Per a request from Hiring and Regulation, we will be discontinuing 
the Employee of the Month Awards effective 06/31. JM4414, Amelia 
Torosyan, will be the final recipient in recognition of her quick 
thinking during JM64's cardiac episode last week.
""",

#http://www.scpwiki.com/scp-3739
"""
Need containment insurance? We've got you covered.

South-Central Protective Services, protecting you against malignant
Fae hexes, hemovore invasions, and flesh-eating Sarkic rituals since
1826.
""",

# From The Things Dr Bright Is Not Allowed To Do At The Foundation
# http://www.scpwiki.com/the-things-dr-bright-is-not-allowed-to-do-at-the-foundation

"""
Dr. Bright is not allowed to challenge Able to unwinnable games like tic-tac-toe.

It was three weeks before Able conceded a draw.
""",

"""
SCP-018 is not to be taunted!
""",

"""
Dr. Bright is not king of anywhere.

Or queen.
""",

"""
SCP-963 is not to be used for recreational or procreational purposes.
""",

"""
SCP-963 is not a joy buzzer.
""",

"""
Dr. Bright is not from an alternate timeline.
""",

"""
Chainsaws are not the solution to every question.
""",

"""
SCP speed dating never happened.

Any one who claims to remember such an event should report to Site
Command for administration of Class A amnesiac.
""",

"""
Nothing in the Foundation is rated 'Over 9000.'
""",

"""
Stop posting classified information on 4-chan.
""",

"""
Foundation credit cards or expense accounts are not to be used to 
purchase pornography.

(Not even anomalous pornography).
""",

"""
"For the Emperor" is not an acceptable justification for any decision.
""",

"""
The Foundation motto is "Secure, Contain, Protect", not 
"Let's use it on 682!"
""",

"""
The Foundation motto is "Secure, Contain, Protect", not 
"Throw D-Class at it until it stops."
""",

"""
The Foundation motto is "Secure, Contain, Protect", not 
"Will it blend?"
""",

"""
Attempts to use Foundation radio telescopes to contact omniscient and 
omnipotent extraterrestrial entities will result in a bill for any 
damage to local space-time, including the cost of demoting objects to 
dwarf planet status.
""",

"""
Dr. Bright is not allowed to arrange, schedule, advertise, promote, or 
sell tickets to, "cage matches" between Able and any SCPs.
""",

"""
"Challenge Accepted" is not a valid excuse for anything.
""",

"""
Dr. Bright is not allowed to 'borrow' SCP-159 for his office.
""",

"""
Dr. Bright is not allowed to refer to D-class personnel as "extra 
lives".
""",

"""
We have never had a Jamaican Vacation Giveaway, Dr. Bright is not in 
charge of it, and SCP-342 is not the official Foundation Travel 
Voucher.
""",

"""
Able is not Kratos.
""",

"""
Dr. Bright is not allowed to submit any incident reports to the Darwin 
Awards. Not even if you are sure it would win.
""",

"""
The eye-pods do not need hats, bow ties or any other form of clothing.
""",

"""
The Serpent's Hand is not a synonym for masturbation.
""",

"""
SCP-682 will not be sated by the ritual sacrifice of a virgin.
""",

"""
Even if Dr. Bright is wearing an eyepatch, he is not allowed to 
"Keel-Haul" anyone.

Not even on "Talk Like a Pirate Day".
""",

"""
Dr. Bright is not Kenny. We also ask new researchers (and Bright) to 
stop referring to him/self as such.
""",

"""
All Foundation personnel are required to attend a seminar on the 
difference between an original idea and a good idea before being 
allowed new or continuing contact with Dr. Bright, Dr. Clef, or 
Dr. Kondraki.
""",

"""
Dr. Bright is not a wizard, no matter what he might tell you.
""",

##"""
##Dr. Bright is not allowed to watch Firefly ever again. Most of the 
##people involved (that are still alive) are still in the psychiatric 
##ward.
##
##Dr Bright IS a leaf on the wind, watch him so- 
##Still too soon? Okay.
##""",

"""
There is no such department known as "The Bright Ideas Department."

If such a department did exist, Dr. Bright would not be in the employ 
of this department.
""",

##"""
##There are NO plans to shut down any site to prevent Corvid-19 infection. 
##
##That being said, if certain staffers do not start WASHING THEIR GODAMN 
##HANDS after using the bathroom, Dr. Bright has full permission to be 
##himself at them. I'm looking at you Magnus. 
##""",


#ORIGINAL... or at least new

"""LOST:

One animate (and extremely hostile) statue.

Answers to "SCP-173" or "Peanut".

If found, please contact  %s.
""" % NOTABLE_STAFF_DICT[random.choice(NOTABLE_STAFF_DICT.keys())]["short_name"],

"""LOST:

Half a grey tabby cat. 

Answers to "SCP-529" or "Josie".

If found, please contact %s.
""" % NOTABLE_STAFF_DICT[random.choice(NOTABLE_STAFF_DICT.keys())]["short_name"],

"""LOST:

One kitten/Feline Espionage Device. 

Answers to "SCP-1316" or "Lucy".

If found, please contact %s.
""" % NOTABLE_STAFF_DICT[random.choice(NOTABLE_STAFF_DICT.keys())]["short_name"]#,


]


def makesign(text, style, fontname, fontsize, margin, backgroundcolour, textcolor, fname, outdir):

    height = 1080
    width = 720

    #text = string.replace(text, "  ", " ")
    #text = string.strip(text)
    #text = text.split("\n\n")

    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, fillColor=backgroundcolour))
    max_linewidth = width-(margin*2)
            
    topline = height-margin-fontsize
    topy = topline
    for line1 in text:
        line1 = string.strip(line1)
        #print "line1: '%s'" %  line1
        l = ""
        oldline = ""
        #for word in string.split(line1, " "):
        for word in string.split(line1):
            if l == "":
                l = word
            else:
                l = "%s %s" % (l, word)
            #thislinewidth = c.stringWidth(l, fontname, fontsize)
            thislinewidth = stringWidth(l, fontname, fontsize)
            if thislinewidth > max_linewidth:
                
                if style == "left":
                    d.add(String(margin, topy, oldline, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
                elif style == "centre":
                    d.add(String(width/2.0, topy, oldline, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
                topy = topy - (fontsize * 1.25)
                oldline = word
                l = word
            else:
                oldline = l

        if l == oldline:
            if style == "left":
                d.add(String(margin, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
            elif style == "centre":
                d.add(String(width/2.0, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
            topy = topy - (fontsize * 1.25)
        elif l == word:
            if style == "left":
                d.add(String(margin, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
            elif style == "centre":
                d.add(String(width/2.0, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
            topy = topy - (fontsize * 1.25)

        topy = topy - (fontsize * 2.5)

    #fname = "Misc_Signs_%02d" % ((n*len(NOTE_TEXTS)) + x)

    renderPM.drawToFile(d, os.path.join(outdir, '%s.png' % fname), 'PNG')
    if VERBOSE == 0:
        print ".",
    else:
        print "Wrote file '%s'" % os.path.join(outdir, '%s.png' % fname)
    if MAKE_PDFS == 1:
        renderPDF.drawToFile(d, os.path.join(outdir, '%s.pdf' % fname), fname)
        if VERBOSE == 0:
            print ".",
        else:
            print "Wrote file '%s'" % os.path.join(outdir, '%s.pdf' % fname)

    return topy

def run():

    for n in (0,1,2):

        #default screen size in our game =
        #gui.init(1920, 1080)
        height = 1080
        width = 720

        shuffled_texts = copy.copy(NOTE_TEXTS)
        random.shuffle(shuffled_texts)
        outdir = os.path.join(THISDIR, "images", "signage", "breakrooms")


        for x in range(0, len(shuffled_texts)-1):
            style = random.choice(("left","centre")) 
            #margin = random.choice((10,12,15,20,24))
            #margin = random.choice((15,20,24))
            text = shuffled_texts.pop()
            text = string.replace(text, "  ", " ")
            text = string.strip(text)
            #text = string.join(string.split(text))
            fontname = random.choice(possible_fonts)
            #fontsize = random.choice((48,72,96))
            text = text.split("\n\n")
            if len(text) > 3:
                poss_font_sizes = (36, 48, 60)
            #a few special fiddles...
            elif string.find(text[0], "DAYS SINCE") >-1:
                #poss_font_sizes = (60, 72, 84, 96)
                #poss_font_sizes = (72, 84, 96)
                poss_font_sizes = (72, 84)
            elif string.find(text[0], "Global Test-a-thon") >-1:
                #poss_font_sizes = (60, 72, 84, 96)
                poss_font_sizes = (36, 48)
            elif string.find(text[0], "GOC Inter-Agency") >-1:
                #poss_font_sizes = (60, 72, 84, 96)
                poss_font_sizes = (36, 48)
            elif string.find(text[0], "If you come across") >-1:
                poss_font_sizes = (36, 48)
            elif string.find(text[0], "SCP vs GOC Inter-Agency ") >-1:
                poss_font_sizes = (36, 48)
            elif string.find(text[0], "The SCP Foundation - Global ") >-1:
                poss_font_sizes = (36, 48)
            elif string.find(text[0], "Please report any ") >-1:
                poss_font_sizes = (36, 48)

            else:
                poss_font_sizes = (48, 60, 72)
            fontsize = random.choice(poss_font_sizes)
            
            if string.find(text[0], "DAYS SINCE") >-1:
                margin = random.choice((fontsize/2,fontsize))
            else:
                margin = random.choice((fontsize/2,fontsize,fontsize*2))

            if string.find(text[0], "Keep on") >-1:
                style = "centre"

            b = random.randint(240,254)
            b = b/255.0
            backgroundcolour = colors.Color(b,b,b,1)

            textcolor = random.choice(ink_colours)
            #d.add(Rect(0, 0, width, height, fillColor=colors.white))


            d = Drawing(width, height)
            d.add(Rect(0, 0, width, height, fillColor=backgroundcolour))
            max_linewidth = width-(margin*2)
            
            topline = height-margin-fontsize
            topy = topline
            style = random.choice(("left","centre")) 
            #for line1 in text.split("\n\n"):
##            for line1 in text:
##                #print "line1: '%s'" %  line1
##                l = ""
##                oldline = ""
##                for word in string.split(line1, " "):
##                    if l == "":
##                        l = word
##                    else:
##                        l = "%s %s" % (l, word)
##                    #thislinewidth = c.stringWidth(l, fontname, fontsize)
##                    thislinewidth = stringWidth(l, fontname, fontsize)
##                    if thislinewidth > max_linewidth:
##                        
##                        if style == "left":
##                            d.add(String(margin, topy, oldline, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
##                        elif style == "centre":
##                            d.add(String(width/2.0, topy, oldline, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
##                        topy = topy - (fontsize * 1.25)
##                        oldline = word
##                        l = word
##                    else:
##                        oldline = l
##
##                if l == oldline:
##                    if style == "left":
##                        d.add(String(margin, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
##                    elif style == "centre":
##                        d.add(String(width/2.0, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
##                    topy = topy - (fontsize * 1.25)
##                elif l == word:
##                    if style == "left":
##                        d.add(String(margin, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=None))
##                    elif style == "centre":
##                        d.add(String(width/2.0, topy, l, fontName=fontname, fontSize=fontsize, fillColor=textcolor, textAnchor='middle'))
##                    topy = topy - (fontsize * 1.25)
##
##                topy = topy - (fontsize * 2.5)

     

            #d.add(String(100, topline, line2, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=strokecol))
            #topline = topline - fontsize * 1.5
            #d.add(String(100, topline, line3, fontName=fontname, fontSize=fontsize, fillColor=textcolor, strokeColor=strokecol))
            #topline = topline - fontsize * 1.5

            fname = "Misc_Signs_%02d" % ((n*len(NOTE_TEXTS)) + x)

            topy = makesign(text=text, style=style, fontname=fontname, fontsize=fontsize, margin = margin, backgroundcolour=backgroundcolour, textcolor = textcolor, fname=fname, outdir=outdir)
            while topy < margin:
                fontsize = fontsize - 5
                topy = makesign(text=text, style=style, fontname=fontname, fontsize=fontsize, margin = margin, backgroundcolour=backgroundcolour, textcolor = textcolor, fname=fname, outdir=outdir)


            ##renderPM.drawToFile(d, os.path.join(outdir, '%s.png' % fname), 'PNG')
            ##print "Wrote file '%s'" % os.path.join(outdir, '%s.png' % fname)
            ##if MAKE_PDFS == 1:
            ##    renderPDF.drawToFile(d, os.path.join(outdir, '%s.pdf' % fname), fname)
            ##    print "Wrote file '%s'" % os.path.join(outdir, '%s.pdf' % fname)
    print "\n\nDONE!\n\n"

if __name__ == "__main__":
    print "make_handwritten_signs.py \n(%s sign versions known about)" % (len(NOTE_TEXTS))
    print random.choice(NOTE_TEXTS)
    run()