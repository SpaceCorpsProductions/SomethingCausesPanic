#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Contains information about book-type SCPs (only anything about them
specifically being books - for anything else see objects.py)."""

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.


VERSION = "0.8.0b"
__VERSION__ = VERSION

# 78 book-type SCPs known about.

import string, random
from types import IntType, FloatType, NoneType, StringType


BOOK_SCPS = [
    "SCP-140",      #'An Incomplete Chronicle'
    "SCP-141",      #'Codex Damnatio'
    "SCP-152",      #'Book of Endings'
    "SCP-223",      #'A Photo Album'
    "SCP-241",      #'Good Home Cooking'
    "SCP-248",      #'"110%"'
    "SCP-454",      #'Comic Book'
    "SCP-546",      #'A Notebook'
    "SCP-592",      #'Inaccurate History Book'
    "SCP-701",      #'The Hanged King's Tragedy'
    "SCP-733-02",   #part of SCP-733: 'A Pair of Scissors'
    "SCP-782",      #'All-New You'
    "SCP-910",      #'Dust, Embodied'
    "SCP-1025",     #'Encyclopedia of Diseases'
    "SCP-1065",     #'Self-Immolating Books'
    "SCP-1082",     #'The Whole Truth'
    "SCP-1138",     #'Book of Letters'
    "SCP-1161",     #'How-To Book'
    "SCP-1195",     #'Child's Storybook'
    "SCP-1230",     #'A Hero is Born'
    "SCP-1235",     #'Atlas Microcosm'
    "SCP-1256",     #'Bees Are Smarter Than You Think'
    "SCP-1326",     #'The Lexicon'
    "SCP-1397",     #'A Failed Work of Art'
    "SCP-1399",     #'Another Way of Hearing'
    "SCP-1425",     #'Star Signals'
    "SCP-1484",     #'Murder Diary'
    "SCP-1554",     #'The Damaged Fellowship'
    "SCP-1665",     #'8 Across, 18 Across'
    "SCP-1772",     #'"Egg" Allergy'
    "SCP-1833",     #'Class of '76'
    "SCP-1839",     #'Reproductive Methods of Bony Fish'
    "SCP-1841",     #'So Much To See, So Much Unseen'
    "SCP-1954",     #'Helen Homemaker's Hints For The Harried Housewife'
    "SCP-1997",     #'Endless Activity Book'
    "SCP-2065",     #'Empty Inside'
    "SCP-2081",     #'Making Your Dreams Your Reality'
    "SCP-2233",     #'Sociosophy'
    "SCP-2233-1",   #'Sociosophy'
    "SCP-2685",     #'Thinking in Abstraction'
    "SCP-2714",     #'Billions of Blue Blistering'
    "SCP-2754",     #'How To Put 110% Into Everything'
    "SCP-2811",     #'Kali Yuga'
    "SCP-2976",     #'Hall of the Last King'
    "SCP-3039",     #'An Antiquated Guide'
    "SCP-3079",     #'300 Tricks: Stage Magic Made Easy'
    "SCP-3163",     #'The Almanack'
    "SCP-3345",     #'Crime Novel'
    "SCP-3348",     #'Lost Dictionary'
    "SCP-3484",     #'Missing Pieces'
    "SCP-3669",     #'A Mathematics Self Help Book'
    "SCP-3692",     #'the notebook'
    "SCP-3726",     #'AnthropomorFic'
    "SCP-3795",     #'Who Killed Your Dog?!'
    "SCP-4147",     #'Encyclopedia Obscura'
    "SCP-4211",     #'Memoirmento'
    "SCP-4248",     #'Alphabet and Omega'
    "SCP-4430",     #'The Faceless Live In Evanholly'
    "SCP-4485",     #'Such Black Light'
    "SCP-4569",     #'Plot Twist'
    "SCP-4679",     #'The Sweet Taste of Victory'
    "SCP-4716",     #'The Plutovore's Cookbook'
    "SCP-4740",     #'As Davy wondered where they'd been, he read a book named Grass and Green.'
    "SCP-4828",     #'The Big Book Of Achievable Spells, made easy'
    "SCP-4854",     #'The "Real" Necronomicon and other Godawful Occult Manuscripts'
    "SCP-4890",     #'Dr. Wondertainment's Guide to History'
    "SCP-4893",     #'Agapanthus'
    "SCP-4942",     #'How to Summon a Lemon'
    "SCP-5096-1",   #'Butterflies work in mysterious ways ??????¯?'
    "SCP-5102",     #'Dear Diary'
    "SCP-5166",     #'Inspiration'
    "SCP-5198",     #'For Your Own Good'
    "SCP-5216",     #'"[ACCESS DENIED]"'
    "SCP-5462",     #'Misery is the State of Every Soul Burdened by Mortality.'
    "SCP-5462-A",   #'Misery is the State of Every Soul Burdened by Mortality.'
    "SCP-5490",     #'The Lost Emperor"'
    "SCP-5628",     #'OCD? Have you tried unicycle yoga?'
    "SCP-5905"#,     #'Gashadokuro'

    ]


BOOK_SCPS_DICT = {

     #SCP-140 - "An Incomplete Chronicle"
    "SCP-140":     {
        "name":         "SCP-140",    # An Incomplete Chronicle
        "designation":  "SCP-140",
        "colour":       "black",
        "binding":      "hardback",
        "title":        "A Chronicle of the Daevas"
        # SCP-140 is a modern hardcopy book with an unremarkable black binding
        # and an unknown number of white pages. The book jacket is missing, but
        # the title, “A Chronicle of the Daevas”, is clearly legible.
        },

    #SCP-141 - "Codex Damnatio"
    "SCP-141":     {
        "name":         "SCP-141",    # Codex Damnatio
        "designation":  "SCP-141",
        "colour":       "leather",
        "binding":      "hardback",
        "title":        "Codex Damnatio"
        # SCP-141 is a small leather-bound codex dating back to
        # Roman times, easily carried in one hand.
        #[codex = "an ancient manuscript text in book form."]
        },

    #SCP-152 - "Book of Endings"
    "SCP-152":     {
        "name":         "SCP-152",    # Book of Endings
        "designation":  "SCP-152",
        "colour":       "leather",
        "binding":      "hardback",
        "title":        "Book of Endings"
        # SCP-152 is a large, hardbound book with leather bindings.
        },

    #SCP-223 - "A Photo Album"
    "SCP-223":     {
        "name":         "SCP-223",    # A Photo Album
        "designation":  "SCP-223",
        "colour":       None,
        "binding":      "hardback",
        "title":        None # Untitled
        # SCP-223 is a photo album, capable of holding thirty
        # (30) photos, bound like a small hardcover book.
        },

    #SCP-241 - "Good Home Cooking"
    "SCP-241":     {
        "name":         "SCP-241",    # Good Home Cooking
        "designation":  "SCP-241",
        "colour":       "red and white",
        "binding":      "hardback",
        "title":        "Good Home Cooking"
        # SCP-241 appears as a normal book, 33 cm x 23 cm x
        # 3.5 cm, entitled Good Home Cooking. The cover of SCP-241 is a red
        # and white checkerboard pattern, with the title in simple black
        # letters on the front and spine.
        },

    #SCP-248 - "110%"
    "SCP-248":     {
        "name":         "SCP-248",    # 110%
        "designation":  "SCP-248",
        "colour":       None, # None given
        "binding":      "booklet",
        "title":        None
        # SCP-248 is a twenty-five (25) page booklet of
        # stickers, each reading "110%" with a small pressed imprint of the
        # words "The Factory" in the bottom right corner. The booklet itself
        # is 7.5 cm in height and 15 cm in length. Each page of SCP-248
        # contains two (2) of the stickers. 
        },

    #SCP-454 - "Comic Book"
    "SCP-454":     {
        "name":         "SCP-454",    # Comic Book
        "designation":  "SCP-454",
        "colour":       None, # special, illustrated
        "binding":      "booklet",
        "title":        "The Crypt of Terror"
        # SCP-454 should be kept in a plastic bag with a thin piece of acid-free
        # cardstock. 
        # SCP-454 is a comic book, titled “The Crypt of Terror”. The front cover
        # has the picture of a female, nervously looking around, with a shadowy
        # figure some distance behind her. The price is listed as ten cents and
        # the issue number is seventeen.
        },

    #SCP-546 - "A Notebook"
    "SCP-546":     {
        "name":         "SCP-546",    # A Notebook
        "designation":  "SCP-546",
        "colour":       None, # None given
        "binding":      "spiral-bound",
        "title":        None # Untitled
        # SCP-546 consists of a single pad of spiral-bound, lined, ████ brand
        # note paper. SCP-546 measures 15 cm x 23 cm, and currently consists of
        # 57 sheets out of the original 60.
        },

    #SCP-592 - "Inaccurate History Book"
    "SCP-592":     {
        "name":         "SCP-592",    # Inaccurate History Book
        "designation":  "SCP-592",
        "colour":       "deep blue", 
        "binding":      "hardback",
        "title":        "Chronicle of the 20th Century"#,
        # SCP-592 is a large hardcover book which exhibits no external qualities
        # that could be considered unusual, but which can cause delusions,
        # psychosis, changes in physical health and appearance, or even severe
        # wounding when read. It is titled "Chronicle of the 20th Century" and
        # consists of 450 all-color printed pages. It is reported that it has a
        # printed cover (no dust jacket) with the title of the book, the
        # publisher, and a selection of illustrations from within the text. The
        # original cover is a deep blue.
        },

    #SCP-701 - "The Hanged King's Tragedy"
    "SCP-701":     {
        "name":         "SCP-701",    # The Hanged King's Tragedy
        "designation":  "SCP-701",
        "colour":       None, #varies with edition
        "binding":      None, #varies with edition
        "title":        "The Hanged King's Tragedy"#,
        # All materials relating to SCP-701 are to be kept in a triple-locked
        # archive at Storage Site-██. These items currently consist of: the two
        # (2) currently extant copies of the 1640 quarto; twenty-seven (27)
        # copies of the 1965 trade paperback edition; ten (10) copies of a 1971
        # hardcover printing; twenty-one (21) floppy diskettes, consisting of
        # data seized from raids on [EXPUNGED]; one (1) S-VHS video cassette
        # tape (designated SCP-701-19██-A); and one (1) steel knife of unknown
        # origin (designated SCP-701-19██-B).
        # SCP-701, The Hanged King's Tragedy, is a Caroline-era revenge tragedy
        # in five acts. Performances of the play are associated with sudden
        # psychotic and suicidal behavior among both observers and participants,
        # as well as the manifestation of a mysterious figure, classified as
        # SCP-701-1.
        },

    #"SCP-733-02",   #part of SCP-733: 'A Pair of Scissors'
    "SCP-733-02":     {
        "name":         "SCP-733-02",    # part of SCP-733: 'A Pair of Scissors'
        "designation":  "SCP-733-02",
        "colour":       "leather",
        "binding":      "hardback",
        "title":        "Diary"
        # SCP-733-01 is a pair of ornate silver scissors, apparently crafted circa 18██. 
        # When discovered, SCP-733-01 was pressed between the pages of
        # SCP-733-02, a hand-crafted, leather-bound book containing
        # approximately 80 pages. The pages of SCP-733-02 contain 33 black and
        # white photographs, as well as 137 fragments of handwritten text. The
        # following inscription is also visible on the front of SCP-733-02:
        # "Diary"
        },

    #SCP-782: 'All-New You'
    "SCP-782":     {
        "name":         "SCP-782",    # All-New You
        "designation":  "SCP-782",
        "colour":       None, # None given
        "binding":      "paperback", #guessed, but it's vanity published.
        "title":        "Three Easy Steps to an All-New You"
        # SCP-782 is an anonymously published self-help book entitled "Three
        # Easy Steps to an All-New You". No author is listed, and its publisher,
        # ███████ █████, closed in 199█. 
        },

    #SCP-910: 'Dust, Embodied'
    "SCP-910":     {
        "name":         "SCP-910",    # Dust, Embodied
        "designation":  "SCP-910",
        "colour":       None, # None given
        "binding":      "hardback", #guessed
        "title":        "Organizational Symbology: New Tools for the Oldest Craft"
        # SCP-910 is an 156-page book titled Organizational Symbology: New Tools
        # for the Oldest Craft, which describes methods to transform mundane
        # organizations into anomalous entities for use in thaumaturgic rituals.
        # Approximately 20 copies of SCP-910 have been printed yearly since 1955
        # by the Penn & Brooke Scribeworks (GoI-154). The author is listed as
        # Erin Ahmadi, whose biographical summary describes as a thaumaturgist
        # and amateur botanist living in Hell, Michigan. No other records of
        # this individual have been located.
        },

    #SCP-1025: 'Encyclopedia of Diseases'
    "SCP-1025":     {
        "name":         "SCP-1025",    # Encyclopedia of Diseases
        "designation":  "SCP-1025",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "The Encyclopedia of Common Diseases"
        # SCP-1025 is a hardcover book, approximately 1,500 pages long. The
        # front cover and spine feature the title "The Encyclopedia of Common
        # Diseases." The publisher's page indicates the book was printed in 19██
        # by █████ Press.
        },

    #SCP-1065: 'Self-Immolating Books'
    "SCP-1065":     {
        "name":         "SCP-1065",    # Self-Immolating Books
        "designation":  "SCP-1065",
        "colour":       "red leather",
        "binding":      "hardback",
        "title":        None
        # SCP-1065 is a four volume series of books written in an Eastern Slavic
        # language, apparently of the early-to-mid 1800's and possibly an
        # obscure local dialect or mixture of languages. The overarching title
        # roughly translates to "The Dangers Of Free Knowledge." They are bound
        # with red leather featuring faux-golden embossing, and show both fire
        # and water damage around the edges, along with significant foxing
        # (discoloration and degradation due to aging, molding, etc.) of the
        # paper.
        },

    #SCP-1082: 'The Whole Truth'
    "SCP-1082":     {
        "name":         "SCP-1082",    # The Whole Truth
        "designation":  "SCP-1082",
        "colour":       None, #None given
        "binding":      None, #None given
        "title":        "The Catcher in the Rye"
        # This book is a copy of The Catcher in the Rye by J.D. Salinger. The
        # title page of the book has been signed by the author and an
        # inscription at the bottom of the title page has on it the words "To
        # Jack, here's to making the world better." The words on its copyright
        # page indicate that the book was printed in 1977 in Chicago.
        # The book keeps you honest. Not only can you not lie, you cannot avoid
        # the truth no matter what you do. There are many ways to deceive
        # others, and once you see this book, you are no longer capable of any
        # of them.
        },

    #SCP-1138: 'Book of Letters'
    "SCP-1138":     {
        "name":         "SCP-1138",    # Book of Letters
        "designation":  "SCP-1138",
        "colour":       None,
        "binding":      None,
        "title":        None # Special, changes when handled by a new person
        # SCP-1138 is perceived to be a book of philosophers' and/or writers'
        # correspondence. Though the writing style always corresponds to a given
        # author, the vast majority of letters are forgeries, with a few found
        # to be genuine unsent drafts. The book's author changes based on the
        # scientific and personal interests of the reader and its contents
        # depend on reader's beliefs regarding the author's ideas.
        },

    #SCP-1161: 'How-To Book'
    "SCP-1161":     {
        "name":         "SCP-1161",    # How-To Book
        "designation":  "SCP-1161",
        "colour":       "black",
        "binding":      "paperback",
        "title":        None #special, changes every 24 hours
        #SCP-1161 is a black paperback book with a varying number of pages. 
        #The title, on both the cover and binding in white lettering changes every 24 
        #hours at precisely 3:00 A.M. GMT, but invariably begin with the words, "How to".
        #The object will always contain instructions on how to perform various actions,
        #ranging from very useful to utterly pointless.
        },

    #SCP-1195: 'Child's Storybook'
    "SCP-1195":     {
        "name":         "SCP-1195",    # Child's Storybook
        "designation":  "SCP-1195",
        "colour":       "leather",
        "binding":      "hardback",
        "title":        None 
        # SCP-1195 is a leather-bound book (approx. 25cm x 17cm) of 
        # indeterminate origin and age; carbon-dating on the pages has given inconsistent 
        # results, and forensic examination of the leather matches no known species. It 
        # seems to have a variable number of pages, averaging approximately at 400.
        },

    #SCP-1230: 'A Hero is Born'
    "SCP-1230":     {
        "name":         "SCP-1230",    # A Hero is Born
        "designation":  "SCP-1230",
        "colour":       "green",
        "binding":      "hardback",
        "title":        None # unlabeled
        # SCP-1230 is an unlabeled, green hardcover book with no apparent
        # exceptional qualities. When SCP-1230 is opened, it displays the phrase
        # "A hero is born" on the first page viewed, while all other pages will
        # be blank.
        },

    #SCP-1235: 'Atlas Microcosm'
    "SCP-1235":     {
        "name":         "SCP-1235",    # Atlas Microcosm
        "designation":  "SCP-1235",
        "colour":       None, # None stated
        "binding":      "hardback", #guess
        "title":        "Andrees Allgemeiner Handatlas" # unlabeled
        # SCP-1235 is a large illustrated German-language atlas of the world
        # (Andrees Allgemeiner Handatlas). The title page claims the atlas to
        # have been printed by Velhagen & Klasing in 1903 as the 3rd revision of
        # the 1899 4th edition; the publisher has no record of this printing.
        # Under microscopic analysis, details such as state names, city
        # locations, and shading for discrete political entities fail to appear.
        # Instead, at higher magnifications the atlas depicts a photorealistic
        # satellite view of the magnified area.
        },

    #SCP-1256: 'Bees Are Smarter Than You Think'
    "SCP-1256":     {
        "name":         "SCP-1256",    # Bees Are Smarter Than You Think
        "designation":  "SCP-1256",
        "colour":       None, # None stated
        "binding":      "booklet",
        "title":        "Bees - Smarter Than You Think" 
        # SCP-1256 is a 24-page pamphlet entitled 'Bees - Smarter Than You
        # Think.' Its contents appear to be intended to be informative; however,
        # much of it is nonsensical. The cover page claims SCP-1256 was authored
        # by Dillaine Iurtey and Ryan Hughes, and published by Redrose
        # Publishing Sydney in 1997. Redrose Publishing Sydney has no record of
        # SCP-1256's publication, and neither author has any recollection of
        # writing SCP-1256.
        },

    #SCP-1326: 'The Lexicon'
    "SCP-1326":     {
        "name":         "SCP-1326",    # The Lexicon
        "designation":  "SCP-1326",
        "colour":       "leather",
        "binding":      "hardback",
        "title":        None # None given 
        # SCP-1326 is an ornate leather-bound hardcover book adorned with
        # various moving parts on its front cover, including a circular numbered
        # dial in its upper-left corner, a semicircular dial in the lower-left
        # corner, and several jointed mechanical arms crossing over its center,
        # ending in mechanical claws or circular lenses. SCP-1326 is secured by
        # a lock on its right side, designed to fit a small key designated
        # SCP-1326-1.
        },

    #SCP-1397: 'A Failed Work of Art'
    "SCP-1397":     {
        "name":         "SCP-1397",    # A Failed Work of Art
        "designation":  "SCP-1397",
        "colour":       None, # varies with individual book
        "binding":      "hardback", #none given, but we need something
        "title":        None # varies with individual book
        # SCP-1397-1 through -5 are a set of five travel guides that describe
        # rural locations in former Czechoslovakia. The author of the five books
        # is listed as one █████ ███████; however, linguistic analysis of the
        # text has indicated that each book was written by a different author.
        # As no evidence of a █████ ███████ has been located, the name is most
        # likely a pseudonym. While there is no copyright page or publisher
        # information present, the information within the books suggests that
        # they were written in the early 1950's.
        },

    #SCP-1399 - "Another Way of Hearing"
    "SCP-1399":     {
        "name":         "SCP-1399",    # Another Way of Hearing
        "designation":  "SCP-1399",
        "colour":       None, # None given
        "binding":      "hardback", # none given, but we need something
        "title":        "Another Way of Hearing"
        # SCP-1399 is a thin fifteen page children’s book titled “Another Way of
        # Hearing.” The cover depicts the earth, with the title above it. There
        # is no author indicated on the cover.
        },

    #SCP-1425: 'Star Signals'
    "SCP-1425":     {
        "name":         "SCP-1425",    # Star Signals
        "designation":  "SCP-1425",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "Star Signals"
        # SCP-1425 is a hardcover book, measuring 20 cm x 35 cm x 5 cm and
        # published in 2005 by the company [REDACTED] Books (now defunct—see
        # Operation Stargazer files). The front cover bears the title "Star
        # Signals". The document is a nonfiction book of the “self-help” genre,
        # advertised as a manual which teaches the use of the “Five-Step Star
        # Signal Method” to achieve the reader’s dreams and ambitions.
        },

    #SCP-1484: 'Murder Diary'
    "SCP-1484":     {
        "name":         "SCP-1484",    # Murder Diary
        "designation":  "SCP-1484",
        "colour":       "leather",
        "binding":      None, # None given
        "title":        None  # None given
        # SCP-1484 is a leather-bound journal measuring 30.2 cm in length,
        # 23.1 cm in width, and 4.7 cm thick. SCP-1484 contains 326 blank pages.
        # However, pages 125-142 of SCP-1484 feature a series of roughly 5cm2
        # areas or "panels" (approximately 20 per page) which, when in contact
        # with human skin, cause the "reader" to experience a range of different
        # tactile sensations throughout their body. Each individual panel
        # corresponds to a different, usually complex set of tactile stimuli.
        },

    #SCP-1554: 'The Damaged Fellowship'
    "SCP-1554":     {
        "name":         "SCP-1554",    # The Damaged Fellowship
        "designation":  "SCP-1554",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        "The Fellowship of the Ring"
        # SCP-1554 is a copy of the book The Fellowship of the Ring by J.R.R.
        # Tolkien, published in 1969 by ██████ Press. SCP-1554 is in very poor
        # condition for its age, with several pages being marked with pen,
        # pencil and crayon, moderate water damage to later chapters, and the
        # entirety of the chapter In The House of Tom Bombadil being missing.
        },

    #SCP-1665: '8 Across, 18 Across'
    "SCP-1665":     {
        "name":         "SCP-1665",    # 8 Across, 18 Across
        "designation":  "SCP-1665",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        None # None given
        # SCP-1665 is a [REDACTED] brand book published by _________ Puzzles,
        # copyrighted 1999.
        # SCP-1665's _________ properties manifest when anyone attempts to
        # maintain written or physical records of it.
        # All written records will be altered so that they are in a form of
        # a crossword ______, making storage of information on SCP-1665
        # difficult.
        },

    #SCP-1772: '"Egg" Allergy'
    "SCP-1772":     {
        "name":         "SCP-1772",    # "Egg" Allergy
        "designation":  "SCP-1772",
        "colour":       None, # None given
        "binding":      "paperback", # It's a "Pocket" edition, so probably softback
        #"title":        "███████-███████ Pocket Spanish-English Dictionary"
        "title":        u"███████-███████ Pocket Spanish-English Dictionary"
        # SCP-1772 is a copy of the 1983 edition of the ███████-███████ Pocket
        # Spanish-English Dictionary, though it has been discovered to have
        # flaws (termed SCP-1772-1) not present in any printings released by the
        # publisher.
        },

    #SCP-1833: 'Class of '76'
    "SCP-1833":     {
        "name":         "SCP-1833",    # Class of '76
        "designation":  "SCP-1833",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "Reflections of '76"
        # SCP-1833 is a copy of the 1976 edition ███████ High School yearbook.
        # Its appearance is consistent with other copies of the book, and
        # appears to have normal wear for an object of its age. The yearbook is
        # entitled "Reflections of '76". It is hardcover, and contains exactly
        # fifty pages. The book is divided into five sections: a collection of
        # student photographs, photographs from around the school year, club
        # photos, photos from athletic events, and an autograph section.
        },

    #SCP-1839: 'Reproductive Methods of Bony Fish'
    "SCP-1839":     {
        "name":         "SCP-1839",    # Reproductive Methods of Bony Fish
        "designation":  "SCP-1839",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "Reproductive Methods of Bony Fish"
        # SCP-1839 is a 1.3 kilogram hardcover textbook 46 cm x 37 cm in size.
        # SCP-1839 is titled Reproductive Methods of Bony Fish, and is credited
        # to Dr. Albert Salernus. The publisher on the sleeve is abbreviated to
        # "Uriah Fetch Publishing". The sleeve of the book shows a rough,
        # colourful diagram of the reproductive system of an Atlantic blue
        # marlin, similar to what the reader currently is.
        },

    #SCP-1841: 'So Much To See, So Much Unseen'
    "SCP-1841":     {
        "name":         "SCP-1841",    # So Much To See, So Much Unseen
        "designation":  "SCP-1841",
        "colour":       None, # None given
        "binding":      "paperback",
        "title":        "1001 Places To Be Before You Die"
        # SCP-1841 is a well-worn soft cover book, titled 1001 Places To Be
        # Before You Die. It contains an indeterminate number of pages, and is
        # 4cm thick. Copyright information listed within SCP-1841 claims it was
        # published by the publisher "Periscope Publishing" in 1989.
        # For the first 95 pages, SCP-1841 lists 95 separate popular tourist
        # locations and describes the main attractions, in addition to
        # recommending methods of transportation which are contemporary to the
        # time period in which SCP-1841 was published.
        # After 95 pages have been read, the subject will report additional
        # locations and activities listed in SCP-1841 that are unique with each
        # viewing.
        },

    #SCP-1954: 'Helen Homemaker's Hints For The Harried Housewife'
    "SCP-1954":     {
        "name":         "SCP-1954",    # Helen Homemaker's Hints For The Harried Housewife
        "designation":  "SCP-1954",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "Helen Homemaker's Hints For The Harried Housewife"
        # SCP-1954 is a 333 page hardcover book bearing the title Helen
        # Homemaker's Hints For The Harried Housewife stamped on front with
        # flaking gold ink. No marks appear elsewhere on cover, including spine.
        # Dust jacket, if ever present, is missing. Copyright page indicates
        # book copyrighted in 1954 by ██████. Summary research into ██████
        # archives indicates no such publication on record.
        },

    #SCP-1997: 'Endless Activity Book'
    "SCP-1997":     {
        "name":         "SCP-1997",    # Endless Activity Book
        "designation":  "SCP-1997",
        "colour":       None, # special, illustrated
        "binding":      "booklet",
        "title":        "Dr. Wondertainment's Infinite Fun-Book™!" 
        # SCP-1997 is a single sheet of white paper folded into a booklet
        # measuring 12cm x 20cm x 5cm. The front cover features a brightly
        # colored illustration depicting two children, a brown-haired boy and a
        # blonde-haired girl, sliding along a Möbius strip twisted into a
        # figure-eight, with a variety of planets, stars and other celestial
        # objects in the background. The words "Dr. Wondertainment's Infinite
        # Fun-Book™! The Wonders of SPACE!" fill the top third of the cover.
        },

    #SCP-2065 - "Empty Inside"
    "SCP-2065":     {
        "name":         "SCP-2065",    # Empty Inside
        "designation":  "SCP-2065",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        "Eat Whatever You Want… and Still Lose Weight!" 
        # SCP-2065 is a book titled Eat Whatever You Want… and Still Lose
        # Weight! by Christian Paulman. If an individual reads any portion of
        # pages 9-23 of SCP-2065, that individual will be converted into an
        # SCP-2065-1 instance.
        },

    #SCP-2081 - "Making Your Dreams Your Reality"
    "SCP-2081":     {
        "name":         "SCP-2081",    # Making Your Dreams Your Reality
        "designation":  "SCP-2081",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "Making Your Dreams Your Reality: Lucidity for Beginners" 
        # SCP-2081 are multiple identical copies of an 82-page hardback volume
        # entitled 'Making Your Dreams Your Reality: Lucidity for Beginners',
        # purporting to be an informal guide to lucid dreaming. The author is
        # cited as Dr. ███████ █████████, a supposed expert in circadian
        # neuroscience.
        },

    #SCP-2233 - "Sociosophy"
    "SCP-2233":     {
        "name":         "SCP-2233",    # Sociosophy
        "designation":  "SCP-2233",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        "Polylogue – Over the horizon of postmodern relativism" 
        # SCP-2233 is an academic discipline called "Sociosophy", manifesting
        # through SCP-2233-1 instances and SCP-2233-2 events.
        # SCP-2233-1 is a book labeled "Polylogue – Over the horizon of
        # postmodern relativism", published by "The Club of Friends of
        # Sociosophy" in Prague, Czech Republic, in 2014. The authors are
        # listed as StbB. Emil František; BasSc., WtaN. Herbert Mužný; DmbS. et
        # DmbS. Martin Příklopa; and collective.
        },
    #SCP-2233 - "Sociosophy"
    "SCP-2233-1":     {
        "name":         "SCP-2233-1",    # Sociosophy
        "designation":  "SCP-2233-1",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        "Polylogue – Over the horizon of postmodern relativism" 
        # SCP-2233 is an academic discipline called "Sociosophy", manifesting
        # through SCP-2233-1 instances and SCP-2233-2 events.
        # SCP-2233-1 is a book labeled "Polylogue – Over the horizon of
        # postmodern relativism", published by "The Club of Friends of
        # Sociosophy" in Prague, Czech Republic, in 2014. The authors are
        # listed as StbB. Emil František; BasSc., WtaN. Herbert Mužný; DmbS. et
        # DmbS. Martin Příklopa; and collective.
        },

    #SCP-2685 - "Thinking in Abstraction"
    "SCP-2685":     {
        "name":         "SCP-2685",    # Thinking in Abstraction
        "designation":  "SCP-2685",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        "Thinking in Abstraction" 
        # SCP-2685 is a philosophy book, copyright 1966, known as Thinking in
        # Abstraction. An author, if any, of SCP-2685 is unknown. SCP-2685 lacks
        # Anglo-Saxon Symbol #5 in its writing, and as a ramification, is
        # stylistically unusual.
        },

    #SCP-2714 - "Billions of Blue Blistering"
    "SCP-2714":     {
        "name":         "SCP-2714",    # Billions of Blue Blistering
        "designation":  "SCP-2714",
        "colour":       None, # none given
        "binding":      None, # none given
        "title":        "The Adventures of Tintin: Flight 714"
        # SCP-2714 is a copy of the 1968 graphic novel The Adventures of Tintin:
        # Flight 714 by Belgian artist Georges Remi (known by his pen name
        # Hergé), translated from French into English by Leslie Lonsdale-Cooper
        # and Michael Turner and published by Methuen Children's Books. SCP-2714
        # shows signs of its age, with some minor damage, but is in mostly good
        # condition.
        },

    #SCP-2754 - "How To Put 110% Into Everything"
    "SCP-2754":     {
        "name":         "SCP-2754",    # How To Put 110% Into Everything
        "designation":  "SCP-2754",
        "colour":       None, 
        "binding":      "paperback",
        "title":        "How To Put 110% Into Everything" 
        # SCP-2754 is a paperback self-help book that is 326 pages in length.
        # The contents of SCP-2754 are split into seven chapters written by the
        # now deceased Ruth Wates and a prolugue [sic] written by Dr. Bill
        # Simmons.
        },

    #SCP-2811 - "Kali Yuga"
    "SCP-2811":     {
        "name":         "SCP-2811",    # Kali Yuga
        "designation":  "SCP-2811",
        "colour":       None, 
        "binding":      "paperback",
        #"title":        "██████, blue" 
        "title":        u"██████, blue" 
        # SCP-2811 is a large paperback book titled "██████, blue". Preliminary
        # investigations revealed no author or publishing house linked to that
        # name. The item numbers 564 pages of text, excluding the title page and
        # a final blank page. 
        },

    #SCP-2976 - "Hall of the Last King"
    "SCP-2976":     {
        "name":         "SCP-2976",    # Hall of the Last King
        "designation":  "SCP-2976",
        "colour":       None, # none given
        "binding":      None, # none given
        "title":        "In the Hall of the Last King"
        # SCP-2976 is a book written by science-fiction writer Harold G. Talont,
        # titled 'In the Hall of the Last King.' First published in 1932 by the
        # now defunct science-fiction publisher 'Bewilder Books', the book
        # describes protagonist Tom Johnson's 'exploration of a temple to
        # strange gods, in darkest Africa.'
        },

    #SCP-3039 - "An Antiquated Guide"
    "SCP-3039":     {
        "name":         "SCP-3039",    # An Antiquated Guide
        "designation":  "SCP-3039",
        "colour":       None, 
        "binding":      "paperback",
        "title":        "An Antiquated Guide to Avoiding Writer’s Block" 
        # SCP-3039 is a set of 34 contained instances of a paperback novel,
        # titled An Antiquated Guide to Avoiding Writer’s Block. The author, R.
        # Sebastian, designated PoI-2665, has authored several other anomalies;
        # attempts to track and capture this person are ongoing. The cover
        # features a cognitohazardous image of a nondescript, grey rectangular
        # prism. Upon viewing the image, any exposed parties will be affected by
        # the manifestation of SCP-3039-1.
        },

    #SCP-3079 - "300 Tricks: Stage Magic Made Easy"
    "SCP-3079":     {
        "name":         "SCP-3079",    # 300 Tricks: Stage Magic Made Easy
        "designation":  "SCP-3079",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "300 Tricks: Stage Magic Made Easy" 
        # SCP-3079, 300 Tricks: Stage Magic Made Easy, is a 435-page hard-back
        # book written and self-published by Tobin Hollis. It contains detailed
        # instructions for performing numerous stage tricks.
        # Instances of SCP-3079-A are instructions contained within SCP-3079
        # which describe methods to achieve anomalous results.
        },

    #SCP-3163: 'The Almanack'
    "SCP-3163":     {
        "name":         "SCP-3163",    # The Almanack
        "designation":  "SCP-3163",
        "colour":       None, # None given
        "binding":      "hardback",
        "title":        "GLATTFELDER’S NEW NORTHTON ALMANACK." 
        # SCP-3163 is a hardbound book, entitled "GLATTFELDER’S NEW NORTHTON
        # ALMANACK." SCP-3163 displays significant signs of wear and use, the
        # most prominent of which are overlapping stains on the rear cover,
        # identified as coffee, beer, and blood. Chemical and historical
        # analyses of the book indicate that SCP-3163 was manufactured in
        # late-nineteenth or early-twentieth century America.
        },

    #SCP-3345 - "Crime Novel"
    "SCP-3345":     {
        "name":         "SCP-3345",    # Crime Novel
        "designation":  "SCP-3345",
        "colour":       None, # None given
        "binding":      "paperback",
        "title":        None#, # None given
        # SCP-3345 is a 15cm×20cm 261 paged paperback book in the style of a
        # 21st-century crime novel. Its cover displays a black and white image
        # of a bloody humanoid hand pressing against a frosted window.
        # Furthermore, the text on SCP-3345’s cover reads like an ordinary
        # novel. However, the subsequent text infers that the novel revolves
        # around an individual who reads SCP-3345 by stating – in block white
        # capitals - that the author is “You”.
        },

    #SCP-3348 - "Lost Dictionary"
    "SCP-3348":     {
        "name":         "SCP-3348",    # Lost Dictionary
        "designation":  "SCP-3348",
        "colour":       "black", # None given
        "binding":      None, # None given
        "title":        "The Compiled Vocabulary of the Kaejnethionian Language"
        # SCP-3348 is a black leather-bound journal. Written in a white field on
        # the front cover is the title The Compiled Vocabulary of the
        # Kaejnethionian Language by Mandred Motzer.
        # The first several pages of the journal contain hand-written entries
        # listing words in a previously unknown language, presumably
        # Kaejnithionian, along with their translations. These words are
        # characterized by their extreme length; no entry has been observed to
        # be any less than six (6) syllables long. In addition, Foundation
        # linguists are currently unable to find consistent traits between each
        # instance, as if their structures are completely random.
        # The remaining pages are blank, but an extra piece of loose paper was
        # found in the back of the journal at the time of recovery (See Addendum
        # 3348-02).
        },

    #SCP-3484 - "Missing Pieces"
    "SCP-3484":     {
        "name":         "SCP-3484",    # Missing Pieces
        "designation":  "SCP-3484",
        "colour":       None, # None given
        "binding":      "hardback", #guess, based on being printed in 1862
        "title":        None#, # None given
        # SCP-3484 is an anatomical handbook produced in 1862. It is written in
        # German and was printed in Göttingen. The object shows wear consistent
        # with a book of similar age kept in storage, with a slight
        # discoloration on the cover from non-caustic chemical exposure. Page 87
        # shows handwritten in the margin the English word "REMOVED???" The
        # object describes a process by which a human body can be disassembled
        # and reassembled without use of any tools. After sufficient study time
        # of SCP-3484, subjects are capable of demonstrating the skills
        # described on themselves and others.
        },

    #SCP-3669 - "A Mathematics Self Help Book"
    "SCP-3669":     {
        "name":         "SCP-3669",    # A Mathematics Self Help Book
        "designation":  "SCP-3669",
        "colour":       "deep green",
        "binding":      None, # None given
        "title":        "Modern Mathematics Made Magical" 
        # SCP-3669 is a non-fictional book entitled "Modern Mathematics Made
        # Magical" by Cornelius Fastthought on October 1st, 1963. It is 16.24
        # centimeters wide and 22.86 centimeters long, with 231 pages. The
        # book's front cover is a deep green, with yellow text displaying the
        # title and the name of the author, as well as the date of publishing.
        },

    #SCP-3692 - "the notebook"
    "SCP-3692":     {
        "name":         "SCP-3692",    # the notebook
        "designation":  "SCP-3692",
        "colour":       "black",
        "binding":      "hardback", 
        "title":        None 
        # SCP-3692 is a small black notebook, visually indistinguishable from a
        # Moleskine brand classic hardcover notebook, measuring 1.2 x 21 x
        # 12.5 cm, with 192 pages contained within. There is visible wear on the
        # notebook - the edges of front and back cover are mildly worn, the
        # elastic band meant to keep the book closed missing, and the included
        # bookmark frayed at the end.
        },

    #SCP-3726 - "AnthropomorFic"
    "SCP-3726":     {
        "name":         "SCP-3726",    # AnthropomorFic
        "designation":  "SCP-3726",
        "binding":      None, # none given
        "colour":       "leather",
        "title":        None 
        # SCP-3726 is a 300-page leather-bound codex. Forensic tests have dated
        # SCP-3726 to the 14th century. Despite being buried under sand for an
        # extended period of time, the codex remains relatively intact.
        },

    #SCP-3795 - "Who Killed Your Dog?!"
    "SCP-3795":     {
        "name":         "SCP-3795",    # Who Killed Your Dog?!
        "designation":  "SCP-3795",
        "binding":      "hardback", 
        "colour":       None, # none given
        "title":        "The Genius of Dogs: How Dogs are Smarter Than You Think" 
        # SCP-3795 is a hardcover copy of the book The Genius of Dogs: How Dogs
        # are Smarter Than You Think by Brian Hare and Vanessa Woods (Plume,
        # 2013). In both its inert and active state, SCP-3795 is physically
        # identical to a non-anomalous copy of the book, except that the phrase
        # "WHO KILLED YOUR DOG?!" has been written on the copyright page in
        # black marker.
        },

    #SCP-4147 - "Encyclopedia Obscura"
    "SCP-4147":     {
        "name":         "SCP-4147",    # Encyclopedia Obscura
        "designation":  "SCP-4147",
        "binding":      "hardback", 
        "colour":       "red",
        "title":        "National Mythos Encyclopedia" 
        # SCP-4147 is a series of encyclopedias divided into several volumes
        # each. The number of volumes per instance varies. Each instance was
        # published in 1912 by "Puffin Publishing". Volumes are hard cover, have
        # non-anomalous ink and paper, and have red colored covers with gold
        # text displaying a title. All titles translate to "National Mythos
        # Encyclopedia". Each instance of SCP-4147 covers a different language
        # and includes descriptions of numerous mythical creatures and legends
        # unique to the nation whose official language corresponds to the text
        # of the instance.
        # There are currently 4 instances of SCP-4147 held by the Foundation, no
        # other instances are confirmed to exist:
        # - SCP-4147-1, English. 
        # - SCP-4147-2, Gaelic. 
        # - SCP-4147-3, Russian. 
        # - SCP-4147-4, Japanese. 
        },

    #SCP-4211 - "Memoirmento"
    "SCP-4211":     {
        "name":         "SCP-4211",    # Memoirmento
        "designation":  "SCP-4211",
        "colour":       None, # None given
        "binding":      None, # None given
        "title":        None#, # None given
        # The diary containing SCP-4211 was found in the possession of Augustus
        # Ehrlich Sr., though it is assumed it was purchased from a third
        # party.
        # SCP-4211 is the collective designation for specific diary entries with
        # cognitohazardous properties — these written works contain
        # cognitohazards to prevent reading of the item's true content unless
        # certain conditions are met. More specifically, the items encrypt
        # their content via obfuscation, altering the text if the reader does
        # not have access to the cipher key.
        },

    #SCP-4248 - "Alphabet and Omega"
    "SCP-4248":     {
        "name":         "SCP-4248",    # Alphabet and Omega
        "designation":  "SCP-4248",
        "colour":       None, # None given
        "binding":      "hardback", # None given, assuming hardback for a children's book
        "title":        "The Alphabet of God"
        # SCP-4248 is a Christian-themed children's book titled "The Alphabet 
        # of God" by Terry A. Davis. No other books by this author have been found, and 
        # Davis has been recorded to have committed suicide by train on 2018/08/11. 
        # SCP-4248 was originally self-published by Davis at some point in 2013
        # as a children's book, and reached critical acclaim in several
        # religious circles. Prior to Incident 4248/001, it is estimated that
        # over 1 million copies were sold.
        },

    #SCP-4430 - "The Faceless Live In Evanholly"
    "SCP-4430":     {
        "name":         "SCP-4430",    # The Faceless Live In Evanholly
        "designation":  "SCP-4430",
        "colour":       None, # varies with edition
        "binding":      "paperback", 
        "title":        "The Faceless Live In Evanholly" 
        # SCP-4430 is the designation for copies of the short story "The
        # Faceless Live In Evanholly" by Clyde Hiller. While the cover of the
        # book has been known to vary between editions, the title and author
        # have remained consistent and are used as the sole method of
        # identification. Copies of SCP-4430 generally present as a paperback
        # book targeted at young children containing various illustrations to
        # punctuate the narrative.
                 },

    #SCP-4485 - "Such Black Light"
    "SCP-4485":     {
        "name":         "SCP-4485",    # Such Black Light
        "designation":  "SCP-4485",
        "colour":       "leather",
        "binding":      None, # None given
        "title":        None, # None given
        # SCP-4485 is a small leatherbound book written by German-French artist
        # Jean Arp (Hans Arp, While the artist's given name under French law was
        # Jean, he continued to refer to himself by his German name, Hans, when
        # speaking German). SCP-4485 itself is unremarkable in appearance, being
        # moderately worn and slightly faded. The name of the author, Hans Arp,
        # is pressed into the leather on the back of the journal in block
        # capitalization. Within the front cover of SCP-4485 are the words "gott
        # ist ohne zweck" ("god is without purpose") beneath a crude drawing of
        # a fish.
                 },

    #SCP-4569 - "Plot Twist"
    "SCP-4569":     {
        "name":         "SCP-4569",    # Plot Twist
        "designation":  "SCP-4569",
        "colour":       "leather",
        "binding":      None, # None given
        "title":        None, # None given
        # SCP-4569 is a leather-cover book... Testing has shown the object dates
        # back from the 16th century.
        # SCP-4569 contains a 151-page biography of the individual reading it, up to the 
        # moment he or she came into contact with it, written in a style and tone similar 
        # to classic fairy tales... regardless of the reader's age or number of events
        # from their life, the number of pages remains consistent, SCP-4569
        # choosing to skip or include details in order to shorten or stretch the
        # story.
        # What all the variations of the text share in common is the ending
        # sentence, that being "Now, it's time for [reader's name] to continue
        # their journey…".
                 },

    #SCP-4679 - "The Sweet Taste of Victory"
    "SCP-4679":     {
        "name":         "SCP-4679",    # The Sweet Taste of Victory
        "designation":  "SCP-4679",
        "colour":       None, # None given
        "binding":      "paperback", 
        "title":        "Recipes to Win" 
        # SCP-4679 is the designation for a paperback cookbook titled "Recipes
        # to Win", authored by "Tim & Daryl". The book has no blurb or summary
        # on the back, except for a single phrase which reads "If you wanna eat
        # like a king, you gotta earn it!". When an individual attempts to eat a
        # meal created while following directions from SCP-4679, they will be
        # subjected to an obstacle course. SCP-4679 is 356 pages long, and has
        # 310 recipes within it.
                 },

    #SCP-4716 - "The Plutovore's Cookbook"
    "SCP-4716":     {
        "name":         "SCP-4716",    # The Plutovore's Cookbook
        "designation":  "SCP-4716",
        "colour":       "leather",
        "binding":      "hardback", 
        "title":        "The Plutovore's Cookbook" 
        # SCP-4716 refers to a manuscript containing several thaumaturgical
        # rituals styled after culinary recipes. Entitled The Plutovore's
        # Cookbook, the rituals in SCP-4716 all have the same intent: the
        # creation of an edible effigy which is to be consumed in an act of
        # symbolic cannibalism in order to enact misfortune upon its target.
        },

    #SCP-4828 - "The Big Book Of Achievable Spells, made easy"
    "SCP-4828":     {
        "name":         "SCP-4828",    # The Big Book Of Achievable Spells, made easy
        "designation":  "SCP-4828",
        "colour":       "black",
        "binding":      "hardback", 
        "title":        "The Big Book Of Achievable Spells, made easy" 
        # SCP-4828 refers to a black hardbound book that has an inconsistent
        # number of pages. In golden letters and Garamond font, the book is
        # entitled "The Big Book Of Achievable Spells, made easy".
        },

    #SCP-4854 - "The "Real" Necronomicon and other Godawful Occult Manuscripts"
    "SCP-4854":     {
        "name":         "SCP-4854",    # The "Real" Necronomicon and other Godawful Occult Manuscripts
        "designation":  "SCP-4854",
        "colour":       None,# None given
        "binding":      None,# None given
        "title":        "The Necronomicon" 
        # SCP-4854 refers to several volumes of occult theory and method which
        # claim to be based on works found in the writings of H.P. Lovecraft and
        # other contributors to the Cthulhu mythos.
        },

    #SCP-4740 - "As Davy wondered where they'd been, he read a book named Grass and Green."
    "SCP-4740":     {
        "name":         "SCP-4740",    # As Davy wondered where they'd been, he read a book named Grass and Green.
        "designation":  "SCP-4740",
        "colour":       None,# None given
        "binding":      None,# None given
        "title":        None 
        # SCP-4740 is a 12-page, wood-chip book containing paintings of grassy
        # landscapes, and a blurred child-like figure.
        },

    #SCP-4890 - "Dr. Wondertainment's Guide to History"
    "SCP-4890":     {
        "name":         "SCP-4890",    # Dr. Wondertainment's Guide to History
        "designation":  "SCP-4890",
        "colour":       None,# None given
        "binding":      "hardback",# None given
        "title":        "Dr. Wondertainment's Guide to History"
        # SCP-4890 is a hardcover children's pop-up book titled "Dr.
        # Wondertainment's Guide to History" with a stylized W at the center of
        # the cover. On the back of the cover of the book, there is a small
        # pocket holding SCP-4890-1. SCP-4890-1 is a 0.147 meters tall origami
        # depicting an individual with a purple suit, bow tie, and hat along
        # with a cane. On the torso piece, is a small stylized W.
        },

    #SCP-4893 - "Agapanthus"
    "SCP-4893":     {
        "name":         "SCP-4893",    # Agapanthus
        "designation":  "SCP-4893",
        "colour":       None,# None given
        "binding":      None,# None given
        "title":        None,# None given
        # SCP-4893 is a poetry book written in Dutch that causes synesthesia in
        # the reader where stimulation by written words produces visions of
        # synonymous flowers in the floriography.
        },

    #SCP-4942 - "How to Summon a Lemon"
    "SCP-4942":     {
        "name":         "SCP-4942",    # How to Summon a Lemon
        "designation":  "SCP-4942",
        "colour":       "leather", # None given, but a guess
        "binding":      "hardback", # None given, but a guess
        "title":        "Principles of the Below",
        # SCP-4942-1 is a lengthy thaumaturgic ritual that summons and binds
        # SCP-4942-2 a specific Tier-Aleph tartarean entity to a
        # practitioner. SCP-4942-1 was originally documented in Principles of
        # the Below, an 16th century manuscript on the occult.
        # Between the publishing of Principles of the Below and the present day,
        # the majority of copies were lost. At present, only forty-two are known
        # to exist. Thirty-four are owned by the Foundation; one is owned by
        # Marshall, Carter & Dark; three are owned by The United Church of
        # Satan, Scientist; four are owned by The Holy Order of Knights Templar,
        # Reformed. All external agencies have agreed to not sell a copy or
        # attempt SCP-4942-1.
        # All copies of the Principles of the Below containing SCP-4942-1 have
        # been accounted for. All copies held by the Foundation are being stored
        # in the Site-36 Library Restricted Zone.
        },

    #SCP-5096-1 - "Butterflies work in mysterious ways ??????¯?"
    #SCP-5096-1 - u'"Butterflies work in mysterious ways \u01b8\u0335\u0321\u04dc\u0335\u0328\u0304\u01b7"'
    "SCP-5096-1":     {
        "name":         "SCP-5096-1",    # Butterflies work in mysterious ways
        "designation":  "SCP-5096-1",
        "colour":       None,# None given
        "binding":      "hardback",# None given
        "title":        "Life of Insects: The Study and Story Behind Entomology"
        # SCP-5096 refers to a singular painted lady butterfly (Vanessa cardui
        # Rhopalocera). SCP-5096 can manifest an entomology book titled 'Life of
        # Insects: The Study and Story Behind Entomology' by Jane Woodsburrow
        # (designated SCP-5096-1). SCP-5096 is capable of turning the pages of
        # SCP-5096-1 via the flapping of its wings. When SCP-5096-1 is opened,
        # the environment depicted on the chosen page will manifest. (Ex: A page
        # about the average earthworm will result in the manifestation of soil
        # and grass.)
        },

    #SCP-5102 - "Dear Diary"
    "SCP-5102":     {
        "name":         "SCP-5102",    # Dear Diary
        "designation":  "SCP-5102",
        "colour":       None,# None given
        "binding":      "paperback",
        "title":        None # 'Dear Diary' isn't a title, it's written in crayon
        # SCP-5102 is a small paperback journal with the words 'Dear Diary'
        # inscribed on the front cover in faded crayon.
        },

    #SCP-5166 - "Inspiration"
    "SCP-5166":     {
        "name":         "SCP-5166",    # Inspiration
        "designation":  "SCP-5166",
        "colour":       None,
        "binding":      None,# None given
        "title":        None,# None given
        # SCP-5166 is a small notebook with illegible text written on its
        # surface in pencil.
        # At variable intervals, scraps of paper similar in appearance to
        # SCP-5166 will appear stuck to any object in its immediate vicinity.
        },

    #SCP-5198 - "For Your Own Good"
    "SCP-5198":     {
        "name":         "SCP-5198",    # For Your Own Good
        "designation":  "SCP-5198",
        "colour":       None,# None given
        "binding":      "hardback",
        "title":        "Get Out of Your Damn Shell!"
        # SCP-5198-A is a hardcover self-help book titled "Get Out of Your Damn
        # Shell!". There is no author or publisher credited, and the content
        # appears to be 502 pages of "Lorem Ipsum" placeholder text.
        },

    #SCP-5216 - ""[ACCESS DENIED]""
    "SCP-5216":     {
        "name":         "SCP-5216",    # "[ACCESS DENIED]"
        "designation":  "SCP-5216",
        "colour":       None,
        "binding":      "hardback",
        "title":        "Even More Good Eats",# None given
        # SCP-5216 is a hardcover cookbook, titled "Even More Good Eats". The
        # number of pages, and by extension the number of recipes it contains,
        # is not constant, and fluctuates with regards to its proximity to items
        # typically regarded as edible, or ingredients for non-anomalous food.
        # SCP-5216 does not readily retain its recipes and information, as new
        # instances are generated when closed or outside of direct observation.
        },

    #SCP-5462 - "Misery is the State of Every Soul Burdened by Mortality."
    "SCP-5462":     {
        "name":         "SCP-5462",    # Misery is the State of Every Soul Burdened by Mortality.
        "designation":  "SCP-5462",
        "colour":       "leather",# None given, but a guess
        "binding":      "hardback", # None given, but a guess
        "title":        None,# None given
        # SCP-5462-A is the journal of Spanish painter Francisco Goya, detailing
        # an anomalous event that resulted in the creation of 15 oil paintings
        # painted between 1819 and 1822 commonly referred to as his Black
        # Paintings due to their emotionally disturbing contents, themes, and
        # use of dark colours.
        },

    #SCP-5462 - "Misery is the State of Every Soul Burdened by Mortality."
    "SCP-5462-A":     {
        "name":         "SCP-5462-A",    # Misery is the State of Every Soul Burdened by Mortality.
        "designation":  "SCP-5462-A",
        "colour":       "leather",# None given, but a guess
        "binding":      "hardback", # None given, but a guess
        "title":        None,# None given
        # SCP-5462-A is the journal of Spanish painter Francisco Goya, detailing
        # an anomalous event that resulted in the creation of 15 oil paintings
        # painted between 1819 and 1822 commonly referred to as his Black
        # Paintings due to their emotionally disturbing contents, themes, and
        # use of dark colours.
        },

    #SCP-5490 - "The Lost Emperor"
    "SCP-5490":     {
        "name":         "SCP-5490",    # The Lost Emperor
        "designation":  "SCP-5490",
        "colour":       "leather",
        "binding":      "hardback", # None given, but a guess
        "title":        None,# None given
        # SCP-5490 is a book wrapped in leather binding with 89 pages, all of
        # which are blank. According to radiometric dating, SCP-5490 is
        # approximately 1880 years old. Despite this, it shows no signs of aging
        # or wear.
        },

    #SCP-5628 - "OCD? Have you tried unicycle yoga?"
    "SCP-5628":     {
        "name":         "SCP-5628",    # OCD? Have you tried unicycle yoga?
        "designation":  "SCP-5628",
        "colour":       None,# None given
        "binding":      None, # None given
        "title":        "Mind over Metaphysics"
        # SCP-5628 is a self-help book titled "Mind over Metaphysics" ostensibly
        # written by Dr. Heathcliffe, who was found to have no memory of such.
        },

    #SCP-5905 - "Gashadokuro"
    "SCP-5905":     {
        "name":         "SCP-5905",    # Gashadokuro
        "designation":  "SCP-5905",
        "colour":       "leather",
        "binding":      None, # None given
        "title":        None
        # SCP-5905 is a leather-bound grimoire recovered from the Huang Shui
        # basin in Qinghai, China. This book details the treatment of prisoners,
        # the preparation of objects of sacrifice, and a number of other
        # ritualistic practices of an unclear cultural origin. Prolonged
        # exposure to SCP-5905 causes hyperstimulation of the hypothalamus,
        # resulting in accelerated metabolism and dramatically increased
        # feelings of hunger and thirst.
        }#,

    }


SCP_1161_TITLES = [
    #SCP-1161 is a black paperback book with a varying number of pages. 
    #The title, on both the cover and binding in white lettering changes every 24 
    #hours at precisely 3:00 A.M. GMT, but invariably begin with the words, "How to".
    #The object will always contain instructions on how to perform various actions,
    #ranging from very useful to utterly pointless.
    #A partial list of titles which have appeared since retrieval include: 

    "How to Build a Campfire",
    "How to Eat Spaghetti and Meatballs",
    "How to Hang a Painting",
    "How to Sculpt a Bird in Flight out of Granite",
    "How to Whistle",
    "How to Strangle a Woman",
    "How to Construct a [REDACTED]",
    "How to Open a Desk Drawer",
    "How to Cross-Country Ski",
    "How to [REDACTED]",
    "How To Clean a Necktie",
    "How to Commit Suicide by Hanging",
    "How to Ascend",
    "How to Assimilate Information",
    "How to Ascend",
    "How to Build a Wooden Rocking Chair",
    #Add some new ones here...?
    ]


SCP_1138_TITLES = [
    # SCP-1138 is perceived to be a book of philosophers' and/or writers'
    # correspondence. Though the writing style always corresponds to a given
    # author, the vast majority of letters are forgeries, with a few found
    # to be genuine unsent drafts. The book's author changes based on the
    # scientific and personal interests of the reader and its contents
    # depend on reader's beliefs regarding the author's ideas.

    #Some of the most interesting instances of SCP-1138 are listed here: 
    "Marcus Tullius Cicero's letters", 
    "Niccolò Machiavelli's letters", 
    "Blaise Pascal's letters", 
    "Friedrich Nietzsche's letters", 
    "Fyodor Dostoyevsky's letters", 
    "O5-█'s letters", 
    "Isaac Asimov's letters", 
    "Collected Letters of V.I. Lenin"#,

    #Add some new ones here...?
    ]

SCP_1138_SUBJECTS = [
    # SCP-1138 is perceived to be a book of philosophers' and/or writers'
    # correspondence. Though the writing style always corresponds to a given
    # author, the vast majority of letters are forgeries, with a few found
    # to be genuine unsent drafts. The book's author changes based on the
    # scientific and personal interests of the reader and its contents
    # depend on reader's beliefs regarding the author's ideas.

    #Some of the most interesting instances of SCP-1138 are listed here: 
    "Marcus Tullius Cicero", 
    "Niccolò Machiavelli", 
    "Blaise Pascal", 
    "Friedrich Nietzsche", 
    "Fyodor Dostoyevsky", 
    "O5-█", 
    "Isaac Asimov", 
    "V.I. Lenin"#,
    #Add some new ones here...?
    ]


SCP_701_VERSIONS = [

    #SCP-701 - "The Hanged King's Tragedy"
    # SCP-701, The Hanged King's Tragedy, is a Caroline-era revenge tragedy
    # in five acts. Performances of the play are associated with sudden
    # psychotic and suicidal behavior among both observers and participants,
    # as well as the manifestation of a mysterious figure, classified as
    # SCP-701-1.

    # these are only the BOOK versions of SCP-701 - doesn't include video tapes and floppy discs.
    "the 1640 quarto",                      # two (2) currently extant copies
    "the 1965 trade paperback edition",     # twenty-seven (27) copies
    "the 1971 hardcover printing"#,          # ten (10) copies
    ]




def IsABook(SCP=None, Extended=0):
    """Given an SCP-number, will return True if it is a book-type SCP, False otherwise.
If given the optional argument "Extended=1", will return a tuple.
If the given SCP is a book, will return True and a brief description of the book,
otherwise will return (False, None).
"""

    if Extended=="1":
        Extended=1

    #print "SCP:", SCP
    thisSCP = None
    if type(SCP) == NoneType:
        if Extended==1:
            return (False, None)
        else:
            return False
    if type(SCP) == IntType:
        thisSCP = "SCP-%03d" % SCP
    if type(SCP) == FloatType:
        thisSCP = "SCP-%03d" % int(SCP)
    if type(SCP) == StringType:
        thisSCP = SCP
    try:
        #eg if passed string "2081" for SCP-2081
        thisSCP = "SCP-%03d" % int(SCP)
    except:
        pass    # haven't been passed a number as a string then
        
    if thisSCP == None:
        if Extended==1:
            return (False, None)
        else:
            return False
    thisSCP = thisSCP.upper()

    #print "thisSCP:", thisSCP
    if thisSCP in BOOK_SCPS:
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in BOOK_SCPS_DICT.keys():
                this_desc = ""
                if BOOK_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["colour"])
                    if BOOK_SCPS_DICT[thisSCP]["colour"] == "leather":
                        this_desc = "%s-bound"  % (this_desc)
                if BOOK_SCPS_DICT[thisSCP]["binding"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["binding"])
                    else:
                        this_desc = "%s %s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["binding"])
                if BOOK_SCPS_DICT[thisSCP]["title"] != None:
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        #pass # don't add the word "book"
                        if this_desc == "":
                            this_desc = "booklet called '%s'"  % (BOOK_SCPS_DICT[thisSCP]["title"])
                        else:
                            this_desc = "%s called '%s'" % (this_desc, BOOK_SCPS_DICT[thisSCP]["title"])
                    else:
                        if this_desc == "":
                            this_desc = "book called '%s'"  % (BOOK_SCPS_DICT[thisSCP]["title"])
                        else:
                            this_desc = "%s book called '%s'" % (this_desc, BOOK_SCPS_DICT[thisSCP]["title"])
                if this_desc == "":
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        this_desc = "booklet"
                    else:
                        this_desc = "book"
                elif BOOK_SCPS_DICT[thisSCP]["title"] == None:
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        pass
                        #this_desc = "%s booklet" % (this_desc)
                    else:
                        this_desc = "%s book" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                this_desc = "book"
                desc = "%s %s." % (desc, this_desc)
            return (True, desc)
        else:
            return True

    elif thisSCP in BOOK_SCPS_DICT.keys():
        #failsafe - should be found by above
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in BOOK_SCPS_DICT.keys():
                this_desc = ""
                if BOOK_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["colour"])
                if BOOK_SCPS_DICT[thisSCP]["binding"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["binding"])
                    else:
                        this_desc = "%s %s"  % (this_desc, BOOK_SCPS_DICT[thisSCP]["binding"])
                if BOOK_SCPS_DICT[thisSCP]["title"] != None:
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        #pass # don't add the word "book"
                        if this_desc == "":
                            this_desc = "booklet called '%s'"  % (BOOK_SCPS_DICT[thisSCP]["title"])
                        else:
                            this_desc = "%s called '%s'" % (this_desc, BOOK_SCPS_DICT[thisSCP]["title"])
                    else:
                        if this_desc == "":
                            this_desc = "book called '%s'"  % (BOOK_SCPS_DICT[thisSCP]["title"])
                        else:
                            this_desc = "%s book called '%s'" % (this_desc, BOOK_SCPS_DICT[thisSCP]["title"])
                if this_desc == "":
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        this_desc = "booklet"
                    else:
                        this_desc = "book"
                elif BOOK_SCPS_DICT[thisSCP]["title"] == None:
                    if BOOK_SCPS_DICT[thisSCP]["binding"] == "booklet":
                        pass
                        #this_desc = "%s booklet" % (this_desc)
                    else:
                        this_desc = "%s book" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                this_desc = "book"
                desc = "%s %s." % (desc, this_desc)
            return (True, desc)
        else:
            return True


    else:
        if Extended==1:
            return (False, None)
        else:
            return False

    # add some machanism for dealing with multi-part SCPS?
    # eg SCP-1397 (A Failed Work of Art) has SCP-1397-1 through -5
    # eg SCP-733 (A Pair of Scissors) has SCP-733-01 (the scissors) and SCP-733-02 (the book)


def CanRead(SCP):
    "If SCP is a book-type SCP, returns True. Else returns False."

    #print "SCP:", SCP
    thisSCP = None
    if type(SCP) == NoneType:
        if Extended==1:
            return (False, None)
        else:
            return False
    if type(SCP) == IntType:
        thisSCP = "SCP-%03d" % SCP
    if type(SCP) == FloatType:
        thisSCP = "SCP-%03d" % int(SCP)
    if type(SCP) == StringType:
        thisSCP = SCP
    try:
        #eg if passed string "2081" for SCP-2081
        thisSCP = "SCP-%03d" % int(SCP)
    except:
        pass    # haven't been passed a number as a string then

    if thisSCP in BOOK_SCPS:
        return True
    else:
        return False



def getSCPFromTitle(title=None, Extended=0):
    """
Tries to look up a book's SCP designantion from its title.
If found, returns a string of the SCP number. Otherwise returns None.
If given the optional argument "Extended=1", will return a tuple.
If the given SCP is a book, will return the SCP-number (as a string) and a brief description of the book,
otherwise will return (None, None).
"""

    if Extended=="1":
        Extended=1

    if title in ("", None):
        if Extended==1:
            return (None, None)
        else:
            return None
    else:
        if type(title) != StringType:
            if Extended==1:
                return (None, None)
            else:
                return None
        poss_SCPs = []
        this_SCP = None
        this_SCP_title = None
        for book in BOOK_SCPS_DICT.keys():
            #print "book:", book
            if BOOK_SCPS_DICT[book]["title"] != None:
                if string.lower(BOOK_SCPS_DICT[book]["title"]) == string.lower(title):
                    this_SCP = BOOK_SCPS_DICT[book]["designation"]
                    this_SCP_title = BOOK_SCPS_DICT[book]["title"]
                    poss_SCPs.append(this_SCP)
        if poss_SCPs == []:
            if string.split(string.lower(title))[0] in ("a", "an", "the"):
                new_title = string.join(string.split(string.lower(title))[1:])
                for book in BOOK_SCPS_DICT.keys():
                    if BOOK_SCPS_DICT[book]["title"] != None:
                        if string.lower(BOOK_SCPS_DICT[book]["title"]) == string.lower(new_title):
                            this_SCP = BOOK_SCPS_DICT[book]["designation"]
                            this_SCP_title = BOOK_SCPS_DICT[book]["title"]
                            poss_SCPs.append(this_SCP)

        if poss_SCPs == []:
            n = ("a", "an", "the")
            for n1 in range (0, len(n)):
                new = n[n1]
                new_title = "%s %s" % (new, string.lower(title))
                #print "new_title:", new_title
                for book in BOOK_SCPS_DICT.keys():
                    if BOOK_SCPS_DICT[book]["title"] != None:
                        if string.lower(BOOK_SCPS_DICT[book]["title"]) == string.lower(new_title):
                            this_SCP = BOOK_SCPS_DICT[book]["designation"]
                            this_SCP_title = BOOK_SCPS_DICT[book]["title"]
                            poss_SCPs.append(this_SCP)

##        #for debugging:    
##        print "title:", title
##        print "poss_SCPs:", poss_SCPs
##        print "this_SCP:", this_SCP
##        print "this_SCP_title:", this_SCP_title

        if poss_SCPs == []:
            if Extended==1:
                return (None, None)
            else:
                return None
        elif len(poss_SCPs) == 1:
            if Extended==1:
                return (this_SCP, "'%s' is %s" % (this_SCP_title, this_SCP))
            else:
                return this_SCP
        elif len(poss_SCPs)>1:
            if Extended==1:
                poss_SCPs_phrase = ""
                for x in poss_SCPs:
                    poss_SCPs_phrase = "%s%s" % (poss_SCPs_phrase, x)
                    if x == poss_SCPs[-1]:
                        poss_SCPs_phrase = "%s." % (poss_SCPs_phrase)
                    else:
                        poss_SCPs_phrase = "%s, " % (poss_SCPs_phrase)
                return (poss_SCPs, "'%s' may refer to the following SCPS: %s" % (this_SCP_title, poss_SCPs_phrase))
            else:
                return poss_SCPs
                            
        else:
            if Extended==1:
                return (None, None)
            else:
                return False


def demo():
    book = random.choice(BOOK_SCPS)
    desc = IsABook(book,1)[1]
    print desc

if __name__ == "__main__":
    print "books.py\n(Version: %s)" % VERSION
    print "%s book-type SCPs known about.\n" % len(BOOK_SCPS)
    print "random book:"
    demo()
    print
    