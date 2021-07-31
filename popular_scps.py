#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""
popular_scps.py: All our information on how popular various SCPs are.

"Popularity" is based on rankings on the SCP Foundation's "Highest
Rated SCPs" page (http://www.scpwiki.com/highest-rated-scps/) scraped
on 18 September 2020.

Module contains the following:

"ALWAYS_USE": A short list of SCPs which should appear in every game
  (since they give an "SCP" flavour to our game). Initially: SCP-173
  ("The Sculpture"), SCP-049 ("Plague Doctor"), SCP-096 (""The "Shy
  Guy""), SCP-106 ("The Old Man") and SCP-5028 ("Empria's Exile"))

"POPULAR_SCPS_DICT": A dict of the top 958 most popular SCPs.
  (ie pages 1 to 10 of the "highest-rated-scps" on scpwiki.com).
  It is names only, with each key being a number in the range 1-958,
  and the corresponding entry being the SCP designation.
  Eg, the first entry is:
      1    :     "SCP-173",

"POPULAR_SCPS_DICT_FULL": Similar to POPULAR_SCPS_DICT, but with more
  information... keys are the popularity ranking, as in
  POPULAR_SCPS_DICT (ie numbers 1-958), contents is another dict with
  the keys "name", "document_name", "popularity", and "to_use".
  ("to_use" is either 1 or 0, and based on the "containment" attribute
  for the corresponding entry in the main objects.py listing. If it's
  uncontained, in another galaxy or an abstract concept, to_use will be 0).
  Eg, the first entry is:
      1    :     {
      "name"                :   "SCP-173",
      "document_name"       :   "The Sculpture - The Original",
      "popularity"          :   1,
      "to_use"              :   1,
      },

"BY_SCPS": Use this if you want to get a 'ranking' for a particular
  SCP from its designation. It's a dict, with each key being a string
  of the SCP designation and the entry being an integer of its
  position in the popularity rankings.
  Eg, the first entry is:
    "SCP-001" : 642,

We don't include any "joke" (-J) SCPs, no matter how popular they are.
Any -J SCPs that appear in the popularity listings will have attributes
of None and a comment stating it has been "[OMITTED]".
  Eg, 
  # 002  : SCP-____-J [OMITTED]
        2    :     None,
"""

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.


__VERSION__ = "0.2.1b"
VERSION = __VERSION__


#ALWAYS have these in a game - they give an SCP flavour to our game. 

ALWAYS_USE = [
    # 001  : (SCP-173, "The Sculpture - The Original")
    "SCP-173",
    # 003  : (SCP-049, "Plague Doctor")
    "SCP-049",
    # 007  : (SCP-096, "The "Shy Guy"")
    "SCP-096",
    # 009  : (SCP-106, "The Old Man")
    "SCP-106",
    #SCP-5028 - "Empria's Exile"
    #Doesn't appear in our standard POPULAR_SCPS_DICT, but just too damn cool not to use!
    "SCP-5028"#,
    ]


# The following were retrieved from the SCP Foundation's "Highest Rated SCPs" page 
# http://www.scpwiki.com/highest-rated-scps/
# on 18 September 2020.

# NAMES ONLY...

POPULAR_SCPS_DICT = {

    # from: http://www.scpwiki.com/highest-rated-scps


    # 001  : SCP-173
    #      : (SCP-173, "The Sculpture - The Original")
      1    :     "SCP-173",


    # 002  : SCP-____-J [OMITTED]
      2    :     None,


    # 003  : SCP-049
    #      : (SCP-049, "Plague Doctor")
      3    :     "SCP-049",


    # 004  : SCP-055
    #      : (SCP-055, "[unknown]")
      4    :     "SCP-055",


    # 005  : SCP-087
    #      : (SCP-087, "The Stairwell")
      5    :     "SCP-087",


    # 006  : SCP-682
    #      : (SCP-682, "Hard-to-Destroy Reptile")
      6    :     "SCP-682",


    # 007  : SCP-096
    #      : (SCP-096, "The "Shy Guy"")
      7    :     "SCP-096",


    # 008  : SCP-093
    #      : (SCP-093, "Red Sea Object")
      8    :     "SCP-093",


    # 009  : SCP-106
    #      : (SCP-106, "The Old Man")
      9    :     "SCP-106",


    # 010  : SCP-914
    #      : (SCP-914, "The Clockworks")
     10    :     "SCP-914",


    # 011  : SCP-3008
    #      : (SCP-3008, "A Perfectly Normal, Regular Old IKEA")
     11    :     "SCP-3008",


    # 012  : SCP-426
    #      : (SCP-426, "I am a Toaster")
     12    :     "SCP-426",


    # 013  : SCP-999
    #      : (SCP-999, "The Tickle Monster")
     13    :     "SCP-999",


    # 014  : SCP-231
    #      : (SCP-231, "Special Personnel Requirements")
     14    :     "SCP-231",


    # 015  : SCP-2317
    #      : (SCP-2317, "A Door to Another World")
     15    :     "SCP-2317",


    # 016  : SCP-1981
    #      : (SCP-1981, ""RONALD REAGAN CUT UP WHILE TALKING"")
     16    :     "SCP-1981",


    # 017  : SCP-1730
    #      : (SCP-1730, "What Happened to Site-13?")
     17    :     "SCP-1730",


    # 018  : SCP-3999
    #      : (SCP-3999, "I Am At The Center of Everything That Happens To Me")
     18    :     "SCP-3999",


    # 019  : SCP-5000
    #      : (SCP-5000, "Why?")
     19    :     "SCP-5000",


    # 020  : SCP-3000
    #      : (SCP-3000, "Ananteshesha")
     20    :     "SCP-3000",


    # 021  : SCP-3001
    #      : (SCP-3001, "Red Reality")
     21    :     "SCP-3001",


    # 022  : SCP-2000
    #      : (SCP-2000, "Deus Ex Machina")
     22    :     "SCP-2000",


    # 023  : SCP-4999
    #      : (SCP-4999, "Someone to Watch Over Us")
     23    :     "SCP-4999",


    # 024  : SCP-294
    #      : (SCP-294, "The Coffee Machine")
     24    :     "SCP-294",


    # 025  : SCP-895
    #      : (SCP-895, "Camera Disruption")
     25    :     "SCP-895",


    # 026  : SCP-1171
    #      : (SCP-1171, "Humans Go Home")
     26    :     "SCP-1171",


    # 027  : SCP-1000
    #      : (SCP-1000, "Bigfoot")
     27    :     "SCP-1000",


    # 028  : SCP-2935
    #      : (SCP-2935, "O, Death")
     28    :     "SCP-2935",


    # 029  : SCP-902
    #      : (SCP-902, "The Final Countdown")
     29    :     "SCP-902",


    # 030  : SCP-4205 [OMITTED]
     30    :     None,


    # 031  : SCP-035
    #      : (SCP-035, "Possessive Mask")
     31    :     "SCP-035",


    # 032  : SCP-002
    #      : (SCP-002, "The "Living" Room")
     32    :     "SCP-002",


    # 033  : SCP-1733
    #      : (SCP-1733, "Season Opener")
     33    :     "SCP-1733",


    # 034  : SCP-2006
    #      : (SCP-2006, "Too Spooky")
     34    :     "SCP-2006",


    # 035  : SCP-701
    #      : (SCP-701, "The Hanged King's Tragedy")
     35    :     "SCP-701",


    # 036  : SCP-006-J [OMITTED]
     36    :     None,


    # 037  : SCP-610
    #      : (SCP-610, "The Flesh that Hates")
     37    :     "SCP-610",


    # 038  : SCP-076
    #      : (SCP-076, ""Able"")
     38    :     "SCP-076",


    # 039  : SCP-085
    #      : (SCP-085, "Hand-drawn ''Cassy''")
     39    :     "SCP-085",


    # 040  : SCP-1048
    #      : (SCP-1048, "Builder Bear")
     40    :     "SCP-1048",


    # 041  : SCP-140
    #      : (SCP-140, "An Incomplete Chronicle")
     41    :     "SCP-140",


    # 042  : SCP-507
    #      : (SCP-507, "Reluctant Dimension Hopper")
     42    :     "SCP-507",


    # 043  : SCP-354
    #      : (SCP-354, "The Red Pool")
     43    :     "SCP-354",


    # 044  : SCP-990
    #      : (SCP-990, "Dream Man")
     44    :     "SCP-990",


    # 045  : SCP-993
    #      : (SCP-993, "Bobble the Clown")
     45    :     "SCP-993",


    # 046  : SCP-1230
    #      : (SCP-1230, "A Hero is Born")
     46    :     "SCP-1230",


    # 047  : SCP-2316
    #      : (SCP-2316, "Field Trip")
     47    :     "SCP-2316",


    # 048  : SCP-2030
    #      : (SCP-2030, "LA U GH IS F UN")
     48    :     "SCP-2030",


    # 049  : SCP-1471
    #      : (SCP-1471, "MalO ver1.0.0")
     49    :     "SCP-1471",


    # 050  : SCP-1370
    #      : (SCP-1370, "Pesterbot")
     50    :     "SCP-1370",


    # 051  : SCP-348
    #      : (SCP-348, "A Gift from Dad")
     51    :     "SCP-348",


    # 052  : SCP-963
    #      : (SCP-963, "Immortality")
     52    :     "SCP-963",


    # 053  : SCP-2662
    #      : (SCP-2662, "cthulhu f'UCK OFF!")
     53    :     "SCP-2662",


    # 054  : SCP-079
    #      : (SCP-079, "Old AI")
     54    :     "SCP-079",


    # 055  : SCP-1762
    #      : (SCP-1762, "Where The Dragons Went")
     55    :     "SCP-1762",


    # 056  : SCP-666-J [OMITTED]
     56    :     None,


    # 057  : SCP-1983
    #      : (SCP-1983, "Doorway to Nowhere")
     57    :     "SCP-1983",


    # 058  : SCP-048
    #      : (SCP-048, "The Cursed SCP Number")
     58    :     "SCP-048",


    # 059  : SCP-2998
    #      : (SCP-2998, "Anomalous Transmission, 2485 MHz")
     59    :     "SCP-2998",


    # 060  : SCP-1440
    #      : (SCP-1440, "The Old Man from Nowhere")
     60    :     "SCP-1440",


    # 061  : SCP-1437
    #      : (SCP-1437, "A Hole to Another Place")
     61    :     "SCP-1437",


    # 062  : SCP-1425
    #      : (SCP-1425, "Star Signals")
     62    :     "SCP-1425",


    # 063  : SCP-1893
    #      : (SCP-1893, "The Minotaur's Tale")
     63    :     "SCP-1893",


    # 064  : SCP-2718
    #      : (SCP-2718, "What Happens After")
     64    :     "SCP-2718",


    # 065  : SCP-504
    #      : (SCP-504, "Critical Tomatoes")
     65    :     "SCP-504",


    # 066  : SCP-3930
    #      : (SCP-3930, "The Pattern Screamer")
     66    :     "SCP-3930",


    # 067  : SCP-184
    #      : (SCP-184, "The Architect")
     67    :     "SCP-184",


    # 068  : SCP-028
    #      : (SCP-028, "Knowledge")
     68    :     "SCP-028",


    # 069  : SCP-1867
    #      : (SCP-1867, "A Gentleman")
     69    :     "SCP-1867",


    # 070  : SCP-073
    #      : (SCP-073, ""Cain"")
     70    :     "SCP-073",


    # 071  : SCP-871
    #      : (SCP-871, "Self-Replacing Cake")
     71    :     "SCP-871",


    # 072  : SCP-004
    #      : (SCP-004, "The 12 Rusty Keys and the Door")
     72    :     "SCP-004",


    # 073  : SCP-5999
    #      : (SCP-5999, "This is Where I Died")
     73    :     "SCP-5999",


    # 074  : SCP-1322
    #      : (SCP-1322, "Glory Hole")
     74    :     "SCP-1322",


    # 075  : SCP-343
    #      : (SCP-343, ""God"")
     75    :     "SCP-343",


    # 076  : SCP-2439
    #      : (SCP-2439, "[SLOT UNALLOCATED]")
     76    :     "SCP-2439",


    # 077  : SCP-420-J [OMITTED]
     77    :     None,


    # 078  : SCP-even [OMITTED]
     78    :     None,


    # 079  : SCP-500
    #      : (SCP-500, "Panacea")
     79    :     "SCP-500",


    # 080  : SCP-1609
    #      : (SCP-1609, "The Remains of a Chair")
     80    :     "SCP-1609",


    # 081  : SCP-8900-EX [OMITTED]
     81    :     None,


    # 082  : SCP-529
    #      : (SCP-529, "Josie the Half-Cat")
     82    :     "SCP-529",


    # 083  : SCP-666Â½-J [OMITTED]
     83    :     None,


    # 084  : SCP-1342
    #      : (SCP-1342, "To the Makers of Music")
     84    :     "SCP-1342",


    # 085  : SCP-882
    #      : (SCP-882, "A Machine")
     85    :     "SCP-882",


    # 086  : SCP-1678
    #      : (SCP-1678, "UnLondon")
     86    :     "SCP-1678",


    # 087  : SCP-TTKU-J [OMITTED]
     87    :     None,


    # 088  : SCP-4666
    #      : (SCP-4666, "The Yule Man")
     88    :     "SCP-4666",


    # 089  : SCP-586
    #      : (SCP-586, "Inscribable Object")
     89    :     "SCP-586",


    # 090  : SCP-015
    #      : (SCP-015, "Pipe Nightmare")
     90    :     "SCP-015",


    # 091  : SCP-3002
    #      : (SCP-3002, "Attempts to Assassinate Thought")
     91    :     "SCP-3002",


    # 092  : SCP-3333
    #      : (SCP-3333, "Tower")
     92    :     "SCP-3333",


    # 093  : SCP-049-J [OMITTED]
     93    :     None,


    # 094  : SCP-5031
    #      : (SCP-5031, "Yet Another Murder Monster")
     94    :     "SCP-5031",



    # from: http://www.scpwiki.com/highest-rated-scps/p/2


    # 095  : SCP-2602, [OMITTED]
     95    :     None,


    # 096  : SCP-3125
    #      : (SCP-3125, "The Escapee")
     96    :     "SCP-3125",


    # 097  : SCP-261
    #      : (SCP-261, "Pan-Dimensional Vending")
     97    :     "SCP-261",


    # 098  : SCP-662
    #      : (SCP-662, "Butler's Hand Bell")
     98    :     "SCP-662",


    # 099  : SCP-186
    #      : (SCP-186, "To End All Wars")
     99    :     "SCP-186",


    # 100  : SCP-1504
    #      : (SCP-1504, "Joe Schmo")
     100    :     "SCP-1504",


    # 101  : SCP-3393
    #      : (SCP-3393, "For Your Eyes Only")
     101    :     "SCP-3393",


    # 102  : SCP-789-J [OMITTED]
     102    :     None,


    # 103  : SCP-682-J [OMITTED]
     103    :     None,


    # 104  : SCP-131
    #      : (SCP-131, "The "Eye Pods"")
     104    :     "SCP-131",


    # 105  : SCP-169
    #      : (SCP-169, "The Leviathan")
     105    :     "SCP-169",


    # 106  : SCP-4001
    #      : (SCP-4001, "Alexandria Eternal")
     106    :     "SCP-4001",


    # 107  : SCP-179
    #      : (SCP-179, "Sauelsuesor")
     107    :     "SCP-179",


    # 108  : SCP-2295
    #      : (SCP-2295, "The Bear with a Heart of Patchwork")
     108    :     "SCP-2295",


    # 109  : SCP-835
    #      : (SCP-835, "Expunged Data Released")
     109    :     "SCP-835",


    # 110  : SCP-4444
    #      : (SCP-4444, "Bush v. Gore")
     110    :     "SCP-4444",


    # 111  : SCP-008
    #      : (SCP-008, "Zombie Plague")
     111    :     "SCP-008",


    # 112  : SCP-001-EX-J [OMITTED]
     112    :     None,


    # 113  : SCP-1193
    #      : (SCP-1193, "Buried Giant")
     113    :     "SCP-1193",


    # 114  : SCP-2399
    #      : (SCP-2399, "A Malfunctioning Destroyer")
     114    :     "SCP-2399",


    # 115  : SCP-939
    #      : (SCP-939, "With Many Voices")
     115    :     "SCP-939",


    # 116  : SCP-1875
    #      : (SCP-1875, "Antique Chess Computer")
     116    :     "SCP-1875",


    # 117  : SCP-513
    #      : (SCP-513, "A Cowbell")
     117    :     "SCP-513",


    # 118  : SCP-4991
    #      : (SCP-4991, ">So this is how the world ends. Not with a bang, but with a shitpost.")
     118    :     "SCP-4991",


    # 119  : SCP-1470
    #      : (SCP-1470, "Telepathic Spider")
     119    :     "SCP-1470",


    # 120  : SCP-3003
    #      : (SCP-3003, "The End of History")
     120    :     "SCP-3003",


    # 121  : SCP-017
    #      : (SCP-017, "Shadow Person")
     121    :     "SCP-017",


    # 122  : SCP-5308-J [OMITTED]
     122    :     None,


    # 123  : SCP-342
    #      : (SCP-342, "A Ticket to Ride")
     123    :     "SCP-342",


    # 124  : SCP-3199
    #      : (SCP-3199, "Humans, Refuted")
     124    :     "SCP-3199",


    # 125  : SCP-1545
    #      : (SCP-1545, "Larry the Loving Llama")
     125    :     "SCP-1545",


    # 126  : SCP-066
    #      : (SCP-066, "Eric's Toy")
     126    :     "SCP-066",


    # 127  : SCP-1689
    #      : (SCP-1689, "Bag of Holding Potatoes")
     127    :     "SCP-1689",


    # 128  : SCP-053
    #      : (SCP-053, "Young Girl")
     128    :     "SCP-053",


    # 129  : SCP-1173
    #      : (SCP-1173, "The Islamic Republic of Eastern Samothrace")
     129    :     "SCP-1173",


    # 130  : SCP-447
    #      : (SCP-447, "Ball of Green Slime")
     130    :     "SCP-447",


    # 131  : SCP-105
    #      : (SCP-105, ""Iris"")
     131    :     "SCP-105",


    # 132  : SCP-3939
    #      : (SCP-3939, "[NUMBER RESERVED; AWAITING RESEARCHER]")
     132    :     "SCP-3939",


    # 133  : SCP-3007
    #      : (SCP-3007, "World of Two Artists")
     133    :     "SCP-3007",


    # 134  : SCP-423
    #      : (SCP-423, "Self-Inserting Character")
     134    :     "SCP-423",


    # 135  : SCP-1234-J [OMITTED]
     135    :     None,


    # 136  : SCP-738
    #      : (SCP-738, "The Devil's Deal")
     136    :     "SCP-738",


    # 137  : SCP-1295
    #      : (SCP-1295, "Meg's Diner")
     137    :     "SCP-1295",


    # 138  : SCP-1057
    #      : (SCP-1057, "Absence of Shark")
     138    :     "SCP-1057",


    # 139  : SCP-058
    #      : (SCP-058, "Heart of Darkness")
     139    :     "SCP-058",


    # 140  : SCP-303
    #      : (SCP-303, "The Doorman")
     140    :     "SCP-303",


    # 141  : SCP-1025
    #      : (SCP-1025, "Encyclopedia of Diseases")
     141    :     "SCP-1025",


    # 142  : SCP-387
    #      : (SCP-387, "Living Lego")
     142    :     "SCP-387",


    # 143  : SCP-009
    #      : (SCP-009, "Red Ice")
     143    :     "SCP-009",


    # 144  : SCP-217
    #      : (SCP-217, "The Clockwork Virus")
     144    :     "SCP-217",


    # 145  : SCP-1004
    #      : (SCP-1004, "Factory Porn")
     145    :     "SCP-1004",


    # 146  : SCP-1958
    #      : (SCP-1958, "Magic Bus")
     146    :     "SCP-1958",


    # 147  : SCP-001-J [OMITTED]
     147    :     None,


    # 148  : SCP-2557
    #      : (SCP-2557, "A Holding of Envelope Logistics®")
     148    :     "SCP-2557",


    # 149  : SCP-024
    #      : (SCP-024, "Game Show of Death")
     149    :     "SCP-024",


    # 150  : SCP-1959
    #      : (SCP-1959, "The Lost Cosmonaut")
     150    :     "SCP-1959",


    # 151  : SCP-173-J [OMITTED]
     151    :     None,


    # 152  : SCP-014
    #      : (SCP-014, "The Concrete Man")
     152    :     "SCP-014",


    # 153  : SCP-966
    #      : (SCP-966, "Sleep Killer")
     153    :     "SCP-966",


    # 154  : SCP-012
    #      : (SCP-012, "A Bad Composition")
     154    :     "SCP-012",


    # 155  : SCP-3213
    #      : (SCP-3213, "F*ck off Carl.")
     155    :     "SCP-3213",


    # 156  : SCP-\Ì\Ì\Ì\Ì-J [OMITTED]
     156    :     None,


    # 157  : SCP-804
    #      : (SCP-804, "World Without Man")
     157    :     "SCP-804",


    # 158  : SCP-3301
    #      : (SCP-3301, "THE FOUNDATION")
     158    :     "SCP-3301",


    # 159  : SCP-089
    #      : (SCP-089, "Tophet")
     159    :     "SCP-089",


    # 160  : SCP-2950
    #      : (SCP-2950, "Just A Chair")
     160    :     "SCP-2950",


    # 161  : SCP-033
    #      : (SCP-033, "The Missing Number")
     161    :     "SCP-033",


    # 162  : SCP-2003
    #      : (SCP-2003, "Preferred Option")
     162    :     "SCP-2003",


    # 163  : SCP-1994-J [OMITTED]
     163    :     None,


    # 164  : SCP-2875
    #      : (SCP-2875, "The Town That Got Fucked By Bears")
     164    :     "SCP-2875",


    # 165  : SCP-3519
    #      : (SCP-3519, "These Quiet Days")
     165    :     "SCP-3519",


    # 166  : SCP-3671
    #      : (SCP-3671, "A very angry box of cereal")
     166    :     "SCP-3671",


    # 167  : SCP-003
    #      : (SCP-003, "Biological Motherboard")
     167    :     "SCP-003",


    # 168  : SCP-439
    #      : (SCP-439, "Bone Hive")
     168    :     "SCP-439",


    # 169  : SCP-2747
    #      : (SCP-2747, "As below, so above")
     169    :     "SCP-2747",


    # 170  : SCP-329-J [OMITTED]
     170    :     None,


    # 171  : SCP-2599
    #      : (SCP-2599, "Not Good Enough")
     171    :     "SCP-2599",


    # 172  : SCP-3740
    #      : (SCP-3740, "God Is Dumb")
     172    :     "SCP-3740",


    # 173  : SCP-111
    #      : (SCP-111, "Dragon-Snails™")
     173    :     "SCP-111",


    # 174  : SCP-1055
    #      : (SCP-1055, "Bugsy")
     174    :     "SCP-1055",


    # 175  : SCP-2137
    #      : (SCP-2137, "The Forensic Ghost Of Tupac Shakur")
     175    :     "SCP-2137",


    # 176  : SCP-176
    #      : (SCP-176, "Observable Time Loop")
     176    :     "SCP-176",


    # 177  : SCP-2682
    #      : (SCP-2682, "The Blind Idiot")
     177    :     "SCP-2682",


    # 178  : SCP-191
    #      : (SCP-191, "Cyborg Child")
     178    :     "SCP-191",


    # 179  : SCP-2264
    #      : (SCP-2264, "In the Court of Alagadda")
     179    :     "SCP-2264",


    # 180  : SCP-SAFE-J [OMITTED]
     180    :     None,


    # 181  : SCP-016
    #      : (SCP-016, "Sentient Micro-Organism")
     181    :     "SCP-016",


    # 182  : SCP-239
    #      : (SCP-239, "The Witch Child")
     182    :     "SCP-239",


    # 183  : SCP-168
    #      : (SCP-168, "Sentient Calculator")
     183    :     "SCP-168",


    # 184  : SCP-962
    #      : (SCP-962, "Tower of Babble")
     184    :     "SCP-962",


    # 185  : SCP-4357-J [OMITTED]
     185    :     None,


    # 186  : SCP-022
    #      : (SCP-022, "The Morgue")
     186    :     "SCP-022",


    # 187  : SCP-3034
    #      : (SCP-3034, "The Counting Station")
     187    :     "SCP-3034",


    # 188  : SCP-2357
    #      : (SCP-2357, "The Perfect SCP")
     188    :     "SCP-2357",



    # from: http://www.scpwiki.com/highest-rated-scps/p/3


    # 189  : SCP-1050
    #      : (SCP-1050, "Obsidian Obelisk of Warning")
     189    :     "SCP-1050",


    # 190  : SCP-1499
    #      : (SCP-1499, "The Gas Mask")
     190    :     "SCP-1499",


    # 191  : SCP-2852
    #      : (SCP-2852, "Cousin Johnny")
     191    :     "SCP-2852",


    # 192  : SCP-2740
    #      : (SCP-2740, "It Wasn't There")
     192    :     "SCP-2740",


    # 193  : SCP-1459
    #      : (SCP-1459, "The Puppy Machine")
     193    :     "SCP-1459",


    # 194  : SCP-2719
    #      : (SCP-2719, "Inside")
     194    :     "SCP-2719",


    # 195  : SCP-2256
    #      : (SCP-2256, "Very Tall Things")
     195    :     "SCP-2256",


    # 196  : SCP-1006
    #      : (SCP-1006, "Spider Proletariat")
     196    :     "SCP-1006",


    # 197  : SCP-2337
    #      : (SCP-2337, ""Dr. Spanko"")
     197    :     "SCP-2337",


    # 198  : SCP-2669
    #      : (SCP-2669, "Khevtuul 1")
     198    :     "SCP-2669",


    # 199  : SCP-009-J [OMITTED]
     199    :     None,


    # 200  : SCP-823
    #      : (SCP-823, "Carnival of Horrors")
     200    :     "SCP-823",


    # 201  : SCP-811
    #      : (SCP-811, "Swamp Woman")
     201    :     "SCP-811",


    # 202  : SCP-163
    #      : (SCP-163, "An Old Castaway")
     202    :     "SCP-163",


    # 203  : SCP-1861
    #      : (SCP-1861, "The Crew of the HMS Wintersheimer")
     203    :     "SCP-1861",


    # 204  : SCP-884
    #      : (SCP-884, "A Shaving Mirror")
     204    :     "SCP-884",


    # 205  : SCP-082
    #      : (SCP-082, ""Fernand" the Cannibal")
     205    :     "SCP-082",


    # 206  : SCP-946
    #      : (SCP-946, "A Formal Discussion")
     206    :     "SCP-946",


    # 207  : SCP-455
    #      : (SCP-455, "Cargo Ship")
     207    :     "SCP-455",


    # 208  : SCP-2952
    #      : (SCP-2952, "Conveyance Of Regional Gwerin Internationally")
     208    :     "SCP-2952",


    # 209  : SCP-3211
    #      : (SCP-3211, "There is No Canon")
     209    :     "SCP-3211",


    # 210  : SCP-2111
    #      : (SCP-2111, "If You Can Read This…")
     210    :     "SCP-2111",


    # 211  : SCP-890
    #      : (SCP-890, "The Rocket Surgeon")
     211    :     "SCP-890",


    # 212  : SCP-086
    #      : (SCP-086, "The Office of Dr. [REDACTED]")
     212    :     "SCP-086",


    # 213  : SCP-3309
    #      : (SCP-3309, "Where We Go When We Fade, Fade Away")
     213    :     "SCP-3309",


    # 214  : SCP-011
    #      : (SCP-011, "Sentient Civil War Memorial Statue")
     214    :     "SCP-011",


    # 215  : SCP-1111
    #      : (SCP-1111, "The White Dog")
     215    :     "SCP-1111",


    # 216  : SCP-1543-J [OMITTED]
     216    :     None,


    # 217  : SCP-321
    #      : (SCP-321, "Child of Man")
     217    :     "SCP-321",


    # 218  : SCP-1422
    #      : (SCP-1422, "The Yellowstone Anomaly")
     218    :     "SCP-1422",


    # 219  : SCP-1968
    #      : (SCP-1968, "Global Retrocausality Torus")
     219    :     "SCP-1968",


    # 220  : SCP-2639
    #      : (SCP-2639, "Video Game Violence")
     220    :     "SCP-2639",


    # 221  : SCP-245
    #      : (SCP-245, "SCP-RPG")
     221    :     "SCP-245",


    # 222  : SCP-3521
    #      : (SCP-3521, "Forced Banana Equivalent Dose by dado")
     222    :     "SCP-3521",


    # 223  : SCP-970
    #      : (SCP-970, "The Recursive Room")
     223    :     "SCP-970",


    # 224  : SCP-527
    #      : (SCP-527, "Mr. Fish")
     224    :     "SCP-527",


    # 225  : SCP-1936
    #      : (SCP-1936, "Daleport")
     225    :     "SCP-1936",


    # 226  : SCP-1522
    #      : (SCP-1522, "Ships That Pass In The Night")
     226    :     "SCP-1522",


    # 227  : SCP-MYSTERY-J [OMITTED]
     227    :     None,


    # 228  : SCP-524
    #      : (SCP-524, "Walter the Omnivorous Rabbit")
     228    :     "SCP-524",


    # 229  : SCP-1986
    #      : (SCP-1986, "Imaginary Library")
     229    :     "SCP-1986",


    # 230  : SCP-1192
    #      : (SCP-1192, ""Timmy"")
     230    :     "SCP-1192",


    # 231  : SCP-999-J [OMITTED]
     231    :     None,


    # 232  : SCP-3300
    #      : (SCP-3300, "The Rain")
     232    :     "SCP-3300",


    # 233  : SCP-005
    #      : (SCP-005, "Skeleton Key")
     233    :     "SCP-005",


    # 234  : SCP-100000-J [OMITTED]
     234    :     None,


    # 235  : SCP-1313
    #      : (SCP-1313, "Solve for Bear")
     235    :     "SCP-1313",


    # 236  : SCP-3005
    #      : (SCP-3005, "A Light That Died")
     236    :     "SCP-3005",


    # 237  : SCP-427
    #      : (SCP-427, "Lovecraftian Locket")
     237    :     "SCP-427",


    # 238  : SCP-2217
    #      : (SCP-2217, "Hammer and Anvil")
     238    :     "SCP-2217",


    # 239  : SCP-650
    #      : (SCP-650, "Startling Statue")
     239    :     "SCP-650",


    # 240  : SCP-5140
    #      : (SCP-5140, "EVEREST")
     240    :     "SCP-5140",


    # 241  : SCP-2480
    #      : (SCP-2480, "An Unfinished Ritual")
     241    :     "SCP-2480",


    # 242  : SCP-1845
    #      : (SCP-1845, "Animal Kingdom")
     242    :     "SCP-1845",


    # 243  : SCP-732
    #      : (SCP-732, "The Fan-Fic Plague")
     243    :     "SCP-732",


    # 244  : SCP-451
    #      : (SCP-451, "Mister Lonely")
     244    :     "SCP-451",


    # 245  : SCP-4500
    #      : (SCP-4500, "Socratic Containment Procedures")
     245    :     "SCP-4500",


    # 246  : SCP-3626
    #      : (SCP-3626, "Do not stop reading this document")
     246    :     "SCP-3626",


    # 247  : SCP-457
    #      : (SCP-457, "Burning Man")
     247    :     "SCP-457",


    # 248  : SCP-5001
    #      : (SCP-5001, "Sacrosanct")
     248    :     "SCP-5001",


    # 249  : SCP-2700
    #      : (SCP-2700, "Teleforce")
     249    :     "SCP-2700",


    # 250  : SCP-216
    #      : (SCP-216, "The Safe")
     250    :     "SCP-216",


    # 251  : SCP-152
    #      : (SCP-152, "Book of Endings")
     251    :     "SCP-152",


    # 252  : SCP-4960
    #      : (SCP-4960, "Why the Foundation Funded a Hentai to Awaken a Sumerian Love Goddess (OR: How I Learned to Stop Worrying and Love Kedesh-Nanaya)")
     252    :     "SCP-4960",


    # 253  : SCP-3900
    #      : (SCP-3900, "The Internet of Things That Are Wolves")
     253    :     "SCP-3900",


    # 254  : SCP-1032
    #      : (SCP-1032, "The Prediction Clock")
     254    :     "SCP-1032",


    # 255  : SCP-2053
    #      : (SCP-2053, "Paternal Rubik's Cube")
     255    :     "SCP-2053",


    # 256  : SCP-178
    #      : (SCP-178, ""3-D" Specs")
     256    :     "SCP-178",


    # 257  : SCP-5002
    #      : (SCP-5002, "A Death in Containment")
     257    :     "SCP-5002",


    # 258  : SCP-453
    #      : (SCP-453, "Scripted Nightclub")
     258    :     "SCP-453",


    # 259  : SCP-3004
    #      : (SCP-3004, "Imago")
     259    :     "SCP-3004",


    # 260  : SCP-2273
    #      : (SCP-2273, "Major Alexei Belitrov, of the Red Army's 22nd Armored Infantry Division")
     260    :     "SCP-2273",


    # 261  : SCP-3078
    #      : (SCP-3078, "Cognitohazardous Shitpost")
     261    :     "SCP-3078",


    # 262  : SCP-1281
    #      : (SCP-1281, "The Harbinger")
     262    :     "SCP-1281",


    # 263  : SCP-315
    #      : (SCP-315, "The Recorded Man")
     263    :     "SCP-315",


    # 264  : SCP-3045
    #      : (SCP-3045, "bzzip.exe")
     264    :     "SCP-3045",


    # 265  : SCP-038
    #      : (SCP-038, "The Everything Tree")
     265    :     "SCP-038",


    # 266  : SCP-031
    #      : (SCP-031, "What is Love?")
     266    :     "SCP-031",


    # 267  : SCP-008-J [OMITTED]
     267    :     None,


    # 268  : SCP-072
    #      : (SCP-072, "The Foot of the Bed")
     268    :     "SCP-072",


    # 269  : SCP-860
    #      : (SCP-860, "Blue Key")
     269    :     "SCP-860",


    # 270  : SCP-3166
    #      : (SCP-3166, "You Have No Idea How Alone You Are, Garfield")
     270    :     "SCP-3166",


    # 271  : SCP-010-J [OMITTED]
     271    :     None,


    # 272  : SCP-1715
    #      : (SCP-1715, "Online Friend")
     272    :     "SCP-1715",


    # 273  : SCP-1539
    #      : (SCP-1539, "Semantic Dissociator")
     273    :     "SCP-1539",


    # 274  : SCP-1231
    #      : (SCP-1231, "The Theoretical Family")
     274    :     "SCP-1231",


    # 275  : SCP-572
    #      : (SCP-572, "Katana of Apparent Invincibility")
     275    :     "SCP-572",


    # 276  : SCP-021
    #      : (SCP-021, "Skin Wyrm")
     276    :     "SCP-021",


    # 277  : SCP-1322-J [OMITTED]
     277    :     None,


    # 278  : SCP-458
    #      : (SCP-458, "The Never-Ending Pizza Box")
     278    :     "SCP-458",


    # 279  : SCP-1739
    #      : (SCP-1739, "Obsolete Laptop")
     279    :     "SCP-1739",


    # 280  : SCP-1316
    #      : (SCP-1316, "Lucy the Kitten Feline Espionage Device")
     280    :     "SCP-1316",



    # from: http://www.scpwiki.com/highest-rated-scps/p/4


    # 281  : SCP-040
    #      : (SCP-040, "Evolution's Child")
     281    :     "SCP-040",


    # 282  : SCP-162
    #      : (SCP-162, "Ball of Sharp")
     282    :     "SCP-162",


    # 283  : SCP-3812
    #      : (SCP-3812, "A Voice Behind Me")
     283    :     "SCP-3812",


    # 284  : SCP-2771
    #      : (SCP-2771, "Border Duty")
     284    :     "SCP-2771",


    # 285  : SCP-1247
    #      : (SCP-1247, "LaBeouf Viewer")
     285    :     "SCP-1247",


    # 286  : SCP-092
    #      : (SCP-092, ""The Best of The 5th Dimension"")
     286    :     "SCP-092",


    # 287  : SCP-1128
    #      : (SCP-1128, "Aquatic Horror")
     287    :     "SCP-1128",


    # 288  : SCP-2207
    #      : (SCP-2207, "Dimensional Razor")
     288    :     "SCP-2207",


    # 289  : SCP-1293
    #      : (SCP-1293, "Squeedle Deedle Dee!")
     289    :     "SCP-1293",


    # 290  : SCP-007
    #      : (SCP-007, "Abdominal Planet")
     290    :     "SCP-007",


    # 291  : SCP-3966
    #      : (SCP-3966, "Falling Out")
     291    :     "SCP-3966",


    # 292  : SCP-1802
    #      : (SCP-1802, ""Skip"")
     292    :     "SCP-1802",


    # 293  : SCP-006
    #      : (SCP-006, "Fountain of Youth")
     293    :     "SCP-006",


    # 294  : SCP-3201
    #      : (SCP-3201, "well, it was low-entropy while it lasted.")
     294    :     "SCP-3201",


    # 295  : SCP-127
    #      : (SCP-127, "The Living Gun")
     295    :     "SCP-127",


    # 296  : SCP-120
    #      : (SCP-120, "Teleporting Paddling Pool")
     296    :     "SCP-120",


    # 297  : SCP-205
    #      : (SCP-205, "Shadow Lamps")
     297    :     "SCP-205",


    # 298  : SCP-2774
    #      : (SCP-2774, "The Slow Burn Sloth")
     298    :     "SCP-2774",


    # 299  : SCP-2845
    #      : (SCP-2845, "THE DEER")
     299    :     "SCP-2845",


    # 300  : SCP-407
    #      : (SCP-407, "The Song of Genesis")
     300    :     "SCP-407",


    # 301  : SCP-069
    #      : (SCP-069, "Second Chance")
     301    :     "SCP-069",


    # 302  : SCP-148
    #      : (SCP-148, "The "Telekill" Alloy")
     302    :     "SCP-148",


    # 303  : SCP-1312
    #      : (SCP-1312, "Site 41")
     303    :     "SCP-1312",


    # 304  : SCP-931
    #      : (SCP-931, "A Rice Bowl")
     304    :     "SCP-931",


    # 305  : SCP-2571
    #      : (SCP-2571, "Cragglewood Park")
     305    :     "SCP-2571",


    # 306  : SCP-1233
    #      : (SCP-1233, "The Lunatic")
     306    :     "SCP-1233",


    # 307  : SCP-3922
    #      : (SCP-3922, "STOPRIGHTTHERECRIMINALSCUM!!!")
     307    :     "SCP-3922",


    # 308  : SCP-50-AE-J [OMITTED]
     308    :     None,


    # 309  : SCP-084
    #      : (SCP-084, "Static Tower")
     309    :     "SCP-084",


    # 310  : SCP-1562
    #      : (SCP-1562, "Tunnel Slide")
     310    :     "SCP-1562",


    # 311  : SCP-978
    #      : (SCP-978, "Desire Camera")
     311    :     "SCP-978",


    # 312  : SCP-674
    #      : (SCP-674, "The Exposition Gun")
     312    :     "SCP-674",


    # 313  : SCP-209
    #      : (SCP-209, "The Sadist's Tumbler")
     313    :     "SCP-209",


    # 314  : SCP-2915
    #      : (SCP-2915, "Frostee-Flesh")
     314    :     "SCP-2915",


    # 315  : SCP-1529
    #      : (SCP-1529, "King of the Mountain")
     315    :     "SCP-1529",


    # 316  : SCP-3171
    #      : (SCP-3171, "How the Foundation Came to Operate a Phone Sex Hotline")
     316    :     "SCP-3171",


    # 317  : SCP-112
    #      : (SCP-112, "The Variable Coaster")
     317    :     "SCP-112",


    # 318  : SCP-026
    #      : (SCP-026, "Afterschool Retention")
     318    :     "SCP-026",


    # 319  : SCP-5004
    #      : (SCP-5004, "MEGALOMANIA")
     319    :     "SCP-5004",


    # 320  : SCP-450
    #      : (SCP-450, "Abandoned Federal Penitentiary")
     320    :     "SCP-450",


    # 321  : SCP-3101
    #      : (SCP-3101, "Contain Me Harder")
     321    :     "SCP-3101",


    # 322  : SCP-2922
    #      : (SCP-2922, "Notes From the Under")
     322    :     "SCP-2922",


    # 323  : SCP-013
    #      : (SCP-013, "Blue Lady Cigarettes")
     323    :     "SCP-013",


    # 324  : SCP-2999
    #      : (SCP-2999, "The Black Cat and the White Rabbit")
     324    :     "SCP-2999",


    # 325  : SCP-10101-J [OMITTED]
     325    :     None,


    # 326  : SCP-2343
    #      : (SCP-2343, "How I Got To Memphis")
     326    :     "SCP-2343",


    # 327  : SCP-1633
    #      : (SCP-1633, "The Most Dangerous Video Game")
     327    :     "SCP-1633",


    # 328  : SCP-020
    #      : (SCP-020, "Unseen Mold")
     328    :     "SCP-020",


    # 329  : SCP-3043
    #      : (SCP-3043, "Murphy Law in… Type 3043 — FOR MURDER!")
     329    :     "SCP-3043",


    # 330  : SCP-027
    #      : (SCP-027, "The Vermin God")
     330    :     "SCP-027",


    # 331  : SCP-3799
    #      : (SCP-3799, "A Short History of Snowfall")
     331    :     "SCP-3799",


    # 332  : SCP-1160
    #      : (SCP-1160, "Effective Containment")
     332    :     "SCP-1160",


    # 333  : SCP-2598
    #      : (SCP-2598, "Traveling Moth Salesman")
     333    :     "SCP-2598",


    # 334  : SCP-1782
    #      : (SCP-1782, "Tabula Rasa")
     334    :     "SCP-1782",


    # 335  : SCP-000-J [OMITTED]
     335    :     None,


    # 336  : SCP-1500
    #      : (SCP-1500, "Zachary Callahan")
     336    :     "SCP-1500",


    # 337  : SCP-4335
    #      : (SCP-4335, "A Welt In The Crucible")
     337    :     "SCP-4335",


    # 338  : SCP-3935
    #      : (SCP-3935, "This Thing a Quiet Madness Made")
     338    :     "SCP-3935",


    # 339  : SCP-097
    #      : (SCP-097, "Old Fairgrounds")
     339    :     "SCP-097",


    # 340  : SCP-1296
    #      : (SCP-1296, "Dial-a-Llama")
     340    :     "SCP-1296",


    # 341  : SCP-826
    #      : (SCP-826, "Draws You into the Book")
     341    :     "SCP-826",


    # 342  : SCP-953
    #      : (SCP-953, "Polymorphic Humanoid")
     342    :     "SCP-953",


    # 343  : SCP-2851
    #      : (SCP-2851, "Red")
     343    :     "SCP-2851",


    # 344  : SCP-113
    #      : (SCP-113, "The Gender-Switcher")
     344    :     "SCP-113",


    # 345  : SCP-1584
    #      : (SCP-1584, "www.floatationdevice.███")
     345    :     "SCP-1584",


    # 346  : SCP-4975
    #      : (SCP-4975, "Time's Up")
     346    :     "SCP-4975",


    # 347  : SCP-435
    #      : (SCP-435, "He-Who-Made-Dark")
     347    :     "SCP-435",


    # 348  : SCP-2800
    #      : (SCP-2800, "Cactusman")
     348    :     "SCP-2800",


    # 349  : SCP-1555
    #      : (SCP-1555, "Facility")
     349    :     "SCP-1555",


    # 350  : SCP-2558-J [OMITTED]
     350    :     None,


    # 351  : SCP-019
    #      : (SCP-019, "The Monster Pot")
     351    :     "SCP-019",


    # 352  : SCP-1442
    #      : (SCP-1442, "Incorporated")
     352    :     "SCP-1442",


    # 353  : SCP-1799
    #      : (SCP-1799, "Mr. Laugh")
     353    :     "SCP-1799",


    # 354  : SCP-4006
    #      : (SCP-4006, "#MassaTruthetts")
     354    :     "SCP-4006",


    # 355  : SCP-1472
    #      : (SCP-1472, "Multiverse Strip Club")
     355    :     "SCP-1472",


    # 356  : SCP-956
    #      : (SCP-956, "The Child-Breaker")
     356    :     "SCP-956",


    # 357  : SCP-711
    #      : (SCP-711, "Paradoxical Insurance Policy")
     357    :     "SCP-711",


    # 358  : SCP-212
    #      : (SCP-212, "The Improver")
     358    :     "SCP-212",


    # 359  : SCP-846
    #      : (SCP-846, "Robo-Dude")
     359    :     "SCP-846",


    # 360  : SCP-2206
    #      : (SCP-2206, "Maximum League Baseball")
     360    :     "SCP-2206",


    # 361  : SCP-052
    #      : (SCP-052, "Time-Traveling Train")
     361    :     "SCP-052",


    # 362  : SCP-108
    #      : (SCP-108, "Extradimensional Nasal Cavity")
     362    :     "SCP-108",


    # 363  : SCP-2786
    #      : (SCP-2786, "The Archetype")
     363    :     "SCP-2786",


    # 364  : SCP-4100
    #      : (SCP-4100, "Future Imperfect")
     364    :     "SCP-4100",


    # 365  : SCP-262
    #      : (SCP-262, "A Coat of Many Arms")
     365    :     "SCP-262",


    # 366  : SCP-3512
    #      : (SCP-3512, "The More You Know")
     366    :     "SCP-3512",


    # 367  : SCP-1384
    #      : (SCP-1384, "Taker of Turns")
     367    :     "SCP-1384",


    # 368  : SCP-063
    #      : (SCP-063, ""The World's Best TothBrush"")
     368    :     "SCP-063",


    # 369  : SCP-2508
    #      : (SCP-2508, "The Long Wait")
     369    :     "SCP-2508",


    # 370  : SCP-2085
    #      : (SCP-2085, "The Black Rabbit Company")
     370    :     "SCP-2085",


    # 371  : SCP-1795
    #      : (SCP-1795, "The Star Womb")
     371    :     "SCP-1795",


    # 372  : SCP-870
    #      : (SCP-870, "The Maybe There Monsters")
     372    :     "SCP-870",


    # 373  : SCP-2614
    #      : (SCP-2614, "Sometimes I Go Out In Pity For Myself")
     373    :     "SCP-2614",



    # from: http://www.scpwiki.com/highest-rated-scps/p/5


    # 374  : SCP-3949
    #      : (SCP-3949, "Penumbra W.A.V.E. #1 Fan!")
     374    :     "SCP-3949",


    # 375  : SCP-2419
    #      : (SCP-2419, "The Laughing Men")
     375    :     "SCP-2419",


    # 376  : SCP-1360
    #      : (SCP-1360, "PSHUD #31")
     376    :     "SCP-1360",


    # 377  : SCP-023
    #      : (SCP-023, "Black Shuck")
     377    :     "SCP-023",


    # 378  : SCP-1155
    #      : (SCP-1155, "Predatory Street Art")
     378    :     "SCP-1155",


    # 379  : SCP-030
    #      : (SCP-030, "The Homunculus")
     379    :     "SCP-030",


    # 380  : SCP-5500
    #      : (SCP-5500, "Death of the Authors")
     380    :     "SCP-5500",


    # 381  : SCP-1903
    #      : (SCP-1903, "Jackie's Secret")
     381    :     "SCP-1903",


    # 382  : SCP-1851-EX [OMITTED]
     382    :     None,


    # 383  : SCP-1483
    #      : (SCP-1483, "The Third Antarctic Empire")
     383    :     "SCP-1483",


    # 384  : SCP-060
    #      : (SCP-060, "Infernal Occult Skeleton")
     384    :     "SCP-060",


    # 385  : SCP-2420
    #      : (SCP-2420, "A Good Dog")
     385    :     "SCP-2420",


    # 386  : SCP-370
    #      : (SCP-370, "A Key")
     386    :     "SCP-370",


    # 387  : SCP-2021
    #      : (SCP-2021, "Single-sided Paper")
     387    :     "SCP-2021",


    # 388  : SCP-4514
    #      : (SCP-4514, "The Thing That Kills You")
     388    :     "SCP-4514",


    # 389  : SCP-3108
    #      : (SCP-3108, "The Nerfing Gun")
     389    :     "SCP-3108",


    # 390  : SCP-609
    #      : (SCP-609, "Dr. Wondertainment's Ontological 6-Balls®")
     390    :     "SCP-609",


    # 391  : SCP-517
    #      : (SCP-517, "Grammie Knows")
     391    :     "SCP-517",


    # 392  : SCP-050
    #      : (SCP-050, "To The Cleverest")
     392    :     "SCP-050",


    # 393  : SCP-4290
    #      : (SCP-4290, "The Child Hungers")
     393    :     "SCP-4290",


    # 394  : SCP-1237
    #      : (SCP-1237, "The Epsilon Wave")
     394    :     "SCP-1237",


    # 395  : SCP-1485
    #      : (SCP-1485, "Normality")
     395    :     "SCP-1485",


    # 396  : SCP-2063
    #      : (SCP-2063, "A Past Vision of the Future")
     396    :     "SCP-2063",


    # 397  : SCP-1884
    #      : (SCP-1884, "Madame Rezarta and Her Amazing Palm Reader")
     397    :     "SCP-1884",


    # 398  : SCP-2932
    #      : (SCP-2932, "Titania's Prison")
     398    :     "SCP-2932",


    # 399  : SCP-319
    #      : (SCP-319, "A Curious Device")
     399    :     "SCP-319",


    # 400  : SCP-3448
    #      : (SCP-3448, "Halfterlife")
     400    :     "SCP-3448",


    # 401  : SCP-3280
    #      : (SCP-3280, "After the Storm")
     401    :     "SCP-3280",


    # 402  : SCP-5005
    #      : (SCP-5005, "Lamplight")
     402    :     "SCP-5005",


    # 403  : SCP-604
    #      : (SCP-604, "The Cannibal's Banquet; A Corrupted Ritual")
     403    :     "SCP-604",


    # 404  : SCP-K9-J-EX [OMITTED]
     404    :     None,


    # 405  : SCP-2300
    #      : (SCP-2300, "Periodic Golems")
     405    :     "SCP-2300",


    # 406  : SCP-1812
    #      : (SCP-1812, "Extralunar Meme")
     406    :     "SCP-1812",


    # 407  : SCP-1590
    #      : (SCP-1590, "The Book of Tamlin")
     407    :     "SCP-1590",


    # 408  : SCP-165
    #      : (SCP-165, "The Creeping, Hungry Sands of Tule")
     408    :     "SCP-165",


    # 409  : SCP-7143-J [OMITTED]
     409    :     None,


    # 410  : SCP-3688
    #      : (SCP-3688, "You Can Dance If You Want To")
     410    :     "SCP-3688",


    # 411  : SCP-3312
    #      : (SCP-3312, "OwO what's this?")
     411    :     "SCP-3312",


    # 412  : SCP-2702
    #      : (SCP-2702, "Professor Abnormal's Science Lab")
     412    :     "SCP-2702",


    # 413  : SCP-1427
    #      : (SCP-1427, "Extinguishing Stele")
     413    :     "SCP-1427",


    # 414  : SCP-3790
    #      : (SCP-3790, "Department of Abnormalities")
     414    :     "SCP-3790",


    # 415  : SCP-1972
    #      : (SCP-1972, "The Whore and the Cop")
     415    :     "SCP-1972",


    # 416  : SCP-5555
    #      : (SCP-5555, "Made in Heaven")
     416    :     "SCP-5555",


    # 417  : SCP-2078
    #      : (SCP-2078, "Third Party")
     417    :     "SCP-2078",


    # 418  : SCP-536
    #      : (SCP-536, "Physical Law Testing Chamber")
     418    :     "SCP-536",


    # 419  : SCP-413
    #      : (SCP-413, "Endless Garage")
     419    :     "SCP-413",


    # 420  : SCP-4955
    #      : (SCP-4955, "KNIFEA Knife Only Seen Through Gaslight")
     420    :     "SCP-4955",


    # 421  : SCP-1921
    #      : (SCP-1921, "Black Cotton Candy")
     421    :     "SCP-1921",


    # 422  : SCP-4010
    #      : (SCP-4010, "Attempt to look at what we accomplished")
     422    :     "SCP-4010",


    # 423  : SCP-3006
    #      : (SCP-3006, "Twice The Number One")
     423    :     "SCP-3006",


    # 424  : SCP-123-J [OMITTED]
     424    :     None,


    # 425  : SCP-3200
    #      : (SCP-3200, "Chronos")
     425    :     "SCP-3200",


    # 426  : SCP-029
    #      : (SCP-029, "Daughter of Shadows")
     426    :     "SCP-029",


    # 427  : SCP-1212-J [OMITTED]
     427    :     None,


    # 428  : SCP-1780
    #      : (SCP-1780, "The Temporal Anomalies Department")
     428    :     "SCP-1780",


    # 429  : SCP-1810
    #      : (SCP-1810, "Mr. Pierrot")
     429    :     "SCP-1810",


    # 430  : SCP-1337
    #      : (SCP-1337, "The Hitchhiker")
     430    :     "SCP-1337",


    # 431  : SCP-4062
    #      : (SCP-4062, "Soggy Doggy")
     431    :     "SCP-4062",


    # 432  : SCP-042-J [OMITTED]
     432    :     None,


    # 433  : SCP-1984
    #      : (SCP-1984, "Dead Hand")
     433    :     "SCP-1984",


    # 434  : SCP-272
    #      : (SCP-272, "An Old Iron Nail")
     434    :     "SCP-272",


    # 435  : SCP-3450
    #      : (SCP-3450, "OC DO NOT STEAL")
     435    :     "SCP-3450",


    # 436  : SCP-3020
    #      : (SCP-3020, "Depression")
     436    :     "SCP-3020",


    # 437  : SCP-2001
    #      : (SCP-2001, "A Space Oddity")
     437    :     "SCP-2001",


    # 438  : SCP-1456
    #      : (SCP-1456, ""You've Won!"")
     438    :     "SCP-1456",


    # 439  : SCP-411
    #      : (SCP-411, "Ancient Precog")
     439    :     "SCP-411",


    # 440  : SCP-1454
    #      : (SCP-1454, "Sibling Rivalry")
     440    :     "SCP-1454",


    # 441  : SCP-752
    #      : (SCP-752, "Altruistic Utopia")
     441    :     "SCP-752",


    # 442  : SCP-4182
    #      : (SCP-4182, "There is no Site-5")
     442    :     "SCP-4182",


    # 443  : SCP-3250
    #      : (SCP-3250, "Jesus Fried Chicken")
     443    :     "SCP-3250",


    # 444  : SCP-2020
    #      : (SCP-2020, "Cliche, Right?")
     444    :     "SCP-2020",


    # 445  : SCP-2881
    #      : (SCP-2881, "The Tree You Cannot Climb")
     445    :     "SCP-2881",


    # 446  : SCP-1348
    #      : (SCP-1348, "Inner Sanctum")
     446    :     "SCP-1348",


    # 447  : SCP-557
    #      : (SCP-557, "Ancient Containment Site")
     447    :     "SCP-557",


    # 448  : SCP-699
    #      : (SCP-699, "Mystery Box")
     448    :     "SCP-699",


    # 449  : SCP-067
    #      : (SCP-067, "The Artist's Pen")
     449    :     "SCP-067",


    # 450  : SCP-2193
    #      : (SCP-2193, ""Monthly Termination"")
     450    :     "SCP-2193",


    # 451  : SCP-2406
    #      : (SCP-2406, "The Colossus")
     451    :     "SCP-2406",


    # 452  : SCP-705
    #      : (SCP-705, "Militaristic Play-Doh")
     452    :     "SCP-705",


    # 453  : SCP-231-J [OMITTED]
     453    :     None,


    # 454  : SCP-1915
    #      : (SCP-1915, "Status Quo")
     454    :     "SCP-1915",


    # 455  : SCP-1468
    #      : (SCP-1468, "Literature Birds")
     455    :     "SCP-1468",


    # 456  : SCP-100
    #      : (SCP-100, ""Jamaican Joe's Junkyard Jubilee"")
     456    :     "SCP-100",


    # 457  : SCP-3388
    #      : (SCP-3388, "Cacthulhu")
     457    :     "SCP-3388",


    # 458  : SCP-3456
    #      : (SCP-3456, "The Orcadian Horsemen")
     458    :     "SCP-3456",


    # 459  : SCP-2191
    #      : (SCP-2191, ""Dracula Factory"")
     459    :     "SCP-2191",


    # 460  : SCP-1846
    #      : (SCP-1846, "Maize Angel")
     460    :     "SCP-1846",


    # 461  : SCP-1165
    #      : (SCP-1165, "Minus Level")
     461    :     "SCP-1165",


    # 462  : SCP-268
    #      : (SCP-268, "Cap of Neglect")
     462    :     "SCP-268",


    # 463  : SCP-4971
    #      : (SCP-4971, "Rituals")
     463    :     "SCP-4971",


    # 464  : SCP-3999-J [OMITTED]
     464    :     None,


    # 465  : SCP-2075
    #      : (SCP-2075, "The Way of All Flesh")
     465    :     "SCP-2075",


    # 466  : SCP-3484
    #      : (SCP-3484, "Missing Pieces")
     466    :     "SCP-3484",


    # 467  : SCP-228
    #      : (SCP-228, "Psychiatric Diagnostic Tool")
     467    :     "SCP-228",


    # 468  : SCP-372
    #      : (SCP-372, "Peripheral Jumper")
     468    :     "SCP-372",


    # 469  : SCP-649-2568-J [OMITTED]
     469    :     None,



    # from: http://www.scpwiki.com/highest-rated-scps/p/6


    # 470  : SCP-1659
    #      : (SCP-1659, "Directorate K")
     470    :     "SCP-1659",


    # 471  : SCP-1D6-J [OMITTED]
     471    :     None,


    # 472  : SCP-603
    #      : (SCP-603, "Self-Replicating Computer Program")
     472    :     "SCP-603",


    # 473  : SCP-2547
    #      : (SCP-2547, "Dog Days Of Summer")
     473    :     "SCP-2547",


    # 474  : SCP-1833
    #      : (SCP-1833, "Class of '76")
     474    :     "SCP-1833",


    # 475  : SCP-025
    #      : (SCP-025, "A Well-Worn Wardrobe")
     475    :     "SCP-025",


    # 476  : SCP-847
    #      : (SCP-847, "The Mannequin")
     476    :     "SCP-847",


    # 477  : SCP-4774
    #      : (SCP-4774, "The Ninth Planet [citation needed]")
     477    :     "SCP-4774",


    # 478  : SCP-198
    #      : (SCP-198, "Cup of Joe")
     478    :     "SCP-198",


    # 479  : SCP-247
    #      : (SCP-247, "A Harmless Kitten")
     479    :     "SCP-247",


    # 480  : SCP-143
    #      : (SCP-143, "The Bladewood Grove")
     480    :     "SCP-143",


    # 481  : SCP-2203
    #      : (SCP-2203, "Find the One for You!")
     481    :     "SCP-2203",


    # 482  : SCP-2118
    #      : (SCP-2118, "The Lost Child")
     482    :     "SCP-2118",


    # 483  : SCP-2980
    #      : (SCP-2980, "Devil's Nightlight")
     483    :     "SCP-2980",


    # 484  : SCP-166
    #      : (SCP-166, "Teenage Succubus")
     484    :     "SCP-166",


    # 485  : SCP-3515
    #      : (SCP-3515, "Unearth")
     485    :     "SCP-3515",


    # 486  : SCP-4028
    #      : (SCP-4028, "La Historia de Don Quixote de la Mancha")
     486    :     "SCP-4028",


    # 487  : SCP-2072
    #      : (SCP-2072, "Prime Ministerial Pet Cemetery")
     487    :     "SCP-2072",


    # 488  : SCP-4511
    #      : (SCP-4511, "SWINE GOD")
     488    :     "SCP-4511",


    # 489  : SCP-SCP-J [OMITTED]
     489    :     None,


    # 490  : SCP-973
    #      : (SCP-973, "Smokey")
     490    :     "SCP-973",


    # 491  : SCP-4233
    #      : (SCP-4233, "The Dreadnought")
     491    :     "SCP-4233",


    # 492  : SCP-3041
    #      : (SCP-3041, "The Red Knife")
     492    :     "SCP-3041",


    # 493  : SCP-745
    #      : (SCP-745, "The Headlights")
     493    :     "SCP-745",


    # 494  : SCP-4966
    #      : (SCP-4966, "Tubbioca: Devourer of Souls, Consumer of Secrets, Lord of Munchies")
     494    :     "SCP-4966",


    # 495  : SCP-777-J [OMITTED]
     495    :     None,


    # 496  : SCP-668
    #      : (SCP-668, "13" Chef's Knife")
     496    :     "SCP-668",


    # 497  : SCP-144
    #      : (SCP-144, "Tibetan Rope to Heaven")
     497    :     "SCP-144",


    # 498  : SCP-2424
    #      : (SCP-2424, "Hostile Walrus Cyborg research ongoing")
     498    :     "SCP-2424",


    # 499  : SCP-1459-J [OMITTED]
     499    :     None,


    # 500  : SCP-187
    #      : (SCP-187, "Double Vision")
     500    :     "SCP-187",


    # 501  : SCP-361
    #      : (SCP-361, "Bronze Liver")
     501    :     "SCP-361",


    # 502  : SCP-332
    #      : (SCP-332, "The 1976 Kirk Lonwood High School Marching Band")
     502    :     "SCP-332",


    # 503  : SCP-1616
    #      : (SCP-1616, "Nibbles")
     503    :     "SCP-1616",


    # 504  : SCP-920
    #      : (SCP-920, "Mr. Lost")
     504    :     "SCP-920",


    # 505  : SCP-432
    #      : (SCP-432, "Cabinet Maze")
     505    :     "SCP-432",


    # 506  : SCP-3035
    #      : (SCP-3035, "Science Bugs")
     506    :     "SCP-3035",


    # 507  : SCP-400
    #      : (SCP-400, "Beautiful Babies")
     507    :     "SCP-400",


    # 508  : SCP-1660
    #      : (SCP-1660, "Unearthly Forest")
     508    :     "SCP-1660",


    # 509  : SCP-1033
    #      : (SCP-1033, "33 Second Man")
     509    :     "SCP-1033",


    # 510  : SCP-536-J [OMITTED]
     510    :     None,


    # 511  : SCP-208
    #      : (SCP-208, ""Bes"")
     511    :     "SCP-208",


    # 512  : SCP-145
    #      : (SCP-145, "Man-Absorbing Phone")
     512    :     "SCP-145",


    # 513  : SCP-2460
    #      : (SCP-2460, "Dark Satellite")
     513    :     "SCP-2460",


    # 514  : SCP-1162
    #      : (SCP-1162, "A Hole in the Wall")
     514    :     "SCP-1162",


    # 515  : SCP-095-J [OMITTED]
     515    :     None,


    # 516  : SCP-4008
    #      : (SCP-4008, "Wormwood")
     516    :     "SCP-4008",


    # 517  : SCP-2790
    #      : (SCP-2790, "You've Got a Squid in Me")
     517    :     "SCP-2790",


    # 518  : SCP-1722
    #      : (SCP-1722, "Curmudgeon's Cudgel")
     518    :     "SCP-1722",


    # 519  : SCP-1147
    #      : (SCP-1147, "Adaptive Plum Tree")
     519    :     "SCP-1147",


    # 520  : SCP-582
    #      : (SCP-582, "A Bundle of Stories")
     520    :     "SCP-582",


    # 521  : SCP-3908
    #      : (SCP-3908, "SCP-3908")
     521    :     "SCP-3908",


    # 522  : SCP-1710
    #      : (SCP-1710, "Life as a Tree")
     522    :     "SCP-1710",


    # 523  : SCP-098
    #      : (SCP-098, "Surgeon Crabs")
     523    :     "SCP-098",


    # 524  : SCP-645
    #      : (SCP-645, "Mouth of Truth")
     524    :     "SCP-645",


    # 525  : SCP-5552
    #      : (SCP-5552, "Our Stolen Theory")
     525    :     "SCP-5552",


    # 526  : SCP-616
    #      : (SCP-616, "The Vessel and the Gate")
     526    :     "SCP-616",


    # 527  : SCP-1761
    #      : (SCP-1761, "The Republic of Arnold Fitzwilliams")
     527    :     "SCP-1761",


    # 528  : SCP-1304
    #      : (SCP-1304, "Metafictional Rebirth Ritual")
     528    :     "SCP-1304",


    # 529  : SCP-629
    #      : (SCP-629, "Mr. Brass")
     529    :     "SCP-629",


    # 530  : SCP-1123
    #      : (SCP-1123, "Atrocity Skull")
     530    :     "SCP-1123",


    # 531  : SCP-1011
    #      : (SCP-1011, "Humanization Process")
     531    :     "SCP-1011",


    # 532  : SCP-3305
    #      : (SCP-3305, "The Father, The Son, and The Holy Toast")
     532    :     "SCP-3305",


    # 533  : SCP-028-J [OMITTED]
     533    :     None,


    # 534  : SCP-3240
    #      : (SCP-3240, "The Bones Of What You Believe")
     534    :     "SCP-3240",


    # 535  : SCP-1127
    #      : (SCP-1127, "A Film Festival")
     535    :     "SCP-1127",


    # 536  : SCP-1103
    #      : (SCP-1103, "Dr. Wondertainment Young Surgeon's Transplant Kit")
     536    :     "SCP-1103",


    # 537  : SCP-514
    #      : (SCP-514, "A Flock of Doves")
     537    :     "SCP-514",


    # 538  : SCP-1860
    #      : (SCP-1860, "Its Bleeding Song")
     538    :     "SCP-1860",


    # 539  : SCP-270
    #      : (SCP-270, "Secluded Telephone")
     539    :     "SCP-270",


    # 540  : SCP-4002
    #      : (SCP-4002, "The Black Moon Howls From Beyond The Edge Of Time")
     540    :     "SCP-4002",


    # 541  : SCP-682-CU [OMITTED]
     541    :     None,


    # 542  : SCP-2002
    #      : (SCP-2002, "A Dead Future")
     542    :     "SCP-2002",


    # 543  : SCP-1719
    #      : (SCP-1719, "The Harrison-Grey Effect")
     543    :     "SCP-1719",


    # 544  : SCP-445
    #      : (SCP-445, ""Dr. Wondertainment's Super Paper"")
     544    :     "SCP-445",


    # 545  : SCP-3929
    #      : (SCP-3929, "boner pill by dado")
     545    :     "SCP-3929",


    # 546  : SCP-2746
    #      : (SCP-2746, "████ is dead.")
     546    :     "SCP-2746",


    # 547  : SCP-2014
    #      : (SCP-2014, "Zsar Magoth")
     547    :     "SCP-2014",


    # 548  : SCP-1859
    #      : (SCP-1859, "Life Over Geological Time")
     548    :     "SCP-1859",


    # 549  : SCP-2578
    #      : (SCP-2578, ""This Machine Kills Fascists"")
     549    :     "SCP-2578",


    # 550  : SCP-2004
    #      : (SCP-2004, "Personal Data Assistants of the Gods")
     550    :     "SCP-2004",


    # 551  : SCP-1541
    #      : (SCP-1541, "The Drunken God")
     551    :     "SCP-1541",


    # 552  : SCP-727-J [OMITTED]
     552    :     None,


    # 553  : SCP-4338
    #      : (SCP-4338, "Vulcan, the Disaster")
     553    :     "SCP-4338",


    # 554  : SCP-4498
    #      : (SCP-4498, "The Plurality of Jack Bright")
     554    :     "SCP-4498",


    # 555  : SCP-2200
    #      : (SCP-2200, "Soulberg")
     555    :     "SCP-2200",


    # 556  : SCP-687
    #      : (SCP-687, "NOIR")
     556    :     "SCP-687",


    # 557  : SCP-119
    #      : (SCP-119, "Timecrowave")
     557    :     "SCP-119",


    # 558  : SCP-4517
    #      : (SCP-4517, "Not Very 𝒩")
     558    :     "SCP-4517",


    # 559  : SCP-2798
    #      : (SCP-2798, "This Dying World")
     559    :     "SCP-2798",


    # 560  : SCP-409
    #      : (SCP-409, "Contagious Crystal")
     560    :     "SCP-409",


    # 561  : SCP-1535
    #      : (SCP-1535, "Purgatory")
     561    :     "SCP-1535",


    # 562  : SCP-4003
    #      : (SCP-4003, "On Cowboys, Catholicism, and the Cretaceous")
     562    :     "SCP-4003",


    # 563  : SCP-2501
    #      : (SCP-2501, "The Claw")
     563    :     "SCP-2501",


    # 564  : SCP-3980
    #      : (SCP-3980, "Blind Lead the Blind")
     564    :     "SCP-3980",


    # 565  : SCP-2190
    #      : (SCP-2190, "Phone calls from Mom")
     565    :     "SCP-2190",



    # from: http://www.scpwiki.com/highest-rated-scps/p/7


    # 566  : SCP-1015
    #      : (SCP-1015, "Poor Man's Midas")
     566    :     "SCP-1015",


    # 567  : SCP-3936
    #      : (SCP-3936, "Working as Intended")
     567    :     "SCP-3936",


    # 568  : SCP-3998
    #      : (SCP-3998, "The Wicker Witch Lives")
     568    :     "SCP-3998",


    # 569  : SCP-592
    #      : (SCP-592, "Inaccurate History Book")
     569    :     "SCP-592",


    # 570  : SCP-3009
    #      : (SCP-3009, "Hi, I'm Your Snappelganger!")
     570    :     "SCP-3009",


    # 571  : SCP-3340
    #      : (SCP-3340, "You Think, Therefore We Are")
     571    :     "SCP-3340",


    # 572  : SCP-729-J [OMITTED]
     572    :     None,


    # 573  : SCP-2820
    #      : (SCP-2820, "Vaishnavastra")
     573    :     "SCP-2820",


    # 574  : SCP-184-J [OMITTED]
     574    :     None,


    # 575  : SCP-957
    #      : (SCP-957, "Baiting")
     575    :     "SCP-957",


    # 576  : SCP-511
    #      : (SCP-511, "Basement Cat")
     576    :     "SCP-511",


    # 577  : SCP-408
    #      : (SCP-408, "Illusory Butterflies")
     577    :     "SCP-408",


    # 578  : SCP-3636
    #      : (SCP-3636, "World's Greatest Jukebox")
     578    :     "SCP-3636",


    # 579  : SCP-032
    #      : (SCP-032, "Brothers' Bride")
     579    :     "SCP-032",


    # 580  : SCP-1319
    #      : (SCP-1319, "The Split-Up")
     580    :     "SCP-1319",


    # 581  : SCP-1059
    #      : (SCP-1059, "Infectious Censorship")
     581    :     "SCP-1059",


    # 582  : SCP-5858
    #      : (SCP-5858, "The Kindness of Strangers")
     582    :     "SCP-5858",


    # 583  : SCP-3241
    #      : (SCP-3241, "The SS Sommerfeld")
     583    :     "SCP-3241",


    # 584  : SCP-2933
    #      : (SCP-2933, "Mr. Scary")
     584    :     "SCP-2933",


    # 585  : SCP-1340
    #      : (SCP-1340, "The Fraternal Order of Cave Mantas")
     585    :     "SCP-1340",


    # 586  : SCP-1357
    #      : (SCP-1357, "The Children's Park")
     586    :     "SCP-1357",


    # 587  : SCP-1844
    #      : (SCP-1844, "Crater at 31.7███° N, 35.1███° E")
     587    :     "SCP-1844",


    # 588  : SCP-967
    #      : (SCP-967, "Infinite Scrapyard")
     588    :     "SCP-967",


    # 589  : SCP-3844
    #      : (SCP-3844, "To Slay A Dragon")
     589    :     "SCP-3844",


    # 590  : SCP-1679
    #      : (SCP-1679, "Post-Mortem Peoples' Choice")
     590    :     "SCP-1679",


    # 591  : SCP-1310
    #      : (SCP-1310, "Examination Room 10")
     591    :     "SCP-1310",


    # 592  : SCP-583
    #      : (SCP-583, "Deathly Video Tape")
     592    :     "SCP-583",


    # 593  : SCP-018
    #      : (SCP-018, "Super Ball")
     593    :     "SCP-018",


    # 594  : SCP-2115
    #      : (SCP-2115, "Meet Other People")
     594    :     "SCP-2115",


    # 595  : SCP-726
    #      : (SCP-726, "Reconstructive Maggots")
     595    :     "SCP-726",


    # 596  : SCP-4633
    #      : (SCP-4633, "Rock, Paper, Yog-Sothoth")
     596    :     "SCP-4633",


    # 597  : SCP-3128
    #      : (SCP-3128, "Let's Play Monopoly!")
     597    :     "SCP-3128",


    # 598  : SCP-748
    #      : (SCP-748, "Industrial Dissolution")
     598    :     "SCP-748",


    # 599  : SCP-172
    #      : (SCP-172, "The Gearman")
     599    :     "SCP-172",


    # 600  : SCP-1682
    #      : (SCP-1682, "Solar Parasite")
     600    :     "SCP-1682",


    # 601  : SCP-469
    #      : (SCP-469, "Many-Winged Angel")
     601    :     "SCP-469",


    # 602  : SCP-5003
    #      : (SCP-5003, "Powerless")
     602    :     "SCP-5003",


    # 603  : SCP-4057
    #      : (SCP-4057, "Save Her")
     603    :     "SCP-4057",


    # 604  : SCP-2090
    #      : (SCP-2090, "Potentially XK Tim Duncan")
     604    :     "SCP-2090",


    # 605  : SCP-743
    #      : (SCP-743, "A Chocolate Fountain")
     605    :     "SCP-743",


    # 606  : SCP-4005
    #      : (SCP-4005, "The Holy and Heavenly City of Fabled China")
     606    :     "SCP-4005",


    # 607  : SCP-2700-EX [OMITTED]
     607    :     None,


    # 608  : SCP-838
    #      : (SCP-838, "The Dream Job")
     608    :     "SCP-838",


    # 609  : SCP-1152
    #      : (SCP-1152, "A Common Raccoon")
     609    :     "SCP-1152",


    # 610  : SCP-5200-J [OMITTED]
     610    :     None,


    # 611  : SCP-1520
    #      : (SCP-1520, "An Elderly Monk")
     611    :     "SCP-1520",


    # 612  : SCP-698
    #      : (SCP-698, "Judgmental Turtle")
     612    :     "SCP-698",


    # 613  : SCP-590
    #      : (SCP-590, "He Feels Your Pain")
     613    :     "SCP-590",


    # 614  : SCP-3984
    #      : (SCP-3984, "Poking Death with a Stick")
     614    :     "SCP-3984",


    # 615  : SCP-1839
    #      : (SCP-1839, "Reproductive Methods of Bony Fish")
     615    :     "SCP-1839",


    # 616  : SCP-1702
    #      : (SCP-1702, "The French Hive")
     616    :     "SCP-1702",


    # 617  : SCP-1510
    #      : (SCP-1510, "The Tarnished Legionnaire")
     617    :     "SCP-1510",


    # 618  : SCP-1045
    #      : (SCP-1045, "Candle of Life")
     618    :     "SCP-1045",


    # 619  : SCP-765
    #      : (SCP-765, "Duck Pond")
     619    :     "SCP-765",


    # 620  : SCP-5370
    #      : (SCP-5370, "Chessland")
     620    :     "SCP-5370",


    # 621  : SCP-4144
    #      : (SCP-4144, "The Most Important Meal Of The Day")
     621    :     "SCP-4144",


    # 622  : SCP-3022
    #      : (SCP-3022, "Hooked on a Feeling")
     622    :     "SCP-3022",


    # 623  : SCP-531
    #      : (SCP-531, "Paired Brass Guard Cats")
     623    :     "SCP-531",


    # 624  : SCP-2061
    #      : (SCP-2061, ""Entire Local Family Chokes To Death On Single Calculator"")
     624    :     "SCP-2061",


    # 625  : SCP-123
    #      : (SCP-123, "Contained Miniature Black Hole")
     625    :     "SCP-123",


    # 626  : SCP-2017
    #      : (SCP-2017, "The Girl with the Made-Up Disease")
     626    :     "SCP-2017",


    # 627  : SCP-158
    #      : (SCP-158, "Soul Extractor")
     627    :     "SCP-158",


    # 628  : SCP-689
    #      : (SCP-689, "Haunter in the Dark")
     628    :     "SCP-689",


    # 629  : SCP-1548
    #      : (SCP-1548, "The Star, the Hateful")
     629    :     "SCP-1548",


    # 630  : SCP-2331
    #      : (SCP-2331, "SCRAVECROW")
     630    :     "SCP-2331",


    # 631  : SCP-2094
    #      : (SCP-2094, "Motormouth")
     631    :     "SCP-2094",


    # 632  : SCP-1883
    #      : (SCP-1883, "Gamification")
     632    :     "SCP-1883",


    # 633  : SCP-2505
    #      : (SCP-2505, "Entry Creation Wizard")
     633    :     "SCP-2505",


    # 634  : SCP-1638
    #      : (SCP-1638, "Silence")
     634    :     "SCP-1638",


    # 635  : SCP-4746
    #      : (SCP-4746, "Marked for Death")
     635    :     "SCP-4746",


    # 636  : SCP-4040
    #      : (SCP-4040, "At The Bottom Of A Bottomless Pit")
     636    :     "SCP-4040",


    # 637  : SCP-404-J [OMITTED]
     637    :     None,


    # 638  : SCP-5280-J [OMITTED]
     638    :     None,


    # 639  : SCP-401
    #      : (SCP-401, "A Palm Tree")
     639    :     "SCP-401",


    # 640  : SCP-2317-J [OMITTED]
     640    :     None,


    # 641  : SCP-3027
    #      : (SCP-3027, "Strong Language")
     641    :     "SCP-3027",


    # 642  : SCP-2140
    #      : (SCP-2140, "Retroconverter")
     642    :     "SCP-2140",


    # 643  : SCP-711-EX [OMITTED]
     643    :     None,


    # 644  : SCP-201
    #      : (SCP-201, "The Empty World")
     644    :     "SCP-201",


    # 645  : SCP-3088
    #      : (SCP-3088, "Law Of The Land")
     645    :     "SCP-3088",


    # 646  : SCP-2165
    #      : (SCP-2165, "Irredeemable")
     646    :     "SCP-2165",


    # 647  : SCP-2019
    #      : (SCP-2019, "Gelatinous Brain Cube")
     647    :     "SCP-2019",


    # 648  : SCP-1879
    #      : (SCP-1879, "Indoor Salesman")
     648    :     "SCP-1879",


    # 649  : SCP-1382
    #      : (SCP-1382, "Save Our Souls")
     649    :     "SCP-1382",


    # 650  : SCP-1588
    #      : (SCP-1588, "The Cliff Face")
     650    :     "SCP-1588",


    # 651  : SCP-1012
    #      : (SCP-1012, "Secret Chord")
     651    :     "SCP-1012",


    # 652  : SCP-078
    #      : (SCP-078, "Guilt")
     652    :     "SCP-078",


    # 653  : SCP-2338
    #      : (SCP-2338, "An Unorthodox Adoption")
     653    :     "SCP-2338",


    # 654  : SCP-2099
    #      : (SCP-2099, "Brain in a Jar")
     654    :     "SCP-2099",


    # 655  : SCP-1252
    #      : (SCP-1252, "A Half-Formed Idea")
     655    :     "SCP-1252",


    # 656  : SCP-3480
    #      : (SCP-3480, "Olympus Mons")
     656    :     "SCP-3480",


    # 657  : SCP-2059
    #      : (SCP-2059, "Wall of Flesh")
     657    :     "SCP-2059",


    # 658  : SCP-2310
    #      : (SCP-2310, "The House That Makes You Sarah Palmer")
     658    :     "SCP-2310",


    # 659  : SCP-1836
    #      : (SCP-1836, "Mother in the Ice")
     659    :     "SCP-1836",


    # 660  : SCP-091
    #      : (SCP-091, "Nostalgia")
     660    :     "SCP-091",


    # 661  : SCP-4281
    #      : (SCP-4281, "Stalled Conversation")
     661    :     "SCP-4281",


    # 662  : SCP-2991
    #      : (SCP-2991, ""Scarf"")
     662    :     "SCP-2991",


    # 663  : SCP-1619
    #      : (SCP-1619, "Site-45-C: Floor 24")
     663    :     "SCP-1619",


    # 664  : SCP-065-J [OMITTED]
     664    :     None,


    # 665  : SCP-4098
    #      : (SCP-4098, "S-C-P, easy as 19-3-16!")
     665    :     "SCP-4098",



    # from: http://www.scpwiki.com/highest-rated-scps/p/8


    # 666  : SCP-4242
    #      : (SCP-4242, "Foundations")
     666    :     "SCP-4242",


    # 667  : SCP-2513
    #      : (SCP-2513, "Also, Carthage Must Be Destroyed")
     667    :     "SCP-2513",


    # 668  : SCP-1074
    #      : (SCP-1074, "Stendhal's Nightmare")
     668    :     "SCP-1074",


    # 669  : SCP-431
    #      : (SCP-431, "Dr. Gideon")
     669    :     "SCP-431",


    # 670  : SCP-352
    #      : (SCP-352, ""Baba Yaga"")
     670    :     "SCP-352",


    # 671  : SCP-5045
    #      : (SCP-5045, "You Get Used to It")
     671    :     "SCP-5045",


    # 672  : SCP-1020
    #      : (SCP-1020, "An Important Letter")
     672    :     "SCP-1020",


    # 673  : SCP-099
    #      : (SCP-099, "The Portrait")
     673    :     "SCP-099",


    # 674  : SCP-3017
    #      : (SCP-3017, "Person of Interest")
     674    :     "SCP-3017",


    # 675  : SCP-736
    #      : (SCP-736, "The Iapetus Anomaly")
     675    :     "SCP-736",


    # 676  : SCP-919
    #      : (SCP-919, "Needy Mirror")
     676    :     "SCP-919",


    # 677  : SCP-4773-2 [OMITTED]
     677    :     None,


    # 678  : SCP-2900
    #      : (SCP-2900, "Nobody gets left behind")
     678    :     "SCP-2900",


    # 679  : SCP-2022
    #      : (SCP-2022, "Sunlight Pills™")
     679    :     "SCP-2022",


    # 680  : SCP-057
    #      : (SCP-057, "The Daily Grind")
     680    :     "SCP-057",


    # 681  : SCP-3143
    #      : (SCP-3143, "Murphy Law in… The Foundation Always Rings Twice!")
     681    :     "SCP-3143",


    # 682  : SCP-3513
    #      : (SCP-3513, "The brain that ate itself")
     682    :     "SCP-3513",


    # 683  : SCP-026-J [OMITTED]
     683    :     None,


    # 684  : SCP-5150-J [OMITTED]
     684    :     None,


    # 685  : SCP-2133
    #      : (SCP-2133, "Our Land, Our Bondage")
     685    :     "SCP-2133",


    # 686  : SCP-1177
    #      : (SCP-1177, "The Coupon Cutter")
     686    :     "SCP-1177",


    # 687  : SCP-115
    #      : (SCP-115, "Miniature Dump Truck")
     687    :     "SCP-115",


    # 688  : SCP-3774
    #      : (SCP-3774, "My Heart DEETs Faster For You")
     688    :     "SCP-3774",


    # 689  : SCP-2432
    #      : (SCP-2432, "Room Service")
     689    :     "SCP-2432",


    # 690  : SCP-2996
    #      : (SCP-2996, "ERROR / ERROR")
     690    :     "SCP-2996",


    # 691  : SCP-071
    #      : (SCP-071, "Degenerative Metamorphic Entity")
     691    :     "SCP-071",


    # 692  : SCP-1788
    #      : (SCP-1788, "The Adults")
     692    :     "SCP-1788",


    # 693  : SCP-296
    #      : (SCP-296, "Armed Containment Site-03")
     693    :     "SCP-296",


    # 694  : SCP-064
    #      : (SCP-064, "Flawed von Neumann Structure")
     694    :     "SCP-064",


    # 695  : SCP-2805
    #      : (SCP-2805, "Disney on Ice")
     695    :     "SCP-2805",


    # 696  : SCP-1417-J [OMITTED]
     696    :     None,


    # 697  : SCP-1639
    #      : (SCP-1639, "The Jazz Station")
     697    :     "SCP-1639",


    # 698  : SCP-523
    #      : (SCP-523, "The Most Unhelpful Object On Earth")
     698    :     "SCP-523",


    # 699  : SCP-4661
    #      : (SCP-4661, "Sin City")
     699    :     "SCP-4661",


    # 700  : SCP-3074
    #      : (SCP-3074, "Kafka's Parking Garage")
     700    :     "SCP-3074",


    # 701  : SCP-3338
    #      : (SCP-3338, "Otamatone wants to be your roommate~")
     701    :     "SCP-3338",


    # 702  : SCP-3021
    #      : (SCP-3021, "Q=")
     702    :     "SCP-3021",


    # 703  : SCP-2874
    #      : (SCP-2874, "Don-Burten Explosive Dev13e")
     703    :     "SCP-2874",


    # 704  : SCP-1396
    #      : (SCP-1396, "Jovian Kill-Sats")
     704    :     "SCP-1396",


    # 705  : SCP-1269
    #      : (SCP-1269, "Stalker Mailbox")
     705    :     "SCP-1269",


    # 706  : SCP-1036
    #      : (SCP-1036, "Nkondi")
     706    :     "SCP-1036",


    # 707  : SCP-054
    #      : (SCP-054, "Water Nymph")
     707    :     "SCP-054",


    # 708  : SCP-001
    #      : (SCP-001, "Awaiting De-classification [Blocked]")
     708    :     "SCP-001",


    # 709  : SCP-004-J [OMITTED]
     709    :     None,


    # 710  : SCP-2282
    #      : (SCP-2282, "Goat.")
     710    :     "SCP-2282",


    # 711  : SCP-940
    #      : (SCP-940, "Araneae Marionettes")
     711    :     "SCP-940",


    # 712  : SCP-297
    #      : (SCP-297, ""Steely Dan"")
     712    :     "SCP-297",


    # 713  : SCP-014-J [OMITTED]
     713    :     None,


    # 714  : SCP-134
    #      : (SCP-134, "Star-Eyed Child")
     714    :     "SCP-134",


    # 715  : SCP-3866
    #      : (SCP-3866, "Youth In Asia by dado")
     715    :     "SCP-3866",


    # 716  : SCP-872
    #      : (SCP-872, "The Tattered Farmer")
     716    :     "SCP-872",


    # 717  : SCP-252
    #      : (SCP-252, "Humboldt Squid")
     717    :     "SCP-252",


    # 718  : SCP-666
    #      : (SCP-666, "Spirit Lodge")
     718    :     "SCP-666",


    # 719  : SCP-2293
    #      : (SCP-2293, "An Inside Joke")
     719    :     "SCP-2293",


    # 720  : SCP-2686
    #      : (SCP-2686, "Moon Wizard")
     720    :     "SCP-2686",


    # 721  : SCP-414
    #      : (SCP-414, "Regardless, I Might Prefer Myself Sick")
     721    :     "SCP-414",


    # 722  : SCP-1241
    #      : (SCP-1241, "Livin' With Werewolves")
     722    :     "SCP-1241",


    # 723  : SCP-753
    #      : (SCP-753, "Automatic Artist")
     723    :     "SCP-753",


    # 724  : SCP-4004
    #      : (SCP-4004, "A Dream Come True")
     724    :     "SCP-4004",


    # 725  : SCP-2049
    #      : (SCP-2049, "The Interdimensional Weather Station")
     725    :     "SCP-2049",


    # 726  : SCP-1577
    #      : (SCP-1577, "A Flare Gun")
     726    :     "SCP-1577",


    # 727  : SCP-107
    #      : (SCP-107, "The Turtle Shell")
     727    :     "SCP-107",


    # 728  : SCP-5554
    #      : (SCP-5554, "Aki Aki! 🍊🐻")
     728    :     "SCP-5554",


    # 729  : SCP-2232
    #      : (SCP-2232, "Birdphone. Think Different.")
     729    :     "SCP-2232",


    # 730  : SCP-1306
    #      : (SCP-1306, "Potion of Summon Bird")
     730    :     "SCP-1306",


    # 731  : SCP-1184
    #      : (SCP-1184, "Truth")
     731    :     "SCP-1184",


    # 732  : SCP-1523
    #      : (SCP-1523, "Soul Brother")
     732    :     "SCP-1523",


    # 733  : SCP-1047
    #      : (SCP-1047, "Vengefully Ironic Street Signs")
     733    :     "SCP-1047",


    # 734  : SCP-602
    #      : (SCP-602, "The Sculptor of SoHo")
     734    :     "SCP-602",


    # 735  : SCP-4007
    #      : (SCP-4007, "Kagemusha")
     735    :     "SCP-4007",


    # 736  : SCP-323
    #      : (SCP-323, "Wendigo Skull")
     736    :     "SCP-323",


    # 737  : SCP-877
    #      : (SCP-877, "University Microchips")
     737    :     "SCP-877",


    # 738  : SCP-4231
    #      : (SCP-4231, "The Montauk House")
     738    :     "SCP-4231",


    # 739  : SCP-2610
    #      : (SCP-2610, "Procreation")
     739    :     "SCP-2610",


    # 740  : SCP-4069
    #      : (SCP-4069, "Out of Range")
     740    :     "SCP-4069",


    # 741  : SCP-2076
    #      : (SCP-2076, ""Shooting Yourself Can Increase Your Bullet Resistance"")
     741    :     "SCP-2076",


    # 742  : SCP-2703
    #      : (SCP-2703, "For a Good Time Call")
     742    :     "SCP-2703",


    # 743  : SCP-1899
    #      : (SCP-1899, "Suspended Bullet")
     743    :     "SCP-1899",


    # 744  : SCP-988
    #      : (SCP-988, "Unopenable Chest")
     744    :     "SCP-988",


    # 745  : SCP-4465
    #      : (SCP-4465, "No Man is an Island")
     745    :     "SCP-4465",


    # 746  : SCP-4011
    #      : (SCP-4011, "History is Written by the Victors")
     746    :     "SCP-4011",


    # 747  : SCP-783
    #      : (SCP-783, "There Was A Crooked Man")
     747    :     "SCP-783",


    # 748  : SCP-3288
    #      : (SCP-3288, "The Aristocrats")
     748    :     "SCP-3288",


    # 749  : SCP-2472
    #      : (SCP-2472, "A Small Metal Air Coupler That Is Apparently Not Anomalous")
     749    :     "SCP-2472",


    # 750  : SCP-147
    #      : (SCP-147, "Anachronistic Television")
     750    :     "SCP-147",


    # 751  : SCP-4950
    #      : (SCP-4950, "Triple Six Five Forked Tongue")
     751    :     "SCP-4950",


    # 752  : SCP-1372
    #      : (SCP-1372, "The Utter West")
     752    :     "SCP-1372",


    # 753  : SCP-335
    #      : (SCP-335, "One Hundred and Fifty 3.5" Floppy Disks")
     753    :     "SCP-335",


    # 754  : SCP-3562
    #      : (SCP-3562, "See Me After Class")
     754    :     "SCP-3562",


    # 755  : SCP-3989
    #      : (SCP-3989, "The Bone Orchard")
     755    :     "SCP-3989",


    # 756  : SCP-715
    #      : (SCP-715, "My Face That I May Be")
     756    :     "SCP-715",


    # 757  : SCP-2170
    #      : (SCP-2170, "The Clown Vaccine")
     757    :     "SCP-2170",


    # 758  : SCP-3052
    #      : (SCP-3052, "Disturbed")
     758    :     "SCP-3052",


    # 759  : SCP-1864
    #      : (SCP-1864, "The Lonely Liar")
     759    :     "SCP-1864",


    # 760  : SCP-122
    #      : (SCP-122, "No More Monsters")
     760    :     "SCP-122",


    # 761  : SCP-330
    #      : (SCP-330, "Take Only Two")
     761    :     "SCP-330",


    # 762  : SCP-3780
    #      : (SCP-3780, "Who Shot J.F.K.?")
     762    :     "SCP-3780",



    # from: http://www.scpwiki.com/highest-rated-scps/p/9


    # 763  : SCP-2951
    #      : (SCP-2951, "10,000 Years")
     763    :     "SCP-2951",


    # 764  : SCP-2031
    #      : (SCP-2031, "Ant farm")
     764    :     "SCP-2031",


    # 765  : SCP-1985
    #      : (SCP-1985, "Recovered K-Class Scenario Research Device")
     765    :     "SCP-1985",


    # 766  : SCP-3848
    #      : (SCP-3848, "History Exists for the Memorable")
     766    :     "SCP-3848",


    # 767  : SCP-3319
    #      : (SCP-3319, "The Clusterfuckalypse")
     767    :     "SCP-3319",


    # 768  : SCP-3049
    #      : (SCP-3049, "To Make an Apple Pie from Scratch")
     768    :     "SCP-3049",


    # 769  : SCP-3145
    #      : (SCP-3145, "Self-Insert")
     769    :     "SCP-3145",


    # 770  : SCP-046
    #      : (SCP-046, ""Predatory" Holly Bush")
     770    :     "SCP-046",


    # 771  : SCP-599
    #      : (SCP-599, "Uncharted City")
     771    :     "SCP-599",


    # 772  : SCP-230
    #      : (SCP-230, "The Gayest Man Alive")
     772    :     "SCP-230",


    # 773  : SCP-3890
    #      : (SCP-3890, "Forget-Me-Not")
     773    :     "SCP-3890",


    # 774  : SCP-2886
    #      : (SCP-2886, "Planet-Hopping Volcano")
     774    :     "SCP-2886",


    # 775  : SCP-6327-J [OMITTED]
     775    :     None,


    # 776  : SCP-1122
    #      : (SCP-1122, "The House of Tomorrow")
     776    :     "SCP-1122",


    # 777  : SCP-2762
    #      : (SCP-2762, "Moon Snakes")
     777    :     "SCP-2762",


    # 778  : SCP-1376
    #      : (SCP-1376, "Documentary Camcorder")
     778    :     "SCP-1376",


    # 779  : SCP-1543
    #      : (SCP-1543, "Efrain's Dialtone")
     779    :     "SCP-1543",


    # 780  : SCP-670
    #      : (SCP-670, "Family of Cotton")
     780    :     "SCP-670",


    # 781  : SCP-312
    #      : (SCP-312, "Atmospheric Jellyfish")
     781    :     "SCP-312",


    # 782  : SCP-081
    #      : (SCP-081, "Spontaneous Combustion Virus")
     782    :     "SCP-081",


    # 783  : SCP-2268
    #      : (SCP-2268, "Loaf Page")
     783    :     "SCP-2268",


    # 784  : SCP-2712
    #      : (SCP-2712, "The Entry for SCP-2712 in the Foundation Database")
     784    :     "SCP-2712",


    # 785  : SCP-2095
    #      : (SCP-2095, "The Siege of Gyaros")
     785    :     "SCP-2095",


    # 786  : SCP-2070
    #      : (SCP-2070, "The Fingers of God")
     786    :     "SCP-2070",


    # 787  : SCP-1850
    #      : (SCP-1850, "Accipiter sopwithii")
     787    :     "SCP-1850",


    # 788  : SCP-3494
    #      : (SCP-3494, "Waste Management by dado")
     788    :     "SCP-3494",


    # 789  : SCP-2308
    #      : (SCP-2308, "Futures Trading")
     789    :     "SCP-2308",


    # 790  : SCP-2305
    #      : (SCP-2305, "great ideas that are TOTALY USELESS (lulz)")
     790    :     "SCP-2305",


    # 791  : SCP-1561
    #      : (SCP-1561, "The Tyrant's Pretext")
     791    :     "SCP-1561",


    # 792  : SCP-039
    #      : (SCP-039, "Proboscis Engineers")
     792    :     "SCP-039",


    # 793  : SCP-206
    #      : (SCP-206, "The Voyager")
     793    :     "SCP-206",


    # 794  : SCP-3396
    #      : (SCP-3396, "The Empyrean Parasite")
     794    :     "SCP-3396",


    # 795  : SCP-2107
    #      : (SCP-2107, "Diet Ghost™")
     795    :     "SCP-2107",


    # 796  : SCP-909
    #      : (SCP-909, "Mr. Forgetful")
     796    :     "SCP-909",


    # 797  : SCP-735
    #      : (SCP-735, "Insult Box")
     797    :     "SCP-735",


    # 798  : SCP-034
    #      : (SCP-034, "Obsidian Ritual Knife")
     798    :     "SCP-034",


    # 799  : SCP-5000-J [OMITTED]
     799    :     None,


    # 800  : SCP-1781
    #      : (SCP-1781, "The Moonlight Theater")
     800    :     "SCP-1781",


    # 801  : SCP-784
    #      : (SCP-784, "Christmas Cheer")
     801    :     "SCP-784",


    # 802  : SCP-1046
    #      : (SCP-1046, "A House Without a Bedroom")
     802    :     "SCP-1046",


    # 803  : SCP-1474
    #      : (SCP-1474, "In Solidarity with Xiu Lidao, Great Sage, Equal of Heaven")
     803    :     "SCP-1474",


    # 804  : SCP-1841-EX [OMITTED]
    # 804  : SCP-1841
    #      : (SCP-1841, "So Much To See, So Much Unseen")
     804    :     "SCP-1841",


    # 805  : SCP-110
    #      : (SCP-110, "Subterranean City")
     805    :     "SCP-110",


    # 806  : SCP-1763-EX [OMITTED]
    # 806  : SCP-1763
    # 806  : (SCP-1763 "Found Space Theatre")
     806    :     "SCP-1763",


    # 807  : SCP-437
    #      : (SCP-437, "Summer of '91")
     807    :     "SCP-437",


    # 808  : SCP-696
    #      : (SCP-696, "Abyssal Typewriter")
     808    :     "SCP-696",


    # 809  : SCP-1512
    #      : (SCP-1512, "Irrational Root")
     809    :     "SCP-1512",


    # 810  : SCP-155
    #      : (SCP-155, "Infinite Speed Computer")
     810    :     "SCP-155",


    # 811  : SCP-478
    #      : (SCP-478, "Tooth Fairies")
     811    :     "SCP-478",


    # 812  : SCP-2481
    #      : (SCP-2481, "Kill the Suns")
     812    :     "SCP-2481",


    # 813  : SCP-2701
    #      : (SCP-2701, "True Solitary")
     813    :     "SCP-2701",


    # 814  : SCP-242
    #      : (SCP-242, "Self "Cleaning" Pool")
     814    :     "SCP-242",


    # 815  : SCP-044
    #      : (SCP-044, "World War II Era Molecular-Fission Cannon")
     815    :     "SCP-044",


    # 816  : SCP-043
    #      : (SCP-043, "The Beatle")
     816    :     "SCP-043",


    # 817  : SCP-5545
    #      : (SCP-5545, "𝙰 𝙱 𝙽 𝙾 𝚁 𝙼 𝙰 𝙻 𝙸 𝚃 𝚈")
     817    :     "SCP-5545",


    # 818  : SCP-3133
    #      : (SCP-3133, "An Email to O5-05")
     818    :     "SCP-3133",


    # 819  : SCP-2553
    #      : (SCP-2553, "Juridical Person")
     819    :     "SCP-2553",


    # 820  : SCP-911
    #      : (SCP-911, "Egyptian Book of the Dead")
     820    :     "SCP-911",


    # 821  : SCP-2664
    #      : (SCP-2664, "Redline")
     821    :     "SCP-2664",


    # 822  : SCP-2412
    #      : (SCP-2412, "Cassandra Bot")
     822    :     "SCP-2412",


    # 823  : SCP-1329
    #      : (SCP-1329, "The Aquarium")
     823    :     "SCP-1329",


    # 824  : SCP-1008
    #      : (SCP-1008, "Exile Stone")
     824    :     "SCP-1008",


    # 825  : SCP-374
    #      : (SCP-374, "Oracular Guillotine")
     825    :     "SCP-374",


    # 826  : SCP-5131
    #      : (SCP-5131, "D-13131")
     826    :     "SCP-5131",


    # 827  : SCP-013-J [OMITTED]
     827    :     None,


    # 828  : SCP-2408
    #      : (SCP-2408, "Orok's Fall")
     828    :     "SCP-2408",


    # 829  : SCP-554
    #      : (SCP-554, "The Perfect Murder")
     829    :     "SCP-554",


    # 830  : SCP-1156
    #      : (SCP-1156, "Wellington the Wonder Horse")
     830    :     "SCP-1156",


    # 831  : SCP-363
    #      : (SCP-363, "Not Centipedes")
     831    :     "SCP-363",


    # 832  : SCP-138
    #      : (SCP-138, "The Ever-Living Man")
     832    :     "SCP-138",


    # 833  : SCP-5983
    #      : (SCP-5983, "Nuke York, Nuke York")
     833    :     "SCP-5983",


    # 834  : SCP-1176
    #      : (SCP-1176, "Mellified Man")
     834    :     "SCP-1176",


    # 835  : SCP-1076
    #      : (SCP-1076, "The Only Child")
     835    :     "SCP-1076",


    # 836  : SCP-1364
    #      : (SCP-1364, "Ultra-Vulnerable Mammal")
     836    :     "SCP-1364",


    # 837  : SCP-713
    #      : (SCP-713, "Click Anywhere Computer")
     837    :     "SCP-713",


    # 838  : SCP-807
    #      : (SCP-807, "Heart Attack on a Plate")
     838    :     "SCP-807",


    # 839  : SCP-5935
    #      : (SCP-5935, "Blood and the Breaking of My Heart")
     839    :     "SCP-5935",


    # 840  : SCP-1753
    #      : (SCP-1753, "Vertigo")
     840    :     "SCP-1753",


    # 841  : SCP-022-J [OMITTED]
     841    :     None,


    # 842  : SCP-1007
    #      : (SCP-1007, "Mr. Life and Mr. Death")
     842    :     "SCP-1007",


    # 843  : SCP-095
    #      : (SCP-095, "The Atomic Adventures of Ronnie Ray-Gun")
     843    :     "SCP-095",


    # 844  : SCP-Big [OMITTED]
     844    :     None,


    # 845  : SCP-4321
    #      : (SCP-4321, "Sometimes I Look At The Sky So I Can Feel Small")
     845    :     "SCP-4321",


    # 846  : SCP-3054
    #      : (SCP-3054, "Cragstaff Sanitarium")
     846    :     "SCP-3054",


    # 847  : SCP-2912
    #      : (SCP-2912, "Clowny Clown Clown")
     847    :     "SCP-2912",


    # 848  : SCP-2112
    #      : (SCP-2112, "And the Meek Shall Inherit the Earth")
     848    :     "SCP-2112",


    # 849  : SCP-1514
    #      : (SCP-1514, "Star Wars")
     849    :     "SCP-1514",


    # 850  : SCP-505
    #      : (SCP-505, "Ink Stain")
     850    :     "SCP-505",


    # 851  : SCP-4949
    #      : (SCP-4949, "Dr. Wondertainment's dr playtime kit for the kiddostm ft. dado")
     851    :     "SCP-4949",


    # 852  : SCP-3449
    #      : (SCP-3449, "The Things Left Unsaid")
     852    :     "SCP-3449",


    # 853  : SCP-3838
    #      : (SCP-3838, "Nomads of the 4th-Dimensional Steppe")
     853    :     "SCP-3838",


    # 854  : SCP-2987
    #      : (SCP-2987, "Invictus")
     854    :     "SCP-2987",


    # 855  : SCP-2622
    #      : (SCP-2622, "Ambassador from the Mole People")
     855    :     "SCP-2622",


    # 856  : SCP-1030
    #      : (SCP-1030, "Anything Golem")
     856    :     "SCP-1030",


    # 857  : SCP-795
    #      : (SCP-795, "Reality-Bending Cat")
     857    :     "SCP-795",


    # 858  : SCP-3220
    #      : (SCP-3220, "Panopticon II")
     858    :     "SCP-3220",


    # 859  : SCP-7000-J [OMITTED]
     859    :     None,



    # from: http://www.scpwiki.com/highest-rated-scps/p/10


    # 860  : SCP-885-J [OMITTED]
     860    :     None,


    # 861  : SCP-353
    #      : (SCP-353, ""Vector"")
     861    :     "SCP-353",


    # 862  : SCP-4645
    #      : (SCP-4645, "Blackmailing Computer")
     862    :     "SCP-4645",


    # 863  : SCP-3127
    #      : (SCP-3127, "Nineteen Year Old Jessica Lambert And A Female Pig Of Abnormal Size, Forever")
     863    :     "SCP-3127",


    # 864  : SCP-3031
    #      : (SCP-3031, "Future Gift")
     864    :     "SCP-3031",


    # 865  : SCP-1478
    #      : (SCP-1478, "Inconveniently Stereotypical Cacti")
     865    :     "SCP-1478",


    # 866  : SCP-1235
    #      : (SCP-1235, "Atlas Microcosm")
     866    :     "SCP-1235",


    # 867  : SCP-1947
    #      : (SCP-1947, "Emission Sphere")
     867    :     "SCP-1947",


    # 868  : SCP-124
    #      : (SCP-124, "Fertile Soil")
     868    :     "SCP-124",


    # 869  : SCP-5149
    #      : (SCP-5149, "None of us are blind, Joe.")
     869    :     "SCP-5149",


    # 870  : SCP-3689
    #      : (SCP-3689, "Legendary Sandwich of the Deep")
     870    :     "SCP-3689",


    # 871  : SCP-2306
    #      : (SCP-2306, "Revenant AI")
     871    :     "SCP-2306",


    # 872  : SCP-2271
    #      : (SCP-2271, "Factory Loans")
     872    :     "SCP-2271",


    # 873  : SCP-157
    #      : (SCP-157, "Mimetic Predator")
     873    :     "SCP-157",


    # 874  : SCP-5040
    #      : (SCP-5040, "血の涙 ("Tears of Blood")")
     874    :     "SCP-5040",


    # 875  : SCP-4266
    #      : (SCP-4266, "The Thing That Makes You Kill People")
     875    :     "SCP-4266",


    # 876  : SCP-3737
    #      : (SCP-3737, "Rainbow Bridge")
     876    :     "SCP-3737",


    # 877  : SCP-900-J [OMITTED]
     877    :     None,


    # 878  : SCP-1142
    #      : (SCP-1142, "A Cry for Help")
     878    :     "SCP-1142",


    # 879  : SCP-𝕐
    #      : (SCP-5789, "SCP-𝕐 - Cannibalistic Mathematics")
     879    :     "SCP-5789",


    # 880  : SCP-5832
    #      : (SCP-5832, "Stained")
     880    :     "SCP-5832",


    # 881  : SCP-2679
    #      : (SCP-2679, "The Many Graves of Jeannette Parslov")
     881    :     "SCP-2679",


    # 882  : SCP-3637
    #      : (SCP-3637, "Many Waters")
     882    :     "SCP-3637",


    # 883  : SCP-3883
    #      : (SCP-3883, "Dildos Have Dreams Too")
     883    :     "SCP-3883",


    # 884  : SCP-1003
    #      : (SCP-1003, "Tapeworm Child")
     884    :     "SCP-1003",


    # 885  : SCP-5423
    #      : (SCP-5423, "The Empty Room")
     885    :     "SCP-5423",


    # 886  : SCP-051
    #      : (SCP-051, "Japanese Obstetrical Model")
     886    :     "SCP-051",


    # 887  : SCP-3880
    #      : (SCP-3880, " - ILLEST RAIN SOUNDS ∞ Hours No Looping - White Noise, Nature/Healing/Ambient, Meditation/Insomnia/Study ASMR [ORIGINAL]")
     887    :     "SCP-3880",


    # 888  : SCP-3733
    #      : (SCP-3733, "Everybody Else")
     888    :     "SCP-3733",


    # 889  : SCP-2221
    #      : (SCP-2221, "A Friendly Agreement")
     889    :     "SCP-2221",


    # 890  : SCP-2197
    #      : (SCP-2197, "Shop Class")
     890    :     "SCP-2197",


    # 891  : SCP-1487
    #      : (SCP-1487, "Beautiful Bones")
     891    :     "SCP-1487",


    # 892  : SCP-1207
    #      : (SCP-1207, "Not a Mirror")
     892    :     "SCP-1207",


    # 893  : SCP-121
    #      : (SCP-121, "Concrete Cradle")
     893    :     "SCP-121",


    # 894  : SCP-644
    #      : (SCP-644, "Mr. Hot")
     894    :     "SCP-644",


    # 895  : SCP-2816
    #      : (SCP-2816, "Nuclear Forgery")
     895    :     "SCP-2816",


    # 896  : SCP-132
    #      : (SCP-132, "Broken Desert")
     896    :     "SCP-132",


    # 897  : SCP-3885
    #      : (SCP-3885, "The High-Octane Full-Throttle Adventures of the Exploding Zombie Gearheads")
     897    :     "SCP-3885",


    # 898  : SCP-1557
    #      : (SCP-1557, "Giraffe Hell")
     898    :     "SCP-1557",


    # 899  : SCP-1161
    #      : (SCP-1161, "How-To Book")
     899    :     "SCP-1161",


    # 900  : SCP-756
    #      : (SCP-756, "Miniature Solar System")
     900    :     "SCP-756",


    # 901  : SCP-4200
    #      : (SCP-4200, "The World, Idealized")
     901    :     "SCP-4200",


    # 902  : SCP-1132-J [OMITTED]
     902    :     None,


    # 903  : SCP-1356
    #      : (SCP-1356, "Rubber Ducky")
     903    :     "SCP-1356",


    # 904  : SCP-3667
    #      : (SCP-3667, "All's Well that Ends Hell")
     904    :     "SCP-3667",


    # 905  : SCP-2779
    #      : (SCP-2779, "Oinkers")
     905    :     "SCP-2779",


    # 906  : SCP-2960
    #      : (SCP-2960, "The Show MUST Go On…")
     906    :     "SCP-2960",


    # 907  : SCP-2089
    #      : (SCP-2089, "/john/")
     907    :     "SCP-2089",


    # 908  : SCP-1800
    #      : (SCP-1800, "The Minotaur")
     908    :     "SCP-1800",


    # 909  : SCP-225
    #      : (SCP-225, "Unstoppable and Immovable")
     909    :     "SCP-225",


    # 910  : SCP-136
    #      : (SCP-136, "Naked Doll")
     910    :     "SCP-136",


    # 911  : SCP-4192
    #      : (SCP-4192, "As Above")
     911    :     "SCP-4192",


    # 912  : SCP-4780
    #      : (SCP-4780, "Shrunk")
     912    :     "SCP-4780",


    # 913  : SCP-2776
    #      : (SCP-2776, "Mr. President")
     913    :     "SCP-2776",


    # 914  : SCP-1735
    #      : (SCP-1735, "Kind of Impenetrable Barrier")
     914    :     "SCP-1735",


    # 915  : SCP-1447
    #      : (SCP-1447, "Tulpa")
     915    :     "SCP-1447",


    # 916  : SCP-075
    #      : (SCP-075, "Corrosive Snail")
     916    :     "SCP-075",


    # 917  : SCP-5320
    #      : (SCP-5320, "The People's Church Of The Fish That Just Goes On Forever")
     917    :     "SCP-5320",


    # 918  : SCP-2632
    #      : (SCP-2632, "No Fury")
     918    :     "SCP-2632",


    # 919  : SCP-048-J [OMITTED]
     919    :     None,


    # 920  : SCP-2172
    #      : (SCP-2172, "This Light Never Turns Green")
     920    :     "SCP-2172",


    # 921  : SCP-466
    #      : (SCP-466, "Mobile Veins")
     921    :     "SCP-466",


    # 922  : SCP-5720
    #      : (SCP-5720, "Astronomically-Inclined Crane")
     922    :     "SCP-5720",


    # 923  : SCP-078-J [OMITTED]
     923    :     None,


    # 924  : SCP-596
    #      : (SCP-596, "Cursed Regeneration Statue")
     924    :     "SCP-596",


    # 925  : SCP-4494
    #      : (SCP-4494, "The Specter Fights For Justice! Fights For Justice!")
     925    :     "SCP-4494",


    # 926  : SCP-2540
    #      : (SCP-2540, "Time Lime")
     926    :     "SCP-2540",


    # 927  : SCP-2000-J [OMITTED]
     927    :     None,


    # 928  : SCP-4183
    #      : (SCP-4183, "Automatic Containment Procedures")
     928    :     "SCP-4183",


    # 929  : SCP-2304
    #      : (SCP-2304, ""Like This Image To Die Instantly"")
     929    :     "SCP-2304",


    # 930  : SCP-3000-EX [OMITTED]
     930    :     None,


    # 931  : SCP-1115
    #      : (SCP-1115, "Distant Early Warning")
     931    :     "SCP-1115",


    # 932  : SCP-607
    #      : (SCP-607, "Dorian the Grey Cat")
     932    :     "SCP-607",


    # 933  : SCP-2136
    #      : (SCP-2136, "An Utterly Driven Scientist")
     933    :     "SCP-2136",


    # 934  : SCP-1692
    #      : (SCP-1692, "Came Back Haunted")
     934    :     "SCP-1692",


    # 935  : SCP-1481
    #      : (SCP-1481, "Crack Genie")
     935    :     "SCP-1481",


    # 936  : SCP-1265
    #      : (SCP-1265, "The Mesozoic Preserve")
     936    :     "SCP-1265",


    # 937  : SCP-573
    #      : (SCP-573, "The Pied Pipe")
     937    :     "SCP-573",


    # 938  : SCP-094
    #      : (SCP-094, "Miniature Event Horizon")
     938    :     "SCP-094",


    # 939  : SCP-2941
    #      : (SCP-2941, "Do Not Eat or Inspire")
     939    :     "SCP-2941",


    # 940  : SCP-619
    #      : (SCP-619, "Lucky Jeans")
     940    :     "SCP-619",


    # 941  : SCP-1507
    #      : (SCP-1507, "Pink Flamingos")
     941    :     "SCP-1507",


    # 942  : SCP-1040
    #      : (SCP-1040, ""Daniel"")
     942    :     "SCP-1040",


    # 943  : SCP-100-J [OMITTED]
     943    :     None,


    # 944  : SCP-2902
    #      : (SCP-2902, "The Human Skeleton Closet (and his cat)")
     944    :     "SCP-2902",


    # 945  : SCP-1726
    #      : (SCP-1726, "The Library and the Pillar")
     945    :     "SCP-1726",


    # 946  : SCP-1922-J [OMITTED]
     946    :     None,


    # 947  : SCP-1005
    #      : (SCP-1005, "The Painted Man")
     947    :     "SCP-1005",


    # 948  : SCP-614
    #      : (SCP-614, "IP Address 57.32.███.███")
     948    :     "SCP-614",


    # 949  : SCP-516
    #      : (SCP-516, "Intelligent Tank")
     949    :     "SCP-516",


    # 950  : SCP-4634
    #      : (SCP-4634, "Out-of-Order")
     950    :     "SCP-4634",


    # 951  : SCP-2624
    #      : (SCP-2624, "Laika's Sweetheart Space-Beacon")
     951    :     "SCP-2624",


    # 952  : SCP-2040
    #      : (SCP-2040, "The Iron Messenger")
     952    :     "SCP-2040",


    # 953  : SCP-1728
    #      : (SCP-1728, "Buttery Decapitated Highwayman")
     953    :     "SCP-1728",


    # 954  : SCP-1441
    #      : (SCP-1441, "Cold Fusion Paper-Towel Dispenser")
     954    :     "SCP-1441",


    # 955  : SCP-5972-J [OMITTED]
     955    :     None,


    # 956  : SCP-786
    #      : (SCP-786, "Funnel Factor Twelve")
     956    :     "SCP-786",


    # 957  : SCP-3117
    #      : (SCP-3117, "A Monster-Shaped Hole")
     957    :     "SCP-3117",


    # 958  : SCP-2522
    #      : (SCP-2522, "hatbot.aic")
     958    :     "SCP-2522",

    }


# FULL VERSION, with popularity, name, and "to_use" attribute

# 482 SCPs in have a non-None 'containment' attribute.
# This is 50.31% of the 958 SCPS in POPULAR_SCPS_DICT (popular_scps.py).
# This is 8.81% of the 5470 SCPS in KNOWN_SCPS_DICT (objects.py).

POPULAR_SCPS_DICT_FULL = {

    # 001  : SCP-173
    #      : (SCP-173, "The Sculpture - The Original")
      1    :     {
      "name"                :   "SCP-173",
      "document_name"       :   "The Sculpture - The Original",
      "popularity"          :   1,
      "to_use"              :   1,
      },


    # 002  : None
    #      : (None, [OMITTED])
      2    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   2,
      "to_use"              :   0,
      },


    # 003  : SCP-049
    #      : (SCP-049, "Plague Doctor")
      3    :     {
      "name"                :   "SCP-049",
      "document_name"       :   "Plague Doctor",
      "popularity"          :   3,
      "to_use"              :   1,
      },


    # 004  : SCP-055
    #      : (SCP-055, "[unknown]")
      4    :     {
      "name"                :   "SCP-055",
      "document_name"       :   "[unknown]",
      "popularity"          :   4,
      "to_use"              :   1,
      },


    # 005  : SCP-087
    #      : (SCP-087, "The Stairwell")
      5    :     {
      "name"                :   "SCP-087",
      "document_name"       :   "The Stairwell",
      "popularity"          :   5,
      "to_use"              :   1,
      },


    # 006  : SCP-682
    #      : (SCP-682, "Hard-to-Destroy Reptile")
      6    :     {
      "name"                :   "SCP-682",
      "document_name"       :   "Hard-to-Destroy Reptile",
      "popularity"          :   6,
      "to_use"              :   1,
      },


    # 007  : SCP-096
    #      : (SCP-096, '''The "Shy Guy"''')
      7    :     {
      "name"                :   "SCP-096",
      "document_name"       :   '''The "Shy Guy"''',
      "popularity"          :   7,
      "to_use"              :   1,
      },


    # 008  : SCP-093
    #      : (SCP-093, "Red Sea Object")
      8    :     {
      "name"                :   "SCP-093",
      "document_name"       :   "Red Sea Object",
      "popularity"          :   8,
      "to_use"              :   1,
      },


    # 009  : SCP-106
    #      : (SCP-106, "The Old Man")
      9    :     {
      "name"                :   "SCP-106",
      "document_name"       :   "The Old Man",
      "popularity"          :   9,
      "to_use"              :   1,
      },


    # 010  : SCP-914
    #      : (SCP-914, "The Clockworks")
      10    :     {
      "name"                :   "SCP-914",
      "document_name"       :   "The Clockworks",
      "popularity"          :   10,
      "to_use"              :   1,
      },


    # 011  : SCP-3008
    #      : (SCP-3008, "A Perfectly Normal, Regular Old IKEA")
      11    :     {
      "name"                :   "SCP-3008",
      "document_name"       :   "A Perfectly Normal, Regular Old IKEA",
      "popularity"          :   11,
      "to_use"              :   0,
      },


    # 012  : SCP-426
    #      : (SCP-426, "I am a Toaster")
      12    :     {
      "name"                :   "SCP-426",
      "document_name"       :   "I am a Toaster",
      "popularity"          :   12,
      "to_use"              :   1,
      },


    # 013  : SCP-999
    #      : (SCP-999, "The Tickle Monster")
      13    :     {
      "name"                :   "SCP-999",
      "document_name"       :   "The Tickle Monster",
      "popularity"          :   13,
      "to_use"              :   1,
      },


    # 014  : SCP-231
    #      : (SCP-231, "Special Personnel Requirements")
      14    :     {
      "name"                :   "SCP-231",
      "document_name"       :   "Special Personnel Requirements",
      "popularity"          :   14,
      "to_use"              :   1,
      },


    # 015  : SCP-2317
    #      : (SCP-2317, "A Door to Another World")
      15    :     {
      "name"                :   "SCP-2317",
      "document_name"       :   "A Door to Another World",
      "popularity"          :   15,
      "to_use"              :   1,
      },


    # 016  : SCP-1981
    #      : (SCP-1981, '''"RONALD REAGAN CUT UP WHILE TALKING"''')
      16    :     {
      "name"                :   "SCP-1981",
      "document_name"       :   '''"RONALD REAGAN CUT UP WHILE TALKING"''',
      "popularity"          :   16,
      "to_use"              :   1,
      },


    # 017  : SCP-1730
    #      : (SCP-1730, "What Happened to Site-13?")
      17    :     {
      "name"                :   "SCP-1730",
      "document_name"       :   "What Happened to Site-13?",
      "popularity"          :   17,
      "to_use"              :   0,
      },


    # 018  : SCP-3999
    #      : (SCP-3999, "I Am At The Center of Everything That Happens To Me")
      18    :     {
      "name"                :   "SCP-3999",
      "document_name"       :   "I Am At The Center of Everything That Happens To Me",
      "popularity"          :   18,
      "to_use"              :   1,
      },


    # 019  : SCP-5000
    #      : (SCP-5000, "Why?")
      19    :     {
      "name"                :   "SCP-5000",
      "document_name"       :   "Why?",
      "popularity"          :   19,
      "to_use"              :   1,
      },


    # 020  : SCP-3000
    #      : (SCP-3000, "Ananteshesha")
      20    :     {
      "name"                :   "SCP-3000",
      "document_name"       :   "Ananteshesha",
      "popularity"          :   20,
      "to_use"              :   0,
      },


    # 021  : SCP-3001
    #      : (SCP-3001, "Red Reality")
      21    :     {
      "name"                :   "SCP-3001",
      "document_name"       :   "Red Reality",
      "popularity"          :   21,
      "to_use"              :   0,
      },


    # 022  : SCP-2000
    #      : (SCP-2000, "Deus Ex Machina")
      22    :     {
      "name"                :   "SCP-2000",
      "document_name"       :   "Deus Ex Machina",
      "popularity"          :   22,
      "to_use"              :   0,
      },


    # 023  : SCP-4999
    #      : (SCP-4999, "Someone to Watch Over Us")
      23    :     {
      "name"                :   "SCP-4999",
      "document_name"       :   "Someone to Watch Over Us",
      "popularity"          :   23,
      "to_use"              :   0,
      },


    # 024  : SCP-294
    #      : (SCP-294, "The Coffee Machine")
      24    :     {
      "name"                :   "SCP-294",
      "document_name"       :   "The Coffee Machine",
      "popularity"          :   24,
      "to_use"              :   1,
      },


    # 025  : SCP-895
    #      : (SCP-895, "Camera Disruption")
      25    :     {
      "name"                :   "SCP-895",
      "document_name"       :   "Camera Disruption",
      "popularity"          :   25,
      "to_use"              :   1,
      },


    # 026  : SCP-1171
    #      : (SCP-1171, "Humans Go Home")
      26    :     {
      "name"                :   "SCP-1171",
      "document_name"       :   "Humans Go Home",
      "popularity"          :   26,
      "to_use"              :   0,
      },


    # 027  : SCP-1000
    #      : (SCP-1000, "Bigfoot")
      27    :     {
      "name"                :   "SCP-1000",
      "document_name"       :   "Bigfoot",
      "popularity"          :   27,
      "to_use"              :   0,
      },


    # 028  : SCP-2935
    #      : (SCP-2935, "O, Death")
      28    :     {
      "name"                :   "SCP-2935",
      "document_name"       :   "O, Death",
      "popularity"          :   28,
      "to_use"              :   0,
      },


    # 029  : SCP-902
    #      : (SCP-902, "The Final Countdown")
      29    :     {
      "name"                :   "SCP-902",
      "document_name"       :   "The Final Countdown",
      "popularity"          :   29,
      "to_use"              :   1,
      },


    # 030  : None
    #      : (None, [OMITTED])
      30    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   30,
      "to_use"              :   0,
      },


    # 031  : SCP-035
    #      : (SCP-035, "Possessive Mask")
      31    :     {
      "name"                :   "SCP-035",
      "document_name"       :   "Possessive Mask",
      "popularity"          :   31,
      "to_use"              :   1,
      },


    # 032  : SCP-002
    #      : (SCP-002, '''The "Living" Room''')
      32    :     {
      "name"                :   "SCP-002",
      "document_name"       :   '''The "Living" Room''',
      "popularity"          :   32,
      "to_use"              :   1,
      },


    # 033  : SCP-1733
    #      : (SCP-1733, "Season Opener")
      33    :     {
      "name"                :   "SCP-1733",
      "document_name"       :   "Season Opener",
      "popularity"          :   33,
      "to_use"              :   1,
      },


    # 034  : SCP-2006
    #      : (SCP-2006, "Too Spooky")
      34    :     {
      "name"                :   "SCP-2006",
      "document_name"       :   "Too Spooky",
      "popularity"          :   34,
      "to_use"              :   1,
      },


    # 035  : SCP-701
    #      : (SCP-701, "The Hanged King's Tragedy")
      35    :     {
      "name"                :   "SCP-701",
      "document_name"       :   "The Hanged King's Tragedy",
      "popularity"          :   35,
      "to_use"              :   1,
      },


    # 036  : None
    #      : (None, [OMITTED])
      36    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   36,
      "to_use"              :   0,
      },


    # 037  : SCP-610
    #      : (SCP-610, "The Flesh That Hates")
      37    :     {
      "name"                :   "SCP-610",
      "document_name"       :   "The Flesh That Hates",
      "popularity"          :   37,
      "to_use"              :   0,
      },


    # 038  : SCP-076
    #      : (SCP-076, '''"Able"''')
      38    :     {
      "name"                :   "SCP-076",
      "document_name"       :   '''"Able"''',
      "popularity"          :   38,
      "to_use"              :   1,
      },


    # 039  : SCP-085
    #      : (SCP-085, "Hand-drawn 'Cassy'")
      39    :     {
      "name"                :   "SCP-085",
      "document_name"       :   "Hand-drawn 'Cassy'",
      "popularity"          :   39,
      "to_use"              :   1,
      },


    # 040  : SCP-1048
    #      : (SCP-1048, "Builder Bear")
      40    :     {
      "name"                :   "SCP-1048",
      "document_name"       :   "Builder Bear",
      "popularity"          :   40,
      "to_use"              :   1,
      },


    # 041  : SCP-140
    #      : (SCP-140, "An Incomplete Chronicle")
      41    :     {
      "name"                :   "SCP-140",
      "document_name"       :   "An Incomplete Chronicle",
      "popularity"          :   41,
      "to_use"              :   1,
      },


    # 042  : SCP-507
    #      : (SCP-507, "Reluctant Dimension Hopper")
      42    :     {
      "name"                :   "SCP-507",
      "document_name"       :   "Reluctant Dimension Hopper",
      "popularity"          :   42,
      "to_use"              :   1,
      },


    # 043  : SCP-354
    #      : (SCP-354, "The Red Pool")
      43    :     {
      "name"                :   "SCP-354",
      "document_name"       :   "The Red Pool",
      "popularity"          :   43,
      "to_use"              :   0,
      },


    # 044  : SCP-990
    #      : (SCP-990, "Dream Man")
      44    :     {
      "name"                :   "SCP-990",
      "document_name"       :   "Dream Man",
      "popularity"          :   44,
      "to_use"              :   0,
      },


    # 045  : SCP-993
    #      : (SCP-993, "Bobble the Clown")
      45    :     {
      "name"                :   "SCP-993",
      "document_name"       :   "Bobble the Clown",
      "popularity"          :   45,
      "to_use"              :   0,
      },


    # 046  : SCP-1230
    #      : (SCP-1230, "A Hero is Born")
      46    :     {
      "name"                :   "SCP-1230",
      "document_name"       :   "A Hero is Born",
      "popularity"          :   46,
      "to_use"              :   1,
      },


    # 047  : SCP-2316
    #      : (SCP-2316, "Field Trip")
      47    :     {
      "name"                :   "SCP-2316",
      "document_name"       :   "Field Trip",
      "popularity"          :   47,
      "to_use"              :   0,
      },


    # 048  : SCP-2030
    #      : (SCP-2030, "LA U GH IS F UN")
      48    :     {
      "name"                :   "SCP-2030",
      "document_name"       :   "LA U GH IS F UN",
      "popularity"          :   48,
      "to_use"              :   0,
      },


    # 049  : SCP-1471
    #      : (SCP-1471, "MalO ver1.0.0")
      49    :     {
      "name"                :   "SCP-1471",
      "document_name"       :   "MalO ver1.0.0",
      "popularity"          :   49,
      "to_use"              :   0,
      },


    # 050  : SCP-1370
    #      : (SCP-1370, "Pesterbot")
      50    :     {
      "name"                :   "SCP-1370",
      "document_name"       :   "Pesterbot",
      "popularity"          :   50,
      "to_use"              :   1,
      },


    # 051  : SCP-348
    #      : (SCP-348, "A Gift from Dad")
      51    :     {
      "name"                :   "SCP-348",
      "document_name"       :   "A Gift from Dad",
      "popularity"          :   51,
      "to_use"              :   1,
      },


    # 052  : SCP-963
    #      : (SCP-963, "Immortality")
      52    :     {
      "name"                :   "SCP-963",
      "document_name"       :   "Immortality",
      "popularity"          :   52,
      "to_use"              :   1,
      },


    # 053  : SCP-2662
    #      : (SCP-2662, "Cthulhu f'UCK OFF!")
      53    :     {
      "name"                :   "SCP-2662",
      "document_name"       :   "Cthulhu f'UCK OFF!",
      "popularity"          :   53,
      "to_use"              :   1,
      },


    # 054  : SCP-079
    #      : (SCP-079, "Old AI")
      54    :     {
      "name"                :   "SCP-079",
      "document_name"       :   "Old AI",
      "popularity"          :   54,
      "to_use"              :   1,
      },


    # 055  : SCP-1762
    #      : (SCP-1762, "Where The Dragons Went")
      55    :     {
      "name"                :   "SCP-1762",
      "document_name"       :   "Where The Dragons Went",
      "popularity"          :   55,
      "to_use"              :   1,
      },


    # 056  : None
    #      : (None, [OMITTED])
      56    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   56,
      "to_use"              :   0,
      },


    # 057  : SCP-1983
    #      : (SCP-1983, "Doorway to Nowhere")
      57    :     {
      "name"                :   "SCP-1983",
      "document_name"       :   "Doorway to Nowhere",
      "popularity"          :   57,
      "to_use"              :   0,
      },


    # 058  : SCP-048
    #      : (SCP-048, "The Cursed SCP Number")
      58    :     {
      "name"                :   "SCP-048",
      "document_name"       :   "The Cursed SCP Number",
      "popularity"          :   58,
      "to_use"              :   0,
      },


    # 059  : SCP-2998
    #      : (SCP-2998, "Anomalous Transmission, 2485 MHz")
      59    :     {
      "name"                :   "SCP-2998",
      "document_name"       :   "Anomalous Transmission, 2485 MHz",
      "popularity"          :   59,
      "to_use"              :   0,
      },


    # 060  : SCP-1440
    #      : (SCP-1440, "The Old Man from Nowhere")
      60    :     {
      "name"                :   "SCP-1440",
      "document_name"       :   "The Old Man from Nowhere",
      "popularity"          :   60,
      "to_use"              :   0,
      },


    # 061  : SCP-1437
    #      : (SCP-1437, "A Hole to Another Place")
      61    :     {
      "name"                :   "SCP-1437",
      "document_name"       :   "A Hole to Another Place",
      "popularity"          :   61,
      "to_use"              :   0,
      },


    # 062  : SCP-1425
    #      : (SCP-1425, "Star Signals")
      62    :     {
      "name"                :   "SCP-1425",
      "document_name"       :   "Star Signals",
      "popularity"          :   62,
      "to_use"              :   1,
      },


    # 063  : SCP-1893
    #      : (SCP-1893, "The Minotaur's Tale")
      63    :     {
      "name"                :   "SCP-1893",
      "document_name"       :   "The Minotaur's Tale",
      "popularity"          :   63,
      "to_use"              :   0,
      },


    # 064  : SCP-2718
    #      : (SCP-2718, "What Happens After")
      64    :     {
      "name"                :   "SCP-2718",
      "document_name"       :   "What Happens After",
      "popularity"          :   64,
      "to_use"              :   0,
      },


    # 065  : SCP-504
    #      : (SCP-504, "Critical Tomatoes")
      65    :     {
      "name"                :   "SCP-504",
      "document_name"       :   "Critical Tomatoes",
      "popularity"          :   65,
      "to_use"              :   1,
      },


    # 066  : SCP-3930
    #      : (SCP-3930, "The Pattern Screamer")
      66    :     {
      "name"                :   "SCP-3930",
      "document_name"       :   "The Pattern Screamer",
      "popularity"          :   66,
      "to_use"              :   0,
      },


    # 067  : SCP-184
    #      : (SCP-184, "The Architect")
      67    :     {
      "name"                :   "SCP-184",
      "document_name"       :   "The Architect",
      "popularity"          :   67,
      "to_use"              :   0,
      },


    # 068  : SCP-028
    #      : (SCP-028, "Knowledge")
      68    :     {
      "name"                :   "SCP-028",
      "document_name"       :   "Knowledge",
      "popularity"          :   68,
      "to_use"              :   0,
      },


    # 069  : SCP-1867
    #      : (SCP-1867, "A Gentleman")
      69    :     {
      "name"                :   "SCP-1867",
      "document_name"       :   "A Gentleman",
      "popularity"          :   69,
      "to_use"              :   1,
      },


    # 070  : SCP-073
    #      : (SCP-073, '''"Cain"''')
      70    :     {
      "name"                :   "SCP-073",
      "document_name"       :   '''"Cain"''',
      "popularity"          :   70,
      "to_use"              :   1,
      },


    # 071  : SCP-871
    #      : (SCP-871, "Self-Replacing Cake")
      71    :     {
      "name"                :   "SCP-871",
      "document_name"       :   "Self-Replacing Cake",
      "popularity"          :   71,
      "to_use"              :   1,
      },


    # 072  : SCP-004
    #      : (SCP-004, "The 12 Rusty Keys and the Door")
      72    :     {
      "name"                :   "SCP-004",
      "document_name"       :   "The 12 Rusty Keys and the Door",
      "popularity"          :   72,
      "to_use"              :   1,
      },


    # 073  : SCP-5999
    #      : (SCP-5999, "This is Where I Died")
      73    :     {
      "name"                :   "SCP-5999",
      "document_name"       :   "This is Where I Died",
      "popularity"          :   73,
      "to_use"              :   0,
      },


    # 074  : SCP-1322
    #      : (SCP-1322, "Glory Hole")
      74    :     {
      "name"                :   "SCP-1322",
      "document_name"       :   "Glory Hole",
      "popularity"          :   74,
      "to_use"              :   1,
      },


    # 075  : SCP-343
    #      : (SCP-343, '''"God"''')
      75    :     {
      "name"                :   "SCP-343",
      "document_name"       :   '''"God"''',
      "popularity"          :   75,
      "to_use"              :   1,
      },


    # 076  : SCP-2439
    #      : (SCP-2439, "[SLOT UNALLOCATED]")
      76    :     {
      "name"                :   "SCP-2439",
      "document_name"       :   "[SLOT UNALLOCATED]",
      "popularity"          :   76,
      "to_use"              :   0,
      },


    # 077  : None
    #      : (None, [OMITTED])
      77    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   77,
      "to_use"              :   0,
      },


    # 078  : None
    #      : (None, [OMITTED])
      78    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   78,
      "to_use"              :   0,
      },


    # 079  : SCP-500
    #      : (SCP-500, "Panacea")
      79    :     {
      "name"                :   "SCP-500",
      "document_name"       :   "Panacea",
      "popularity"          :   79,
      "to_use"              :   1,
      },


    # 080  : SCP-1609
    #      : (SCP-1609, "The Remains of a Chair")
      80    :     {
      "name"                :   "SCP-1609",
      "document_name"       :   "The Remains of a Chair",
      "popularity"          :   80,
      "to_use"              :   1,
      },


    # 081  : None
    #      : (None, [OMITTED])
      81    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   81,
      "to_use"              :   0,
      },


    # 082  : SCP-529
    #      : (SCP-529, "Josie the Half-Cat")
      82    :     {
      "name"                :   "SCP-529",
      "document_name"       :   "Josie the Half-Cat",
      "popularity"          :   82,
      "to_use"              :   1,
      },


    # 083  : None
    #      : (None, [OMITTED])
      83    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   83,
      "to_use"              :   0,
      },


    # 084  : SCP-1342
    #      : (SCP-1342, "To the Makers of Music")
      84    :     {
      "name"                :   "SCP-1342",
      "document_name"       :   "To the Makers of Music",
      "popularity"          :   84,
      "to_use"              :   1,
      },


    # 085  : SCP-882
    #      : (SCP-882, "A Machine")
      85    :     {
      "name"                :   "SCP-882",
      "document_name"       :   "A Machine",
      "popularity"          :   85,
      "to_use"              :   1,
      },


    # 086  : SCP-1678
    #      : (SCP-1678, "UnLondon")
      86    :     {
      "name"                :   "SCP-1678",
      "document_name"       :   "UnLondon",
      "popularity"          :   86,
      "to_use"              :   0,
      },


    # 087  : None
    #      : (None, [OMITTED])
      87    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   87,
      "to_use"              :   0,
      },


    # 088  : SCP-4666
    #      : (SCP-4666, "The Yule Man")
      88    :     {
      "name"                :   "SCP-4666",
      "document_name"       :   "The Yule Man",
      "popularity"          :   88,
      "to_use"              :   0,
      },


    # 089  : SCP-586
    #      : (SCP-586, "Inscribable Object")
      89    :     {
      "name"                :   "SCP-586",
      "document_name"       :   "Inscribable Object",
      "popularity"          :   89,
      "to_use"              :   1,
      },


    # 090  : SCP-015
    #      : (SCP-015, "Pipe Nightmare")
      90    :     {
      "name"                :   "SCP-015",
      "document_name"       :   "Pipe Nightmare",
      "popularity"          :   90,
      "to_use"              :   0,
      },


    # 091  : SCP-3002
    #      : (SCP-3002, "Attempts to Assassinate Thought")
      91    :     {
      "name"                :   "SCP-3002",
      "document_name"       :   "Attempts to Assassinate Thought",
      "popularity"          :   91,
      "to_use"              :   0,
      },


    # 092  : SCP-3333
    #      : (SCP-3333, "Tower")
      92    :     {
      "name"                :   "SCP-3333",
      "document_name"       :   "Tower",
      "popularity"          :   92,
      "to_use"              :   0,
      },


    # 093  : None
    #      : (None, [OMITTED])
      93    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   93,
      "to_use"              :   0,
      },


    # 094  : SCP-5031
    #      : (SCP-5031, "Yet Another Murder Monster")
      94    :     {
      "name"                :   "SCP-5031",
      "document_name"       :   "Yet Another Murder Monster",
      "popularity"          :   94,
      "to_use"              :   1,
      },


    # 095  : None
    #      : (None, [OMITTED])
      95    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   95,
      "to_use"              :   0,
      },


    # 096  : SCP-3125
    #      : (SCP-3125, "The Escapee")
      96    :     {
      "name"                :   "SCP-3125",
      "document_name"       :   "The Escapee",
      "popularity"          :   96,
      "to_use"              :   0,
      },


    # 097  : SCP-261
    #      : (SCP-261, "Pan-Dimensional Vending")
      97    :     {
      "name"                :   "SCP-261",
      "document_name"       :   "Pan-Dimensional Vending",
      "popularity"          :   97,
      "to_use"              :   1,
      },


    # 098  : SCP-662
    #      : (SCP-662, "Butler's Hand Bell")
      98    :     {
      "name"                :   "SCP-662",
      "document_name"       :   "Butler's Hand Bell",
      "popularity"          :   98,
      "to_use"              :   1,
      },


    # 099  : SCP-186
    #      : (SCP-186, "To End All Wars")
      99    :     {
      "name"                :   "SCP-186",
      "document_name"       :   "To End All Wars",
      "popularity"          :   99,
      "to_use"              :   0,
      },


    # 100  : SCP-1504
    #      : (SCP-1504, "Joe Schmo")
      100    :     {
      "name"                :   "SCP-1504",
      "document_name"       :   "Joe Schmo",
      "popularity"          :   100,
      "to_use"              :   1,
      },


    # 101  : SCP-3393
    #      : (SCP-3393, "For Your Eyes Only")
      101    :     {
      "name"                :   "SCP-3393",
      "document_name"       :   "For Your Eyes Only",
      "popularity"          :   101,
      "to_use"              :   0,
      },


    # 102  : None
    #      : (None, [OMITTED])
      102    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   102,
      "to_use"              :   0,
      },


    # 103  : None
    #      : (None, [OMITTED])
      103    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   103,
      "to_use"              :   0,
      },


    # 104  : SCP-131
    #      : (SCP-131, '''The "Eye Pods"''')
      104    :     {
      "name"                :   "SCP-131",
      "document_name"       :   '''The "Eye Pods"''',
      "popularity"          :   104,
      "to_use"              :   1,
      },


    # 105  : SCP-169
    #      : (SCP-169, "The Leviathan")
      105    :     {
      "name"                :   "SCP-169",
      "document_name"       :   "The Leviathan",
      "popularity"          :   105,
      "to_use"              :   0,
      },


    # 106  : SCP-4001
    #      : (SCP-4001, "Alexandria Eternal")
      106    :     {
      "name"                :   "SCP-4001",
      "document_name"       :   "Alexandria Eternal",
      "popularity"          :   106,
      "to_use"              :   0,
      },


    # 107  : SCP-179
    #      : (SCP-179, "Sauelsuesor")
      107    :     {
      "name"                :   "SCP-179",
      "document_name"       :   "Sauelsuesor",
      "popularity"          :   107,
      "to_use"              :   0,
      },


    # 108  : SCP-2295
    #      : (SCP-2295, "The Bear with a Heart of Patchwork")
      108    :     {
      "name"                :   "SCP-2295",
      "document_name"       :   "The Bear with a Heart of Patchwork",
      "popularity"          :   108,
      "to_use"              :   1,
      },


    # 109  : SCP-835
    #      : (SCP-835, "Expunged Data Released")
      109    :     {
      "name"                :   "SCP-835",
      "document_name"       :   "Expunged Data Released",
      "popularity"          :   109,
      "to_use"              :   0,
      },


    # 110  : SCP-4444
    #      : (SCP-4444, "Bush v. Gore")
      110    :     {
      "name"                :   "SCP-4444",
      "document_name"       :   "Bush v. Gore",
      "popularity"          :   110,
      "to_use"              :   0,
      },


    # 111  : SCP-008
    #      : (SCP-008, "Zombie Plague")
      111    :     {
      "name"                :   "SCP-008",
      "document_name"       :   "Zombie Plague",
      "popularity"          :   111,
      "to_use"              :   1,
      },


    # 112  : None
    #      : (None, [OMITTED])
      112    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   112,
      "to_use"              :   0,
      },


    # 113  : SCP-1193
    #      : (SCP-1193, "Buried Giant")
      113    :     {
      "name"                :   "SCP-1193",
      "document_name"       :   "Buried Giant",
      "popularity"          :   113,
      "to_use"              :   0,
      },


    # 114  : SCP-2399
    #      : (SCP-2399, "A Malfunctioning Destroyer")
      114    :     {
      "name"                :   "SCP-2399",
      "document_name"       :   "A Malfunctioning Destroyer",
      "popularity"          :   114,
      "to_use"              :   0,
      },


    # 115  : SCP-939
    #      : (SCP-939, "With Many Voices")
      115    :     {
      "name"                :   "SCP-939",
      "document_name"       :   "With Many Voices",
      "popularity"          :   115,
      "to_use"              :   1,
      },


    # 116  : SCP-1875
    #      : (SCP-1875, "Antique Chess Computer")
      116    :     {
      "name"                :   "SCP-1875",
      "document_name"       :   "Antique Chess Computer",
      "popularity"          :   116,
      "to_use"              :   1,
      },


    # 117  : SCP-513
    #      : (SCP-513, "A Cowbell")
      117    :     {
      "name"                :   "SCP-513",
      "document_name"       :   "A Cowbell",
      "popularity"          :   117,
      "to_use"              :   1,
      },


    # 118  : SCP-4991
    #      : (SCP-4991, ">So this is how the world ends. Not with a bang, but with a shitpost.")
      118    :     {
      "name"                :   "SCP-4991",
      "document_name"       :   ">So this is how the world ends. Not with a bang, but with a shitpost.",
      "popularity"          :   118,
      "to_use"              :   0,
      },


    # 119  : SCP-1470
    #      : (SCP-1470, "Telepathic Spider")
      119    :     {
      "name"                :   "SCP-1470",
      "document_name"       :   "Telepathic Spider",
      "popularity"          :   119,
      "to_use"              :   1,
      },


    # 120  : SCP-3003
    #      : (SCP-3003, "The End of History")
      120    :     {
      "name"                :   "SCP-3003",
      "document_name"       :   "The End of History",
      "popularity"          :   120,
      "to_use"              :   0,
      },


    # 121  : SCP-017
    #      : (SCP-017, "Shadow Person")
      121    :     {
      "name"                :   "SCP-017",
      "document_name"       :   "Shadow Person",
      "popularity"          :   121,
      "to_use"              :   1,
      },


    # 122  : None
    #      : (None, [OMITTED])
      122    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   122,
      "to_use"              :   0,
      },


    # 123  : SCP-342
    #      : (SCP-342, "A Ticket to Ride")
      123    :     {
      "name"                :   "SCP-342",
      "document_name"       :   "A Ticket to Ride",
      "popularity"          :   123,
      "to_use"              :   1,
      },


    # 124  : SCP-3199
    #      : (SCP-3199, "Humans, Refuted")
      124    :     {
      "name"                :   "SCP-3199",
      "document_name"       :   "Humans, Refuted",
      "popularity"          :   124,
      "to_use"              :   1,
      },


    # 125  : SCP-1545
    #      : (SCP-1545, "Larry the Loving Llama")
      125    :     {
      "name"                :   "SCP-1545",
      "document_name"       :   "Larry the Loving Llama",
      "popularity"          :   125,
      "to_use"              :   1,
      },


    # 126  : SCP-066
    #      : (SCP-066, "Eric's Toy")
      126    :     {
      "name"                :   "SCP-066",
      "document_name"       :   "Eric's Toy",
      "popularity"          :   126,
      "to_use"              :   1,
      },


    # 127  : SCP-1689
    #      : (SCP-1689, "Bag of Holding Potatoes")
      127    :     {
      "name"                :   "SCP-1689",
      "document_name"       :   "Bag of Holding Potatoes",
      "popularity"          :   127,
      "to_use"              :   1,
      },


    # 128  : SCP-053
    #      : (SCP-053, "Young Girl")
      128    :     {
      "name"                :   "SCP-053",
      "document_name"       :   "Young Girl",
      "popularity"          :   128,
      "to_use"              :   1,
      },


    # 129  : SCP-1173
    #      : (SCP-1173, "The Islamic Republic of Eastern Samothrace")
      129    :     {
      "name"                :   "SCP-1173",
      "document_name"       :   "The Islamic Republic of Eastern Samothrace",
      "popularity"          :   129,
      "to_use"              :   0,
      },


    # 130  : SCP-447
    #      : (SCP-447, "Ball of Green Slime")
      130    :     {
      "name"                :   "SCP-447",
      "document_name"       :   "Ball of Green Slime",
      "popularity"          :   130,
      "to_use"              :   1,
      },


    # 131  : SCP-105
    #      : (SCP-105, "Iris")
      131    :     {
      "name"                :   "SCP-105",
      "document_name"       :   "Iris",
      "popularity"          :   131,
      "to_use"              :   1,
      },


    # 132  : SCP-3939
    #      : (SCP-3939, "[NUMBER RESERVED; AWAITING RESEARCHER]")
      132    :     {
      "name"                :   "SCP-3939",
      "document_name"       :   "[NUMBER RESERVED; AWAITING RESEARCHER]",
      "popularity"          :   132,
      "to_use"              :   0,
      },


    # 133  : SCP-3007
    #      : (SCP-3007, "World of Two Artists")
      133    :     {
      "name"                :   "SCP-3007",
      "document_name"       :   "World of Two Artists",
      "popularity"          :   133,
      "to_use"              :   0,
      },


    # 134  : SCP-423
    #      : (SCP-423, "Self-Inserting Character")
      134    :     {
      "name"                :   "SCP-423",
      "document_name"       :   "Self-Inserting Character",
      "popularity"          :   134,
      "to_use"              :   0,
      },


    # 135  : None
    #      : (None, [OMITTED])
      135    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   135,
      "to_use"              :   0,
      },


    # 136  : SCP-738
    #      : (SCP-738, "The Devil's Deal")
      136    :     {
      "name"                :   "SCP-738",
      "document_name"       :   "The Devil's Deal",
      "popularity"          :   136,
      "to_use"              :   1,
      },


    # 137  : SCP-1295
    #      : (SCP-1295, "Meg's Diner")
      137    :     {
      "name"                :   "SCP-1295",
      "document_name"       :   "Meg's Diner",
      "popularity"          :   137,
      "to_use"              :   0,
      },


    # 138  : SCP-1057
    #      : (SCP-1057, "Absence of Shark")
      138    :     {
      "name"                :   "SCP-1057",
      "document_name"       :   "Absence of Shark",
      "popularity"          :   138,
      "to_use"              :   1,
      },


    # 139  : SCP-058
    #      : (SCP-058, "Heart of Darkness")
      139    :     {
      "name"                :   "SCP-058",
      "document_name"       :   "Heart of Darkness",
      "popularity"          :   139,
      "to_use"              :   1,
      },


    # 140  : SCP-303
    #      : (SCP-303, "The Doorman")
      140    :     {
      "name"                :   "SCP-303",
      "document_name"       :   "The Doorman",
      "popularity"          :   140,
      "to_use"              :   1,
      },


    # 141  : SCP-1025
    #      : (SCP-1025, "Encyclopedia of Diseases")
      141    :     {
      "name"                :   "SCP-1025",
      "document_name"       :   "Encyclopedia of Diseases",
      "popularity"          :   141,
      "to_use"              :   1,
      },


    # 142  : SCP-387
    #      : (SCP-387, "Living Lego")
      142    :     {
      "name"                :   "SCP-387",
      "document_name"       :   "Living Lego",
      "popularity"          :   142,
      "to_use"              :   1,
      },


    # 143  : SCP-009
    #      : (SCP-009, "Red Ice")
      143    :     {
      "name"                :   "SCP-009",
      "document_name"       :   "Red Ice",
      "popularity"          :   143,
      "to_use"              :   1,
      },


    # 144  : SCP-217
    #      : (SCP-217, "The Clockwork Virus")
      144    :     {
      "name"                :   "SCP-217",
      "document_name"       :   "The Clockwork Virus",
      "popularity"          :   144,
      "to_use"              :   1,
      },


    # 145  : SCP-1004
    #      : (SCP-1004, "Factory Porn")
      145    :     {
      "name"                :   "SCP-1004",
      "document_name"       :   "Factory Porn",
      "popularity"          :   145,
      "to_use"              :   1,
      },


    # 146  : SCP-1958
    #      : (SCP-1958, "Magic Bus")
      146    :     {
      "name"                :   "SCP-1958",
      "document_name"       :   "Magic Bus",
      "popularity"          :   146,
      "to_use"              :   0,
      },


    # 147  : None
    #      : (None, [OMITTED])
      147    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   147,
      "to_use"              :   0,
      },


    # 148  : SCP-2557
    #      : (SCP-2557, "A Holding of Envelope Logistics®")
      148    :     {
      "name"                :   "SCP-2557",
      "document_name"       :   "A Holding of Envelope Logistics®",
      "popularity"          :   148,
      "to_use"              :   0,
      },


    # 149  : SCP-024
    #      : (SCP-024, "Game Show of Death")
      149    :     {
      "name"                :   "SCP-024",
      "document_name"       :   "Game Show of Death",
      "popularity"          :   149,
      "to_use"              :   0,
      },


    # 150  : SCP-1959
    #      : (SCP-1959, "The Lost Cosmonaut")
      150    :     {
      "name"                :   "SCP-1959",
      "document_name"       :   "The Lost Cosmonaut",
      "popularity"          :   150,
      "to_use"              :   1,
      },


    # 151  : None
    #      : (None, [OMITTED])
      151    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   151,
      "to_use"              :   0,
      },


    # 152  : SCP-014
    #      : (SCP-014, "The Concrete Man")
      152    :     {
      "name"                :   "SCP-014",
      "document_name"       :   "The Concrete Man",
      "popularity"          :   152,
      "to_use"              :   1,
      },


    # 153  : SCP-966
    #      : (SCP-966, "Sleep Killer")
      153    :     {
      "name"                :   "SCP-966",
      "document_name"       :   "Sleep Killer",
      "popularity"          :   153,
      "to_use"              :   1,
      },


    # 154  : SCP-012
    #      : (SCP-012, "A Bad Composition")
      154    :     {
      "name"                :   "SCP-012",
      "document_name"       :   "A Bad Composition",
      "popularity"          :   154,
      "to_use"              :   1,
      },


    # 155  : SCP-3213
    #      : (SCP-3213, "F*ck off Carl.")
      155    :     {
      "name"                :   "SCP-3213",
      "document_name"       :   "F*ck off Carl.",
      "popularity"          :   155,
      "to_use"              :   1,
      },


    # 156  : None
    #      : (None, [OMITTED])
      156    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   156,
      "to_use"              :   0,
      },


    # 157  : SCP-804
    #      : (SCP-804, "World Without Man")
      157    :     {
      "name"                :   "SCP-804",
      "document_name"       :   "World Without Man",
      "popularity"          :   157,
      "to_use"              :   0,
      },


    # 158  : SCP-3301
    #      : (SCP-3301, "THE FOUNDATION")
      158    :     {
      "name"                :   "SCP-3301",
      "document_name"       :   "THE FOUNDATION",
      "popularity"          :   158,
      "to_use"              :   1,
      },


    # 159  : SCP-089
    #      : (SCP-089, "Tophet")
      159    :     {
      "name"                :   "SCP-089",
      "document_name"       :   "Tophet",
      "popularity"          :   159,
      "to_use"              :   1,
      },


    # 160  : SCP-2950
    #      : (SCP-2950, "Just A Chair")
      160    :     {
      "name"                :   "SCP-2950",
      "document_name"       :   "Just A Chair",
      "popularity"          :   160,
      "to_use"              :   1,
      },


    # 161  : SCP-033
    #      : (SCP-033, "The Missing Number")
      161    :     {
      "name"                :   "SCP-033",
      "document_name"       :   "The Missing Number",
      "popularity"          :   161,
      "to_use"              :   1,
      },


    # 162  : SCP-2003
    #      : (SCP-2003, "Preferred Option")
      162    :     {
      "name"                :   "SCP-2003",
      "document_name"       :   "Preferred Option",
      "popularity"          :   162,
      "to_use"              :   0,
      },


    # 163  : None
    #      : (None, [OMITTED])
      163    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   163,
      "to_use"              :   0,
      },


    # 164  : SCP-2875
    #      : (SCP-2875, "The Town That Got Fucked By Bears")
      164    :     {
      "name"                :   "SCP-2875",
      "document_name"       :   "The Town That Got Fucked By Bears",
      "popularity"          :   164,
      "to_use"              :   0,
      },


    # 165  : SCP-3519
    #      : (SCP-3519, "These Quiet Days")
      165    :     {
      "name"                :   "SCP-3519",
      "document_name"       :   "These Quiet Days",
      "popularity"          :   165,
      "to_use"              :   0,
      },


    # 166  : SCP-3671
    #      : (SCP-3671, "A Very Angry Box of Cereal")
      166    :     {
      "name"                :   "SCP-3671",
      "document_name"       :   "A Very Angry Box of Cereal",
      "popularity"          :   166,
      "to_use"              :   1,
      },


    # 167  : SCP-003
    #      : (SCP-003, "Biological Motherboard")
      167    :     {
      "name"                :   "SCP-003",
      "document_name"       :   "Biological Motherboard",
      "popularity"          :   167,
      "to_use"              :   1,
      },


    # 168  : SCP-439
    #      : (SCP-439, "Bone Hive")
      168    :     {
      "name"                :   "SCP-439",
      "document_name"       :   "Bone Hive",
      "popularity"          :   168,
      "to_use"              :   1,
      },


    # 169  : SCP-2747
    #      : (SCP-2747, "As Below, So Above")
      169    :     {
      "name"                :   "SCP-2747",
      "document_name"       :   "As Below, So Above",
      "popularity"          :   169,
      "to_use"              :   0,
      },


    # 170  : None
    #      : (None, [OMITTED])
      170    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   170,
      "to_use"              :   0,
      },


    # 171  : SCP-2599
    #      : (SCP-2599, "Not Good Enough")
      171    :     {
      "name"                :   "SCP-2599",
      "document_name"       :   "Not Good Enough",
      "popularity"          :   171,
      "to_use"              :   1,
      },


    # 172  : SCP-3740
    #      : (SCP-3740, "God Is Dumb")
      172    :     {
      "name"                :   "SCP-3740",
      "document_name"       :   "God Is Dumb",
      "popularity"          :   172,
      "to_use"              :   1,
      },


    # 173  : SCP-111
    #      : (SCP-111, "Dragon-Snails™")
      173    :     {
      "name"                :   "SCP-111",
      "document_name"       :   "Dragon-Snails™",
      "popularity"          :   173,
      "to_use"              :   1,
      },


    # 174  : SCP-1055
    #      : (SCP-1055, "Bugsy")
      174    :     {
      "name"                :   "SCP-1055",
      "document_name"       :   "Bugsy",
      "popularity"          :   174,
      "to_use"              :   0,
      },


    # 175  : SCP-2137
    #      : (SCP-2137, "The Forensic Ghost Of Tupac Shakur")
      175    :     {
      "name"                :   "SCP-2137",
      "document_name"       :   "The Forensic Ghost Of Tupac Shakur",
      "popularity"          :   175,
      "to_use"              :   1,
      },


    # 176  : SCP-176
    #      : (SCP-176, "Observable Time Loop")
      176    :     {
      "name"                :   "SCP-176",
      "document_name"       :   "Observable Time Loop",
      "popularity"          :   176,
      "to_use"              :   0,
      },


    # 177  : SCP-2682
    #      : (SCP-2682, "The Blind Idiot")
      177    :     {
      "name"                :   "SCP-2682",
      "document_name"       :   "The Blind Idiot",
      "popularity"          :   177,
      "to_use"              :   0,
      },


    # 178  : SCP-191
    #      : (SCP-191, "Cyborg Child")
      178    :     {
      "name"                :   "SCP-191",
      "document_name"       :   "Cyborg Child",
      "popularity"          :   178,
      "to_use"              :   1,
      },


    # 179  : SCP-2264
    #      : (SCP-2264, "In the Court of Alagadda")
      179    :     {
      "name"                :   "SCP-2264",
      "document_name"       :   "In the Court of Alagadda",
      "popularity"          :   179,
      "to_use"              :   0,
      },


    # 180  : None
    #      : (None, [OMITTED])
      180    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   180,
      "to_use"              :   0,
      },


    # 181  : SCP-016
    #      : (SCP-016, "Sentient Micro-Organism")
      181    :     {
      "name"                :   "SCP-016",
      "document_name"       :   "Sentient Micro-Organism",
      "popularity"          :   181,
      "to_use"              :   1,
      },


    # 182  : SCP-239
    #      : (SCP-239, "The Witch Child")
      182    :     {
      "name"                :   "SCP-239",
      "document_name"       :   "The Witch Child",
      "popularity"          :   182,
      "to_use"              :   1,
      },


    # 183  : SCP-168
    #      : (SCP-168, "Sentient Calculator")
      183    :     {
      "name"                :   "SCP-168",
      "document_name"       :   "Sentient Calculator",
      "popularity"          :   183,
      "to_use"              :   1,
      },


    # 184  : SCP-962
    #      : (SCP-962, "Tower of Babble")
      184    :     {
      "name"                :   "SCP-962",
      "document_name"       :   "Tower of Babble",
      "popularity"          :   184,
      "to_use"              :   0,
      },


    # 185  : None
    #      : (None, [OMITTED])
      185    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   185,
      "to_use"              :   0,
      },


    # 186  : SCP-022
    #      : (SCP-022, "The Morgue")
      186    :     {
      "name"                :   "SCP-022",
      "document_name"       :   "The Morgue",
      "popularity"          :   186,
      "to_use"              :   0,
      },


    # 187  : SCP-3034
    #      : (SCP-3034, "The Counting Station")
      187    :     {
      "name"                :   "SCP-3034",
      "document_name"       :   "The Counting Station",
      "popularity"          :   187,
      "to_use"              :   0,
      },


    # 188  : SCP-2357
    #      : (SCP-2357, "The Perfect SCP")
      188    :     {
      "name"                :   "SCP-2357",
      "document_name"       :   "The Perfect SCP",
      "popularity"          :   188,
      "to_use"              :   0,
      },


    # 189  : SCP-1050
    #      : (SCP-1050, "Obsidian Obelisk of Warning")
      189    :     {
      "name"                :   "SCP-1050",
      "document_name"       :   "Obsidian Obelisk of Warning",
      "popularity"          :   189,
      "to_use"              :   1,
      },


    # 190  : SCP-1499
    #      : (SCP-1499, "The Gas Mask")
      190    :     {
      "name"                :   "SCP-1499",
      "document_name"       :   "The Gas Mask",
      "popularity"          :   190,
      "to_use"              :   1,
      },


    # 191  : SCP-2852
    #      : (SCP-2852, "Cousin Johnny")
      191    :     {
      "name"                :   "SCP-2852",
      "document_name"       :   "Cousin Johnny",
      "popularity"          :   191,
      "to_use"              :   0,
      },


    # 192  : SCP-2740
    #      : (SCP-2740, "It Wasn't There")
      192    :     {
      "name"                :   "SCP-2740",
      "document_name"       :   "It Wasn't There",
      "popularity"          :   192,
      "to_use"              :   0,
      },


    # 193  : SCP-1459
    #      : (SCP-1459, "The Puppy Machine")
      193    :     {
      "name"                :   "SCP-1459",
      "document_name"       :   "The Puppy Machine",
      "popularity"          :   193,
      "to_use"              :   1,
      },


    # 194  : SCP-2719
    #      : (SCP-2719, "Inside")
      194    :     {
      "name"                :   "SCP-2719",
      "document_name"       :   "Inside",
      "popularity"          :   194,
      "to_use"              :   0,
      },


    # 195  : SCP-2256
    #      : (SCP-2256, "Very Tall Things")
      195    :     {
      "name"                :   "SCP-2256",
      "document_name"       :   "Very Tall Things",
      "popularity"          :   195,
      "to_use"              :   0,
      },


    # 196  : SCP-1006
    #      : (SCP-1006, "Spider Proletariat")
      196    :     {
      "name"                :   "SCP-1006",
      "document_name"       :   "Spider Proletariat",
      "popularity"          :   196,
      "to_use"              :   0,
      },


    # 197  : SCP-2337
    #      : (SCP-2337, '''"Dr. Spanko"''')
      197    :     {
      "name"                :   "SCP-2337",
      "document_name"       :   '''"Dr. Spanko"''',
      "popularity"          :   197,
      "to_use"              :   1,
      },


    # 198  : SCP-2669
    #      : (SCP-2669, "Khevtuul 1")
      198    :     {
      "name"                :   "SCP-2669",
      "document_name"       :   "Khevtuul 1",
      "popularity"          :   198,
      "to_use"              :   0,
      },


    # 199  : None
    #      : (None, [OMITTED])
      199    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   199,
      "to_use"              :   0,
      },


    # 200  : SCP-823
    #      : (SCP-823, "Carnival of Horrors")
      200    :     {
      "name"                :   "SCP-823",
      "document_name"       :   "Carnival of Horrors",
      "popularity"          :   200,
      "to_use"              :   0,
      },


    # 201  : SCP-811
    #      : (SCP-811, "Swamp Woman")
      201    :     {
      "name"                :   "SCP-811",
      "document_name"       :   "Swamp Woman",
      "popularity"          :   201,
      "to_use"              :   1,
      },


    # 202  : SCP-163
    #      : (SCP-163, "An Old Castaway")
      202    :     {
      "name"                :   "SCP-163",
      "document_name"       :   "An Old Castaway",
      "popularity"          :   202,
      "to_use"              :   1,
      },


    # 203  : SCP-1861
    #      : (SCP-1861, "The Crew of the HMS Wintersheimer")
      203    :     {
      "name"                :   "SCP-1861",
      "document_name"       :   "The Crew of the HMS Wintersheimer",
      "popularity"          :   203,
      "to_use"              :   0,
      },


    # 204  : SCP-884
    #      : (SCP-884, "A Shaving Mirror")
      204    :     {
      "name"                :   "SCP-884",
      "document_name"       :   "A Shaving Mirror",
      "popularity"          :   204,
      "to_use"              :   1,
      },


    # 205  : SCP-082
    #      : (SCP-082, '''"Fernand" the Cannibal''')
      205    :     {
      "name"                :   "SCP-082",
      "document_name"       :   '''"Fernand" the Cannibal''',
      "popularity"          :   205,
      "to_use"              :   1,
      },


    # 206  : SCP-946
    #      : (SCP-946, "A Formal Discussion")
      206    :     {
      "name"                :   "SCP-946",
      "document_name"       :   "A Formal Discussion",
      "popularity"          :   206,
      "to_use"              :   1,
      },


    # 207  : SCP-455
    #      : (SCP-455, "Cargo Ship")
      207    :     {
      "name"                :   "SCP-455",
      "document_name"       :   "Cargo Ship",
      "popularity"          :   207,
      "to_use"              :   0,
      },


    # 208  : SCP-2952
    #      : (SCP-2952, "Conveyance Of Regional Gwerin Internationally")
      208    :     {
      "name"                :   "SCP-2952",
      "document_name"       :   "Conveyance Of Regional Gwerin Internationally",
      "popularity"          :   208,
      "to_use"              :   0,
      },


    # 209  : SCP-3211
    #      : (SCP-3211, "There is No Canon")
      209    :     {
      "name"                :   "SCP-3211",
      "document_name"       :   "There is No Canon",
      "popularity"          :   209,
      "to_use"              :   1,
      },


    # 210  : SCP-2111
    #      : (SCP-2111, "If You Can Read This…")
      210    :     {
      "name"                :   "SCP-2111",
      "document_name"       :   "If You Can Read This…",
      "popularity"          :   210,
      "to_use"              :   0,
      },


    # 211  : SCP-890
    #      : (SCP-890, "The Rocket Surgeon")
      211    :     {
      "name"                :   "SCP-890",
      "document_name"       :   "The Rocket Surgeon",
      "popularity"          :   211,
      "to_use"              :   1,
      },


    # 212  : SCP-086
    #      : (SCP-086, "The Office of Dr. [REDACTED]")
      212    :     {
      "name"                :   "SCP-086",
      "document_name"       :   "The Office of Dr. [REDACTED]",
      "popularity"          :   212,
      "to_use"              :   1,
      },


    # 213  : SCP-3309
    #      : (SCP-3309, "Where We Go When We Fade, Fade Away")
      213    :     {
      "name"                :   "SCP-3309",
      "document_name"       :   "Where We Go When We Fade, Fade Away",
      "popularity"          :   213,
      "to_use"              :   0,
      },


    # 214  : SCP-011
    #      : (SCP-011, "Sentient Civil War Memorial Statue")
      214    :     {
      "name"                :   "SCP-011",
      "document_name"       :   "Sentient Civil War Memorial Statue",
      "popularity"          :   214,
      "to_use"              :   0,
      },


    # 215  : SCP-1111
    #      : (SCP-1111, "The White Dog")
      215    :     {
      "name"                :   "SCP-1111",
      "document_name"       :   "The White Dog",
      "popularity"          :   215,
      "to_use"              :   0,
      },


    # 216  : None
    #      : (None, [OMITTED])
      216    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   216,
      "to_use"              :   0,
      },


    # 217  : SCP-321
    #      : (SCP-321, "Child of Man")
      217    :     {
      "name"                :   "SCP-321",
      "document_name"       :   "Child of Man",
      "popularity"          :   217,
      "to_use"              :   1,
      },


    # 218  : SCP-1422
    #      : (SCP-1422, "The Yellowstone Anomaly")
      218    :     {
      "name"                :   "SCP-1422",
      "document_name"       :   "The Yellowstone Anomaly",
      "popularity"          :   218,
      "to_use"              :   0,
      },


    # 219  : SCP-1968
    #      : (SCP-1968, "Global Retrocausality Torus")
      219    :     {
      "name"                :   "SCP-1968",
      "document_name"       :   "Global Retrocausality Torus",
      "popularity"          :   219,
      "to_use"              :   1,
      },


    # 220  : SCP-2639
    #      : (SCP-2639, "Video Game Violence")
      220    :     {
      "name"                :   "SCP-2639",
      "document_name"       :   "Video Game Violence",
      "popularity"          :   220,
      "to_use"              :   1,
      },


    # 221  : SCP-245
    #      : (SCP-245, "SCP-RPG")
      221    :     {
      "name"                :   "SCP-245",
      "document_name"       :   "SCP-RPG",
      "popularity"          :   221,
      "to_use"              :   1,
      },


    # 222  : SCP-3521
    #      : (SCP-3521, "Forced Banana Equivalent Dose by dado")
      222    :     {
      "name"                :   "SCP-3521",
      "document_name"       :   "Forced Banana Equivalent Dose by dado",
      "popularity"          :   222,
      "to_use"              :   1,
      },


    # 223  : SCP-970
    #      : (SCP-970, "The Recursive Room")
      223    :     {
      "name"                :   "SCP-970",
      "document_name"       :   "The Recursive Room",
      "popularity"          :   223,
      "to_use"              :   0,
      },


    # 224  : SCP-527
    #      : (SCP-527, "Mr. Fish")
      224    :     {
      "name"                :   "SCP-527",
      "document_name"       :   "Mr. Fish",
      "popularity"          :   224,
      "to_use"              :   1,
      },


    # 225  : SCP-1936
    #      : (SCP-1936, "Daleport")
      225    :     {
      "name"                :   "SCP-1936",
      "document_name"       :   "Daleport",
      "popularity"          :   225,
      "to_use"              :   0,
      },


    # 226  : SCP-1522
    #      : (SCP-1522, "Ships That Pass In The Night")
      226    :     {
      "name"                :   "SCP-1522",
      "document_name"       :   "Ships That Pass In The Night",
      "popularity"          :   226,
      "to_use"              :   0,
      },


    # 227  : None
    #      : (None, [OMITTED])
      227    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   227,
      "to_use"              :   0,
      },


    # 228  : SCP-524
    #      : (SCP-524, "Walter the Omnivorous Rabbit")
      228    :     {
      "name"                :   "SCP-524",
      "document_name"       :   "Walter the Omnivorous Rabbit",
      "popularity"          :   228,
      "to_use"              :   1,
      },


    # 229  : SCP-1986
    #      : (SCP-1986, "Imaginary Library")
      229    :     {
      "name"                :   "SCP-1986",
      "document_name"       :   "Imaginary Library",
      "popularity"          :   229,
      "to_use"              :   0,
      },


    # 230  : SCP-1192
    #      : (SCP-1192, '''"Timmy"''')
      230    :     {
      "name"                :   "SCP-1192",
      "document_name"       :   '''"Timmy"''',
      "popularity"          :   230,
      "to_use"              :   1,
      },


    # 231  : None
    #      : (None, [OMITTED])
      231    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   231,
      "to_use"              :   0,
      },


    # 232  : SCP-3300
    #      : (SCP-3300, "The Rain")
      232    :     {
      "name"                :   "SCP-3300",
      "document_name"       :   "The Rain",
      "popularity"          :   232,
      "to_use"              :   0,
      },


    # 233  : SCP-005
    #      : (SCP-005, "Skeleton Key")
      233    :     {
      "name"                :   "SCP-005",
      "document_name"       :   "Skeleton Key",
      "popularity"          :   233,
      "to_use"              :   1,
      },


    # 234  : None
    #      : (None, [OMITTED])
      234    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   234,
      "to_use"              :   0,
      },


    # 235  : SCP-1313
    #      : (SCP-1313, "Solve for Bear")
      235    :     {
      "name"                :   "SCP-1313",
      "document_name"       :   "Solve for Bear",
      "popularity"          :   235,
      "to_use"              :   0,
      },


    # 236  : SCP-3005
    #      : (SCP-3005, "A Light That Died")
      236    :     {
      "name"                :   "SCP-3005",
      "document_name"       :   "A Light That Died",
      "popularity"          :   236,
      "to_use"              :   0,
      },


    # 237  : SCP-427
    #      : (SCP-427, "Lovecraftian Locket")
      237    :     {
      "name"                :   "SCP-427",
      "document_name"       :   "Lovecraftian Locket",
      "popularity"          :   237,
      "to_use"              :   1,
      },


    # 238  : SCP-2217
    #      : (SCP-2217, "Hammer and Anvil")
      238    :     {
      "name"                :   "SCP-2217",
      "document_name"       :   "Hammer and Anvil",
      "popularity"          :   238,
      "to_use"              :   0,
      },


    # 239  : SCP-650
    #      : (SCP-650, "Startling Statue")
      239    :     {
      "name"                :   "SCP-650",
      "document_name"       :   "Startling Statue",
      "popularity"          :   239,
      "to_use"              :   1,
      },


    # 240  : SCP-5140
    #      : (SCP-5140, "EVEREST")
      240    :     {
      "name"                :   "SCP-5140",
      "document_name"       :   "EVEREST",
      "popularity"          :   240,
      "to_use"              :   0,
      },


    # 241  : SCP-2480
    #      : (SCP-2480, "An Unfinished Ritual")
      241    :     {
      "name"                :   "SCP-2480",
      "document_name"       :   "An Unfinished Ritual",
      "popularity"          :   241,
      "to_use"              :   0,
      },


    # 242  : SCP-1845
    #      : (SCP-1845, "Animal Kingdom")
      242    :     {
      "name"                :   "SCP-1845",
      "document_name"       :   "Animal Kingdom",
      "popularity"          :   242,
      "to_use"              :   1,
      },


    # 243  : SCP-732
    #      : (SCP-732, "The Fan-Fic Plague")
      243    :     {
      "name"                :   "SCP-732",
      "document_name"       :   "The Fan-Fic Plague",
      "popularity"          :   243,
      "to_use"              :   0,
      },


    # 244  : SCP-451
    #      : (SCP-451, "Mister Lonely")
      244    :     {
      "name"                :   "SCP-451",
      "document_name"       :   "Mister Lonely",
      "popularity"          :   244,
      "to_use"              :   0,
      },


    # 245  : SCP-4500
    #      : (SCP-4500, "Socratic Containment Procedures")
      245    :     {
      "name"                :   "SCP-4500",
      "document_name"       :   "Socratic Containment Procedures",
      "popularity"          :   245,
      "to_use"              :   0,
      },


    # 246  : SCP-3626
    #      : (SCP-3626, "Do Not Stop Reading This Document")
      246    :     {
      "name"                :   "SCP-3626",
      "document_name"       :   "Do Not Stop Reading This Document",
      "popularity"          :   246,
      "to_use"              :   1,
      },


    # 247  : SCP-457
    #      : (SCP-457, "Burning Man")
      247    :     {
      "name"                :   "SCP-457",
      "document_name"       :   "Burning Man",
      "popularity"          :   247,
      "to_use"              :   1,
      },


    # 248  : SCP-5001
    #      : (SCP-5001, "Sacrosanct")
      248    :     {
      "name"                :   "SCP-5001",
      "document_name"       :   "Sacrosanct",
      "popularity"          :   248,
      "to_use"              :   0,
      },


    # 249  : SCP-2700
    #      : (SCP-2700, "Teleforce")
      249    :     {
      "name"                :   "SCP-2700",
      "document_name"       :   "Teleforce",
      "popularity"          :   249,
      "to_use"              :   1,
      },


    # 250  : SCP-216
    #      : (SCP-216, "The Safe")
      250    :     {
      "name"                :   "SCP-216",
      "document_name"       :   "The Safe",
      "popularity"          :   250,
      "to_use"              :   1,
      },


    # 251  : SCP-152
    #      : (SCP-152, "Book of Endings")
      251    :     {
      "name"                :   "SCP-152",
      "document_name"       :   "Book of Endings",
      "popularity"          :   251,
      "to_use"              :   1,
      },


    # 252  : SCP-4960
    #      : (SCP-4960, "Why the Foundation Funded a Hentai to Awaken a Sumerian Love Goddess (or: How I Learned to Stop Worrying and Love Kedesh-Nanaya)")
      252    :     {
      "name"                :   "SCP-4960",
      "document_name"       :   "Why the Foundation Funded a Hentai to Awaken a Sumerian Love Goddess (or: How I Learned to Stop Worrying and Love Kedesh-Nanaya)",
      "popularity"          :   252,
      "to_use"              :   1,
      },


    # 253  : SCP-3900
    #      : (SCP-3900, "The Internet of Things That Are Wolves")
      253    :     {
      "name"                :   "SCP-3900",
      "document_name"       :   "The Internet of Things That Are Wolves",
      "popularity"          :   253,
      "to_use"              :   0,
      },


    # 254  : SCP-1032
    #      : (SCP-1032, "The Prediction Clock")
      254    :     {
      "name"                :   "SCP-1032",
      "document_name"       :   "The Prediction Clock",
      "popularity"          :   254,
      "to_use"              :   1,
      },


    # 255  : SCP-2053
    #      : (SCP-2053, "Paternal Rubik's Cube")
      255    :     {
      "name"                :   "SCP-2053",
      "document_name"       :   "Paternal Rubik's Cube",
      "popularity"          :   255,
      "to_use"              :   1,
      },


    # 256  : SCP-178
    #      : (SCP-178, '''"3-D" Specs''')
      256    :     {
      "name"                :   "SCP-178",
      "document_name"       :   '''"3-D" Specs''',
      "popularity"          :   256,
      "to_use"              :   1,
      },


    # 257  : SCP-5002
    #      : (SCP-5002, "A Death in Containment")
      257    :     {
      "name"                :   "SCP-5002",
      "document_name"       :   "A Death in Containment",
      "popularity"          :   257,
      "to_use"              :   1,
      },


    # 258  : SCP-453
    #      : (SCP-453, "Scripted Nightclub")
      258    :     {
      "name"                :   "SCP-453",
      "document_name"       :   "Scripted Nightclub",
      "popularity"          :   258,
      "to_use"              :   0,
      },


    # 259  : SCP-3004
    #      : (SCP-3004, "Imago")
      259    :     {
      "name"                :   "SCP-3004",
      "document_name"       :   "Imago",
      "popularity"          :   259,
      "to_use"              :   0,
      },


    # 260  : SCP-2273
    #      : (SCP-2273, "Major Alexei Belitrov, of the Red Army's 22nd Armored Infantry Division")
      260    :     {
      "name"                :   "SCP-2273",
      "document_name"       :   "Major Alexei Belitrov, of the Red Army's 22nd Armored Infantry Division",
      "popularity"          :   260,
      "to_use"              :   1,
      },


    # 261  : SCP-3078
    #      : (SCP-3078, "Cognitohazardous Shitpost")
      261    :     {
      "name"                :   "SCP-3078",
      "document_name"       :   "Cognitohazardous Shitpost",
      "popularity"          :   261,
      "to_use"              :   0,
      },


    # 262  : SCP-1281
    #      : (SCP-1281, "The Harbinger")
      262    :     {
      "name"                :   "SCP-1281",
      "document_name"       :   "The Harbinger",
      "popularity"          :   262,
      "to_use"              :   1,
      },


    # 263  : SCP-315
    #      : (SCP-315, "The Recorded Man")
      263    :     {
      "name"                :   "SCP-315",
      "document_name"       :   "The Recorded Man",
      "popularity"          :   263,
      "to_use"              :   1,
      },


    # 264  : SCP-3045
    #      : (SCP-3045, "bzzip.exe")
      264    :     {
      "name"                :   "SCP-3045",
      "document_name"       :   "bzzip.exe",
      "popularity"          :   264,
      "to_use"              :   1,
      },


    # 265  : SCP-038
    #      : (SCP-038, "The Everything Tree")
      265    :     {
      "name"                :   "SCP-038",
      "document_name"       :   "The Everything Tree",
      "popularity"          :   265,
      "to_use"              :   1,
      },


    # 266  : SCP-031
    #      : (SCP-031, "What is Love?")
      266    :     {
      "name"                :   "SCP-031",
      "document_name"       :   "What is Love?",
      "popularity"          :   266,
      "to_use"              :   1,
      },


    # 267  : None
    #      : (None, [OMITTED])
      267    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   267,
      "to_use"              :   0,
      },


    # 268  : SCP-072
    #      : (SCP-072, "The Foot of the Bed")
      268    :     {
      "name"                :   "SCP-072",
      "document_name"       :   "The Foot of the Bed",
      "popularity"          :   268,
      "to_use"              :   1,
      },


    # 269  : SCP-860
    #      : (SCP-860, "Blue Key")
      269    :     {
      "name"                :   "SCP-860",
      "document_name"       :   "Blue Key",
      "popularity"          :   269,
      "to_use"              :   1,
      },


    # 270  : SCP-3166
    #      : (SCP-3166, "You Have No Idea How Alone You Are, Garfield")
      270    :     {
      "name"                :   "SCP-3166",
      "document_name"       :   "You Have No Idea How Alone You Are, Garfield",
      "popularity"          :   270,
      "to_use"              :   1,
      },


    # 271  : None
    #      : (None, [OMITTED])
      271    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   271,
      "to_use"              :   0,
      },


    # 272  : SCP-1715
    #      : (SCP-1715, "Online Friend")
      272    :     {
      "name"                :   "SCP-1715",
      "document_name"       :   "Online Friend",
      "popularity"          :   272,
      "to_use"              :   0,
      },


    # 273  : SCP-1539
    #      : (SCP-1539, "Semantic Dissociator")
      273    :     {
      "name"                :   "SCP-1539",
      "document_name"       :   "Semantic Dissociator",
      "popularity"          :   273,
      "to_use"              :   0,
      },


    # 274  : SCP-1231
    #      : (SCP-1231, "The Theoretical Family")
      274    :     {
      "name"                :   "SCP-1231",
      "document_name"       :   "The Theoretical Family",
      "popularity"          :   274,
      "to_use"              :   1,
      },


    # 275  : SCP-572
    #      : (SCP-572, "Katana of Apparent Invincibility")
      275    :     {
      "name"                :   "SCP-572",
      "document_name"       :   "Katana of Apparent Invincibility",
      "popularity"          :   275,
      "to_use"              :   1,
      },


    # 276  : SCP-021
    #      : (SCP-021, "Skin Wyrm")
      276    :     {
      "name"                :   "SCP-021",
      "document_name"       :   "Skin Wyrm",
      "popularity"          :   276,
      "to_use"              :   1,
      },


    # 277  : None
    #      : (None, [OMITTED])
      277    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   277,
      "to_use"              :   0,
      },


    # 278  : SCP-458
    #      : (SCP-458, "The Never-Ending Pizza Box")
      278    :     {
      "name"                :   "SCP-458",
      "document_name"       :   "The Never-Ending Pizza Box",
      "popularity"          :   278,
      "to_use"              :   1,
      },


    # 279  : SCP-1739
    #      : (SCP-1739, "Obsolete Laptop")
      279    :     {
      "name"                :   "SCP-1739",
      "document_name"       :   "Obsolete Laptop",
      "popularity"          :   279,
      "to_use"              :   1,
      },


    # 280  : SCP-1316
    #      : (SCP-1316, "Lucy the Kitten Feline Espionage Device")
      280    :     {
      "name"                :   "SCP-1316",
      "document_name"       :   "Lucy the Kitten Feline Espionage Device",
      "popularity"          :   280,
      "to_use"              :   1,
      },


    # 281  : SCP-040
    #      : (SCP-040, "Evolution's Child")
      281    :     {
      "name"                :   "SCP-040",
      "document_name"       :   "Evolution's Child",
      "popularity"          :   281,
      "to_use"              :   1,
      },


    # 282  : SCP-162
    #      : (SCP-162, "Ball of Sharp")
      282    :     {
      "name"                :   "SCP-162",
      "document_name"       :   "Ball of Sharp",
      "popularity"          :   282,
      "to_use"              :   1,
      },


    # 283  : SCP-3812
    #      : (SCP-3812, "A Voice Behind Me")
      283    :     {
      "name"                :   "SCP-3812",
      "document_name"       :   "A Voice Behind Me",
      "popularity"          :   283,
      "to_use"              :   0,
      },


    # 284  : SCP-2771
    #      : (SCP-2771, "Border Duty")
      284    :     {
      "name"                :   "SCP-2771",
      "document_name"       :   "Border Duty",
      "popularity"          :   284,
      "to_use"              :   0,
      },


    # 285  : SCP-1247
    #      : (SCP-1247, "LaBeouf Viewer")
      285    :     {
      "name"                :   "SCP-1247",
      "document_name"       :   "LaBeouf Viewer",
      "popularity"          :   285,
      "to_use"              :   1,
      },


    # 286  : SCP-092
    #      : (SCP-092, '''"The Best of The 5th Dimension"''')
      286    :     {
      "name"                :   "SCP-092",
      "document_name"       :   '''"The Best of The 5th Dimension"''',
      "popularity"          :   286,
      "to_use"              :   1,
      },


    # 287  : SCP-1128
    #      : (SCP-1128, "Aquatic Horror")
      287    :     {
      "name"                :   "SCP-1128",
      "document_name"       :   "Aquatic Horror",
      "popularity"          :   287,
      "to_use"              :   0,
      },


    # 288  : SCP-2207
    #      : (SCP-2207, "Dimensional Razor")
      288    :     {
      "name"                :   "SCP-2207",
      "document_name"       :   "Dimensional Razor",
      "popularity"          :   288,
      "to_use"              :   1,
      },


    # 289  : SCP-1293
    #      : (SCP-1293, "Squeedle Deedle Dee!")
      289    :     {
      "name"                :   "SCP-1293",
      "document_name"       :   "Squeedle Deedle Dee!",
      "popularity"          :   289,
      "to_use"              :   1,
      },


    # 290  : SCP-007
    #      : (SCP-007, "Abdominal Planet")
      290    :     {
      "name"                :   "SCP-007",
      "document_name"       :   "Abdominal Planet",
      "popularity"          :   290,
      "to_use"              :   1,
      },


    # 291  : SCP-3966
    #      : (SCP-3966, "Falling Out")
      291    :     {
      "name"                :   "SCP-3966",
      "document_name"       :   "Falling Out",
      "popularity"          :   291,
      "to_use"              :   1,
      },


    # 292  : SCP-1802
    #      : (SCP-1802, '''"Skip"''')
      292    :     {
      "name"                :   "SCP-1802",
      "document_name"       :   '''"Skip"''',
      "popularity"          :   292,
      "to_use"              :   1,
      },


    # 293  : SCP-006
    #      : (SCP-006, "Fountain of Youth")
      293    :     {
      "name"                :   "SCP-006",
      "document_name"       :   "Fountain of Youth",
      "popularity"          :   293,
      "to_use"              :   0,
      },


    # 294  : SCP-3201
    #      : (SCP-3201, "Well, It Was Low-Entropy While It Lasted.")
      294    :     {
      "name"                :   "SCP-3201",
      "document_name"       :   "Well, It Was Low-Entropy While It Lasted.",
      "popularity"          :   294,
      "to_use"              :   0,
      },


    # 295  : SCP-127
    #      : (SCP-127, "The Living Gun")
      295    :     {
      "name"                :   "SCP-127",
      "document_name"       :   "The Living Gun",
      "popularity"          :   295,
      "to_use"              :   1,
      },


    # 296  : SCP-120
    #      : (SCP-120, "Teleporting Paddling Pool")
      296    :     {
      "name"                :   "SCP-120",
      "document_name"       :   "Teleporting Paddling Pool",
      "popularity"          :   296,
      "to_use"              :   1,
      },


    # 297  : SCP-205
    #      : (SCP-205, "Shadow Lamps")
      297    :     {
      "name"                :   "SCP-205",
      "document_name"       :   "Shadow Lamps",
      "popularity"          :   297,
      "to_use"              :   1,
      },


    # 298  : SCP-2774
    #      : (SCP-2774, "The Slow Burn Sloth")
      298    :     {
      "name"                :   "SCP-2774",
      "document_name"       :   "The Slow Burn Sloth",
      "popularity"          :   298,
      "to_use"              :   0,
      },


    # 299  : SCP-2845
    #      : (SCP-2845, "THE DEER")
      299    :     {
      "name"                :   "SCP-2845",
      "document_name"       :   "THE DEER",
      "popularity"          :   299,
      "to_use"              :   0,
      },


    # 300  : SCP-407
    #      : (SCP-407, "The Song of Genesis")
      300    :     {
      "name"                :   "SCP-407",
      "document_name"       :   "The Song of Genesis",
      "popularity"          :   300,
      "to_use"              :   1,
      },


    # 301  : SCP-069
    #      : (SCP-069, "Second Chance")
      301    :     {
      "name"                :   "SCP-069",
      "document_name"       :   "Second Chance",
      "popularity"          :   301,
      "to_use"              :   1,
      },


    # 302  : SCP-148
    #      : (SCP-148, '''The "Telekill" Alloy''')
      302    :     {
      "name"                :   "SCP-148",
      "document_name"       :   '''The "Telekill" Alloy''',
      "popularity"          :   302,
      "to_use"              :   0,
      },


    # 303  : SCP-1312
    #      : (SCP-1312, "Site 41")
      303    :     {
      "name"                :   "SCP-1312",
      "document_name"       :   "Site 41",
      "popularity"          :   303,
      "to_use"              :   0,
      },


    # 304  : SCP-931
    #      : (SCP-931, "A Rice Bowl")
      304    :     {
      "name"                :   "SCP-931",
      "document_name"       :   "A Rice Bowl",
      "popularity"          :   304,
      "to_use"              :   1,
      },


    # 305  : SCP-2571
    #      : (SCP-2571, "Cragglewood Park")
      305    :     {
      "name"                :   "SCP-2571",
      "document_name"       :   "Cragglewood Park",
      "popularity"          :   305,
      "to_use"              :   0,
      },


    # 306  : SCP-1233
    #      : (SCP-1233, "The Lunatic")
      306    :     {
      "name"                :   "SCP-1233",
      "document_name"       :   "The Lunatic",
      "popularity"          :   306,
      "to_use"              :   1,
      },


    # 307  : SCP-3922
    #      : (SCP-3922, "STOPRIGHTTHERECRIMINALSCUM!!!")
      307    :     {
      "name"                :   "SCP-3922",
      "document_name"       :   "STOPRIGHTTHERECRIMINALSCUM!!!",
      "popularity"          :   307,
      "to_use"              :   1,
      },


    # 308  : None
    #      : (None, [OMITTED])
      308    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   308,
      "to_use"              :   0,
      },


    # 309  : SCP-084
    #      : (SCP-084, "Static Tower")
      309    :     {
      "name"                :   "SCP-084",
      "document_name"       :   "Static Tower",
      "popularity"          :   309,
      "to_use"              :   0,
      },


    # 310  : SCP-1562
    #      : (SCP-1562, "Tunnel Slide")
      310    :     {
      "name"                :   "SCP-1562",
      "document_name"       :   "Tunnel Slide",
      "popularity"          :   310,
      "to_use"              :   1,
      },


    # 311  : SCP-978
    #      : (SCP-978, "Desire Camera")
      311    :     {
      "name"                :   "SCP-978",
      "document_name"       :   "Desire Camera",
      "popularity"          :   311,
      "to_use"              :   1,
      },


    # 312  : SCP-674
    #      : (SCP-674, "The Exposition Gun")
      312    :     {
      "name"                :   "SCP-674",
      "document_name"       :   "The Exposition Gun",
      "popularity"          :   312,
      "to_use"              :   1,
      },


    # 313  : SCP-209
    #      : (SCP-209, "The Sadist's Tumbler")
      313    :     {
      "name"                :   "SCP-209",
      "document_name"       :   "The Sadist's Tumbler",
      "popularity"          :   313,
      "to_use"              :   1,
      },


    # 314  : SCP-2915
    #      : (SCP-2915, "Frostee-Flesh")
      314    :     {
      "name"                :   "SCP-2915",
      "document_name"       :   "Frostee-Flesh",
      "popularity"          :   314,
      "to_use"              :   0,
      },


    # 315  : SCP-1529
    #      : (SCP-1529, "King of the Mountain")
      315    :     {
      "name"                :   "SCP-1529",
      "document_name"       :   "King of the Mountain",
      "popularity"          :   315,
      "to_use"              :   0,
      },


    # 316  : SCP-3171
    #      : (SCP-3171, "How the Foundation Came to Operate a Phone Sex Hotline")
      316    :     {
      "name"                :   "SCP-3171",
      "document_name"       :   "How the Foundation Came to Operate a Phone Sex Hotline",
      "popularity"          :   316,
      "to_use"              :   0,
      },


    # 317  : SCP-112
    #      : (SCP-112, "The Variable Coaster")
      317    :     {
      "name"                :   "SCP-112",
      "document_name"       :   "The Variable Coaster",
      "popularity"          :   317,
      "to_use"              :   0,
      },


    # 318  : SCP-026
    #      : (SCP-026, "Afterschool Retention")
      318    :     {
      "name"                :   "SCP-026",
      "document_name"       :   "Afterschool Retention",
      "popularity"          :   318,
      "to_use"              :   0,
      },


    # 319  : SCP-5004
    #      : (SCP-5004, "MEGALOMANIA")
      319    :     {
      "name"                :   "SCP-5004",
      "document_name"       :   "MEGALOMANIA",
      "popularity"          :   319,
      "to_use"              :   0,
      },


    # 320  : SCP-450
    #      : (SCP-450, "Abandoned Federal Penitentiary")
      320    :     {
      "name"                :   "SCP-450",
      "document_name"       :   "Abandoned Federal Penitentiary",
      "popularity"          :   320,
      "to_use"              :   0,
      },


    # 321  : SCP-3101
    #      : (SCP-3101, "Contain Me Harder")
      321    :     {
      "name"                :   "SCP-3101",
      "document_name"       :   "Contain Me Harder",
      "popularity"          :   321,
      "to_use"              :   0,
      },


    # 322  : SCP-2922
    #      : (SCP-2922, "Notes From the Under")
      322    :     {
      "name"                :   "SCP-2922",
      "document_name"       :   "Notes From the Under",
      "popularity"          :   322,
      "to_use"              :   1,
      },


    # 323  : SCP-013
    #      : (SCP-013, "Blue Lady Cigarettes")
      323    :     {
      "name"                :   "SCP-013",
      "document_name"       :   "Blue Lady Cigarettes",
      "popularity"          :   323,
      "to_use"              :   1,
      },


    # 324  : SCP-2999
    #      : (SCP-2999, "The Black Cat and the White Rabbit")
      324    :     {
      "name"                :   "SCP-2999",
      "document_name"       :   "The Black Cat and the White Rabbit",
      "popularity"          :   324,
      "to_use"              :   1,
      },


    # 325  : None
    #      : (None, [OMITTED])
      325    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   325,
      "to_use"              :   0,
      },


    # 326  : SCP-2343
    #      : (SCP-2343, "How I Got To Memphis")
      326    :     {
      "name"                :   "SCP-2343",
      "document_name"       :   "How I Got To Memphis",
      "popularity"          :   326,
      "to_use"              :   1,
      },


    # 327  : SCP-1633
    #      : (SCP-1633, "The Most Dangerous Video Game")
      327    :     {
      "name"                :   "SCP-1633",
      "document_name"       :   "The Most Dangerous Video Game",
      "popularity"          :   327,
      "to_use"              :   1,
      },


    # 328  : SCP-020
    #      : (SCP-020, "Unseen Mold")
      328    :     {
      "name"                :   "SCP-020",
      "document_name"       :   "Unseen Mold",
      "popularity"          :   328,
      "to_use"              :   1,
      },


    # 329  : SCP-3043
    #      : (SCP-3043, "Murphy Law in… Type 3043 — FOR MURDER!")
      329    :     {
      "name"                :   "SCP-3043",
      "document_name"       :   "Murphy Law in… Type 3043 — FOR MURDER!",
      "popularity"          :   329,
      "to_use"              :   1,
      },


    # 330  : SCP-027
    #      : (SCP-027, "The Vermin God")
      330    :     {
      "name"                :   "SCP-027",
      "document_name"       :   "The Vermin God",
      "popularity"          :   330,
      "to_use"              :   1,
      },


    # 331  : SCP-3799
    #      : (SCP-3799, "A Short History of Snowfall")
      331    :     {
      "name"                :   "SCP-3799",
      "document_name"       :   "A Short History of Snowfall",
      "popularity"          :   331,
      "to_use"              :   0,
      },


    # 332  : SCP-1160
    #      : (SCP-1160, "Effective Containment")
      332    :     {
      "name"                :   "SCP-1160",
      "document_name"       :   "Effective Containment",
      "popularity"          :   332,
      "to_use"              :   0,
      },


    # 333  : SCP-2598
    #      : (SCP-2598, "Traveling Moth Salesman")
      333    :     {
      "name"                :   "SCP-2598",
      "document_name"       :   "Traveling Moth Salesman",
      "popularity"          :   333,
      "to_use"              :   1,
      },


    # 334  : SCP-1782
    #      : (SCP-1782, "Tabula Rasa")
      334    :     {
      "name"                :   "SCP-1782",
      "document_name"       :   "Tabula Rasa",
      "popularity"          :   334,
      "to_use"              :   0,
      },


    # 335  : None
    #      : (None, [OMITTED])
      335    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   335,
      "to_use"              :   0,
      },


    # 336  : SCP-1500
    #      : (SCP-1500, "Zachary Callahan")
      336    :     {
      "name"                :   "SCP-1500",
      "document_name"       :   "Zachary Callahan",
      "popularity"          :   336,
      "to_use"              :   1,
      },


    # 337  : SCP-4335
    #      : (SCP-4335, "A Welt In The Crucible")
      337    :     {
      "name"                :   "SCP-4335",
      "document_name"       :   "A Welt In The Crucible",
      "popularity"          :   337,
      "to_use"              :   0,
      },


    # 338  : SCP-3935
    #      : (SCP-3935, "This Thing a Quiet Madness Made")
      338    :     {
      "name"                :   "SCP-3935",
      "document_name"       :   "This Thing a Quiet Madness Made",
      "popularity"          :   338,
      "to_use"              :   0,
      },


    # 339  : SCP-097
    #      : (SCP-097, "Old Fairgrounds")
      339    :     {
      "name"                :   "SCP-097",
      "document_name"       :   "Old Fairgrounds",
      "popularity"          :   339,
      "to_use"              :   0,
      },


    # 340  : SCP-1296
    #      : (SCP-1296, "Dial-a-Llama")
      340    :     {
      "name"                :   "SCP-1296",
      "document_name"       :   "Dial-a-Llama",
      "popularity"          :   340,
      "to_use"              :   1,
      },


    # 341  : SCP-826
    #      : (SCP-826, "Draws You into the Book")
      341    :     {
      "name"                :   "SCP-826",
      "document_name"       :   "Draws You into the Book",
      "popularity"          :   341,
      "to_use"              :   1,
      },


    # 342  : SCP-953
    #      : (SCP-953, "Polymorphic Humanoid")
      342    :     {
      "name"                :   "SCP-953",
      "document_name"       :   "Polymorphic Humanoid",
      "popularity"          :   342,
      "to_use"              :   1,
      },


    # 343  : SCP-2851
    #      : (SCP-2851, "Red")
      343    :     {
      "name"                :   "SCP-2851",
      "document_name"       :   "Red",
      "popularity"          :   343,
      "to_use"              :   0,
      },


    # 344  : SCP-113
    #      : (SCP-113, "The Gender-Switcher")
      344    :     {
      "name"                :   "SCP-113",
      "document_name"       :   "The Gender-Switcher",
      "popularity"          :   344,
      "to_use"              :   1,
      },


    # 345  : SCP-1584
    #      : (SCP-1584, "www.floatationdevice.███")
      345    :     {
      "name"                :   "SCP-1584",
      "document_name"       :   "www.floatationdevice.███",
      "popularity"          :   345,
      "to_use"              :   0,
      },


    # 346  : SCP-4975
    #      : (SCP-4975, "Time's Up")
      346    :     {
      "name"                :   "SCP-4975",
      "document_name"       :   "Time's Up",
      "popularity"          :   346,
      "to_use"              :   1,
      },


    # 347  : SCP-435
    #      : (SCP-435, "He-Who-Made-Dark")
      347    :     {
      "name"                :   "SCP-435",
      "document_name"       :   "He-Who-Made-Dark",
      "popularity"          :   347,
      "to_use"              :   1,
      },


    # 348  : SCP-2800
    #      : (SCP-2800, "Cactusman")
      348    :     {
      "name"                :   "SCP-2800",
      "document_name"       :   "Cactusman",
      "popularity"          :   348,
      "to_use"              :   1,
      },


    # 349  : SCP-1555
    #      : (SCP-1555, "Facility")
      349    :     {
      "name"                :   "SCP-1555",
      "document_name"       :   "Facility",
      "popularity"          :   349,
      "to_use"              :   0,
      },


    # 350  : None
    #      : (None, [OMITTED])
      350    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   350,
      "to_use"              :   0,
      },


    # 351  : SCP-019
    #      : (SCP-019, "The Monster Pot")
      351    :     {
      "name"                :   "SCP-019",
      "document_name"       :   "The Monster Pot",
      "popularity"          :   351,
      "to_use"              :   1,
      },


    # 352  : SCP-1442
    #      : (SCP-1442, "Incorporated")
      352    :     {
      "name"                :   "SCP-1442",
      "document_name"       :   "Incorporated",
      "popularity"          :   352,
      "to_use"              :   0,
      },


    # 353  : SCP-1799
    #      : (SCP-1799, "Mr. Laugh")
      353    :     {
      "name"                :   "SCP-1799",
      "document_name"       :   "Mr. Laugh",
      "popularity"          :   353,
      "to_use"              :   1,
      },


    # 354  : SCP-4006
    #      : (SCP-4006, "#MassaTruthetts")
      354    :     {
      "name"                :   "SCP-4006",
      "document_name"       :   "#MassaTruthetts",
      "popularity"          :   354,
      "to_use"              :   0,
      },


    # 355  : SCP-1472
    #      : (SCP-1472, "Multiverse Strip Club")
      355    :     {
      "name"                :   "SCP-1472",
      "document_name"       :   "Multiverse Strip Club",
      "popularity"          :   355,
      "to_use"              :   0,
      },


    # 356  : SCP-956
    #      : (SCP-956, "The Child-Breaker")
      356    :     {
      "name"                :   "SCP-956",
      "document_name"       :   "The Child-Breaker",
      "popularity"          :   356,
      "to_use"              :   1,
      },


    # 357  : SCP-711
    #      : (SCP-711, "Paradoxical Insurance Policy")
      357    :     {
      "name"                :   "SCP-711",
      "document_name"       :   "Paradoxical Insurance Policy",
      "popularity"          :   357,
      "to_use"              :   1,
      },


    # 358  : SCP-212
    #      : (SCP-212, "The Improver")
      358    :     {
      "name"                :   "SCP-212",
      "document_name"       :   "The Improver",
      "popularity"          :   358,
      "to_use"              :   1,
      },


    # 359  : SCP-846
    #      : (SCP-846, "Robo-Dude")
      359    :     {
      "name"                :   "SCP-846",
      "document_name"       :   "Robo-Dude",
      "popularity"          :   359,
      "to_use"              :   1,
      },


    # 360  : SCP-2206
    #      : (SCP-2206, "Maximum League Baseball")
      360    :     {
      "name"                :   "SCP-2206",
      "document_name"       :   "Maximum League Baseball",
      "popularity"          :   360,
      "to_use"              :   0,
      },


    # 361  : SCP-052
    #      : (SCP-052, "Time-Traveling Train")
      361    :     {
      "name"                :   "SCP-052",
      "document_name"       :   "Time-Traveling Train",
      "popularity"          :   361,
      "to_use"              :   0,
      },


    # 362  : SCP-108
    #      : (SCP-108, "Extradimensional Nasal Cavity")
      362    :     {
      "name"                :   "SCP-108",
      "document_name"       :   "Extradimensional Nasal Cavity",
      "popularity"          :   362,
      "to_use"              :   1,
      },


    # 363  : SCP-2786
    #      : (SCP-2786, "The Archetype")
      363    :     {
      "name"                :   "SCP-2786",
      "document_name"       :   "The Archetype",
      "popularity"          :   363,
      "to_use"              :   0,
      },


    # 364  : SCP-4100
    #      : (SCP-4100, "Future Imperfect")
      364    :     {
      "name"                :   "SCP-4100",
      "document_name"       :   "Future Imperfect",
      "popularity"          :   364,
      "to_use"              :   0,
      },


    # 365  : SCP-262
    #      : (SCP-262, "A Coat of Many Arms")
      365    :     {
      "name"                :   "SCP-262",
      "document_name"       :   "A Coat of Many Arms",
      "popularity"          :   365,
      "to_use"              :   1,
      },


    # 366  : SCP-3512
    #      : (SCP-3512, "The More You Know")
      366    :     {
      "name"                :   "SCP-3512",
      "document_name"       :   "The More You Know",
      "popularity"          :   366,
      "to_use"              :   0,
      },


    # 367  : SCP-1384
    #      : (SCP-1384, "Taker of Turns")
      367    :     {
      "name"                :   "SCP-1384",
      "document_name"       :   "Taker of Turns",
      "popularity"          :   367,
      "to_use"              :   0,
      },


    # 368  : SCP-063
    #      : (SCP-063, '''"The World's Best TothBrush"''')
      368    :     {
      "name"                :   "SCP-063",
      "document_name"       :   '''"The World's Best TothBrush"''',
      "popularity"          :   368,
      "to_use"              :   1,
      },


    # 369  : SCP-2508
    #      : (SCP-2508, "The Long Wait")
      369    :     {
      "name"                :   "SCP-2508",
      "document_name"       :   "The Long Wait",
      "popularity"          :   369,
      "to_use"              :   0,
      },


    # 370  : SCP-2085
    #      : (SCP-2085, "The Black Rabbit Company")
      370    :     {
      "name"                :   "SCP-2085",
      "document_name"       :   "The Black Rabbit Company",
      "popularity"          :   370,
      "to_use"              :   1,
      },


    # 371  : SCP-1795
    #      : (SCP-1795, "The Star Womb")
      371    :     {
      "name"                :   "SCP-1795",
      "document_name"       :   "The Star Womb",
      "popularity"          :   371,
      "to_use"              :   0,
      },


    # 372  : SCP-870
    #      : (SCP-870, "The Maybe There Monsters")
      372    :     {
      "name"                :   "SCP-870",
      "document_name"       :   "The Maybe There Monsters",
      "popularity"          :   372,
      "to_use"              :   1,
      },


    # 373  : SCP-2614
    #      : (SCP-2614, "Sometimes I Go Out In Pity For Myself")
      373    :     {
      "name"                :   "SCP-2614",
      "document_name"       :   "Sometimes I Go Out In Pity For Myself",
      "popularity"          :   373,
      "to_use"              :   1,
      },


    # 374  : SCP-3949
    #      : (SCP-3949, "Penumbra W.A.V.E. #1 Fan!")
      374    :     {
      "name"                :   "SCP-3949",
      "document_name"       :   "Penumbra W.A.V.E. #1 Fan!",
      "popularity"          :   374,
      "to_use"              :   0,
      },


    # 375  : SCP-2419
    #      : (SCP-2419, "The Laughing Men")
      375    :     {
      "name"                :   "SCP-2419",
      "document_name"       :   "The Laughing Men",
      "popularity"          :   375,
      "to_use"              :   0,
      },


    # 376  : SCP-1360
    #      : (SCP-1360, "PSHUD #31")
      376    :     {
      "name"                :   "SCP-1360",
      "document_name"       :   "PSHUD #31",
      "popularity"          :   376,
      "to_use"              :   1,
      },


    # 377  : SCP-023
    #      : (SCP-023, "Black Shuck")
      377    :     {
      "name"                :   "SCP-023",
      "document_name"       :   "Black Shuck",
      "popularity"          :   377,
      "to_use"              :   1,
      },


    # 378  : SCP-1155
    #      : (SCP-1155, "Predatory Street Art")
      378    :     {
      "name"                :   "SCP-1155",
      "document_name"       :   "Predatory Street Art",
      "popularity"          :   378,
      "to_use"              :   0,
      },


    # 379  : SCP-030
    #      : (SCP-030, "The Homunculus")
      379    :     {
      "name"                :   "SCP-030",
      "document_name"       :   "The Homunculus",
      "popularity"          :   379,
      "to_use"              :   1,
      },


    # 380  : SCP-5500
    #      : (SCP-5500, "Death of the Authors")
      380    :     {
      "name"                :   "SCP-5500",
      "document_name"       :   "Death of the Authors",
      "popularity"          :   380,
      "to_use"              :   0,
      },


    # 381  : SCP-1903
    #      : (SCP-1903, "Jackie's Secret")
      381    :     {
      "name"                :   "SCP-1903",
      "document_name"       :   "Jackie's Secret",
      "popularity"          :   381,
      "to_use"              :   1,
      },


    # 382  : None
    #      : (None, [OMITTED])
      382    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   382,
      "to_use"              :   0,
      },


    # 383  : SCP-1483
    #      : (SCP-1483, "The Third Antarctic Empire")
      383    :     {
      "name"                :   "SCP-1483",
      "document_name"       :   "The Third Antarctic Empire",
      "popularity"          :   383,
      "to_use"              :   0,
      },


    # 384  : SCP-060
    #      : (SCP-060, "Infernal Occult Skeleton")
      384    :     {
      "name"                :   "SCP-060",
      "document_name"       :   "Infernal Occult Skeleton",
      "popularity"          :   384,
      "to_use"              :   0,
      },


    # 385  : SCP-2420
    #      : (SCP-2420, "A Good Dog")
      385    :     {
      "name"                :   "SCP-2420",
      "document_name"       :   "A Good Dog",
      "popularity"          :   385,
      "to_use"              :   1,
      },


    # 386  : SCP-370
    #      : (SCP-370, "A Key")
      386    :     {
      "name"                :   "SCP-370",
      "document_name"       :   "A Key",
      "popularity"          :   386,
      "to_use"              :   1,
      },


    # 387  : SCP-2021
    #      : (SCP-2021, "Single-Sided Paper")
      387    :     {
      "name"                :   "SCP-2021",
      "document_name"       :   "Single-Sided Paper",
      "popularity"          :   387,
      "to_use"              :   1,
      },


    # 388  : SCP-4514
    #      : (SCP-4514, "The Thing That Kills You")
      388    :     {
      "name"                :   "SCP-4514",
      "document_name"       :   "The Thing That Kills You",
      "popularity"          :   388,
      "to_use"              :   1,
      },


    # 389  : SCP-3108
    #      : (SCP-3108, "The Nerfing Gun")
      389    :     {
      "name"                :   "SCP-3108",
      "document_name"       :   "The Nerfing Gun",
      "popularity"          :   389,
      "to_use"              :   1,
      },


    # 390  : SCP-609
    #      : (SCP-609, "Dr. Wondertainment's Ontological 6-Balls®")
      390    :     {
      "name"                :   "SCP-609",
      "document_name"       :   "Dr. Wondertainment's Ontological 6-Balls®",
      "popularity"          :   390,
      "to_use"              :   1,
      },


    # 391  : SCP-517
    #      : (SCP-517, "Grammie Knows")
      391    :     {
      "name"                :   "SCP-517",
      "document_name"       :   "Grammie Knows",
      "popularity"          :   391,
      "to_use"              :   1,
      },


    # 392  : SCP-050
    #      : (SCP-050, "To The Cleverest")
      392    :     {
      "name"                :   "SCP-050",
      "document_name"       :   "To The Cleverest",
      "popularity"          :   392,
      "to_use"              :   1,
      },


    # 393  : SCP-4290
    #      : (SCP-4290, "The Child Hungers")
      393    :     {
      "name"                :   "SCP-4290",
      "document_name"       :   "The Child Hungers",
      "popularity"          :   393,
      "to_use"              :   0,
      },


    # 394  : SCP-1237
    #      : (SCP-1237, "The Epsilon Wave")
      394    :     {
      "name"                :   "SCP-1237",
      "document_name"       :   "The Epsilon Wave",
      "popularity"          :   394,
      "to_use"              :   0,
      },


    # 395  : SCP-1485
    #      : (SCP-1485, "Normality")
      395    :     {
      "name"                :   "SCP-1485",
      "document_name"       :   "Normality",
      "popularity"          :   395,
      "to_use"              :   0,
      },


    # 396  : SCP-2063
    #      : (SCP-2063, "A Past Vision of the Future")
      396    :     {
      "name"                :   "SCP-2063",
      "document_name"       :   "A Past Vision of the Future",
      "popularity"          :   396,
      "to_use"              :   1,
      },


    # 397  : SCP-1884
    #      : (SCP-1884, "Madame Rezarta and Her Amazing Palm Reader")
      397    :     {
      "name"                :   "SCP-1884",
      "document_name"       :   "Madame Rezarta and Her Amazing Palm Reader",
      "popularity"          :   397,
      "to_use"              :   1,
      },


    # 398  : SCP-2932
    #      : (SCP-2932, "Titania's Prison")
      398    :     {
      "name"                :   "SCP-2932",
      "document_name"       :   "Titania's Prison",
      "popularity"          :   398,
      "to_use"              :   0,
      },


    # 399  : SCP-319
    #      : (SCP-319, "A Curious Device")
      399    :     {
      "name"                :   "SCP-319",
      "document_name"       :   "A Curious Device",
      "popularity"          :   399,
      "to_use"              :   1,
      },


    # 400  : SCP-3448
    #      : (SCP-3448, "Halfterlife")
      400    :     {
      "name"                :   "SCP-3448",
      "document_name"       :   "Halfterlife",
      "popularity"          :   400,
      "to_use"              :   1,
      },


    # 401  : SCP-3280
    #      : (SCP-3280, "After the Storm")
      401    :     {
      "name"                :   "SCP-3280",
      "document_name"       :   "After the Storm",
      "popularity"          :   401,
      "to_use"              :   0,
      },


    # 402  : SCP-5005
    #      : (SCP-5005, "Lamplight")
      402    :     {
      "name"                :   "SCP-5005",
      "document_name"       :   "Lamplight",
      "popularity"          :   402,
      "to_use"              :   0,
      },


    # 403  : SCP-604
    #      : (SCP-604, "The Cannibal's Banquet; A Corrupted Ritual")
      403    :     {
      "name"                :   "SCP-604",
      "document_name"       :   "The Cannibal's Banquet; A Corrupted Ritual",
      "popularity"          :   403,
      "to_use"              :   1,
      },


    # 404  : None
    #      : (None, [OMITTED])
      404    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   404,
      "to_use"              :   0,
      },


    # 405  : SCP-2300
    #      : (SCP-2300, "Periodic Golems")
      405    :     {
      "name"                :   "SCP-2300",
      "document_name"       :   "Periodic Golems",
      "popularity"          :   405,
      "to_use"              :   1,
      },


    # 406  : SCP-1812
    #      : (SCP-1812, "Extralunar Meme")
      406    :     {
      "name"                :   "SCP-1812",
      "document_name"       :   "Extralunar Meme",
      "popularity"          :   406,
      "to_use"              :   0,
      },


    # 407  : SCP-1590
    #      : (SCP-1590, "The Book of Tamlin")
      407    :     {
      "name"                :   "SCP-1590",
      "document_name"       :   "The Book of Tamlin",
      "popularity"          :   407,
      "to_use"              :   1,
      },


    # 408  : SCP-165
    #      : (SCP-165, "The Creeping, Hungry Sands of Tule")
      408    :     {
      "name"                :   "SCP-165",
      "document_name"       :   "The Creeping, Hungry Sands of Tule",
      "popularity"          :   408,
      "to_use"              :   1,
      },


    # 409  : None
    #      : (None, [OMITTED])
      409    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   409,
      "to_use"              :   0,
      },


    # 410  : SCP-3688
    #      : (SCP-3688, "You Can Dance If You Want To")
      410    :     {
      "name"                :   "SCP-3688",
      "document_name"       :   "You Can Dance If You Want To",
      "popularity"          :   410,
      "to_use"              :   0,
      },


    # 411  : SCP-3312
    #      : (SCP-3312, "OwO what's this?")
      411    :     {
      "name"                :   "SCP-3312",
      "document_name"       :   "OwO what's this?",
      "popularity"          :   411,
      "to_use"              :   0,
      },


    # 412  : SCP-2702
    #      : (SCP-2702, "Professor Abnormal's Science Lab")
      412    :     {
      "name"                :   "SCP-2702",
      "document_name"       :   "Professor Abnormal's Science Lab",
      "popularity"          :   412,
      "to_use"              :   0,
      },


    # 413  : SCP-1427
    #      : (SCP-1427, "Extinguishing Stele")
      413    :     {
      "name"                :   "SCP-1427",
      "document_name"       :   "Extinguishing Stele",
      "popularity"          :   413,
      "to_use"              :   0,
      },


    # 414  : SCP-3790
    #      : (SCP-3790, "Department of Abnormalities")
      414    :     {
      "name"                :   "SCP-3790",
      "document_name"       :   "Department of Abnormalities",
      "popularity"          :   414,
      "to_use"              :   0,
      },


    # 415  : SCP-1972
    #      : (SCP-1972, "The Whore and the Cop")
      415    :     {
      "name"                :   "SCP-1972",
      "document_name"       :   "The Whore and the Cop",
      "popularity"          :   415,
      "to_use"              :   1,
      },


    # 416  : SCP-5555
    #      : (SCP-5555, "Made in Heaven")
      416    :     {
      "name"                :   "SCP-5555",
      "document_name"       :   "Made in Heaven",
      "popularity"          :   416,
      "to_use"              :   0,
      },


    # 417  : SCP-2078
    #      : (SCP-2078, "Third Party")
      417    :     {
      "name"                :   "SCP-2078",
      "document_name"       :   "Third Party",
      "popularity"          :   417,
      "to_use"              :   0,
      },


    # 418  : SCP-536
    #      : (SCP-536, "Physical Law Testing Chamber")
      418    :     {
      "name"                :   "SCP-536",
      "document_name"       :   "Physical Law Testing Chamber",
      "popularity"          :   418,
      "to_use"              :   1,
      },


    # 419  : SCP-413
    #      : (SCP-413, "Endless Garage")
      419    :     {
      "name"                :   "SCP-413",
      "document_name"       :   "Endless Garage",
      "popularity"          :   419,
      "to_use"              :   0,
      },


    # 420  : SCP-4955
    #      : (SCP-4955, "KNIFE - A Knife Only Seen Through Gaslight")
      420    :     {
      "name"                :   "SCP-4955",
      "document_name"       :   "KNIFE - A Knife Only Seen Through Gaslight",
      "popularity"          :   420,
      "to_use"              :   1,
      },


    # 421  : SCP-1921
    #      : (SCP-1921, "Black Cotton Candy")
      421    :     {
      "name"                :   "SCP-1921",
      "document_name"       :   "Black Cotton Candy",
      "popularity"          :   421,
      "to_use"              :   1,
      },


    # 422  : SCP-4010
    #      : (SCP-4010, "Attempt To Look At What We Accomplished")
      422    :     {
      "name"                :   "SCP-4010",
      "document_name"       :   "Attempt To Look At What We Accomplished",
      "popularity"          :   422,
      "to_use"              :   0,
      },


    # 423  : SCP-3006
    #      : (SCP-3006, "Twice The Number One")
      423    :     {
      "name"                :   "SCP-3006",
      "document_name"       :   "Twice The Number One",
      "popularity"          :   423,
      "to_use"              :   0,
      },


    # 424  : None
    #      : (None, [OMITTED])
      424    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   424,
      "to_use"              :   0,
      },


    # 425  : SCP-3200
    #      : (SCP-3200, "Chronos")
      425    :     {
      "name"                :   "SCP-3200",
      "document_name"       :   "Chronos",
      "popularity"          :   425,
      "to_use"              :   0,
      },


    # 426  : SCP-029
    #      : (SCP-029, "Daughter of Shadows")
      426    :     {
      "name"                :   "SCP-029",
      "document_name"       :   "Daughter of Shadows",
      "popularity"          :   426,
      "to_use"              :   1,
      },


    # 427  : None
    #      : (None, [OMITTED])
      427    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   427,
      "to_use"              :   0,
      },


    # 428  : SCP-1780
    #      : (SCP-1780, "The Temporal Anomalies Department")
      428    :     {
      "name"                :   "SCP-1780",
      "document_name"       :   "The Temporal Anomalies Department",
      "popularity"          :   428,
      "to_use"              :   1,
      },


    # 429  : SCP-1810
    #      : (SCP-1810, "Mr. Pierrot")
      429    :     {
      "name"                :   "SCP-1810",
      "document_name"       :   "Mr. Pierrot",
      "popularity"          :   429,
      "to_use"              :   1,
      },


    # 430  : SCP-1337
    #      : (SCP-1337, "The Hitchhiker")
      430    :     {
      "name"                :   "SCP-1337",
      "document_name"       :   "The Hitchhiker",
      "popularity"          :   430,
      "to_use"              :   0,
      },


    # 431  : SCP-4062
    #      : (SCP-4062, "Soggy Doggy")
      431    :     {
      "name"                :   "SCP-4062",
      "document_name"       :   "Soggy Doggy",
      "popularity"          :   431,
      "to_use"              :   1,
      },


    # 432  : None
    #      : (None, [OMITTED])
      432    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   432,
      "to_use"              :   0,
      },


    # 433  : SCP-1984
    #      : (SCP-1984, "Dead Hand")
      433    :     {
      "name"                :   "SCP-1984",
      "document_name"       :   "Dead Hand",
      "popularity"          :   433,
      "to_use"              :   0,
      },


    # 434  : SCP-272
    #      : (SCP-272, "An Old Iron Nail")
      434    :     {
      "name"                :   "SCP-272",
      "document_name"       :   "An Old Iron Nail",
      "popularity"          :   434,
      "to_use"              :   1,
      },


    # 435  : SCP-3450
    #      : (SCP-3450, "OC DO NOT STEAL")
      435    :     {
      "name"                :   "SCP-3450",
      "document_name"       :   "OC DO NOT STEAL",
      "popularity"          :   435,
      "to_use"              :   1,
      },


    # 436  : SCP-3020
    #      : (SCP-3020, "Depression")
      436    :     {
      "name"                :   "SCP-3020",
      "document_name"       :   "Depression",
      "popularity"          :   436,
      "to_use"              :   0,
      },


    # 437  : SCP-2001
    #      : (SCP-2001, "A Space Oddity")
      437    :     {
      "name"                :   "SCP-2001",
      "document_name"       :   "A Space Oddity",
      "popularity"          :   437,
      "to_use"              :   0,
      },


    # 438  : SCP-1456
    #      : (SCP-1456, '''"You've Won!"''')
      438    :     {
      "name"                :   "SCP-1456",
      "document_name"       :   '''"You've Won!"''',
      "popularity"          :   438,
      "to_use"              :   0,
      },


    # 439  : SCP-411
    #      : (SCP-411, "Ancient Precog")
      439    :     {
      "name"                :   "SCP-411",
      "document_name"       :   "Ancient Precog",
      "popularity"          :   439,
      "to_use"              :   1,
      },


    # 440  : SCP-1454
    #      : (SCP-1454, "Sibling Rivalry")
      440    :     {
      "name"                :   "SCP-1454",
      "document_name"       :   "Sibling Rivalry",
      "popularity"          :   440,
      "to_use"              :   1,
      },


    # 441  : SCP-752
    #      : (SCP-752, "Altruistic Utopia")
      441    :     {
      "name"                :   "SCP-752",
      "document_name"       :   "Altruistic Utopia",
      "popularity"          :   441,
      "to_use"              :   0,
      },


    # 442  : SCP-4182
    #      : (SCP-4182, "There Is No Site-5")
      442    :     {
      "name"                :   "SCP-4182",
      "document_name"       :   "There Is No Site-5",
      "popularity"          :   442,
      "to_use"              :   0,
      },


    # 443  : SCP-3250
    #      : (SCP-3250, "Jesus Fried Chicken")
      443    :     {
      "name"                :   "SCP-3250",
      "document_name"       :   "Jesus Fried Chicken",
      "popularity"          :   443,
      "to_use"              :   1,
      },


    # 444  : SCP-2020
    #      : (SCP-2020, "Cliche, Right?")
      444    :     {
      "name"                :   "SCP-2020",
      "document_name"       :   "Cliche, Right?",
      "popularity"          :   444,
      "to_use"              :   1,
      },


    # 445  : SCP-2881
    #      : (SCP-2881, "The Tree You Cannot Climb")
      445    :     {
      "name"                :   "SCP-2881",
      "document_name"       :   "The Tree You Cannot Climb",
      "popularity"          :   445,
      "to_use"              :   0,
      },


    # 446  : SCP-1348
    #      : (SCP-1348, "Inner Sanctum")
      446    :     {
      "name"                :   "SCP-1348",
      "document_name"       :   "Inner Sanctum",
      "popularity"          :   446,
      "to_use"              :   0,
      },


    # 447  : SCP-557
    #      : (SCP-557, "Ancient Containment Site")
      447    :     {
      "name"                :   "SCP-557",
      "document_name"       :   "Ancient Containment Site",
      "popularity"          :   447,
      "to_use"              :   0,
      },


    # 448  : SCP-699
    #      : (SCP-699, "Mystery Box")
      448    :     {
      "name"                :   "SCP-699",
      "document_name"       :   "Mystery Box",
      "popularity"          :   448,
      "to_use"              :   1,
      },


    # 449  : SCP-067
    #      : (SCP-067, "The Artist's Pen")
      449    :     {
      "name"                :   "SCP-067",
      "document_name"       :   "The Artist's Pen",
      "popularity"          :   449,
      "to_use"              :   1,
      },


    # 450  : SCP-2193
    #      : (SCP-2193, '''"Monthly Termination"''')
      450    :     {
      "name"                :   "SCP-2193",
      "document_name"       :   '''"Monthly Termination"''',
      "popularity"          :   450,
      "to_use"              :   0,
      },


    # 451  : SCP-2406
    #      : (SCP-2406, "The Colossus")
      451    :     {
      "name"                :   "SCP-2406",
      "document_name"       :   "The Colossus",
      "popularity"          :   451,
      "to_use"              :   0,
      },


    # 452  : SCP-705
    #      : (SCP-705, "Militaristic Play-Doh")
      452    :     {
      "name"                :   "SCP-705",
      "document_name"       :   "Militaristic Play-Doh",
      "popularity"          :   452,
      "to_use"              :   1,
      },


    # 453  : None
    #      : (None, [OMITTED])
      453    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   453,
      "to_use"              :   0,
      },


    # 454  : SCP-1915
    #      : (SCP-1915, "Status Quo")
      454    :     {
      "name"                :   "SCP-1915",
      "document_name"       :   "Status Quo",
      "popularity"          :   454,
      "to_use"              :   1,
      },


    # 455  : SCP-1468
    #      : (SCP-1468, "Literature Birds")
      455    :     {
      "name"                :   "SCP-1468",
      "document_name"       :   "Literature Birds",
      "popularity"          :   455,
      "to_use"              :   1,
      },


    # 456  : SCP-100
    #      : (SCP-100, '''"Jamaican Joe's Junkyard Jubilee"''')
      456    :     {
      "name"                :   "SCP-100",
      "document_name"       :   '''"Jamaican Joe's Junkyard Jubilee"''',
      "popularity"          :   456,
      "to_use"              :   0,
      },


    # 457  : SCP-3388
    #      : (SCP-3388, "Cacthulhu")
      457    :     {
      "name"                :   "SCP-3388",
      "document_name"       :   "Cacthulhu",
      "popularity"          :   457,
      "to_use"              :   1,
      },


    # 458  : SCP-3456
    #      : (SCP-3456, "The Orcadian Horsemen")
      458    :     {
      "name"                :   "SCP-3456",
      "document_name"       :   "The Orcadian Horsemen",
      "popularity"          :   458,
      "to_use"              :   0,
      },


    # 459  : SCP-2191
    #      : (SCP-2191, '''"Dracula Factory"''')
      459    :     {
      "name"                :   "SCP-2191",
      "document_name"       :   '''"Dracula Factory"''',
      "popularity"          :   459,
      "to_use"              :   0,
      },


    # 460  : SCP-1846
    #      : (SCP-1846, "Maize Angel")
      460    :     {
      "name"                :   "SCP-1846",
      "document_name"       :   "Maize Angel",
      "popularity"          :   460,
      "to_use"              :   1,
      },


    # 461  : SCP-1165
    #      : (SCP-1165, "Minus Level")
      461    :     {
      "name"                :   "SCP-1165",
      "document_name"       :   "Minus Level",
      "popularity"          :   461,
      "to_use"              :   0,
      },


    # 462  : SCP-268
    #      : (SCP-268, "Cap of Neglect")
      462    :     {
      "name"                :   "SCP-268",
      "document_name"       :   "Cap of Neglect",
      "popularity"          :   462,
      "to_use"              :   1,
      },


    # 463  : SCP-4971
    #      : (SCP-4971, "Rituals")
      463    :     {
      "name"                :   "SCP-4971",
      "document_name"       :   "Rituals",
      "popularity"          :   463,
      "to_use"              :   0,
      },


    # 464  : None
    #      : (None, [OMITTED])
      464    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   464,
      "to_use"              :   0,
      },


    # 465  : SCP-2075
    #      : (SCP-2075, "The Way of All Flesh")
      465    :     {
      "name"                :   "SCP-2075",
      "document_name"       :   "The Way of All Flesh",
      "popularity"          :   465,
      "to_use"              :   1,
      },


    # 466  : SCP-3484
    #      : (SCP-3484, "Missing Pieces")
      466    :     {
      "name"                :   "SCP-3484",
      "document_name"       :   "Missing Pieces",
      "popularity"          :   466,
      "to_use"              :   1,
      },


    # 467  : SCP-228
    #      : (SCP-228, "Psychiatric Diagnostic Tool")
      467    :     {
      "name"                :   "SCP-228",
      "document_name"       :   "Psychiatric Diagnostic Tool",
      "popularity"          :   467,
      "to_use"              :   1,
      },


    # 468  : SCP-372
    #      : (SCP-372, "Peripheral Jumper")
      468    :     {
      "name"                :   "SCP-372",
      "document_name"       :   "Peripheral Jumper",
      "popularity"          :   468,
      "to_use"              :   1,
      },


    # 469  : None
    #      : (None, [OMITTED])
      469    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   469,
      "to_use"              :   0,
      },


    # 470  : SCP-1659
    #      : (SCP-1659, "Directorate K")
      470    :     {
      "name"                :   "SCP-1659",
      "document_name"       :   "Directorate K",
      "popularity"          :   470,
      "to_use"              :   0,
      },


    # 471  : None
    #      : (None, [OMITTED])
      471    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   471,
      "to_use"              :   0,
      },


    # 472  : SCP-603
    #      : (SCP-603, "Self-Replicating Computer Program")
      472    :     {
      "name"                :   "SCP-603",
      "document_name"       :   "Self-Replicating Computer Program",
      "popularity"          :   472,
      "to_use"              :   1,
      },


    # 473  : SCP-2547
    #      : (SCP-2547, "Dog Days Of Summer")
      473    :     {
      "name"                :   "SCP-2547",
      "document_name"       :   "Dog Days Of Summer",
      "popularity"          :   473,
      "to_use"              :   0,
      },


    # 474  : SCP-1833
    #      : (SCP-1833, "Class of '76")
      474    :     {
      "name"                :   "SCP-1833",
      "document_name"       :   "Class of '76",
      "popularity"          :   474,
      "to_use"              :   1,
      },


    # 475  : SCP-025
    #      : (SCP-025, "A Well-Worn Wardrobe")
      475    :     {
      "name"                :   "SCP-025",
      "document_name"       :   "A Well-Worn Wardrobe",
      "popularity"          :   475,
      "to_use"              :   1,
      },


    # 476  : SCP-847
    #      : (SCP-847, "The Mannequin")
      476    :     {
      "name"                :   "SCP-847",
      "document_name"       :   "The Mannequin",
      "popularity"          :   476,
      "to_use"              :   1,
      },


    # 477  : SCP-4774
    #      : (SCP-4774, "The Ninth Planet [citation needed]")
      477    :     {
      "name"                :   "SCP-4774",
      "document_name"       :   "The Ninth Planet [citation needed]",
      "popularity"          :   477,
      "to_use"              :   0,
      },


    # 478  : SCP-198
    #      : (SCP-198, "Cup of Joe")
      478    :     {
      "name"                :   "SCP-198",
      "document_name"       :   "Cup of Joe",
      "popularity"          :   478,
      "to_use"              :   1,
      },


    # 479  : SCP-247
    #      : (SCP-247, "A Harmless Kitten")
      479    :     {
      "name"                :   "SCP-247",
      "document_name"       :   "A Harmless Kitten",
      "popularity"          :   479,
      "to_use"              :   1,
      },


    # 480  : SCP-143
    #      : (SCP-143, "The Bladewood Grove")
      480    :     {
      "name"                :   "SCP-143",
      "document_name"       :   "The Bladewood Grove",
      "popularity"          :   480,
      "to_use"              :   0,
      },


    # 481  : SCP-2203
    #      : (SCP-2203, "Find the One for You!")
      481    :     {
      "name"                :   "SCP-2203",
      "document_name"       :   "Find the One for You!",
      "popularity"          :   481,
      "to_use"              :   1,
      },


    # 482  : SCP-2118
    #      : (SCP-2118, "The Lost Child")
      482    :     {
      "name"                :   "SCP-2118",
      "document_name"       :   "The Lost Child",
      "popularity"          :   482,
      "to_use"              :   1,
      },


    # 483  : SCP-2980
    #      : (SCP-2980, "Devil's Nightlight")
      483    :     {
      "name"                :   "SCP-2980",
      "document_name"       :   "Devil's Nightlight",
      "popularity"          :   483,
      "to_use"              :   1,
      },


    # 484  : SCP-166
    #      : (SCP-166, "Teenage Succubus")
      484    :     {
      "name"                :   "SCP-166",
      "document_name"       :   "Teenage Succubus",
      "popularity"          :   484,
      "to_use"              :   1,
      },


    # 485  : SCP-3515
    #      : (SCP-3515, "Unearth")
      485    :     {
      "name"                :   "SCP-3515",
      "document_name"       :   "Unearth",
      "popularity"          :   485,
      "to_use"              :   1,
      },


    # 486  : SCP-4028
    #      : (SCP-4028, "La Historia de Don Quixote de la Mancha")
      486    :     {
      "name"                :   "SCP-4028",
      "document_name"       :   "La Historia de Don Quixote de la Mancha",
      "popularity"          :   486,
      "to_use"              :   0,
      },


    # 487  : SCP-2072
    #      : (SCP-2072, "Prime Ministerial Pet Cemetery")
      487    :     {
      "name"                :   "SCP-2072",
      "document_name"       :   "Prime Ministerial Pet Cemetery",
      "popularity"          :   487,
      "to_use"              :   0,
      },


    # 488  : SCP-4511
    #      : (SCP-4511, "Swine God")
      488    :     {
      "name"                :   "SCP-4511",
      "document_name"       :   "Swine God",
      "popularity"          :   488,
      "to_use"              :   0,
      },


    # 489  : None
    #      : (None, [OMITTED])
      489    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   489,
      "to_use"              :   0,
      },


    # 490  : SCP-973
    #      : (SCP-973, "Smokey")
      490    :     {
      "name"                :   "SCP-973",
      "document_name"       :   "Smokey",
      "popularity"          :   490,
      "to_use"              :   0,
      },


    # 491  : SCP-4233
    #      : (SCP-4233, "The Dreadnought")
      491    :     {
      "name"                :   "SCP-4233",
      "document_name"       :   "The Dreadnought",
      "popularity"          :   491,
      "to_use"              :   0,
      },


    # 492  : SCP-3041
    #      : (SCP-3041, "The Red Knife")
      492    :     {
      "name"                :   "SCP-3041",
      "document_name"       :   "The Red Knife",
      "popularity"          :   492,
      "to_use"              :   1,
      },


    # 493  : SCP-745
    #      : (SCP-745, "The Headlights")
      493    :     {
      "name"                :   "SCP-745",
      "document_name"       :   "The Headlights",
      "popularity"          :   493,
      "to_use"              :   0,
      },


    # 494  : SCP-4966
    #      : (SCP-4966, "Tubbioca: Devourer of Souls, Consumer of Secrets, Lord of Munchies")
      494    :     {
      "name"                :   "SCP-4966",
      "document_name"       :   "Tubbioca: Devourer of Souls, Consumer of Secrets, Lord of Munchies",
      "popularity"          :   494,
      "to_use"              :   1,
      },


    # 495  : None
    #      : (None, [OMITTED])
      495    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   495,
      "to_use"              :   0,
      },


    # 496  : SCP-668
    #      : (SCP-668, '''13" Chef's Knife''')
      496    :     {
      "name"                :   "SCP-668",
      "document_name"       :   '''13" Chef's Knife''',
      "popularity"          :   496,
      "to_use"              :   1,
      },


    # 497  : SCP-144
    #      : (SCP-144, "Tibetan Rope to Heaven")
      497    :     {
      "name"                :   "SCP-144",
      "document_name"       :   "Tibetan Rope to Heaven",
      "popularity"          :   497,
      "to_use"              :   0,
      },


    # 498  : SCP-2424
    #      : (SCP-2424, "Hostile Walrus Cyborg research ongoing")
      498    :     {
      "name"                :   "SCP-2424",
      "document_name"       :   "Hostile Walrus Cyborg research ongoing",
      "popularity"          :   498,
      "to_use"              :   1,
      },


    # 499  : None
    #      : (None, [OMITTED])
      499    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   499,
      "to_use"              :   0,
      },


    # 500  : SCP-187
    #      : (SCP-187, "Double Vision")
      500    :     {
      "name"                :   "SCP-187",
      "document_name"       :   "Double Vision",
      "popularity"          :   500,
      "to_use"              :   1,
      },


    # 501  : SCP-361
    #      : (SCP-361, "Bronze Liver")
      501    :     {
      "name"                :   "SCP-361",
      "document_name"       :   "Bronze Liver",
      "popularity"          :   501,
      "to_use"              :   1,
      },


    # 502  : SCP-332
    #      : (SCP-332, "The 1976 Kirk Lonwood High School Marching Band")
      502    :     {
      "name"                :   "SCP-332",
      "document_name"       :   "The 1976 Kirk Lonwood High School Marching Band",
      "popularity"          :   502,
      "to_use"              :   0,
      },


    # 503  : SCP-1616
    #      : (SCP-1616, "Nibbles")
      503    :     {
      "name"                :   "SCP-1616",
      "document_name"       :   "Nibbles",
      "popularity"          :   503,
      "to_use"              :   1,
      },


    # 504  : SCP-920
    #      : (SCP-920, "Mr. Lost")
      504    :     {
      "name"                :   "SCP-920",
      "document_name"       :   "Mr. Lost",
      "popularity"          :   504,
      "to_use"              :   1,
      },


    # 505  : SCP-432
    #      : (SCP-432, "Cabinet Maze")
      505    :     {
      "name"                :   "SCP-432",
      "document_name"       :   "Cabinet Maze",
      "popularity"          :   505,
      "to_use"              :   1,
      },


    # 506  : SCP-3035
    #      : (SCP-3035, "Science Bugs")
      506    :     {
      "name"                :   "SCP-3035",
      "document_name"       :   "Science Bugs",
      "popularity"          :   506,
      "to_use"              :   0,
      },


    # 507  : SCP-400
    #      : (SCP-400, "Beautiful Babies")
      507    :     {
      "name"                :   "SCP-400",
      "document_name"       :   "Beautiful Babies",
      "popularity"          :   507,
      "to_use"              :   1,
      },


    # 508  : SCP-1660
    #      : (SCP-1660, "Unearthly Forest")
      508    :     {
      "name"                :   "SCP-1660",
      "document_name"       :   "Unearthly Forest",
      "popularity"          :   508,
      "to_use"              :   1,
      },


    # 509  : SCP-1033
    #      : (SCP-1033, "33 Second Man")
      509    :     {
      "name"                :   "SCP-1033",
      "document_name"       :   "33 Second Man",
      "popularity"          :   509,
      "to_use"              :   1,
      },


    # 510  : None
    #      : (None, [OMITTED])
      510    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   510,
      "to_use"              :   0,
      },


    # 511  : SCP-208
    #      : (SCP-208, '''"Bes"''')
      511    :     {
      "name"                :   "SCP-208",
      "document_name"       :   '''"Bes"''',
      "popularity"          :   511,
      "to_use"              :   1,
      },


    # 512  : SCP-145
    #      : (SCP-145, "Man-Absorbing Phone")
      512    :     {
      "name"                :   "SCP-145",
      "document_name"       :   "Man-Absorbing Phone",
      "popularity"          :   512,
      "to_use"              :   1,
      },


    # 513  : SCP-2460
    #      : (SCP-2460, "Dark Satellite")
      513    :     {
      "name"                :   "SCP-2460",
      "document_name"       :   "Dark Satellite",
      "popularity"          :   513,
      "to_use"              :   0,
      },


    # 514  : SCP-1162
    #      : (SCP-1162, "A Hole in the Wall")
      514    :     {
      "name"                :   "SCP-1162",
      "document_name"       :   "A Hole in the Wall",
      "popularity"          :   514,
      "to_use"              :   1,
      },


    # 515  : None
    #      : (None, [OMITTED])
      515    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   515,
      "to_use"              :   0,
      },


    # 516  : SCP-4008
    #      : (SCP-4008, "Wormwood")
      516    :     {
      "name"                :   "SCP-4008",
      "document_name"       :   "Wormwood",
      "popularity"          :   516,
      "to_use"              :   0,
      },


    # 517  : SCP-2790
    #      : (SCP-2790, "You've Got a Squid in Me")
      517    :     {
      "name"                :   "SCP-2790",
      "document_name"       :   "You've Got a Squid in Me",
      "popularity"          :   517,
      "to_use"              :   1,
      },


    # 518  : SCP-1722
    #      : (SCP-1722, "Curmudgeon's Cudgel")
      518    :     {
      "name"                :   "SCP-1722",
      "document_name"       :   "Curmudgeon's Cudgel",
      "popularity"          :   518,
      "to_use"              :   1,
      },


    # 519  : SCP-1147
    #      : (SCP-1147, "Adaptive Plum Tree")
      519    :     {
      "name"                :   "SCP-1147",
      "document_name"       :   "Adaptive Plum Tree",
      "popularity"          :   519,
      "to_use"              :   0,
      },


    # 520  : SCP-582
    #      : (SCP-582, "A Bundle of Stories")
      520    :     {
      "name"                :   "SCP-582",
      "document_name"       :   "A Bundle of Stories",
      "popularity"          :   520,
      "to_use"              :   0,
      },


    # 521  : SCP-3908
    #      : (SCP-3908, "SCP-3908")
      521    :     {
      "name"                :   "SCP-3908",
      "document_name"       :   "SCP-3908",
      "popularity"          :   521,
      "to_use"              :   1,
      },


    # 522  : SCP-1710
    #      : (SCP-1710, "Life as a Tree")
      522    :     {
      "name"                :   "SCP-1710",
      "document_name"       :   "Life as a Tree",
      "popularity"          :   522,
      "to_use"              :   0,
      },


    # 523  : SCP-098
    #      : (SCP-098, "Surgeon Crabs")
      523    :     {
      "name"                :   "SCP-098",
      "document_name"       :   "Surgeon Crabs",
      "popularity"          :   523,
      "to_use"              :   1,
      },


    # 524  : SCP-645
    #      : (SCP-645, "Mouth of Truth")
      524    :     {
      "name"                :   "SCP-645",
      "document_name"       :   "Mouth of Truth",
      "popularity"          :   524,
      "to_use"              :   1,
      },


    # 525  : SCP-5552
    #      : (SCP-5552, "Our Stolen Theory")
      525    :     {
      "name"                :   "SCP-5552",
      "document_name"       :   "Our Stolen Theory",
      "popularity"          :   525,
      "to_use"              :   0,
      },


    # 526  : SCP-616
    #      : (SCP-616, "The Vessel and the Gate")
      526    :     {
      "name"                :   "SCP-616",
      "document_name"       :   "The Vessel and the Gate",
      "popularity"          :   526,
      "to_use"              :   1,
      },


    # 527  : SCP-1761
    #      : (SCP-1761, "The Republic of Arnold Fitzwilliams")
      527    :     {
      "name"                :   "SCP-1761",
      "document_name"       :   "The Republic of Arnold Fitzwilliams",
      "popularity"          :   527,
      "to_use"              :   1,
      },


    # 528  : SCP-1304
    #      : (SCP-1304, "Metafictional Rebirth Ritual")
      528    :     {
      "name"                :   "SCP-1304",
      "document_name"       :   "Metafictional Rebirth Ritual",
      "popularity"          :   528,
      "to_use"              :   0,
      },


    # 529  : SCP-629
    #      : (SCP-629, "Mr. Brass")
      529    :     {
      "name"                :   "SCP-629",
      "document_name"       :   "Mr. Brass",
      "popularity"          :   529,
      "to_use"              :   1,
      },


    # 530  : SCP-1123
    #      : (SCP-1123, "Atrocity Skull")
      530    :     {
      "name"                :   "SCP-1123",
      "document_name"       :   "Atrocity Skull",
      "popularity"          :   530,
      "to_use"              :   1,
      },


    # 531  : SCP-1011
    #      : (SCP-1011, "Humanization Process")
      531    :     {
      "name"                :   "SCP-1011",
      "document_name"       :   "Humanization Process",
      "popularity"          :   531,
      "to_use"              :   1,
      },


    # 532  : SCP-3305
    #      : (SCP-3305, "The Father, The Son, and The Holy Toast")
      532    :     {
      "name"                :   "SCP-3305",
      "document_name"       :   "The Father, The Son, and The Holy Toast",
      "popularity"          :   532,
      "to_use"              :   0,
      },


    # 533  : None
    #      : (None, [OMITTED])
      533    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   533,
      "to_use"              :   0,
      },


    # 534  : SCP-3240
    #      : (SCP-3240, "The Bones Of What You Believe")
      534    :     {
      "name"                :   "SCP-3240",
      "document_name"       :   "The Bones Of What You Believe",
      "popularity"          :   534,
      "to_use"              :   0,
      },


    # 535  : SCP-1127
    #      : (SCP-1127, "A Film Festival")
      535    :     {
      "name"                :   "SCP-1127",
      "document_name"       :   "A Film Festival",
      "popularity"          :   535,
      "to_use"              :   0,
      },


    # 536  : SCP-1103
    #      : (SCP-1103, "Dr. Wondertainment Young Surgeon's Transplant Kit")
      536    :     {
      "name"                :   "SCP-1103",
      "document_name"       :   "Dr. Wondertainment Young Surgeon's Transplant Kit",
      "popularity"          :   536,
      "to_use"              :   1,
      },


    # 537  : SCP-514
    #      : (SCP-514, "A Flock of Doves")
      537    :     {
      "name"                :   "SCP-514",
      "document_name"       :   "A Flock of Doves",
      "popularity"          :   537,
      "to_use"              :   0,
      },


    # 538  : SCP-1860
    #      : (SCP-1860, "Its Bleeding Song")
      538    :     {
      "name"                :   "SCP-1860",
      "document_name"       :   "Its Bleeding Song",
      "popularity"          :   538,
      "to_use"              :   1,
      },


    # 539  : SCP-270
    #      : (SCP-270, "Secluded Telephone")
      539    :     {
      "name"                :   "SCP-270",
      "document_name"       :   "Secluded Telephone",
      "popularity"          :   539,
      "to_use"              :   0,
      },


    # 540  : SCP-4002
    #      : (SCP-4002, "The Black Moon Howls From Beyond The Edge Of Time")
      540    :     {
      "name"                :   "SCP-4002",
      "document_name"       :   "The Black Moon Howls From Beyond The Edge Of Time",
      "popularity"          :   540,
      "to_use"              :   0,
      },


    # 541  : None
    #      : (None, [OMITTED])
      541    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   541,
      "to_use"              :   0,
      },


    # 542  : SCP-2002
    #      : (SCP-2002, "A Dead Future")
      542    :     {
      "name"                :   "SCP-2002",
      "document_name"       :   "A Dead Future",
      "popularity"          :   542,
      "to_use"              :   0,
      },


    # 543  : SCP-1719
    #      : (SCP-1719, "The Harrison-Grey Effect")
      543    :     {
      "name"                :   "SCP-1719",
      "document_name"       :   "The Harrison-Grey Effect",
      "popularity"          :   543,
      "to_use"              :   1,
      },


    # 544  : SCP-445
    #      : (SCP-445, '''"Dr. Wondertainment's Super Paper"''')
      544    :     {
      "name"                :   "SCP-445",
      "document_name"       :   '''"Dr. Wondertainment's Super Paper"''',
      "popularity"          :   544,
      "to_use"              :   1,
      },


    # 545  : SCP-3929
    #      : (SCP-3929, "boner pill by dado")
      545    :     {
      "name"                :   "SCP-3929",
      "document_name"       :   "boner pill by dado",
      "popularity"          :   545,
      "to_use"              :   1,
      },


    # 546  : SCP-2746
    #      : (SCP-2746, "████ is dead.")
      546    :     {
      "name"                :   "SCP-2746",
      "document_name"       :   "████ is dead.",
      "popularity"          :   546,
      "to_use"              :   0,
      },


    # 547  : SCP-2014
    #      : (SCP-2014, "Zsar Magoth")
      547    :     {
      "name"                :   "SCP-2014",
      "document_name"       :   "Zsar Magoth",
      "popularity"          :   547,
      "to_use"              :   1,
      },


    # 548  : SCP-1859
    #      : (SCP-1859, "Life Over Geological Time")
      548    :     {
      "name"                :   "SCP-1859",
      "document_name"       :   "Life Over Geological Time",
      "popularity"          :   548,
      "to_use"              :   0,
      },


    # 549  : SCP-2578
    #      : (SCP-2578, '''"This Machine Kills Fascists"''')
      549    :     {
      "name"                :   "SCP-2578",
      "document_name"       :   '''"This Machine Kills Fascists"''',
      "popularity"          :   549,
      "to_use"              :   0,
      },


    # 550  : SCP-2004
    #      : (SCP-2004, "Personal Data Assistants of the Gods")
      550    :     {
      "name"                :   "SCP-2004",
      "document_name"       :   "Personal Data Assistants of the Gods",
      "popularity"          :   550,
      "to_use"              :   1,
      },


    # 551  : SCP-1541
    #      : (SCP-1541, "The Drunken God")
      551    :     {
      "name"                :   "SCP-1541",
      "document_name"       :   "The Drunken God",
      "popularity"          :   551,
      "to_use"              :   0,
      },


    # 552  : None
    #      : (None, [OMITTED])
      552    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   552,
      "to_use"              :   0,
      },


    # 553  : SCP-4338
    #      : (SCP-4338, "Vulcan, the Disaster")
      553    :     {
      "name"                :   "SCP-4338",
      "document_name"       :   "Vulcan, the Disaster",
      "popularity"          :   553,
      "to_use"              :   0,
      },


    # 554  : SCP-4498
    #      : (SCP-4498, "The Plurality of Jack Bright")
      554    :     {
      "name"                :   "SCP-4498",
      "document_name"       :   "The Plurality of Jack Bright",
      "popularity"          :   554,
      "to_use"              :   0,
      },


    # 555  : SCP-2200
    #      : (SCP-2200, "Soulberg")
      555    :     {
      "name"                :   "SCP-2200",
      "document_name"       :   "Soulberg",
      "popularity"          :   555,
      "to_use"              :   1,
      },


    # 556  : SCP-687
    #      : (SCP-687, "NOIR")
      556    :     {
      "name"                :   "SCP-687",
      "document_name"       :   "NOIR",
      "popularity"          :   556,
      "to_use"              :   1,
      },


    # 557  : SCP-119
    #      : (SCP-119, "Timecrowave")
      557    :     {
      "name"                :   "SCP-119",
      "document_name"       :   "Timecrowave",
      "popularity"          :   557,
      "to_use"              :   1,
      },


    # 558  : SCP-4517
    #      : (SCP-4517, "Not Very ??")
      558    :     {
      "name"                :   "SCP-4517",
      "document_name"       :   "Not Very ??",
      "popularity"          :   558,
      "to_use"              :   0,
      },


    # 559  : SCP-2798
    #      : (SCP-2798, "This Dying World")
      559    :     {
      "name"                :   "SCP-2798",
      "document_name"       :   "This Dying World",
      "popularity"          :   559,
      "to_use"              :   0,
      },


    # 560  : SCP-409
    #      : (SCP-409, "Contagious Crystal")
      560    :     {
      "name"                :   "SCP-409",
      "document_name"       :   "Contagious Crystal",
      "popularity"          :   560,
      "to_use"              :   1,
      },


    # 561  : SCP-1535
    #      : (SCP-1535, "Purgatory")
      561    :     {
      "name"                :   "SCP-1535",
      "document_name"       :   "Purgatory",
      "popularity"          :   561,
      "to_use"              :   1,
      },


    # 562  : SCP-4003
    #      : (SCP-4003, "On Cowboys, Catholicism, and the Cretaceous")
      562    :     {
      "name"                :   "SCP-4003",
      "document_name"       :   "On Cowboys, Catholicism, and the Cretaceous",
      "popularity"          :   562,
      "to_use"              :   0,
      },


    # 563  : SCP-2501
    #      : (SCP-2501, "The Claw")
      563    :     {
      "name"                :   "SCP-2501",
      "document_name"       :   "The Claw",
      "popularity"          :   563,
      "to_use"              :   1,
      },


    # 564  : SCP-3980
    #      : (SCP-3980, "Blind Lead the Blind")
      564    :     {
      "name"                :   "SCP-3980",
      "document_name"       :   "Blind Lead the Blind",
      "popularity"          :   564,
      "to_use"              :   0,
      },


    # 565  : SCP-2190
    #      : (SCP-2190, "Phone Calls from Mom")
      565    :     {
      "name"                :   "SCP-2190",
      "document_name"       :   "Phone Calls from Mom",
      "popularity"          :   565,
      "to_use"              :   0,
      },


    # 566  : SCP-1015
    #      : (SCP-1015, "Poor Man's Midas")
      566    :     {
      "name"                :   "SCP-1015",
      "document_name"       :   "Poor Man's Midas",
      "popularity"          :   566,
      "to_use"              :   1,
      },


    # 567  : SCP-3936
    #      : (SCP-3936, "Working as Intended")
      567    :     {
      "name"                :   "SCP-3936",
      "document_name"       :   "Working as Intended",
      "popularity"          :   567,
      "to_use"              :   0,
      },


    # 568  : SCP-3998
    #      : (SCP-3998, "The Wicker Witch Lives")
      568    :     {
      "name"                :   "SCP-3998",
      "document_name"       :   "The Wicker Witch Lives",
      "popularity"          :   568,
      "to_use"              :   1,
      },


    # 569  : SCP-592
    #      : (SCP-592, "Inaccurate History Book")
      569    :     {
      "name"                :   "SCP-592",
      "document_name"       :   "Inaccurate History Book",
      "popularity"          :   569,
      "to_use"              :   1,
      },


    # 570  : SCP-3009
    #      : (SCP-3009, "Hi, I'm Your Snappelganger!")
      570    :     {
      "name"                :   "SCP-3009",
      "document_name"       :   "Hi, I'm Your Snappelganger!",
      "popularity"          :   570,
      "to_use"              :   1,
      },


    # 571  : SCP-3340
    #      : (SCP-3340, "You Think, Therefore We Are")
      571    :     {
      "name"                :   "SCP-3340",
      "document_name"       :   "You Think, Therefore We Are",
      "popularity"          :   571,
      "to_use"              :   0,
      },


    # 572  : None
    #      : (None, [OMITTED])
      572    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   572,
      "to_use"              :   0,
      },


    # 573  : SCP-2820
    #      : (SCP-2820, "Vaishnavastra")
      573    :     {
      "name"                :   "SCP-2820",
      "document_name"       :   "Vaishnavastra",
      "popularity"          :   573,
      "to_use"              :   1,
      },


    # 574  : None
    #      : (None, [OMITTED])
      574    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   574,
      "to_use"              :   0,
      },


    # 575  : SCP-957
    #      : (SCP-957, "Baiting")
      575    :     {
      "name"                :   "SCP-957",
      "document_name"       :   "Baiting",
      "popularity"          :   575,
      "to_use"              :   0,
      },


    # 576  : SCP-511
    #      : (SCP-511, "Basement Cat")
      576    :     {
      "name"                :   "SCP-511",
      "document_name"       :   "Basement Cat",
      "popularity"          :   576,
      "to_use"              :   0,
      },


    # 577  : SCP-408
    #      : (SCP-408, "Illusory Butterflies")
      577    :     {
      "name"                :   "SCP-408",
      "document_name"       :   "Illusory Butterflies",
      "popularity"          :   577,
      "to_use"              :   1,
      },


    # 578  : SCP-3636
    #      : (SCP-3636, "World's Greatest Jukebox")
      578    :     {
      "name"                :   "SCP-3636",
      "document_name"       :   "World's Greatest Jukebox",
      "popularity"          :   578,
      "to_use"              :   1,
      },


    # 579  : SCP-032
    #      : (SCP-032, "Brothers' Bride")
      579    :     {
      "name"                :   "SCP-032",
      "document_name"       :   "Brothers' Bride",
      "popularity"          :   579,
      "to_use"              :   1,
      },


    # 580  : SCP-1319
    #      : (SCP-1319, "The Split-Up")
      580    :     {
      "name"                :   "SCP-1319",
      "document_name"       :   "The Split-Up",
      "popularity"          :   580,
      "to_use"              :   1,
      },


    # 581  : SCP-1059
    #      : (SCP-1059, "Infectious Censorship")
      581    :     {
      "name"                :   "SCP-1059",
      "document_name"       :   "Infectious Censorship",
      "popularity"          :   581,
      "to_use"              :   0,
      },


    # 582  : SCP-5858
    #      : (SCP-5858, "The Kindness of Strangers")
      582    :     {
      "name"                :   "SCP-5858",
      "document_name"       :   "The Kindness of Strangers",
      "popularity"          :   582,
      "to_use"              :   0,
      },


    # 583  : SCP-3241
    #      : (SCP-3241, "The SS Sommerfeld")
      583    :     {
      "name"                :   "SCP-3241",
      "document_name"       :   "The SS Sommerfeld",
      "popularity"          :   583,
      "to_use"              :   0,
      },


    # 584  : SCP-2933
    #      : (SCP-2933, "Mr. Scary")
      584    :     {
      "name"                :   "SCP-2933",
      "document_name"       :   "Mr. Scary",
      "popularity"          :   584,
      "to_use"              :   0,
      },


    # 585  : SCP-1340
    #      : (SCP-1340, "The Fraternal Order of Cave Mantas")
      585    :     {
      "name"                :   "SCP-1340",
      "document_name"       :   "The Fraternal Order of Cave Mantas",
      "popularity"          :   585,
      "to_use"              :   1,
      },


    # 586  : SCP-1357
    #      : (SCP-1357, "The Children's Park")
      586    :     {
      "name"                :   "SCP-1357",
      "document_name"       :   "The Children's Park",
      "popularity"          :   586,
      "to_use"              :   0,
      },


    # 587  : SCP-1844
    #      : (SCP-1844, "Crater at 31.7███° N, 35.1███° E")
      587    :     {
      "name"                :   "SCP-1844",
      "document_name"       :   "Crater at 31.7███° N, 35.1███° E",
      "popularity"          :   587,
      "to_use"              :   0,
      },


    # 588  : SCP-967
    #      : (SCP-967, "Infinite Scrapyard")
      588    :     {
      "name"                :   "SCP-967",
      "document_name"       :   "Infinite Scrapyard",
      "popularity"          :   588,
      "to_use"              :   0,
      },


    # 589  : SCP-3844
    #      : (SCP-3844, "To Slay A Dragon")
      589    :     {
      "name"                :   "SCP-3844",
      "document_name"       :   "To Slay A Dragon",
      "popularity"          :   589,
      "to_use"              :   0,
      },


    # 590  : SCP-1679
    #      : (SCP-1679, "Post-Mortem Peoples' Choice")
      590    :     {
      "name"                :   "SCP-1679",
      "document_name"       :   "Post-Mortem Peoples' Choice",
      "popularity"          :   590,
      "to_use"              :   0,
      },


    # 591  : SCP-1310
    #      : (SCP-1310, "Examination Room 10")
      591    :     {
      "name"                :   "SCP-1310",
      "document_name"       :   "Examination Room 10",
      "popularity"          :   591,
      "to_use"              :   0,
      },


    # 592  : SCP-583
    #      : (SCP-583, "Deathly Video Tape")
      592    :     {
      "name"                :   "SCP-583",
      "document_name"       :   "Deathly Video Tape",
      "popularity"          :   592,
      "to_use"              :   1,
      },


    # 593  : SCP-018
    #      : (SCP-018, "Super Ball")
      593    :     {
      "name"                :   "SCP-018",
      "document_name"       :   "Super Ball",
      "popularity"          :   593,
      "to_use"              :   1,
      },


    # 594  : SCP-2115
    #      : (SCP-2115, "Meet Other People")
      594    :     {
      "name"                :   "SCP-2115",
      "document_name"       :   "Meet Other People",
      "popularity"          :   594,
      "to_use"              :   0,
      },


    # 595  : SCP-726
    #      : (SCP-726, "Reconstructive Maggots")
      595    :     {
      "name"                :   "SCP-726",
      "document_name"       :   "Reconstructive Maggots",
      "popularity"          :   595,
      "to_use"              :   0,
      },


    # 596  : SCP-4633
    #      : (SCP-4633, "Rock, Paper, Yog-Sothoth")
      596    :     {
      "name"                :   "SCP-4633",
      "document_name"       :   "Rock, Paper, Yog-Sothoth",
      "popularity"          :   596,
      "to_use"              :   0,
      },


    # 597  : SCP-3128
    #      : (SCP-3128, "Let's Play Monopoly!")
      597    :     {
      "name"                :   "SCP-3128",
      "document_name"       :   "Let's Play Monopoly!",
      "popularity"          :   597,
      "to_use"              :   1,
      },


    # 598  : SCP-748
    #      : (SCP-748, "Industrial Dissolution")
      598    :     {
      "name"                :   "SCP-748",
      "document_name"       :   "Industrial Dissolution",
      "popularity"          :   598,
      "to_use"              :   0,
      },


    # 599  : SCP-172
    #      : (SCP-172, "The Gearman")
      599    :     {
      "name"                :   "SCP-172",
      "document_name"       :   "The Gearman",
      "popularity"          :   599,
      "to_use"              :   1,
      },


    # 600  : SCP-1682
    #      : (SCP-1682, "Solar Parasite")
      600    :     {
      "name"                :   "SCP-1682",
      "document_name"       :   "Solar Parasite",
      "popularity"          :   600,
      "to_use"              :   0,
      },


    # 601  : SCP-469
    #      : (SCP-469, "Many-Winged Angel")
      601    :     {
      "name"                :   "SCP-469",
      "document_name"       :   "Many-Winged Angel",
      "popularity"          :   601,
      "to_use"              :   1,
      },


    # 602  : SCP-5003
    #      : (SCP-5003, "Powerless")
      602    :     {
      "name"                :   "SCP-5003",
      "document_name"       :   "Powerless",
      "popularity"          :   602,
      "to_use"              :   0,
      },


    # 603  : SCP-4057
    #      : (SCP-4057, "Save Her")
      603    :     {
      "name"                :   "SCP-4057",
      "document_name"       :   "Save Her",
      "popularity"          :   603,
      "to_use"              :   1,
      },


    # 604  : SCP-2090
    #      : (SCP-2090, "Potentially XK Tim Duncan")
      604    :     {
      "name"                :   "SCP-2090",
      "document_name"       :   "Potentially XK Tim Duncan",
      "popularity"          :   604,
      "to_use"              :   0,
      },


    # 605  : SCP-743
    #      : (SCP-743, "A Chocolate Fountain")
      605    :     {
      "name"                :   "SCP-743",
      "document_name"       :   "A Chocolate Fountain",
      "popularity"          :   605,
      "to_use"              :   1,
      },


    # 606  : SCP-4005
    #      : (SCP-4005, "The Holy and Heavenly City of Fabled China")
      606    :     {
      "name"                :   "SCP-4005",
      "document_name"       :   "The Holy and Heavenly City of Fabled China",
      "popularity"          :   606,
      "to_use"              :   1,
      },


    # 607  : None
    #      : (None, [OMITTED])
      607    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   607,
      "to_use"              :   0,
      },


    # 608  : SCP-838
    #      : (SCP-838, "The Dream Job")
      608    :     {
      "name"                :   "SCP-838",
      "document_name"       :   "The Dream Job",
      "popularity"          :   608,
      "to_use"              :   0,
      },


    # 609  : SCP-1152
    #      : (SCP-1152, "A Common Raccoon")
      609    :     {
      "name"                :   "SCP-1152",
      "document_name"       :   "A Common Raccoon",
      "popularity"          :   609,
      "to_use"              :   1,
      },


    # 610  : None
    #      : (None, [OMITTED])
      610    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   610,
      "to_use"              :   0,
      },


    # 611  : SCP-1520
    #      : (SCP-1520, "An Elderly Monk")
      611    :     {
      "name"                :   "SCP-1520",
      "document_name"       :   "An Elderly Monk",
      "popularity"          :   611,
      "to_use"              :   1,
      },


    # 612  : SCP-698
    #      : (SCP-698, "Judgmental Turtle")
      612    :     {
      "name"                :   "SCP-698",
      "document_name"       :   "Judgmental Turtle",
      "popularity"          :   612,
      "to_use"              :   1,
      },


    # 613  : SCP-590
    #      : (SCP-590, "He Feels Your Pain")
      613    :     {
      "name"                :   "SCP-590",
      "document_name"       :   "He Feels Your Pain",
      "popularity"          :   613,
      "to_use"              :   1,
      },


    # 614  : SCP-3984
    #      : (SCP-3984, "Poking Death with a Stick")
      614    :     {
      "name"                :   "SCP-3984",
      "document_name"       :   "Poking Death with a Stick",
      "popularity"          :   614,
      "to_use"              :   0,
      },


    # 615  : SCP-1839
    #      : (SCP-1839, "Reproductive Methods of Bony Fish")
      615    :     {
      "name"                :   "SCP-1839",
      "document_name"       :   "Reproductive Methods of Bony Fish",
      "popularity"          :   615,
      "to_use"              :   1,
      },


    # 616  : SCP-1702
    #      : (SCP-1702, "The French Hive")
      616    :     {
      "name"                :   "SCP-1702",
      "document_name"       :   "The French Hive",
      "popularity"          :   616,
      "to_use"              :   1,
      },


    # 617  : SCP-1510
    #      : (SCP-1510, "The Tarnished Legionnaire")
      617    :     {
      "name"                :   "SCP-1510",
      "document_name"       :   "The Tarnished Legionnaire",
      "popularity"          :   617,
      "to_use"              :   1,
      },


    # 618  : SCP-1045
    #      : (SCP-1045, "Candle of Life")
      618    :     {
      "name"                :   "SCP-1045",
      "document_name"       :   "Candle of Life",
      "popularity"          :   618,
      "to_use"              :   1,
      },


    # 619  : SCP-765
    #      : (SCP-765, "Duck Pond")
      619    :     {
      "name"                :   "SCP-765",
      "document_name"       :   "Duck Pond",
      "popularity"          :   619,
      "to_use"              :   0,
      },


    # 620  : SCP-5370
    #      : (SCP-5370, "Chessland")
      620    :     {
      "name"                :   "SCP-5370",
      "document_name"       :   "Chessland",
      "popularity"          :   620,
      "to_use"              :   0,
      },


    # 621  : SCP-4144
    #      : (SCP-4144, "The Most Important Meal Of The Day")
      621    :     {
      "name"                :   "SCP-4144",
      "document_name"       :   "The Most Important Meal Of The Day",
      "popularity"          :   621,
      "to_use"              :   0,
      },


    # 622  : SCP-3022
    #      : (SCP-3022, "Hooked on a Feeling")
      622    :     {
      "name"                :   "SCP-3022",
      "document_name"       :   "Hooked on a Feeling",
      "popularity"          :   622,
      "to_use"              :   1,
      },


    # 623  : SCP-531
    #      : (SCP-531, "Paired Brass Guard Cats")
      623    :     {
      "name"                :   "SCP-531",
      "document_name"       :   "Paired Brass Guard Cats",
      "popularity"          :   623,
      "to_use"              :   1,
      },


    # 624  : SCP-2061
    #      : (SCP-2061, '''"Entire Local Family Chokes To Death On Single Calculator"''')
      624    :     {
      "name"                :   "SCP-2061",
      "document_name"       :   '''"Entire Local Family Chokes To Death On Single Calculator"''',
      "popularity"          :   624,
      "to_use"              :   1,
      },


    # 625  : SCP-123
    #      : (SCP-123, "Contained Miniature Black Hole")
      625    :     {
      "name"                :   "SCP-123",
      "document_name"       :   "Contained Miniature Black Hole",
      "popularity"          :   625,
      "to_use"              :   1,
      },


    # 626  : SCP-2017
    #      : (SCP-2017, "The Girl with the Made-Up Disease")
      626    :     {
      "name"                :   "SCP-2017",
      "document_name"       :   "The Girl with the Made-Up Disease",
      "popularity"          :   626,
      "to_use"              :   1,
      },


    # 627  : SCP-158
    #      : (SCP-158, "Soul Extractor")
      627    :     {
      "name"                :   "SCP-158",
      "document_name"       :   "Soul Extractor",
      "popularity"          :   627,
      "to_use"              :   1,
      },


    # 628  : SCP-689
    #      : (SCP-689, "Haunter in the Dark")
      628    :     {
      "name"                :   "SCP-689",
      "document_name"       :   "Haunter in the Dark",
      "popularity"          :   628,
      "to_use"              :   1,
      },


    # 629  : SCP-1548
    #      : (SCP-1548, "The Star, the Hateful")
      629    :     {
      "name"                :   "SCP-1548",
      "document_name"       :   "The Star, the Hateful",
      "popularity"          :   629,
      "to_use"              :   0,
      },


    # 630  : SCP-2331
    #      : (SCP-2331, "Scravecrow")
      630    :     {
      "name"                :   "SCP-2331",
      "document_name"       :   "Scravecrow",
      "popularity"          :   630,
      "to_use"              :   1,
      },


    # 631  : SCP-2094
    #      : (SCP-2094, "Motormouth")
      631    :     {
      "name"                :   "SCP-2094",
      "document_name"       :   "Motormouth",
      "popularity"          :   631,
      "to_use"              :   1,
      },


    # 632  : SCP-1883
    #      : (SCP-1883, "Gamification")
      632    :     {
      "name"                :   "SCP-1883",
      "document_name"       :   "Gamification",
      "popularity"          :   632,
      "to_use"              :   1,
      },


    # 633  : SCP-2505
    #      : (SCP-2505, "Entry Creation Wizard")
      633    :     {
      "name"                :   "SCP-2505",
      "document_name"       :   "Entry Creation Wizard",
      "popularity"          :   633,
      "to_use"              :   1,
      },


    # 634  : SCP-1638
    #      : (SCP-1638, "Silence")
      634    :     {
      "name"                :   "SCP-1638",
      "document_name"       :   "Silence",
      "popularity"          :   634,
      "to_use"              :   0,
      },


    # 635  : SCP-4746
    #      : (SCP-4746, "Marked for Death")
      635    :     {
      "name"                :   "SCP-4746",
      "document_name"       :   "Marked for Death",
      "popularity"          :   635,
      "to_use"              :   1,
      },


    # 636  : SCP-4040
    #      : (SCP-4040, "At The Bottom Of A Bottomless Pit")
      636    :     {
      "name"                :   "SCP-4040",
      "document_name"       :   "At The Bottom Of A Bottomless Pit",
      "popularity"          :   636,
      "to_use"              :   0,
      },


    # 637  : None
    #      : (None, [OMITTED])
      637    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   637,
      "to_use"              :   0,
      },


    # 638  : None
    #      : (None, [OMITTED])
      638    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   638,
      "to_use"              :   0,
      },


    # 639  : SCP-401
    #      : (SCP-401, "A Palm Tree")
      639    :     {
      "name"                :   "SCP-401",
      "document_name"       :   "A Palm Tree",
      "popularity"          :   639,
      "to_use"              :   1,
      },


    # 640  : None
    #      : (None, [OMITTED])
      640    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   640,
      "to_use"              :   0,
      },


    # 641  : SCP-3027
    #      : (SCP-3027, "Strong Language")
      641    :     {
      "name"                :   "SCP-3027",
      "document_name"       :   "Strong Language",
      "popularity"          :   641,
      "to_use"              :   1,
      },


    # 642  : SCP-2140
    #      : (SCP-2140, "Retroconverter")
      642    :     {
      "name"                :   "SCP-2140",
      "document_name"       :   "Retroconverter",
      "popularity"          :   642,
      "to_use"              :   0,
      },


    # 643  : None
    #      : (None, [OMITTED])
      643    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   643,
      "to_use"              :   0,
      },


    # 644  : SCP-201
    #      : (SCP-201, "The Empty World")
      644    :     {
      "name"                :   "SCP-201",
      "document_name"       :   "The Empty World",
      "popularity"          :   644,
      "to_use"              :   1,
      },


    # 645  : SCP-3088
    #      : (SCP-3088, "Law Of The Land")
      645    :     {
      "name"                :   "SCP-3088",
      "document_name"       :   "Law Of The Land",
      "popularity"          :   645,
      "to_use"              :   0,
      },


    # 646  : SCP-2165
    #      : (SCP-2165, "Irredeemable")
      646    :     {
      "name"                :   "SCP-2165",
      "document_name"       :   "Irredeemable",
      "popularity"          :   646,
      "to_use"              :   0,
      },


    # 647  : SCP-2019
    #      : (SCP-2019, "Gelatinous Brain Cube")
      647    :     {
      "name"                :   "SCP-2019",
      "document_name"       :   "Gelatinous Brain Cube",
      "popularity"          :   647,
      "to_use"              :   1,
      },


    # 648  : SCP-1879
    #      : (SCP-1879, "Indoor Salesman")
      648    :     {
      "name"                :   "SCP-1879",
      "document_name"       :   "Indoor Salesman",
      "popularity"          :   648,
      "to_use"              :   0,
      },


    # 649  : SCP-1382
    #      : (SCP-1382, "Save Our Souls")
      649    :     {
      "name"                :   "SCP-1382",
      "document_name"       :   "Save Our Souls",
      "popularity"          :   649,
      "to_use"              :   0,
      },


    # 650  : SCP-1588
    #      : (SCP-1588, "The Cliff Face")
      650    :     {
      "name"                :   "SCP-1588",
      "document_name"       :   "The Cliff Face",
      "popularity"          :   650,
      "to_use"              :   0,
      },


    # 651  : SCP-1012
    #      : (SCP-1012, "Secret Chord")
      651    :     {
      "name"                :   "SCP-1012",
      "document_name"       :   "Secret Chord",
      "popularity"          :   651,
      "to_use"              :   0,
      },


    # 652  : SCP-078
    #      : (SCP-078, "Guilt")
      652    :     {
      "name"                :   "SCP-078",
      "document_name"       :   "Guilt",
      "popularity"          :   652,
      "to_use"              :   1,
      },


    # 653  : SCP-2338
    #      : (SCP-2338, "An Unorthodox Adoption")
      653    :     {
      "name"                :   "SCP-2338",
      "document_name"       :   "An Unorthodox Adoption",
      "popularity"          :   653,
      "to_use"              :   1,
      },


    # 654  : SCP-2099
    #      : (SCP-2099, "Brain in a Jar")
      654    :     {
      "name"                :   "SCP-2099",
      "document_name"       :   "Brain in a Jar",
      "popularity"          :   654,
      "to_use"              :   0,
      },


    # 655  : SCP-1252
    #      : (SCP-1252, "A Half-Formed Idea")
      655    :     {
      "name"                :   "SCP-1252",
      "document_name"       :   "A Half-Formed Idea",
      "popularity"          :   655,
      "to_use"              :   1,
      },


    # 656  : SCP-3480
    #      : (SCP-3480, "Olympus Mons")
      656    :     {
      "name"                :   "SCP-3480",
      "document_name"       :   "Olympus Mons",
      "popularity"          :   656,
      "to_use"              :   0,
      },


    # 657  : SCP-2059
    #      : (SCP-2059, "Wall of Flesh")
      657    :     {
      "name"                :   "SCP-2059",
      "document_name"       :   "Wall of Flesh",
      "popularity"          :   657,
      "to_use"              :   1,
      },


    # 658  : SCP-2310
    #      : (SCP-2310, "The House That Makes You Sarah Palmer")
      658    :     {
      "name"                :   "SCP-2310",
      "document_name"       :   "The House That Makes You Sarah Palmer",
      "popularity"          :   658,
      "to_use"              :   0,
      },


    # 659  : SCP-1836
    #      : (SCP-1836, "Mother in the Ice")
      659    :     {
      "name"                :   "SCP-1836",
      "document_name"       :   "Mother in the Ice",
      "popularity"          :   659,
      "to_use"              :   0,
      },


    # 660  : SCP-091
    #      : (SCP-091, "Nostalgia")
      660    :     {
      "name"                :   "SCP-091",
      "document_name"       :   "Nostalgia",
      "popularity"          :   660,
      "to_use"              :   1,
      },


    # 661  : SCP-4281
    #      : (SCP-4281, "Stalled Conversation")
      661    :     {
      "name"                :   "SCP-4281",
      "document_name"       :   "Stalled Conversation",
      "popularity"          :   661,
      "to_use"              :   0,
      },


    # 662  : SCP-2991
    #      : (SCP-2991, '''"Scarf"''')
      662    :     {
      "name"                :   "SCP-2991",
      "document_name"       :   '''"Scarf"''',
      "popularity"          :   662,
      "to_use"              :   1,
      },


    # 663  : SCP-1619
    #      : (SCP-1619, "Site-45-C: Floor 24")
      663    :     {
      "name"                :   "SCP-1619",
      "document_name"       :   "Site-45-C: Floor 24",
      "popularity"          :   663,
      "to_use"              :   0,
      },


    # 664  : None
    #      : (None, [OMITTED])
      664    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   664,
      "to_use"              :   0,
      },


    # 665  : SCP-4098
    #      : (SCP-4098, "S-C-P, easy as 19-3-16!")
      665    :     {
      "name"                :   "SCP-4098",
      "document_name"       :   "S-C-P, easy as 19-3-16!",
      "popularity"          :   665,
      "to_use"              :   0,
      },


    # 666  : SCP-4242
    #      : (SCP-4242, "Foundations")
      666    :     {
      "name"                :   "SCP-4242",
      "document_name"       :   "Foundations",
      "popularity"          :   666,
      "to_use"              :   0,
      },


    # 667  : SCP-2513
    #      : (SCP-2513, "Also, Carthage Must Be Destroyed")
      667    :     {
      "name"                :   "SCP-2513",
      "document_name"       :   "Also, Carthage Must Be Destroyed",
      "popularity"          :   667,
      "to_use"              :   0,
      },


    # 668  : SCP-1074
    #      : (SCP-1074, "Stendhal's Nightmare")
      668    :     {
      "name"                :   "SCP-1074",
      "document_name"       :   "Stendhal's Nightmare",
      "popularity"          :   668,
      "to_use"              :   1,
      },


    # 669  : SCP-431
    #      : (SCP-431, "Dr. Gideon")
      669    :     {
      "name"                :   "SCP-431",
      "document_name"       :   "Dr. Gideon",
      "popularity"          :   669,
      "to_use"              :   0,
      },


    # 670  : SCP-352
    #      : (SCP-352, '''"Baba Yaga"''')
      670    :     {
      "name"                :   "SCP-352",
      "document_name"       :   '''"Baba Yaga"''',
      "popularity"          :   670,
      "to_use"              :   1,
      },


    # 671  : SCP-5045
    #      : (SCP-5045, "You Get Used to It")
      671    :     {
      "name"                :   "SCP-5045",
      "document_name"       :   "You Get Used to It",
      "popularity"          :   671,
      "to_use"              :   0,
      },


    # 672  : SCP-1020
    #      : (SCP-1020, "An Important Letter")
      672    :     {
      "name"                :   "SCP-1020",
      "document_name"       :   "An Important Letter",
      "popularity"          :   672,
      "to_use"              :   1,
      },


    # 673  : SCP-099
    #      : (SCP-099, "The Portrait")
      673    :     {
      "name"                :   "SCP-099",
      "document_name"       :   "The Portrait",
      "popularity"          :   673,
      "to_use"              :   1,
      },


    # 674  : SCP-3017
    #      : (SCP-3017, "Person of Interest")
      674    :     {
      "name"                :   "SCP-3017",
      "document_name"       :   "Person of Interest",
      "popularity"          :   674,
      "to_use"              :   0,
      },


    # 675  : SCP-736
    #      : (SCP-736, "The Iapetus Anomaly")
      675    :     {
      "name"                :   "SCP-736",
      "document_name"       :   "The Iapetus Anomaly",
      "popularity"          :   675,
      "to_use"              :   0,
      },


    # 676  : SCP-919
    #      : (SCP-919, "Needy Mirror")
      676    :     {
      "name"                :   "SCP-919",
      "document_name"       :   "Needy Mirror",
      "popularity"          :   676,
      "to_use"              :   1,
      },


    # 677  : None
    #      : (None, [OMITTED])
      677    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   677,
      "to_use"              :   0,
      },


    # 678  : SCP-2900
    #      : (SCP-2900, "Nobody Gets Left Behind")
      678    :     {
      "name"                :   "SCP-2900",
      "document_name"       :   "Nobody Gets Left Behind",
      "popularity"          :   678,
      "to_use"              :   1,
      },


    # 679  : SCP-2022
    #      : (SCP-2022, "Sunlight Pills™")
      679    :     {
      "name"                :   "SCP-2022",
      "document_name"       :   "Sunlight Pills™",
      "popularity"          :   679,
      "to_use"              :   1,
      },


    # 680  : SCP-057
    #      : (SCP-057, "The Daily Grind")
      680    :     {
      "name"                :   "SCP-057",
      "document_name"       :   "The Daily Grind",
      "popularity"          :   680,
      "to_use"              :   0,
      },


    # 681  : SCP-3143
    #      : (SCP-3143, "Murphy Law in… The Foundation Always Rings Twice!")
      681    :     {
      "name"                :   "SCP-3143",
      "document_name"       :   "Murphy Law in… The Foundation Always Rings Twice!",
      "popularity"          :   681,
      "to_use"              :   0,
      },


    # 682  : SCP-3513
    #      : (SCP-3513, "The Brain That Ate Itself")
      682    :     {
      "name"                :   "SCP-3513",
      "document_name"       :   "The Brain That Ate Itself",
      "popularity"          :   682,
      "to_use"              :   0,
      },


    # 683  : None
    #      : (None, [OMITTED])
      683    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   683,
      "to_use"              :   0,
      },


    # 684  : None
    #      : (None, [OMITTED])
      684    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   684,
      "to_use"              :   0,
      },


    # 685  : SCP-2133
    #      : (SCP-2133, "Our Land, Our Bondage")
      685    :     {
      "name"                :   "SCP-2133",
      "document_name"       :   "Our Land, Our Bondage",
      "popularity"          :   685,
      "to_use"              :   0,
      },


    # 686  : SCP-1177
    #      : (SCP-1177, "The Coupon Cutter")
      686    :     {
      "name"                :   "SCP-1177",
      "document_name"       :   "The Coupon Cutter",
      "popularity"          :   686,
      "to_use"              :   1,
      },


    # 687  : SCP-115
    #      : (SCP-115, "Miniature Dump Truck")
      687    :     {
      "name"                :   "SCP-115",
      "document_name"       :   "Miniature Dump Truck",
      "popularity"          :   687,
      "to_use"              :   1,
      },


    # 688  : SCP-3774
    #      : (SCP-3774, "My Heart DEETs Faster For You")
      688    :     {
      "name"                :   "SCP-3774",
      "document_name"       :   "My Heart DEETs Faster For You",
      "popularity"          :   688,
      "to_use"              :   0,
      },


    # 689  : SCP-2432
    #      : (SCP-2432, "Room Service")
      689    :     {
      "name"                :   "SCP-2432",
      "document_name"       :   "Room Service",
      "popularity"          :   689,
      "to_use"              :   0,
      },


    # 690  : SCP-2996
    #      : (SCP-2996, "ERROR / ERROR")
      690    :     {
      "name"                :   "SCP-2996",
      "document_name"       :   "ERROR / ERROR",
      "popularity"          :   690,
      "to_use"              :   0,
      },


    # 691  : SCP-071
    #      : (SCP-071, "Degenerative Metamorphic Entity")
      691    :     {
      "name"                :   "SCP-071",
      "document_name"       :   "Degenerative Metamorphic Entity",
      "popularity"          :   691,
      "to_use"              :   1,
      },


    # 692  : SCP-1788
    #      : (SCP-1788, "The Adults")
      692    :     {
      "name"                :   "SCP-1788",
      "document_name"       :   "The Adults",
      "popularity"          :   692,
      "to_use"              :   0,
      },


    # 693  : SCP-296
    #      : (SCP-296, "Armed Containment Site-03")
      693    :     {
      "name"                :   "SCP-296",
      "document_name"       :   "Armed Containment Site-03",
      "popularity"          :   693,
      "to_use"              :   0,
      },


    # 694  : SCP-064
    #      : (SCP-064, "Flawed von Neumann Structure")
      694    :     {
      "name"                :   "SCP-064",
      "document_name"       :   "Flawed von Neumann Structure",
      "popularity"          :   694,
      "to_use"              :   0,
      },


    # 695  : SCP-2805
    #      : (SCP-2805, "Disney on Ice")
      695    :     {
      "name"                :   "SCP-2805",
      "document_name"       :   "Disney on Ice",
      "popularity"          :   695,
      "to_use"              :   1,
      },


    # 696  : None
    #      : (None, [OMITTED])
      696    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   696,
      "to_use"              :   0,
      },


    # 697  : SCP-1639
    #      : (SCP-1639, "The Jazz Station")
      697    :     {
      "name"                :   "SCP-1639",
      "document_name"       :   "The Jazz Station",
      "popularity"          :   697,
      "to_use"              :   1,
      },


    # 698  : SCP-523
    #      : (SCP-523, "The Most Unhelpful Object On Earth")
      698    :     {
      "name"                :   "SCP-523",
      "document_name"       :   "The Most Unhelpful Object On Earth",
      "popularity"          :   698,
      "to_use"              :   0,
      },


    # 699  : SCP-4661
    #      : (SCP-4661, "Sin City")
      699    :     {
      "name"                :   "SCP-4661",
      "document_name"       :   "Sin City",
      "popularity"          :   699,
      "to_use"              :   0,
      },


    # 700  : SCP-3074
    #      : (SCP-3074, "Kafka's Parking Garage")
      700    :     {
      "name"                :   "SCP-3074",
      "document_name"       :   "Kafka's Parking Garage",
      "popularity"          :   700,
      "to_use"              :   0,
      },


    # 701  : SCP-3338
    #      : (SCP-3338, "Otamatone Wants To Be Your Roommate~")
      701    :     {
      "name"                :   "SCP-3338",
      "document_name"       :   "Otamatone Wants To Be Your Roommate~",
      "popularity"          :   701,
      "to_use"              :   0,
      },


    # 702  : SCP-3021
    #      : (SCP-3021, "Q=")
      702    :     {
      "name"                :   "SCP-3021",
      "document_name"       :   "Q=",
      "popularity"          :   702,
      "to_use"              :   0,
      },


    # 703  : SCP-2874
    #      : (SCP-2874, "Don-Burten Explosive Dev13e")
      703    :     {
      "name"                :   "SCP-2874",
      "document_name"       :   "Don-Burten Explosive Dev13e",
      "popularity"          :   703,
      "to_use"              :   1,
      },


    # 704  : SCP-1396
    #      : (SCP-1396, "Jovian Kill-Sats")
      704    :     {
      "name"                :   "SCP-1396",
      "document_name"       :   "Jovian Kill-Sats",
      "popularity"          :   704,
      "to_use"              :   0,
      },


    # 705  : SCP-1269
    #      : (SCP-1269, "Stalker Mailbox")
      705    :     {
      "name"                :   "SCP-1269",
      "document_name"       :   "Stalker Mailbox",
      "popularity"          :   705,
      "to_use"              :   0,
      },


    # 706  : SCP-1036
    #      : (SCP-1036, "Nkondi")
      706    :     {
      "name"                :   "SCP-1036",
      "document_name"       :   "Nkondi",
      "popularity"          :   706,
      "to_use"              :   1,
      },


    # 707  : SCP-054
    #      : (SCP-054, "Water Nymph")
      707    :     {
      "name"                :   "SCP-054",
      "document_name"       :   "Water Nymph",
      "popularity"          :   707,
      "to_use"              :   1,
      },


    # 708  : SCP-001
    #      : (SCP-001, "Awaiting De-classification [Blocked]")
      708    :     {
      "name"                :   "SCP-001",
      "document_name"       :   "Awaiting De-classification [Blocked]",
      "popularity"          :   708,
      "to_use"              :   0,
      },


    # 709  : None
    #      : (None, [OMITTED])
      709    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   709,
      "to_use"              :   0,
      },


    # 710  : SCP-2282
    #      : (SCP-2282, "Goat.")
      710    :     {
      "name"                :   "SCP-2282",
      "document_name"       :   "Goat.",
      "popularity"          :   710,
      "to_use"              :   0,
      },


    # 711  : SCP-940
    #      : (SCP-940, "Araneae Marionettes")
      711    :     {
      "name"                :   "SCP-940",
      "document_name"       :   "Araneae Marionettes",
      "popularity"          :   711,
      "to_use"              :   1,
      },


    # 712  : SCP-297
    #      : (SCP-297, '''"Steely Dan"''')
      712    :     {
      "name"                :   "SCP-297",
      "document_name"       :   '''"Steely Dan"''',
      "popularity"          :   712,
      "to_use"              :   1,
      },


    # 713  : None
    #      : (None, [OMITTED])
      713    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   713,
      "to_use"              :   0,
      },


    # 714  : SCP-134
    #      : (SCP-134, "Star-Eyed Child")
      714    :     {
      "name"                :   "SCP-134",
      "document_name"       :   "Star-Eyed Child",
      "popularity"          :   714,
      "to_use"              :   1,
      },


    # 715  : SCP-3866
    #      : (SCP-3866, "Youth In Asia by dado")
      715    :     {
      "name"                :   "SCP-3866",
      "document_name"       :   "Youth In Asia by dado",
      "popularity"          :   715,
      "to_use"              :   1,
      },


    # 716  : SCP-872
    #      : (SCP-872, "The Tattered Farmer")
      716    :     {
      "name"                :   "SCP-872",
      "document_name"       :   "The Tattered Farmer",
      "popularity"          :   716,
      "to_use"              :   1,
      },


    # 717  : SCP-252
    #      : (SCP-252, "Humboldt Squid")
      717    :     {
      "name"                :   "SCP-252",
      "document_name"       :   "Humboldt Squid",
      "popularity"          :   717,
      "to_use"              :   1,
      },


    # 718  : SCP-666
    #      : (SCP-666, "Spirit Lodge")
      718    :     {
      "name"                :   "SCP-666",
      "document_name"       :   "Spirit Lodge",
      "popularity"          :   718,
      "to_use"              :   0,
      },


    # 719  : SCP-2293
    #      : (SCP-2293, "An Inside Joke")
      719    :     {
      "name"                :   "SCP-2293",
      "document_name"       :   "An Inside Joke",
      "popularity"          :   719,
      "to_use"              :   0,
      },


    # 720  : SCP-2686
    #      : (SCP-2686, "Moon Wizard")
      720    :     {
      "name"                :   "SCP-2686",
      "document_name"       :   "Moon Wizard",
      "popularity"          :   720,
      "to_use"              :   0,
      },


    # 721  : SCP-414
    #      : (SCP-414, "Regardless, I Might Prefer Myself Sick")
      721    :     {
      "name"                :   "SCP-414",
      "document_name"       :   "Regardless, I Might Prefer Myself Sick",
      "popularity"          :   721,
      "to_use"              :   0,
      },


    # 722  : SCP-1241
    #      : (SCP-1241, "Livin' With Werewolves")
      722    :     {
      "name"                :   "SCP-1241",
      "document_name"       :   "Livin' With Werewolves",
      "popularity"          :   722,
      "to_use"              :   0,
      },


    # 723  : SCP-753
    #      : (SCP-753, "Automatic Artist")
      723    :     {
      "name"                :   "SCP-753",
      "document_name"       :   "Automatic Artist",
      "popularity"          :   723,
      "to_use"              :   1,
      },


    # 724  : SCP-4004
    #      : (SCP-4004, "A Dream Come True")
      724    :     {
      "name"                :   "SCP-4004",
      "document_name"       :   "A Dream Come True",
      "popularity"          :   724,
      "to_use"              :   0,
      },


    # 725  : SCP-2049
    #      : (SCP-2049, "The Interdimensional Weather Station")
      725    :     {
      "name"                :   "SCP-2049",
      "document_name"       :   "The Interdimensional Weather Station",
      "popularity"          :   725,
      "to_use"              :   0,
      },


    # 726  : SCP-1577
    #      : (SCP-1577, "A Flare Gun")
      726    :     {
      "name"                :   "SCP-1577",
      "document_name"       :   "A Flare Gun",
      "popularity"          :   726,
      "to_use"              :   1,
      },


    # 727  : SCP-107
    #      : (SCP-107, "The Turtle Shell")
      727    :     {
      "name"                :   "SCP-107",
      "document_name"       :   "The Turtle Shell",
      "popularity"          :   727,
      "to_use"              :   1,
      },


    # 728  : SCP-5554
    #      : (SCP-5554, "Aki Aki! 🍊🐻")
      728    :     {
      "name"                :   "SCP-5554",
      "document_name"       :   "Aki Aki! 🍊🐻",
      "popularity"          :   728,
      "to_use"              :   0,
      },


    # 729  : SCP-2232
    #      : (SCP-2232, "Birdphone. Think Different.")
      729    :     {
      "name"                :   "SCP-2232",
      "document_name"       :   "Birdphone. Think Different.",
      "popularity"          :   729,
      "to_use"              :   1,
      },


    # 730  : SCP-1306
    #      : (SCP-1306, "Potion of Summon Bird")
      730    :     {
      "name"                :   "SCP-1306",
      "document_name"       :   "Potion of Summon Bird",
      "popularity"          :   730,
      "to_use"              :   1,
      },


    # 731  : SCP-1184
    #      : (SCP-1184, "Truth")
      731    :     {
      "name"                :   "SCP-1184",
      "document_name"       :   "Truth",
      "popularity"          :   731,
      "to_use"              :   1,
      },


    # 732  : SCP-1523
    #      : (SCP-1523, "Soul Brother")
      732    :     {
      "name"                :   "SCP-1523",
      "document_name"       :   "Soul Brother",
      "popularity"          :   732,
      "to_use"              :   1,
      },


    # 733  : SCP-1047
    #      : (SCP-1047, "Vengefully Ironic Street Signs")
      733    :     {
      "name"                :   "SCP-1047",
      "document_name"       :   "Vengefully Ironic Street Signs",
      "popularity"          :   733,
      "to_use"              :   1,
      },


    # 734  : SCP-602
    #      : (SCP-602, "The Sculptor of SoHo")
      734    :     {
      "name"                :   "SCP-602",
      "document_name"       :   "The Sculptor of SoHo",
      "popularity"          :   734,
      "to_use"              :   0,
      },


    # 735  : SCP-4007
    #      : (SCP-4007, "Kagemusha")
      735    :     {
      "name"                :   "SCP-4007",
      "document_name"       :   "Kagemusha",
      "popularity"          :   735,
      "to_use"              :   0,
      },


    # 736  : SCP-323
    #      : (SCP-323, "Wendigo Skull")
      736    :     {
      "name"                :   "SCP-323",
      "document_name"       :   "Wendigo Skull",
      "popularity"          :   736,
      "to_use"              :   1,
      },


    # 737  : SCP-877
    #      : (SCP-877, "University Microchips")
      737    :     {
      "name"                :   "SCP-877",
      "document_name"       :   "University Microchips",
      "popularity"          :   737,
      "to_use"              :   1,
      },


    # 738  : SCP-4231
    #      : (SCP-4231, "The Montauk House")
      738    :     {
      "name"                :   "SCP-4231",
      "document_name"       :   "The Montauk House",
      "popularity"          :   738,
      "to_use"              :   0,
      },


    # 739  : SCP-2610
    #      : (SCP-2610, "Procreation")
      739    :     {
      "name"                :   "SCP-2610",
      "document_name"       :   "Procreation",
      "popularity"          :   739,
      "to_use"              :   0,
      },


    # 740  : SCP-4069
    #      : (SCP-4069, "Out of Range")
      740    :     {
      "name"                :   "SCP-4069",
      "document_name"       :   "Out of Range",
      "popularity"          :   740,
      "to_use"              :   0,
      },


    # 741  : SCP-2076
    #      : (SCP-2076, '''"Shooting Yourself Can Increase Your Bullet Resistance"''')
      741    :     {
      "name"                :   "SCP-2076",
      "document_name"       :   '''"Shooting Yourself Can Increase Your Bullet Resistance"''',
      "popularity"          :   741,
      "to_use"              :   0,
      },


    # 742  : SCP-2703
    #      : (SCP-2703, "For a Good Time Call")
      742    :     {
      "name"                :   "SCP-2703",
      "document_name"       :   "For a Good Time Call",
      "popularity"          :   742,
      "to_use"              :   0,
      },


    # 743  : SCP-1899
    #      : (SCP-1899, "Suspended Bullet")
      743    :     {
      "name"                :   "SCP-1899",
      "document_name"       :   "Suspended Bullet",
      "popularity"          :   743,
      "to_use"              :   0,
      },


    # 744  : SCP-988
    #      : (SCP-988, "Unopenable Chest")
      744    :     {
      "name"                :   "SCP-988",
      "document_name"       :   "Unopenable Chest",
      "popularity"          :   744,
      "to_use"              :   1,
      },


    # 745  : SCP-4465
    #      : (SCP-4465, "No Man is an Island")
      745    :     {
      "name"                :   "SCP-4465",
      "document_name"       :   "No Man is an Island",
      "popularity"          :   745,
      "to_use"              :   1,
      },


    # 746  : SCP-4011
    #      : (SCP-4011, "History is Written by the Victors")
      746    :     {
      "name"                :   "SCP-4011",
      "document_name"       :   "History is Written by the Victors",
      "popularity"          :   746,
      "to_use"              :   0,
      },


    # 747  : SCP-783
    #      : (SCP-783, "There Was A Crooked Man")
      747    :     {
      "name"                :   "SCP-783",
      "document_name"       :   "There Was A Crooked Man",
      "popularity"          :   747,
      "to_use"              :   0,
      },


    # 748  : SCP-3288
    #      : (SCP-3288, "The Aristocrats")
      748    :     {
      "name"                :   "SCP-3288",
      "document_name"       :   "The Aristocrats",
      "popularity"          :   748,
      "to_use"              :   1,
      },


    # 749  : SCP-2472
    #      : (SCP-2472, "A Small Metal Air Coupler That Is Apparently Not Anomalous")
      749    :     {
      "name"                :   "SCP-2472",
      "document_name"       :   "A Small Metal Air Coupler That Is Apparently Not Anomalous",
      "popularity"          :   749,
      "to_use"              :   0,
      },


    # 750  : SCP-147
    #      : (SCP-147, "Anachronistic Television")
      750    :     {
      "name"                :   "SCP-147",
      "document_name"       :   "Anachronistic Television",
      "popularity"          :   750,
      "to_use"              :   1,
      },


    # 751  : SCP-4950
    #      : (SCP-4950, "Triple Six Five Forked Tongue")
      751    :     {
      "name"                :   "SCP-4950",
      "document_name"       :   "Triple Six Five Forked Tongue",
      "popularity"          :   751,
      "to_use"              :   1,
      },


    # 752  : SCP-1372
    #      : (SCP-1372, "The Utter West")
      752    :     {
      "name"                :   "SCP-1372",
      "document_name"       :   "The Utter West",
      "popularity"          :   752,
      "to_use"              :   0,
      },


    # 753  : SCP-335
    #      : (SCP-335, '''One Hundred and Fifty 3.5" Floppy Disks''')
      753    :     {
      "name"                :   "SCP-335",
      "document_name"       :   '''One Hundred and Fifty 3.5" Floppy Disks''',
      "popularity"          :   753,
      "to_use"              :   1,
      },


    # 754  : SCP-3562
    #      : (SCP-3562, "See Me After Class")
      754    :     {
      "name"                :   "SCP-3562",
      "document_name"       :   "See Me After Class",
      "popularity"          :   754,
      "to_use"              :   0,
      },


    # 755  : SCP-3989
    #      : (SCP-3989, "The Bone Orchard")
      755    :     {
      "name"                :   "SCP-3989",
      "document_name"       :   "The Bone Orchard",
      "popularity"          :   755,
      "to_use"              :   1,
      },


    # 756  : SCP-715
    #      : (SCP-715, "My Face That I May Be")
      756    :     {
      "name"                :   "SCP-715",
      "document_name"       :   "My Face That I May Be",
      "popularity"          :   756,
      "to_use"              :   1,
      },


    # 757  : SCP-2170
    #      : (SCP-2170, "The Clown Vaccine")
      757    :     {
      "name"                :   "SCP-2170",
      "document_name"       :   "The Clown Vaccine",
      "popularity"          :   757,
      "to_use"              :   0,
      },


    # 758  : SCP-3052
    #      : (SCP-3052, "Disturbed")
      758    :     {
      "name"                :   "SCP-3052",
      "document_name"       :   "Disturbed",
      "popularity"          :   758,
      "to_use"              :   1,
      },


    # 759  : SCP-1864
    #      : (SCP-1864, "The Lonely Liar")
      759    :     {
      "name"                :   "SCP-1864",
      "document_name"       :   "The Lonely Liar",
      "popularity"          :   759,
      "to_use"              :   0,
      },


    # 760  : SCP-122
    #      : (SCP-122, "No More Monsters")
      760    :     {
      "name"                :   "SCP-122",
      "document_name"       :   "No More Monsters",
      "popularity"          :   760,
      "to_use"              :   1,
      },


    # 761  : SCP-330
    #      : (SCP-330, "Take Only Two")
      761    :     {
      "name"                :   "SCP-330",
      "document_name"       :   "Take Only Two",
      "popularity"          :   761,
      "to_use"              :   1,
      },


    # 762  : SCP-3780
    #      : (SCP-3780, "Who Shot J.F.K.?")
      762    :     {
      "name"                :   "SCP-3780",
      "document_name"       :   "Who Shot J.F.K.?",
      "popularity"          :   762,
      "to_use"              :   0,
      },


    # 763  : SCP-2951
    #      : (SCP-2951, "10,000 Years")
      763    :     {
      "name"                :   "SCP-2951",
      "document_name"       :   "10,000 Years",
      "popularity"          :   763,
      "to_use"              :   0,
      },


    # 764  : SCP-2031
    #      : (SCP-2031, "Ant Farm")
      764    :     {
      "name"                :   "SCP-2031",
      "document_name"       :   "Ant Farm",
      "popularity"          :   764,
      "to_use"              :   1,
      },


    # 765  : SCP-1985
    #      : (SCP-1985, "Recovered K-Class Scenario Research Device")
      765    :     {
      "name"                :   "SCP-1985",
      "document_name"       :   "Recovered K-Class Scenario Research Device",
      "popularity"          :   765,
      "to_use"              :   1,
      },


    # 766  : SCP-3848
    #      : (SCP-3848, "History Exists for the Memorable")
      766    :     {
      "name"                :   "SCP-3848",
      "document_name"       :   "History Exists for the Memorable",
      "popularity"          :   766,
      "to_use"              :   0,
      },


    # 767  : SCP-3319
    #      : (SCP-3319, "The Clusterfuckalypse")
      767    :     {
      "name"                :   "SCP-3319",
      "document_name"       :   "The Clusterfuckalypse",
      "popularity"          :   767,
      "to_use"              :   0,
      },


    # 768  : SCP-3049
    #      : (SCP-3049, "To Make an Apple Pie from Scratch")
      768    :     {
      "name"                :   "SCP-3049",
      "document_name"       :   "To Make an Apple Pie from Scratch",
      "popularity"          :   768,
      "to_use"              :   1,
      },


    # 769  : SCP-3145
    #      : (SCP-3145, "Self-Insert")
      769    :     {
      "name"                :   "SCP-3145",
      "document_name"       :   "Self-Insert",
      "popularity"          :   769,
      "to_use"              :   1,
      },


    # 770  : SCP-046
    #      : (SCP-046, '''"Predatory" Holly Bush''')
      770    :     {
      "name"                :   "SCP-046",
      "document_name"       :   '''"Predatory" Holly Bush''',
      "popularity"          :   770,
      "to_use"              :   0,
      },


    # 771  : SCP-599
    #      : (SCP-599, "Uncharted City")
      771    :     {
      "name"                :   "SCP-599",
      "document_name"       :   "Uncharted City",
      "popularity"          :   771,
      "to_use"              :   0,
      },


    # 772  : SCP-230
    #      : (SCP-230, "The Gayest Man Alive")
      772    :     {
      "name"                :   "SCP-230",
      "document_name"       :   "The Gayest Man Alive",
      "popularity"          :   772,
      "to_use"              :   1,
      },


    # 773  : SCP-3890
    #      : (SCP-3890, "Forget-Me-Not")
      773    :     {
      "name"                :   "SCP-3890",
      "document_name"       :   "Forget-Me-Not",
      "popularity"          :   773,
      "to_use"              :   0,
      },


    # 774  : SCP-2886
    #      : (SCP-2886, "Planet-Hopping Volcano")
      774    :     {
      "name"                :   "SCP-2886",
      "document_name"       :   "Planet-Hopping Volcano",
      "popularity"          :   774,
      "to_use"              :   0,
      },


    # 775  : None
    #      : (None, [OMITTED])
      775    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   775,
      "to_use"              :   0,
      },


    # 776  : SCP-1122
    #      : (SCP-1122, "The House of Tomorrow")
      776    :     {
      "name"                :   "SCP-1122",
      "document_name"       :   "The House of Tomorrow",
      "popularity"          :   776,
      "to_use"              :   0,
      },


    # 777  : SCP-2762
    #      : (SCP-2762, "Moon Snakes")
      777    :     {
      "name"                :   "SCP-2762",
      "document_name"       :   "Moon Snakes",
      "popularity"          :   777,
      "to_use"              :   0,
      },


    # 778  : SCP-1376
    #      : (SCP-1376, "Documentary Camcorder")
      778    :     {
      "name"                :   "SCP-1376",
      "document_name"       :   "Documentary Camcorder",
      "popularity"          :   778,
      "to_use"              :   1,
      },


    # 779  : SCP-1543
    #      : (SCP-1543, "Efrain's Dialtone")
      779    :     {
      "name"                :   "SCP-1543",
      "document_name"       :   "Efrain's Dialtone",
      "popularity"          :   779,
      "to_use"              :   0,
      },


    # 780  : SCP-670
    #      : (SCP-670, "Family of Cotton")
      780    :     {
      "name"                :   "SCP-670",
      "document_name"       :   "Family of Cotton",
      "popularity"          :   780,
      "to_use"              :   1,
      },


    # 781  : SCP-312
    #      : (SCP-312, "Atmospheric Jellyfish")
      781    :     {
      "name"                :   "SCP-312",
      "document_name"       :   "Atmospheric Jellyfish",
      "popularity"          :   781,
      "to_use"              :   1,
      },


    # 782  : SCP-081
    #      : (SCP-081, "Spontaneous Combustion Virus")
      782    :     {
      "name"                :   "SCP-081",
      "document_name"       :   "Spontaneous Combustion Virus",
      "popularity"          :   782,
      "to_use"              :   1,
      },


    # 783  : SCP-2268
    #      : (SCP-2268, "Loaf Page")
      783    :     {
      "name"                :   "SCP-2268",
      "document_name"       :   "Loaf Page",
      "popularity"          :   783,
      "to_use"              :   0,
      },


    # 784  : SCP-2712
    #      : (SCP-2712, "The Entry for SCP-2712 in the Foundation Database")
      784    :     {
      "name"                :   "SCP-2712",
      "document_name"       :   "The Entry for SCP-2712 in the Foundation Database",
      "popularity"          :   784,
      "to_use"              :   0,
      },


    # 785  : SCP-2095
    #      : (SCP-2095, "The Siege of Gyaros")
      785    :     {
      "name"                :   "SCP-2095",
      "document_name"       :   "The Siege of Gyaros",
      "popularity"          :   785,
      "to_use"              :   0,
      },


    # 786  : SCP-2070
    #      : (SCP-2070, "The Fingers of God")
      786    :     {
      "name"                :   "SCP-2070",
      "document_name"       :   "The Fingers of God",
      "popularity"          :   786,
      "to_use"              :   1,
      },


    # 787  : SCP-1850
    #      : (SCP-1850, "Accipiter sopwithii")
      787    :     {
      "name"                :   "SCP-1850",
      "document_name"       :   "Accipiter sopwithii",
      "popularity"          :   787,
      "to_use"              :   1,
      },


    # 788  : SCP-3494
    #      : (SCP-3494, "Waste Management by dado")
      788    :     {
      "name"                :   "SCP-3494",
      "document_name"       :   "Waste Management by dado",
      "popularity"          :   788,
      "to_use"              :   1,
      },


    # 789  : SCP-2308
    #      : (SCP-2308, "Futures Trading")
      789    :     {
      "name"                :   "SCP-2308",
      "document_name"       :   "Futures Trading",
      "popularity"          :   789,
      "to_use"              :   0,
      },


    # 790  : SCP-2305
    #      : (SCP-2305, "great ideas that are TOTALY USELESS (lulz)")
      790    :     {
      "name"                :   "SCP-2305",
      "document_name"       :   "great ideas that are TOTALY USELESS (lulz)",
      "popularity"          :   790,
      "to_use"              :   1,
      },


    # 791  : SCP-1561
    #      : (SCP-1561, "The Tyrant's Pretext")
      791    :     {
      "name"                :   "SCP-1561",
      "document_name"       :   "The Tyrant's Pretext",
      "popularity"          :   791,
      "to_use"              :   1,
      },


    # 792  : SCP-039
    #      : (SCP-039, "Proboscis Engineers")
      792    :     {
      "name"                :   "SCP-039",
      "document_name"       :   "Proboscis Engineers",
      "popularity"          :   792,
      "to_use"              :   1,
      },


    # 793  : SCP-206
    #      : (SCP-206, "The Voyager")
      793    :     {
      "name"                :   "SCP-206",
      "document_name"       :   "The Voyager",
      "popularity"          :   793,
      "to_use"              :   0,
      },


    # 794  : SCP-3396
    #      : (SCP-3396, "The Empyrean Parasite")
      794    :     {
      "name"                :   "SCP-3396",
      "document_name"       :   "The Empyrean Parasite",
      "popularity"          :   794,
      "to_use"              :   0,
      },


    # 795  : SCP-2107
    #      : (SCP-2107, "Diet Ghost™")
      795    :     {
      "name"                :   "SCP-2107",
      "document_name"       :   "Diet Ghost™",
      "popularity"          :   795,
      "to_use"              :   1,
      },


    # 796  : SCP-909
    #      : (SCP-909, "Mr. Forgetful")
      796    :     {
      "name"                :   "SCP-909",
      "document_name"       :   "Mr. Forgetful",
      "popularity"          :   796,
      "to_use"              :   1,
      },


    # 797  : SCP-735
    #      : (SCP-735, "Insult Box")
      797    :     {
      "name"                :   "SCP-735",
      "document_name"       :   "Insult Box",
      "popularity"          :   797,
      "to_use"              :   1,
      },


    # 798  : SCP-034
    #      : (SCP-034, "Obsidian Ritual Knife")
      798    :     {
      "name"                :   "SCP-034",
      "document_name"       :   "Obsidian Ritual Knife",
      "popularity"          :   798,
      "to_use"              :   1,
      },


    # 799  : None
    #      : (None, [OMITTED])
      799    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   799,
      "to_use"              :   0,
      },


    # 800  : SCP-1781
    #      : (SCP-1781, "The Moonlight Theater")
      800    :     {
      "name"                :   "SCP-1781",
      "document_name"       :   "The Moonlight Theater",
      "popularity"          :   800,
      "to_use"              :   0,
      },


    # 801  : SCP-784
    #      : (SCP-784, "Christmas Cheer")
      801    :     {
      "name"                :   "SCP-784",
      "document_name"       :   "Christmas Cheer",
      "popularity"          :   801,
      "to_use"              :   0,
      },


    # 802  : SCP-1046
    #      : (SCP-1046, "A House Without a Bedroom")
      802    :     {
      "name"                :   "SCP-1046",
      "document_name"       :   "A House Without a Bedroom",
      "popularity"          :   802,
      "to_use"              :   0,
      },


    # 803  : SCP-1474
    #      : (SCP-1474, "In Solidarity with Xiu Lidao, Great Sage, Equal of Heaven")
      803    :     {
      "name"                :   "SCP-1474",
      "document_name"       :   "In Solidarity with Xiu Lidao, Great Sage, Equal of Heaven",
      "popularity"          :   803,
      "to_use"              :   0,
      },


    # 804  : SCP-1841
    #      : (SCP-1841, "So Much To See, So Much Unseen")
      804    :     {
      "name"                :   "SCP-1841",
      "document_name"       :   "So Much To See, So Much Unseen",
      "popularity"          :   804,
      "to_use"              :   1,
      },


    # 805  : SCP-110
    #      : (SCP-110, "Subterranean City")
      805    :     {
      "name"                :   "SCP-110",
      "document_name"       :   "Subterranean City",
      "popularity"          :   805,
      "to_use"              :   0,
      },


    # 806  : SCP-1763
    #      : (SCP-1763, "Found Space Theatre")
      806    :     {
      "name"                :   "SCP-1763",
      "document_name"       :   "Found Space Theatre",
      "popularity"          :   806,
      "to_use"              :   0,
      },


    # 807  : SCP-437
    #      : (SCP-437, "Summer of '91")
      807    :     {
      "name"                :   "SCP-437",
      "document_name"       :   "Summer of '91",
      "popularity"          :   807,
      "to_use"              :   1,
      },


    # 808  : SCP-696
    #      : (SCP-696, "Abyssal Typewriter")
      808    :     {
      "name"                :   "SCP-696",
      "document_name"       :   "Abyssal Typewriter",
      "popularity"          :   808,
      "to_use"              :   1,
      },


    # 809  : SCP-1512
    #      : (SCP-1512, "Irrational Root")
      809    :     {
      "name"                :   "SCP-1512",
      "document_name"       :   "Irrational Root",
      "popularity"          :   809,
      "to_use"              :   0,
      },


    # 810  : SCP-155
    #      : (SCP-155, "Infinite Speed Computer")
      810    :     {
      "name"                :   "SCP-155",
      "document_name"       :   "Infinite Speed Computer",
      "popularity"          :   810,
      "to_use"              :   1,
      },


    # 811  : SCP-478
    #      : (SCP-478, "Tooth Fairies")
      811    :     {
      "name"                :   "SCP-478",
      "document_name"       :   "Tooth Fairies",
      "popularity"          :   811,
      "to_use"              :   1,
      },


    # 812  : SCP-2481
    #      : (SCP-2481, "Kill the Suns")
      812    :     {
      "name"                :   "SCP-2481",
      "document_name"       :   "Kill the Suns",
      "popularity"          :   812,
      "to_use"              :   0,
      },


    # 813  : SCP-2701
    #      : (SCP-2701, "True Solitary")
      813    :     {
      "name"                :   "SCP-2701",
      "document_name"       :   "True Solitary",
      "popularity"          :   813,
      "to_use"              :   0,
      },


    # 814  : SCP-242
    #      : (SCP-242, '''Self "Cleaning" Pool''')
      814    :     {
      "name"                :   "SCP-242",
      "document_name"       :   '''Self "Cleaning" Pool''',
      "popularity"          :   814,
      "to_use"              :   0,
      },


    # 815  : SCP-044
    #      : (SCP-044, "World War II Era Molecular-Fission Cannon")
      815    :     {
      "name"                :   "SCP-044",
      "document_name"       :   "World War II Era Molecular-Fission Cannon",
      "popularity"          :   815,
      "to_use"              :   0,
      },


    # 816  : SCP-043
    #      : (SCP-043, "The Beatle")
      816    :     {
      "name"                :   "SCP-043",
      "document_name"       :   "The Beatle",
      "popularity"          :   816,
      "to_use"              :   1,
      },


    # 817  : SCP-5545
    #      : (SCP-5545, "𝙰 𝙱 𝙽 𝙾 𝚁 𝙼 𝙰 𝙻 𝙸 𝚃 𝚈")
      817    :     {
      "name"                :   "SCP-5545",
      "document_name"       :   "𝙰 𝙱 𝙽 𝙾 𝚁 𝙼 𝙰 𝙻 𝙸 𝚃 𝚈",
      "popularity"          :   817,
      "to_use"              :   0,
      },


    # 818  : SCP-3133
    #      : (SCP-3133, "An Email to O5-05")
      818    :     {
      "name"                :   "SCP-3133",
      "document_name"       :   "An Email to O5-05",
      "popularity"          :   818,
      "to_use"              :   0,
      },


    # 819  : SCP-2553
    #      : (SCP-2553, "Juridical Person")
      819    :     {
      "name"                :   "SCP-2553",
      "document_name"       :   "Juridical Person",
      "popularity"          :   819,
      "to_use"              :   0,
      },


    # 820  : SCP-911
    #      : (SCP-911, "Egyptian Book of the Dead")
      820    :     {
      "name"                :   "SCP-911",
      "document_name"       :   "Egyptian Book of the Dead",
      "popularity"          :   820,
      "to_use"              :   1,
      },


    # 821  : SCP-2664
    #      : (SCP-2664, "Redline")
      821    :     {
      "name"                :   "SCP-2664",
      "document_name"       :   "Redline",
      "popularity"          :   821,
      "to_use"              :   0,
      },


    # 822  : SCP-2412
    #      : (SCP-2412, "Cassandra Bot")
      822    :     {
      "name"                :   "SCP-2412",
      "document_name"       :   "Cassandra Bot",
      "popularity"          :   822,
      "to_use"              :   1,
      },


    # 823  : SCP-1329
    #      : (SCP-1329, "The Aquarium")
      823    :     {
      "name"                :   "SCP-1329",
      "document_name"       :   "The Aquarium",
      "popularity"          :   823,
      "to_use"              :   0,
      },


    # 824  : SCP-1008
    #      : (SCP-1008, "Exile Stone")
      824    :     {
      "name"                :   "SCP-1008",
      "document_name"       :   "Exile Stone",
      "popularity"          :   824,
      "to_use"              :   1,
      },


    # 825  : SCP-374
    #      : (SCP-374, "Oracular Guillotine")
      825    :     {
      "name"                :   "SCP-374",
      "document_name"       :   "Oracular Guillotine",
      "popularity"          :   825,
      "to_use"              :   1,
      },


    # 826  : SCP-5131
    #      : (SCP-5131, "D-13131")
      826    :     {
      "name"                :   "SCP-5131",
      "document_name"       :   "D-13131",
      "popularity"          :   826,
      "to_use"              :   0,
      },


    # 827  : None
    #      : (None, [OMITTED])
      827    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   827,
      "to_use"              :   0,
      },


    # 828  : SCP-2408
    #      : (SCP-2408, "Orok's Fall")
      828    :     {
      "name"                :   "SCP-2408",
      "document_name"       :   "Orok's Fall",
      "popularity"          :   828,
      "to_use"              :   0,
      },


    # 829  : SCP-554
    #      : (SCP-554, "The Perfect Murder")
      829    :     {
      "name"                :   "SCP-554",
      "document_name"       :   "The Perfect Murder",
      "popularity"          :   829,
      "to_use"              :   0,
      },


    # 830  : SCP-1156
    #      : (SCP-1156, "Wellington the Wonder Horse")
      830    :     {
      "name"                :   "SCP-1156",
      "document_name"       :   "Wellington the Wonder Horse",
      "popularity"          :   830,
      "to_use"              :   1,
      },


    # 831  : SCP-363
    #      : (SCP-363, "Not Centipedes")
      831    :     {
      "name"                :   "SCP-363",
      "document_name"       :   "Not Centipedes",
      "popularity"          :   831,
      "to_use"              :   1,
      },


    # 832  : SCP-138
    #      : (SCP-138, "The Ever-Living Man")
      832    :     {
      "name"                :   "SCP-138",
      "document_name"       :   "The Ever-Living Man",
      "popularity"          :   832,
      "to_use"              :   1,
      },


    # 833  : SCP-5983
    #      : (SCP-5983, "Nuke York, Nuke York")
      833    :     {
      "name"                :   "SCP-5983",
      "document_name"       :   "Nuke York, Nuke York",
      "popularity"          :   833,
      "to_use"              :   0,
      },


    # 834  : SCP-1176
    #      : (SCP-1176, "Mellified Man")
      834    :     {
      "name"                :   "SCP-1176",
      "document_name"       :   "Mellified Man",
      "popularity"          :   834,
      "to_use"              :   1,
      },


    # 835  : SCP-1076
    #      : (SCP-1076, "The Only Child")
      835    :     {
      "name"                :   "SCP-1076",
      "document_name"       :   "The Only Child",
      "popularity"          :   835,
      "to_use"              :   1,
      },


    # 836  : SCP-1364
    #      : (SCP-1364, "Ultra-Vulnerable Mammal")
      836    :     {
      "name"                :   "SCP-1364",
      "document_name"       :   "Ultra-Vulnerable Mammal",
      "popularity"          :   836,
      "to_use"              :   1,
      },


    # 837  : SCP-713
    #      : (SCP-713, "Click Anywhere Computer")
      837    :     {
      "name"                :   "SCP-713",
      "document_name"       :   "Click Anywhere Computer",
      "popularity"          :   837,
      "to_use"              :   1,
      },


    # 838  : SCP-807
    #      : (SCP-807, "Heart Attack on a Plate")
      838    :     {
      "name"                :   "SCP-807",
      "document_name"       :   "Heart Attack on a Plate",
      "popularity"          :   838,
      "to_use"              :   1,
      },


    # 839  : SCP-5935
    #      : (SCP-5935, "Blood and the Breaking of My Heart")
      839    :     {
      "name"                :   "SCP-5935",
      "document_name"       :   "Blood and the Breaking of My Heart",
      "popularity"          :   839,
      "to_use"              :   1,
      },


    # 840  : SCP-1753
    #      : (SCP-1753, "Vertigo")
      840    :     {
      "name"                :   "SCP-1753",
      "document_name"       :   "Vertigo",
      "popularity"          :   840,
      "to_use"              :   1,
      },


    # 841  : None
    #      : (None, [OMITTED])
      841    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   841,
      "to_use"              :   0,
      },


    # 842  : SCP-1007
    #      : (SCP-1007, "Mr. Life and Mr. Death")
      842    :     {
      "name"                :   "SCP-1007",
      "document_name"       :   "Mr. Life and Mr. Death",
      "popularity"          :   842,
      "to_use"              :   1,
      },


    # 843  : SCP-095
    #      : (SCP-095, "The Atomic Adventures of Ronnie Ray-Gun")
      843    :     {
      "name"                :   "SCP-095",
      "document_name"       :   "The Atomic Adventures of Ronnie Ray-Gun",
      "popularity"          :   843,
      "to_use"              :   1,
      },


    # 844  : None
    #      : (None, [OMITTED])
      844    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   844,
      "to_use"              :   0,
      },


    # 845  : SCP-4321
    #      : (SCP-4321, "Sometimes I Look At The Sky So I Can Feel Small")
      845    :     {
      "name"                :   "SCP-4321",
      "document_name"       :   "Sometimes I Look At The Sky So I Can Feel Small",
      "popularity"          :   845,
      "to_use"              :   0,
      },


    # 846  : SCP-3054
    #      : (SCP-3054, "Cragstaff Sanitarium")
      846    :     {
      "name"                :   "SCP-3054",
      "document_name"       :   "Cragstaff Sanitarium",
      "popularity"          :   846,
      "to_use"              :   0,
      },


    # 847  : SCP-2912
    #      : (SCP-2912, "Clowny Clown Clown")
      847    :     {
      "name"                :   "SCP-2912",
      "document_name"       :   "Clowny Clown Clown",
      "popularity"          :   847,
      "to_use"              :   1,
      },


    # 848  : SCP-2112
    #      : (SCP-2112, "And the Meek Shall Inherit the Earth")
      848    :     {
      "name"                :   "SCP-2112",
      "document_name"       :   "And the Meek Shall Inherit the Earth",
      "popularity"          :   848,
      "to_use"              :   0,
      },


    # 849  : SCP-1514
    #      : (SCP-1514, "Star Wars")
      849    :     {
      "name"                :   "SCP-1514",
      "document_name"       :   "Star Wars",
      "popularity"          :   849,
      "to_use"              :   1,
      },


    # 850  : SCP-505
    #      : (SCP-505, "Ink Stain")
      850    :     {
      "name"                :   "SCP-505",
      "document_name"       :   "Ink Stain",
      "popularity"          :   850,
      "to_use"              :   1,
      },


    # 851  : SCP-4949
    #      : (SCP-4949, "Dr. Wondertainment's dr playtime kit for the kiddostm ft. dado")
      851    :     {
      "name"                :   "SCP-4949",
      "document_name"       :   "Dr. Wondertainment's dr playtime kit for the kiddostm ft. dado",
      "popularity"          :   851,
      "to_use"              :   1,
      },


    # 852  : SCP-3449
    #      : (SCP-3449, "The Things Left Unsaid")
      852    :     {
      "name"                :   "SCP-3449",
      "document_name"       :   "The Things Left Unsaid",
      "popularity"          :   852,
      "to_use"              :   1,
      },


    # 853  : SCP-3838
    #      : (SCP-3838, "Nomads of the 4th-Dimensional Steppe")
      853    :     {
      "name"                :   "SCP-3838",
      "document_name"       :   "Nomads of the 4th-Dimensional Steppe",
      "popularity"          :   853,
      "to_use"              :   0,
      },


    # 854  : SCP-2987
    #      : (SCP-2987, "Invictus")
      854    :     {
      "name"                :   "SCP-2987",
      "document_name"       :   "Invictus",
      "popularity"          :   854,
      "to_use"              :   1,
      },


    # 855  : SCP-2622
    #      : (SCP-2622, "Ambassador from the Mole People")
      855    :     {
      "name"                :   "SCP-2622",
      "document_name"       :   "Ambassador from the Mole People",
      "popularity"          :   855,
      "to_use"              :   1,
      },


    # 856  : SCP-1030
    #      : (SCP-1030, "Anything Golem")
      856    :     {
      "name"                :   "SCP-1030",
      "document_name"       :   "Anything Golem",
      "popularity"          :   856,
      "to_use"              :   1,
      },


    # 857  : SCP-795
    #      : (SCP-795, "Reality-Bending Cat")
      857    :     {
      "name"                :   "SCP-795",
      "document_name"       :   "Reality-Bending Cat",
      "popularity"          :   857,
      "to_use"              :   1,
      },


    # 858  : SCP-3220
    #      : (SCP-3220, "Panopticon II")
      858    :     {
      "name"                :   "SCP-3220",
      "document_name"       :   "Panopticon II",
      "popularity"          :   858,
      "to_use"              :   0,
      },


    # 859  : None
    #      : (None, [OMITTED])
      859    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   859,
      "to_use"              :   0,
      },


    # 860  : None
    #      : (None, [OMITTED])
      860    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   860,
      "to_use"              :   0,
      },


    # 861  : SCP-353
    #      : (SCP-353, '''"Vector"''')
      861    :     {
      "name"                :   "SCP-353",
      "document_name"       :   '''"Vector"''',
      "popularity"          :   861,
      "to_use"              :   1,
      },


    # 862  : SCP-4645
    #      : (SCP-4645, "Blackmailing Computer")
      862    :     {
      "name"                :   "SCP-4645",
      "document_name"       :   "Blackmailing Computer",
      "popularity"          :   862,
      "to_use"              :   1,
      },


    # 863  : SCP-3127
    #      : (SCP-3127, "Nineteen Year Old Jessica Lambert And A Female Pig Of Abnormal Size, Forever")
      863    :     {
      "name"                :   "SCP-3127",
      "document_name"       :   "Nineteen Year Old Jessica Lambert And A Female Pig Of Abnormal Size, Forever",
      "popularity"          :   863,
      "to_use"              :   0,
      },


    # 864  : SCP-3031
    #      : (SCP-3031, "Future Gift")
      864    :     {
      "name"                :   "SCP-3031",
      "document_name"       :   "Future Gift",
      "popularity"          :   864,
      "to_use"              :   0,
      },


    # 865  : SCP-1478
    #      : (SCP-1478, "Inconveniently Stereotypical Cacti")
      865    :     {
      "name"                :   "SCP-1478",
      "document_name"       :   "Inconveniently Stereotypical Cacti",
      "popularity"          :   865,
      "to_use"              :   0,
      },


    # 866  : SCP-1235
    #      : (SCP-1235, "Atlas Microcosm")
      866    :     {
      "name"                :   "SCP-1235",
      "document_name"       :   "Atlas Microcosm",
      "popularity"          :   866,
      "to_use"              :   1,
      },


    # 867  : SCP-1947
    #      : (SCP-1947, "Emission Sphere")
      867    :     {
      "name"                :   "SCP-1947",
      "document_name"       :   "Emission Sphere",
      "popularity"          :   867,
      "to_use"              :   1,
      },


    # 868  : SCP-124
    #      : (SCP-124, "Fertile Soil")
      868    :     {
      "name"                :   "SCP-124",
      "document_name"       :   "Fertile Soil",
      "popularity"          :   868,
      "to_use"              :   1,
      },


    # 869  : SCP-5149
    #      : (SCP-5149, "None Of Us Are Blind, Joe.")
      869    :     {
      "name"                :   "SCP-5149",
      "document_name"       :   "None Of Us Are Blind, Joe.",
      "popularity"          :   869,
      "to_use"              :   0,
      },


    # 870  : SCP-3689
    #      : (SCP-3689, "Legendary Sandwich of the Deep")
      870    :     {
      "name"                :   "SCP-3689",
      "document_name"       :   "Legendary Sandwich of the Deep",
      "popularity"          :   870,
      "to_use"              :   1,
      },


    # 871  : SCP-2306
    #      : (SCP-2306, "Revenant AI")
      871    :     {
      "name"                :   "SCP-2306",
      "document_name"       :   "Revenant AI",
      "popularity"          :   871,
      "to_use"              :   1,
      },


    # 872  : SCP-2271
    #      : (SCP-2271, "Factory Loans")
      872    :     {
      "name"                :   "SCP-2271",
      "document_name"       :   "Factory Loans",
      "popularity"          :   872,
      "to_use"              :   0,
      },


    # 873  : SCP-157
    #      : (SCP-157, "Mimetic Predator")
      873    :     {
      "name"                :   "SCP-157",
      "document_name"       :   "Mimetic Predator",
      "popularity"          :   873,
      "to_use"              :   1,
      },


    # 874  : SCP-5040
    #      : (SCP-5040, '''血の涙 ("Tears of Blood")''')
      874    :     {
      "name"                :   "SCP-5040",
      "document_name"       :   '''血の涙 ("Tears of Blood")''',
      "popularity"          :   874,
      "to_use"              :   0,
      },


    # 875  : SCP-4266
    #      : (SCP-4266, "The Thing That Makes You Kill People")
      875    :     {
      "name"                :   "SCP-4266",
      "document_name"       :   "The Thing That Makes You Kill People",
      "popularity"          :   875,
      "to_use"              :   0,
      },


    # 876  : SCP-3737
    #      : (SCP-3737, "Rainbow Bridge")
      876    :     {
      "name"                :   "SCP-3737",
      "document_name"       :   "Rainbow Bridge",
      "popularity"          :   876,
      "to_use"              :   0,
      },


    # 877  : None
    #      : (None, [OMITTED])
      877    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   877,
      "to_use"              :   0,
      },


    # 878  : SCP-1142
    #      : (SCP-1142, "A Cry for Help")
      878    :     {
      "name"                :   "SCP-1142",
      "document_name"       :   "A Cry for Help",
      "popularity"          :   878,
      "to_use"              :   1,
      },


    # 879  : SCP-5789
    #      : (SCP-5789, "SCP-𝕐 - Cannibalistic Mathematics")
      879    :     {
      "name"                :   "SCP-5789",
      "document_name"       :   "SCP-𝕐 - Cannibalistic Mathematics",
      "popularity"          :   879,
      "to_use"              :   0,
      },


    # 880  : SCP-5832
    #      : (SCP-5832, "Stained")
      880    :     {
      "name"                :   "SCP-5832",
      "document_name"       :   "Stained",
      "popularity"          :   880,
      "to_use"              :   0,
      },


    # 881  : SCP-2679
    #      : (SCP-2679, "The Many Graves of Jeannette Parslov")
      881    :     {
      "name"                :   "SCP-2679",
      "document_name"       :   "The Many Graves of Jeannette Parslov",
      "popularity"          :   881,
      "to_use"              :   0,
      },


    # 882  : SCP-3637
    #      : (SCP-3637, "Many Waters")
      882    :     {
      "name"                :   "SCP-3637",
      "document_name"       :   "Many Waters",
      "popularity"          :   882,
      "to_use"              :   0,
      },


    # 883  : SCP-3883
    #      : (SCP-3883, "Dildos Have Dreams Too")
      883    :     {
      "name"                :   "SCP-3883",
      "document_name"       :   "Dildos Have Dreams Too",
      "popularity"          :   883,
      "to_use"              :   1,
      },


    # 884  : SCP-1003
    #      : (SCP-1003, "Tapeworm Child")
      884    :     {
      "name"                :   "SCP-1003",
      "document_name"       :   "Tapeworm Child",
      "popularity"          :   884,
      "to_use"              :   1,
      },


    # 885  : SCP-5423
    #      : (SCP-5423, "The Empty Room")
      885    :     {
      "name"                :   "SCP-5423",
      "document_name"       :   "The Empty Room",
      "popularity"          :   885,
      "to_use"              :   0,
      },


    # 886  : SCP-051
    #      : (SCP-051, "Japanese Obstetrical Model")
      886    :     {
      "name"                :   "SCP-051",
      "document_name"       :   "Japanese Obstetrical Model",
      "popularity"          :   886,
      "to_use"              :   1,
      },


    # 887  : SCP-3880
    #      : (SCP-3880, " - ILLEST RAIN SOUNDS 8 Hours No Looping - White Noise, Nature/Healing/Ambient, Meditation/Insomnia/Study ASMR [ORIGINAL]")
      887    :     {
      "name"                :   "SCP-3880",
      "document_name"       :   " - ILLEST RAIN SOUNDS 8 Hours No Looping - White Noise, Nature/Healing/Ambient, Meditation/Insomnia/Study ASMR [ORIGINAL]",
      "popularity"          :   887,
      "to_use"              :   0,
      },


    # 888  : SCP-3733
    #      : (SCP-3733, "Everybody Else")
      888    :     {
      "name"                :   "SCP-3733",
      "document_name"       :   "Everybody Else",
      "popularity"          :   888,
      "to_use"              :   1,
      },


    # 889  : SCP-2221
    #      : (SCP-2221, "A Friendly Agreement")
      889    :     {
      "name"                :   "SCP-2221",
      "document_name"       :   "A Friendly Agreement",
      "popularity"          :   889,
      "to_use"              :   0,
      },


    # 890  : SCP-2197
    #      : (SCP-2197, "Shop Class")
      890    :     {
      "name"                :   "SCP-2197",
      "document_name"       :   "Shop Class",
      "popularity"          :   890,
      "to_use"              :   0,
      },


    # 891  : SCP-1487
    #      : (SCP-1487, "Beautiful Bones")
      891    :     {
      "name"                :   "SCP-1487",
      "document_name"       :   "Beautiful Bones",
      "popularity"          :   891,
      "to_use"              :   1,
      },


    # 892  : SCP-1207
    #      : (SCP-1207, "Not a Mirror")
      892    :     {
      "name"                :   "SCP-1207",
      "document_name"       :   "Not a Mirror",
      "popularity"          :   892,
      "to_use"              :   1,
      },


    # 893  : SCP-121
    #      : (SCP-121, "Concrete Cradle")
      893    :     {
      "name"                :   "SCP-121",
      "document_name"       :   "Concrete Cradle",
      "popularity"          :   893,
      "to_use"              :   0,
      },


    # 894  : SCP-644
    #      : (SCP-644, "Mr. Hot")
      894    :     {
      "name"                :   "SCP-644",
      "document_name"       :   "Mr. Hot",
      "popularity"          :   894,
      "to_use"              :   1,
      },


    # 895  : SCP-2816
    #      : (SCP-2816, "Nuclear Forgery")
      895    :     {
      "name"                :   "SCP-2816",
      "document_name"       :   "Nuclear Forgery",
      "popularity"          :   895,
      "to_use"              :   1,
      },


    # 896  : SCP-132
    #      : (SCP-132, "Broken Desert")
      896    :     {
      "name"                :   "SCP-132",
      "document_name"       :   "Broken Desert",
      "popularity"          :   896,
      "to_use"              :   1,
      },


    # 897  : SCP-3885
    #      : (SCP-3885, "The High-Octane Full-Throttle Adventures of the Exploding Zombie Gearheads")
      897    :     {
      "name"                :   "SCP-3885",
      "document_name"       :   "The High-Octane Full-Throttle Adventures of the Exploding Zombie Gearheads",
      "popularity"          :   897,
      "to_use"              :   0,
      },


    # 898  : SCP-1557
    #      : (SCP-1557, "Giraffe Hell")
      898    :     {
      "name"                :   "SCP-1557",
      "document_name"       :   "Giraffe Hell",
      "popularity"          :   898,
      "to_use"              :   0,
      },


    # 899  : SCP-1161
    #      : (SCP-1161, "How-To Book")
      899    :     {
      "name"                :   "SCP-1161",
      "document_name"       :   "How-To Book",
      "popularity"          :   899,
      "to_use"              :   1,
      },


    # 900  : SCP-756
    #      : (SCP-756, "Miniature Solar System")
      900    :     {
      "name"                :   "SCP-756",
      "document_name"       :   "Miniature Solar System",
      "popularity"          :   900,
      "to_use"              :   1,
      },


    # 901  : SCP-4200
    #      : (SCP-4200, "The World, Idealized")
      901    :     {
      "name"                :   "SCP-4200",
      "document_name"       :   "The World, Idealized",
      "popularity"          :   901,
      "to_use"              :   0,
      },


    # 902  : None
    #      : (None, [OMITTED])
      902    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   902,
      "to_use"              :   0,
      },


    # 903  : SCP-1356
    #      : (SCP-1356, "Rubber Ducky")
      903    :     {
      "name"                :   "SCP-1356",
      "document_name"       :   "Rubber Ducky",
      "popularity"          :   903,
      "to_use"              :   1,
      },


    # 904  : SCP-3667
    #      : (SCP-3667, "All's Well that Ends Hell")
      904    :     {
      "name"                :   "SCP-3667",
      "document_name"       :   "All's Well that Ends Hell",
      "popularity"          :   904,
      "to_use"              :   0,
      },


    # 905  : SCP-2779
    #      : (SCP-2779, "Oinkers")
      905    :     {
      "name"                :   "SCP-2779",
      "document_name"       :   "Oinkers",
      "popularity"          :   905,
      "to_use"              :   1,
      },


    # 906  : SCP-2960
    #      : (SCP-2960, "The Show MUST Go On…")
      906    :     {
      "name"                :   "SCP-2960",
      "document_name"       :   "The Show MUST Go On…",
      "popularity"          :   906,
      "to_use"              :   0,
      },


    # 907  : SCP-2089
    #      : (SCP-2089, "/john/")
      907    :     {
      "name"                :   "SCP-2089",
      "document_name"       :   "/john/",
      "popularity"          :   907,
      "to_use"              :   0,
      },


    # 908  : SCP-1800
    #      : (SCP-1800, "The Minotaur")
      908    :     {
      "name"                :   "SCP-1800",
      "document_name"       :   "The Minotaur",
      "popularity"          :   908,
      "to_use"              :   1,
      },


    # 909  : SCP-225
    #      : (SCP-225, "Unstoppable and Immovable")
      909    :     {
      "name"                :   "SCP-225",
      "document_name"       :   "Unstoppable and Immovable",
      "popularity"          :   909,
      "to_use"              :   1,
      },


    # 910  : SCP-136
    #      : (SCP-136, "Naked Doll")
      910    :     {
      "name"                :   "SCP-136",
      "document_name"       :   "Naked Doll",
      "popularity"          :   910,
      "to_use"              :   1,
      },


    # 911  : SCP-4192
    #      : (SCP-4192, "As Above")
      911    :     {
      "name"                :   "SCP-4192",
      "document_name"       :   "As Above",
      "popularity"          :   911,
      "to_use"              :   0,
      },


    # 912  : SCP-4780
    #      : (SCP-4780, "Shrunk")
      912    :     {
      "name"                :   "SCP-4780",
      "document_name"       :   "Shrunk",
      "popularity"          :   912,
      "to_use"              :   0,
      },


    # 913  : SCP-2776
    #      : (SCP-2776, "Mr. President")
      913    :     {
      "name"                :   "SCP-2776",
      "document_name"       :   "Mr. President",
      "popularity"          :   913,
      "to_use"              :   1,
      },


    # 914  : SCP-1735
    #      : (SCP-1735, "Kind of Impenetrable Barrier")
      914    :     {
      "name"                :   "SCP-1735",
      "document_name"       :   "Kind of Impenetrable Barrier",
      "popularity"          :   914,
      "to_use"              :   0,
      },


    # 915  : SCP-1447
    #      : (SCP-1447, "Tulpa")
      915    :     {
      "name"                :   "SCP-1447",
      "document_name"       :   "Tulpa",
      "popularity"          :   915,
      "to_use"              :   1,
      },


    # 916  : SCP-075
    #      : (SCP-075, "Corrosive Snail")
      916    :     {
      "name"                :   "SCP-075",
      "document_name"       :   "Corrosive Snail",
      "popularity"          :   916,
      "to_use"              :   1,
      },


    # 917  : SCP-5320
    #      : (SCP-5320, "The People's Church Of The Fish That Just Goes On Forever")
      917    :     {
      "name"                :   "SCP-5320",
      "document_name"       :   "The People's Church Of The Fish That Just Goes On Forever",
      "popularity"          :   917,
      "to_use"              :   0,
      },


    # 918  : SCP-2632
    #      : (SCP-2632, "No Fury")
      918    :     {
      "name"                :   "SCP-2632",
      "document_name"       :   "No Fury",
      "popularity"          :   918,
      "to_use"              :   1,
      },


    # 919  : None
    #      : (None, [OMITTED])
      919    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   919,
      "to_use"              :   0,
      },


    # 920  : SCP-2172
    #      : (SCP-2172, "This Light Never Turns Green")
      920    :     {
      "name"                :   "SCP-2172",
      "document_name"       :   "This Light Never Turns Green",
      "popularity"          :   920,
      "to_use"              :   1,
      },


    # 921  : SCP-466
    #      : (SCP-466, "Mobile Veins")
      921    :     {
      "name"                :   "SCP-466",
      "document_name"       :   "Mobile Veins",
      "popularity"          :   921,
      "to_use"              :   1,
      },


    # 922  : SCP-5720
    #      : (SCP-5720, "Astronomically-Inclined Crane")
      922    :     {
      "name"                :   "SCP-5720",
      "document_name"       :   "Astronomically-Inclined Crane",
      "popularity"          :   922,
      "to_use"              :   1,
      },


    # 923  : None
    #      : (None, [OMITTED])
      923    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   923,
      "to_use"              :   0,
      },


    # 924  : SCP-596
    #      : (SCP-596, "Cursed Regeneration Statue")
      924    :     {
      "name"                :   "SCP-596",
      "document_name"       :   "Cursed Regeneration Statue",
      "popularity"          :   924,
      "to_use"              :   1,
      },


    # 925  : SCP-4494
    #      : (SCP-4494, "The Specter Fights For Justice! Fights For Justice!")
      925    :     {
      "name"                :   "SCP-4494",
      "document_name"       :   "The Specter Fights For Justice! Fights For Justice!",
      "popularity"          :   925,
      "to_use"              :   0,
      },


    # 926  : SCP-2540
    #      : (SCP-2540, "Time Lime")
      926    :     {
      "name"                :   "SCP-2540",
      "document_name"       :   "Time Lime",
      "popularity"          :   926,
      "to_use"              :   1,
      },


    # 927  : None
    #      : (None, [OMITTED])
      927    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   927,
      "to_use"              :   0,
      },


    # 928  : SCP-4183
    #      : (SCP-4183, "Automatic Containment Procedures")
      928    :     {
      "name"                :   "SCP-4183",
      "document_name"       :   "Automatic Containment Procedures",
      "popularity"          :   928,
      "to_use"              :   1,
      },


    # 929  : SCP-2304
    #      : (SCP-2304, '''"Like This Image To Die Instantly"''')
      929    :     {
      "name"                :   "SCP-2304",
      "document_name"       :   '''"Like This Image To Die Instantly"''',
      "popularity"          :   929,
      "to_use"              :   0,
      },


    # 930  : None
    #      : (None, [OMITTED])
      930    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   930,
      "to_use"              :   0,
      },


    # 931  : SCP-1115
    #      : (SCP-1115, "Distant Early Warning")
      931    :     {
      "name"                :   "SCP-1115",
      "document_name"       :   "Distant Early Warning",
      "popularity"          :   931,
      "to_use"              :   0,
      },


    # 932  : SCP-607
    #      : (SCP-607, "Dorian the Grey Cat")
      932    :     {
      "name"                :   "SCP-607",
      "document_name"       :   "Dorian the Grey Cat",
      "popularity"          :   932,
      "to_use"              :   1,
      },


    # 933  : SCP-2136
    #      : (SCP-2136, "An Utterly Driven Scientist")
      933    :     {
      "name"                :   "SCP-2136",
      "document_name"       :   "An Utterly Driven Scientist",
      "popularity"          :   933,
      "to_use"              :   0,
      },


    # 934  : SCP-1692
    #      : (SCP-1692, "Came Back Haunted")
      934    :     {
      "name"                :   "SCP-1692",
      "document_name"       :   "Came Back Haunted",
      "popularity"          :   934,
      "to_use"              :   0,
      },


    # 935  : SCP-1481
    #      : (SCP-1481, "Crack Genie")
      935    :     {
      "name"                :   "SCP-1481",
      "document_name"       :   "Crack Genie",
      "popularity"          :   935,
      "to_use"              :   1,
      },


    # 936  : SCP-1265
    #      : (SCP-1265, "The Mesozoic Preserve")
      936    :     {
      "name"                :   "SCP-1265",
      "document_name"       :   "The Mesozoic Preserve",
      "popularity"          :   936,
      "to_use"              :   0,
      },


    # 937  : SCP-573
    #      : (SCP-573, "The Pied Pipe")
      937    :     {
      "name"                :   "SCP-573",
      "document_name"       :   "The Pied Pipe",
      "popularity"          :   937,
      "to_use"              :   1,
      },


    # 938  : SCP-094
    #      : (SCP-094, "Miniature Event Horizon")
      938    :     {
      "name"                :   "SCP-094",
      "document_name"       :   "Miniature Event Horizon",
      "popularity"          :   938,
      "to_use"              :   0,
      },


    # 939  : SCP-2941
    #      : (SCP-2941, "Do Not Eat or Inspire")
      939    :     {
      "name"                :   "SCP-2941",
      "document_name"       :   "Do Not Eat or Inspire",
      "popularity"          :   939,
      "to_use"              :   1,
      },


    # 940  : SCP-619
    #      : (SCP-619, "Lucky Jeans")
      940    :     {
      "name"                :   "SCP-619",
      "document_name"       :   "Lucky Jeans",
      "popularity"          :   940,
      "to_use"              :   1,
      },


    # 941  : SCP-1507
    #      : (SCP-1507, "Pink Flamingos")
      941    :     {
      "name"                :   "SCP-1507",
      "document_name"       :   "Pink Flamingos",
      "popularity"          :   941,
      "to_use"              :   0,
      },


    # 942  : SCP-1040
    #      : (SCP-1040, '''"Daniel"''')
      942    :     {
      "name"                :   "SCP-1040",
      "document_name"       :   '''"Daniel"''',
      "popularity"          :   942,
      "to_use"              :   1,
      },


    # 943  : None
    #      : (None, [OMITTED])
      943    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   943,
      "to_use"              :   0,
      },


    # 944  : SCP-2902
    #      : (SCP-2902, "The Human Skeleton Closet (and his cat)")
      944    :     {
      "name"                :   "SCP-2902",
      "document_name"       :   "The Human Skeleton Closet (and his cat)",
      "popularity"          :   944,
      "to_use"              :   1,
      },


    # 945  : SCP-1726
    #      : (SCP-1726, "The Library and the Pillar")
      945    :     {
      "name"                :   "SCP-1726",
      "document_name"       :   "The Library and the Pillar",
      "popularity"          :   945,
      "to_use"              :   0,
      },


    # 946  : None
    #      : (None, [OMITTED])
      946    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   946,
      "to_use"              :   0,
      },


    # 947  : SCP-1005
    #      : (SCP-1005, "The Painted Man")
      947    :     {
      "name"                :   "SCP-1005",
      "document_name"       :   "The Painted Man",
      "popularity"          :   947,
      "to_use"              :   1,
      },


    # 948  : SCP-614
    #      : (SCP-614, "IP Address 57.32.███.███")
      948    :     {
      "name"                :   "SCP-614",
      "document_name"       :   "IP Address 57.32.███.███",
      "popularity"          :   948,
      "to_use"              :   0,
      },


    # 949  : SCP-516
    #      : (SCP-516, "Intelligent Tank")
      949    :     {
      "name"                :   "SCP-516",
      "document_name"       :   "Intelligent Tank",
      "popularity"          :   949,
      "to_use"              :   1,
      },


    # 950  : SCP-4634
    #      : (SCP-4634, "Out-of-Order")
      950    :     {
      "name"                :   "SCP-4634",
      "document_name"       :   "Out-of-Order",
      "popularity"          :   950,
      "to_use"              :   1,
      },


    # 951  : SCP-2624
    #      : (SCP-2624, "Laika's Sweetheart Space-Beacon")
      951    :     {
      "name"                :   "SCP-2624",
      "document_name"       :   "Laika's Sweetheart Space-Beacon",
      "popularity"          :   951,
      "to_use"              :   0,
      },


    # 952  : SCP-2040
    #      : (SCP-2040, "The Iron Messenger")
      952    :     {
      "name"                :   "SCP-2040",
      "document_name"       :   "The Iron Messenger",
      "popularity"          :   952,
      "to_use"              :   1,
      },


    # 953  : SCP-1728
    #      : (SCP-1728, "Buttery Decapitated Highwayman")
      953    :     {
      "name"                :   "SCP-1728",
      "document_name"       :   "Buttery Decapitated Highwayman",
      "popularity"          :   953,
      "to_use"              :   1,
      },


    # 954  : SCP-1441
    #      : (SCP-1441, "Cold Fusion Paper-Towel Dispenser")
      954    :     {
      "name"                :   "SCP-1441",
      "document_name"       :   "Cold Fusion Paper-Towel Dispenser",
      "popularity"          :   954,
      "to_use"              :   1,
      },


    # 955  : None
    #      : (None, [OMITTED])
      955    :     {
      "name"                :   None,
      "document_name"       :   "[OMITTED]",
      "popularity"          :   955,
      "to_use"              :   0,
      },


    # 956  : SCP-786
    #      : (SCP-786, "Funnel Factor Twelve")
      956    :     {
      "name"                :   "SCP-786",
      "document_name"       :   "Funnel Factor Twelve",
      "popularity"          :   956,
      "to_use"              :   1,
      },


    # 957  : SCP-3117
    #      : (SCP-3117, "A Monster-Shaped Hole")
      957    :     {
      "name"                :   "SCP-3117",
      "document_name"       :   "A Monster-Shaped Hole",
      "popularity"          :   957,
      "to_use"              :   0,
      },


    # 958  : SCP-2522
    #      : (SCP-2522, "hatbot.aic")
      958    :     {
      "name"                :   "SCP-2522",
      "document_name"       :   "hatbot.aic",
      "popularity"          :   958,
      "to_use"              :   0,
      }#,

    }


#use this if you want to get a 'ranking' for a particular SCP from its designation.

BY_SCPS = {

    "SCP-001" : 642,
    "SCP-002" : 30,
    "SCP-003" : 147,
    "SCP-004" : 68,
    "SCP-005" : 206,
    "SCP-006" : 262,
    "SCP-007" : 259,
    "SCP-008" : 98,
    "SCP-009" : 127,
    "SCP-011" : 190,
    "SCP-012" : 136,
    "SCP-013" : 291,
    "SCP-014" : 134,
    "SCP-015" : 81,
    "SCP-016" : 159,
    "SCP-017" : 107,
    "SCP-018" : 538,
    "SCP-019" : 316,
    "SCP-020" : 295,
    "SCP-021" : 246,
    "SCP-022" : 163,
    "SCP-023" : 342,
    "SCP-024" : 132,
    "SCP-025" : 430,
    "SCP-026" : 286,
    "SCP-027" : 297,
    "SCP-028" : 64,
    "SCP-029" : 387,
    "SCP-030" : 344,
    "SCP-031" : 238,
    "SCP-032" : 524,
    "SCP-033" : 142,
    "SCP-034" : 729,
    "SCP-035" : 29,
    "SCP-038" : 237,
    "SCP-039" : 723,
    "SCP-040" : 250,
    "SCP-043" : 744,
    "SCP-044" : 743,
    "SCP-046" : 702,
    "SCP-048" : 54,
    "SCP-049" : 2,
    "SCP-050" : 356,
    "SCP-051" : 807,
    "SCP-052" : 326,
    "SCP-053" : 113,
    "SCP-054" : 641,
    "SCP-055" : 3,
    "SCP-057" : 617,
    "SCP-058" : 123,
    "SCP-060" : 348,
    "SCP-063" : 333,
    "SCP-064" : 629,
    "SCP-066" : 111,
    "SCP-067" : 408,
    "SCP-069" : 270,
    "SCP-071" : 626,
    "SCP-072" : 239,
    "SCP-073" : 66,
    "SCP-075" : 836,
    "SCP-076" : 35,
    "SCP-078" : 591,
    "SCP-079" : 51,
    "SCP-081" : 713,
    "SCP-082" : 181,
    "SCP-084" : 277,
    "SCP-085" : 36,
    "SCP-086" : 188,
    "SCP-087" : 4,
    "SCP-089" : 140,
    "SCP-091" : 599,
    "SCP-092" : 255,
    "SCP-093" : 7,
    "SCP-094" : 854,
    "SCP-095" : 769,
    "SCP-096" : 6,
    "SCP-097" : 305,
    "SCP-098" : 473,
    "SCP-099" : 611,
    "SCP-100" : 414,
    "SCP-1000" : 26,
    "SCP-1003" : 805,
    "SCP-1004" : 129,
    "SCP-1005" : 861,
    "SCP-1006" : 173,
    "SCP-1007" : 768,
    "SCP-1008" : 752,
    "SCP-1011" : 481,
    "SCP-1012" : 590,
    "SCP-1015" : 513,
    "SCP-1020" : 610,
    "SCP-1025" : 125,
    "SCP-1030" : 781,
    "SCP-1032" : 226,
    "SCP-1033" : 461,
    "SCP-1036" : 640,
    "SCP-1040" : 858,
    "SCP-1045" : 561,
    "SCP-1046" : 732,
    "SCP-1047" : 665,
    "SCP-1048" : 37,
    "SCP-105" : 116,
    "SCP-1050" : 166,
    "SCP-1055" : 153,
    "SCP-1057" : 122,
    "SCP-1059" : 526,
    "SCP-106" : 8,
    "SCP-107" : 659,
    "SCP-1074" : 606,
    "SCP-1076" : 762,
    "SCP-108" : 327,
    "SCP-110" : 734,
    "SCP-1103" : 485,
    "SCP-111" : 152,
    "SCP-1111" : 191,
    "SCP-1115" : 847,
    "SCP-112" : 285,
    "SCP-1122" : 707,
    "SCP-1123" : 480,
    "SCP-1127" : 484,
    "SCP-1128" : 256,
    "SCP-113" : 310,
    "SCP-1142" : 800,
    "SCP-1147" : 469,
    "SCP-115" : 622,
    "SCP-1152" : 553,
    "SCP-1155" : 343,
    "SCP-1156" : 757,
    "SCP-1160" : 299,
    "SCP-1161" : 820,
    "SCP-1162" : 465,
    "SCP-1165" : 419,
    "SCP-1171" : 25,
    "SCP-1173" : 114,
    "SCP-1176" : 761,
    "SCP-1177" : 621,
    "SCP-1184" : 663,
    "SCP-119" : 504,
    "SCP-1192" : 204,
    "SCP-1193" : 99,
    "SCP-120" : 265,
    "SCP-1207" : 813,
    "SCP-121" : 814,
    "SCP-122" : 692,
    "SCP-123" : 568,
    "SCP-1230" : 43,
    "SCP-1231" : 244,
    "SCP-1233" : 275,
    "SCP-1235" : 789,
    "SCP-1237" : 358,
    "SCP-124" : 791,
    "SCP-1241" : 654,
    "SCP-1247" : 254,
    "SCP-1252" : 594,
    "SCP-1265" : 852,
    "SCP-1269" : 639,
    "SCP-127" : 264,
    "SCP-1281" : 234,
    "SCP-1293" : 258,
    "SCP-1295" : 121,
    "SCP-1296" : 306,
    "SCP-1304" : 478,
    "SCP-1306" : 662,
    "SCP-131" : 91,
    "SCP-1310" : 536,
    "SCP-1312" : 272,
    "SCP-1313" : 207,
    "SCP-1316" : 249,
    "SCP-1319" : 525,
    "SCP-132" : 817,
    "SCP-1322" : 70,
    "SCP-1329" : 751,
    "SCP-1337" : 390,
    "SCP-134" : 646,
    "SCP-1340" : 530,
    "SCP-1342" : 76,
    "SCP-1348" : 405,
    "SCP-1356" : 823,
    "SCP-1357" : 531,
    "SCP-136" : 830,
    "SCP-1360" : 341,
    "SCP-1364" : 763,
    "SCP-1370" : 47,
    "SCP-1372" : 684,
    "SCP-1376" : 709,
    "SCP-138" : 759,
    "SCP-1382" : 588,
    "SCP-1384" : 332,
    "SCP-1396" : 638,
    "SCP-140" : 38,
    "SCP-1422" : 193,
    "SCP-1425" : 58,
    "SCP-1427" : 375,
    "SCP-143" : 435,
    "SCP-1437" : 57,
    "SCP-144" : 450,
    "SCP-1440" : 56,
    "SCP-1441" : 868,
    "SCP-1442" : 317,
    "SCP-1447" : 835,
    "SCP-145" : 463,
    "SCP-1454" : 399,
    "SCP-1456" : 397,
    "SCP-1459" : 170,
    "SCP-1468" : 413,
    "SCP-147" : 682,
    "SCP-1470" : 105,
    "SCP-1471" : 46,
    "SCP-1472" : 320,
    "SCP-1474" : 733,
    "SCP-1478" : 788,
    "SCP-148" : 271,
    "SCP-1481" : 851,
    "SCP-1483" : 347,
    "SCP-1485" : 359,
    "SCP-1487" : 812,
    "SCP-1499" : 167,
    "SCP-1500" : 302,
    "SCP-1504" : 89,
    "SCP-1507" : 857,
    "SCP-1510" : 560,
    "SCP-1512" : 737,
    "SCP-1514" : 774,
    "SCP-152" : 223,
    "SCP-1520" : 554,
    "SCP-1522" : 201,
    "SCP-1523" : 664,
    "SCP-1529" : 283,
    "SCP-1535" : 508,
    "SCP-1539" : 243,
    "SCP-1541" : 499,
    "SCP-1543" : 710,
    "SCP-1545" : 110,
    "SCP-1548" : 572,
    "SCP-155" : 738,
    "SCP-1555" : 315,
    "SCP-1557" : 819,
    "SCP-1561" : 722,
    "SCP-1562" : 278,
    "SCP-157" : 796,
    "SCP-1577" : 658,
    "SCP-158" : 570,
    "SCP-1584" : 311,
    "SCP-1588" : 589,
    "SCP-1590" : 370,
    "SCP-1609" : 74,
    "SCP-1616" : 455,
    "SCP-1619" : 602,
    "SCP-162" : 251,
    "SCP-163" : 178,
    "SCP-1633" : 294,
    "SCP-1638" : 577,
    "SCP-1639" : 631,
    "SCP-165" : 371,
    "SCP-1659" : 426,
    "SCP-166" : 439,
    "SCP-1660" : 460,
    "SCP-1678" : 78,
    "SCP-1679" : 535,
    "SCP-168" : 161,
    "SCP-1682" : 545,
    "SCP-1689" : 112,
    "SCP-169" : 92,
    "SCP-1692" : 850,
    "SCP-1702" : 559,
    "SCP-1710" : 472,
    "SCP-1715" : 242,
    "SCP-1719" : 491,
    "SCP-172" : 544,
    "SCP-1722" : 468,
    "SCP-1726" : 860,
    "SCP-1728" : 867,
    "SCP-173" : 1,
    "SCP-1730" : 16,
    "SCP-1733" : 31,
    "SCP-1735" : 834,
    "SCP-1739" : 248,
    "SCP-1753" : 767,
    "SCP-176" : 155,
    "SCP-1761" : 477,
    "SCP-1762" : 52,
    "SCP-178" : 228,
    "SCP-1780" : 388,
    "SCP-1781" : 730,
    "SCP-1782" : 301,
    "SCP-1788" : 627,
    "SCP-179" : 94,
    "SCP-1795" : 336,
    "SCP-1799" : 318,
    "SCP-1800" : 828,
    "SCP-1802" : 261,
    "SCP-1810" : 389,
    "SCP-1812" : 369,
    "SCP-1833" : 429,
    "SCP-1836" : 598,
    "SCP-1839" : 558,
    "SCP-184" : 63,
    "SCP-1844" : 532,
    "SCP-1845" : 214,
    "SCP-1846" : 418,
    "SCP-1850" : 718,
    "SCP-1859" : 496,
    "SCP-186" : 88,
    "SCP-1860" : 487,
    "SCP-1861" : 179,
    "SCP-1864" : 691,
    "SCP-1867" : 65,
    "SCP-187" : 452,
    "SCP-1875" : 102,
    "SCP-1879" : 587,
    "SCP-1883" : 575,
    "SCP-1884" : 361,
    "SCP-1893" : 59,
    "SCP-1899" : 675,
    "SCP-1903" : 346,
    "SCP-191" : 157,
    "SCP-1915" : 412,
    "SCP-1921" : 383,
    "SCP-1936" : 200,
    "SCP-1947" : 790,
    "SCP-1958" : 130,
    "SCP-1959" : 133,
    "SCP-1968" : 194,
    "SCP-1972" : 377,
    "SCP-198" : 433,
    "SCP-1981" : 15,
    "SCP-1983" : 53,
    "SCP-1984" : 392,
    "SCP-1985" : 697,
    "SCP-1986" : 203,
    "SCP-2000" : 21,
    "SCP-2001" : 396,
    "SCP-2002" : 490,
    "SCP-2003" : 143,
    "SCP-2004" : 498,
    "SCP-2006" : 32,
    "SCP-201" : 583,
    "SCP-2014" : 495,
    "SCP-2017" : 569,
    "SCP-2019" : 586,
    "SCP-2020" : 403,
    "SCP-2021" : 351,
    "SCP-2022" : 616,
    "SCP-2030" : 45,
    "SCP-2031" : 696,
    "SCP-2040" : 866,
    "SCP-2049" : 657,
    "SCP-205" : 266,
    "SCP-2053" : 227,
    "SCP-2059" : 596,
    "SCP-206" : 724,
    "SCP-2061" : 567,
    "SCP-2063" : 360,
    "SCP-2070" : 717,
    "SCP-2072" : 442,
    "SCP-2075" : 422,
    "SCP-2076" : 673,
    "SCP-2078" : 379,
    "SCP-208" : 462,
    "SCP-2085" : 335,
    "SCP-2089" : 827,
    "SCP-209" : 281,
    "SCP-2090" : 549,
    "SCP-2094" : 574,
    "SCP-2095" : 716,
    "SCP-2099" : 593,
    "SCP-2107" : 726,
    "SCP-2111" : 186,
    "SCP-2112" : 773,
    "SCP-2115" : 539,
    "SCP-2118" : 437,
    "SCP-212" : 323,
    "SCP-2133" : 620,
    "SCP-2136" : 849,
    "SCP-2137" : 154,
    "SCP-2140" : 582,
    "SCP-216" : 222,
    "SCP-2165" : 585,
    "SCP-217" : 128,
    "SCP-2170" : 689,
    "SCP-2172" : 839,
    "SCP-2190" : 512,
    "SCP-2191" : 417,
    "SCP-2193" : 409,
    "SCP-2197" : 811,
    "SCP-2200" : 502,
    "SCP-2203" : 436,
    "SCP-2206" : 325,
    "SCP-2207" : 257,
    "SCP-2217" : 210,
    "SCP-2221" : 810,
    "SCP-2232" : 661,
    "SCP-225" : 829,
    "SCP-2256" : 172,
    "SCP-2264" : 158,
    "SCP-2268" : 714,
    "SCP-2271" : 795,
    "SCP-2273" : 232,
    "SCP-228" : 424,
    "SCP-2282" : 643,
    "SCP-2293" : 651,
    "SCP-2295" : 95,
    "SCP-230" : 704,
    "SCP-2300" : 368,
    "SCP-2304" : 846,
    "SCP-2305" : 721,
    "SCP-2306" : 794,
    "SCP-2308" : 720,
    "SCP-231" : 13,
    "SCP-2310" : 597,
    "SCP-2316" : 44,
    "SCP-2317" : 14,
    "SCP-2331" : 573,
    "SCP-2337" : 174,
    "SCP-2338" : 592,
    "SCP-2343" : 293,
    "SCP-2357" : 165,
    "SCP-239" : 160,
    "SCP-2399" : 100,
    "SCP-2406" : 410,
    "SCP-2408" : 755,
    "SCP-2412" : 750,
    "SCP-2419" : 340,
    "SCP-242" : 742,
    "SCP-2420" : 349,
    "SCP-2424" : 451,
    "SCP-2432" : 624,
    "SCP-2439" : 72,
    "SCP-245" : 196,
    "SCP-2460" : 464,
    "SCP-247" : 434,
    "SCP-2472" : 681,
    "SCP-2480" : 213,
    "SCP-2481" : 740,
    "SCP-2501" : 510,
    "SCP-2505" : 576,
    "SCP-2508" : 334,
    "SCP-2513" : 605,
    "SCP-252" : 649,
    "SCP-2522" : 871,
    "SCP-2540" : 844,
    "SCP-2547" : 428,
    "SCP-2553" : 747,
    "SCP-2557" : 131,
    "SCP-2571" : 274,
    "SCP-2578" : 497,
    "SCP-2598" : 300,
    "SCP-2599" : 150,
    "SCP-261" : 86,
    "SCP-2610" : 671,
    "SCP-2614" : 338,
    "SCP-262" : 330,
    "SCP-2622" : 780,
    "SCP-2624" : 865,
    "SCP-2632" : 838,
    "SCP-2639" : 195,
    "SCP-2662" : 50,
    "SCP-2664" : 749,
    "SCP-2669" : 175,
    "SCP-2679" : 802,
    "SCP-268" : 420,
    "SCP-2682" : 156,
    "SCP-2686" : 652,
    "SCP-270" : 488,
    "SCP-2700" : 221,
    "SCP-2701" : 741,
    "SCP-2702" : 374,
    "SCP-2703" : 674,
    "SCP-2712" : 715,
    "SCP-2718" : 60,
    "SCP-2719" : 171,
    "SCP-272" : 393,
    "SCP-2740" : 169,
    "SCP-2746" : 494,
    "SCP-2747" : 149,
    "SCP-2762" : 708,
    "SCP-2771" : 253,
    "SCP-2774" : 267,
    "SCP-2776" : 833,
    "SCP-2779" : 825,
    "SCP-2786" : 328,
    "SCP-2790" : 467,
    "SCP-2798" : 506,
    "SCP-2800" : 314,
    "SCP-2805" : 630,
    "SCP-2816" : 816,
    "SCP-2820" : 519,
    "SCP-2845" : 268,
    "SCP-2851" : 309,
    "SCP-2852" : 168,
    "SCP-2874" : 637,
    "SCP-2875" : 144,
    "SCP-2881" : 404,
    "SCP-2886" : 706,
    "SCP-2900" : 615,
    "SCP-2902" : 859,
    "SCP-2912" : 772,
    "SCP-2915" : 282,
    "SCP-2922" : 290,
    "SCP-2932" : 362,
    "SCP-2933" : 529,
    "SCP-2935" : 27,
    "SCP-294" : 23,
    "SCP-2941" : 855,
    "SCP-2950" : 141,
    "SCP-2951" : 695,
    "SCP-2952" : 184,
    "SCP-296" : 628,
    "SCP-2960" : 826,
    "SCP-297" : 645,
    "SCP-2980" : 438,
    "SCP-2987" : 779,
    "SCP-2991" : 601,
    "SCP-2996" : 625,
    "SCP-2998" : 55,
    "SCP-2999" : 292,
    "SCP-3000" : 19,
    "SCP-3001" : 20,
    "SCP-3002" : 82,
    "SCP-3003" : 106,
    "SCP-3004" : 231,
    "SCP-3005" : 208,
    "SCP-3006" : 385,
    "SCP-3007" : 118,
    "SCP-3008" : 10,
    "SCP-3009" : 517,
    "SCP-3017" : 612,
    "SCP-3020" : 395,
    "SCP-3021" : 636,
    "SCP-3022" : 565,
    "SCP-3027" : 581,
    "SCP-303" : 124,
    "SCP-3031" : 787,
    "SCP-3034" : 164,
    "SCP-3035" : 458,
    "SCP-3041" : 446,
    "SCP-3043" : 296,
    "SCP-3045" : 236,
    "SCP-3049" : 700,
    "SCP-3052" : 690,
    "SCP-3054" : 771,
    "SCP-3074" : 634,
    "SCP-3078" : 233,
    "SCP-3088" : 584,
    "SCP-3101" : 289,
    "SCP-3108" : 353,
    "SCP-3117" : 870,
    "SCP-312" : 712,
    "SCP-3125" : 85,
    "SCP-3127" : 786,
    "SCP-3128" : 542,
    "SCP-3133" : 746,
    "SCP-3143" : 618,
    "SCP-3145" : 701,
    "SCP-315" : 235,
    "SCP-3166" : 241,
    "SCP-3171" : 284,
    "SCP-319" : 363,
    "SCP-3199" : 109,
    "SCP-3200" : 386,
    "SCP-3201" : 263,
    "SCP-321" : 192,
    "SCP-3211" : 185,
    "SCP-3213" : 137,
    "SCP-3220" : 783,
    "SCP-323" : 668,
    "SCP-3240" : 483,
    "SCP-3241" : 528,
    "SCP-3250" : 402,
    "SCP-3280" : 365,
    "SCP-3288" : 680,
    "SCP-330" : 693,
    "SCP-3300" : 205,
    "SCP-3301" : 139,
    "SCP-3305" : 482,
    "SCP-3309" : 189,
    "SCP-3312" : 373,
    "SCP-3319" : 699,
    "SCP-332" : 454,
    "SCP-3333" : 83,
    "SCP-3338" : 635,
    "SCP-3340" : 518,
    "SCP-335" : 685,
    "SCP-3388" : 415,
    "SCP-3393" : 90,
    "SCP-3396" : 725,
    "SCP-342" : 108,
    "SCP-343" : 71,
    "SCP-3448" : 364,
    "SCP-3449" : 777,
    "SCP-3450" : 394,
    "SCP-3456" : 416,
    "SCP-348" : 48,
    "SCP-3480" : 595,
    "SCP-3484" : 423,
    "SCP-3494" : 719,
    "SCP-3512" : 331,
    "SCP-3513" : 619,
    "SCP-3515" : 440,
    "SCP-3519" : 145,
    "SCP-352" : 608,
    "SCP-3521" : 197,
    "SCP-353" : 784,
    "SCP-354" : 40,
    "SCP-3562" : 686,
    "SCP-361" : 453,
    "SCP-3626" : 218,
    "SCP-363" : 758,
    "SCP-3636" : 523,
    "SCP-3637" : 803,
    "SCP-3667" : 824,
    "SCP-3671" : 146,
    "SCP-3688" : 372,
    "SCP-3689" : 793,
    "SCP-370" : 350,
    "SCP-372" : 425,
    "SCP-3733" : 809,
    "SCP-3737" : 799,
    "SCP-374" : 753,
    "SCP-3740" : 151,
    "SCP-3774" : 623,
    "SCP-3780" : 694,
    "SCP-3790" : 376,
    "SCP-3799" : 298,
    "SCP-3812" : 252,
    "SCP-3838" : 778,
    "SCP-3844" : 534,
    "SCP-3848" : 698,
    "SCP-3866" : 647,
    "SCP-387" : 126,
    "SCP-3880" : 808,
    "SCP-3883" : 804,
    "SCP-3885" : 818,
    "SCP-3890" : 705,
    "SCP-3900" : 225,
    "SCP-3908" : 471,
    "SCP-3922" : 276,
    "SCP-3929" : 493,
    "SCP-3930" : 62,
    "SCP-3935" : 304,
    "SCP-3936" : 514,
    "SCP-3939" : 117,
    "SCP-3949" : 339,
    "SCP-3966" : 260,
    "SCP-3980" : 511,
    "SCP-3984" : 557,
    "SCP-3989" : 687,
    "SCP-3998" : 515,
    "SCP-3999" : 17,
    "SCP-400" : 459,
    "SCP-4001" : 93,
    "SCP-4002" : 489,
    "SCP-4003" : 509,
    "SCP-4004" : 656,
    "SCP-4005" : 551,
    "SCP-4006" : 319,
    "SCP-4007" : 667,
    "SCP-4008" : 466,
    "SCP-401" : 580,
    "SCP-4010" : 384,
    "SCP-4011" : 678,
    "SCP-4028" : 441,
    "SCP-4040" : 579,
    "SCP-4057" : 548,
    "SCP-4062" : 391,
    "SCP-4069" : 672,
    "SCP-407" : 269,
    "SCP-408" : 522,
    "SCP-409" : 507,
    "SCP-4098" : 603,
    "SCP-4100" : 329,
    "SCP-411" : 398,
    "SCP-413" : 381,
    "SCP-414" : 653,
    "SCP-4144" : 564,
    "SCP-4182" : 401,
    "SCP-4183" : 845,
    "SCP-4192" : 831,
    "SCP-4200" : 822,
    "SCP-423" : 119,
    "SCP-4231" : 670,
    "SCP-4233" : 445,
    "SCP-4242" : 604,
    "SCP-426" : 11,
    "SCP-4266" : 798,
    "SCP-427" : 209,
    "SCP-4281" : 600,
    "SCP-4290" : 357,
    "SCP-431" : 607,
    "SCP-432" : 457,
    "SCP-4321" : 770,
    "SCP-4335" : 303,
    "SCP-4338" : 500,
    "SCP-435" : 313,
    "SCP-437" : 735,
    "SCP-439" : 148,
    "SCP-4444" : 97,
    "SCP-445" : 492,
    "SCP-4465" : 677,
    "SCP-447" : 115,
    "SCP-4494" : 843,
    "SCP-4498" : 501,
    "SCP-450" : 288,
    "SCP-4500" : 217,
    "SCP-451" : 216,
    "SCP-4511" : 443,
    "SCP-4514" : 352,
    "SCP-4517" : 505,
    "SCP-453" : 230,
    "SCP-455" : 183,
    "SCP-457" : 219,
    "SCP-458" : 247,
    "SCP-4633" : 541,
    "SCP-4634" : 864,
    "SCP-4645" : 785,
    "SCP-466" : 840,
    "SCP-4661" : 633,
    "SCP-4666" : 79,
    "SCP-469" : 546,
    "SCP-4746" : 578,
    "SCP-4774" : 432,
    "SCP-478" : 739,
    "SCP-4780" : 832,
    "SCP-4949" : 776,
    "SCP-4950" : 683,
    "SCP-4955" : 382,
    "SCP-4960" : 224,
    "SCP-4966" : 448,
    "SCP-4971" : 421,
    "SCP-4975" : 312,
    "SCP-4991" : 104,
    "SCP-4999" : 22,
    "SCP-500" : 73,
    "SCP-5000" : 18,
    "SCP-5001" : 220,
    "SCP-5002" : 229,
    "SCP-5003" : 547,
    "SCP-5004" : 287,
    "SCP-5005" : 366,
    "SCP-5031" : 84,
    "SCP-504" : 61,
    "SCP-5040" : 797,
    "SCP-5045" : 609,
    "SCP-505" : 775,
    "SCP-507" : 39,
    "SCP-511" : 521,
    "SCP-513" : 103,
    "SCP-5131" : 754,
    "SCP-514" : 486,
    "SCP-5140" : 212,
    "SCP-5149" : 792,
    "SCP-516" : 863,
    "SCP-517" : 355,
    "SCP-523" : 632,
    "SCP-524" : 202,
    "SCP-527" : 199,
    "SCP-529" : 75,
    "SCP-531" : 566,
    "SCP-5320" : 837,
    "SCP-536" : 380,
    "SCP-5370" : 563,
    "SCP-5423" : 806,
    "SCP-5500" : 345,
    "SCP-554" : 756,
    "SCP-5545" : 745,
    "SCP-5552" : 475,
    "SCP-5554" : 660,
    "SCP-5555" : 378,
    "SCP-557" : 406,
    "SCP-572" : 245,
    "SCP-5720" : 841,
    "SCP-573" : 853,
    "SCP-5789" : 879,
    "SCP-582" : 470,
    "SCP-583" : 537,
    "SCP-5832" : 801,
    "SCP-5858" : 527,
    "SCP-586" : 80,
    "SCP-590" : 556,
    "SCP-592" : 516,
    "SCP-5935" : 766,
    "SCP-596" : 842,
    "SCP-5983" : 760,
    "SCP-599" : 703,
    "SCP-5999" : 69,
    "SCP-602" : 666,
    "SCP-603" : 427,
    "SCP-604" : 367,
    "SCP-607" : 848,
    "SCP-609" : 354,
    "SCP-610" : 34,
    "SCP-614" : 862,
    "SCP-616" : 476,
    "SCP-619" : 856,
    "SCP-629" : 479,
    "SCP-644" : 815,
    "SCP-645" : 474,
    "SCP-650" : 211,
    "SCP-662" : 87,
    "SCP-666" : 650,
    "SCP-668" : 449,
    "SCP-670" : 711,
    "SCP-674" : 280,
    "SCP-682" : 5,
    "SCP-687" : 503,
    "SCP-689" : 571,
    "SCP-696" : 736,
    "SCP-698" : 555,
    "SCP-699" : 407,
    "SCP-701" : 33,
    "SCP-705" : 411,
    "SCP-711" : 322,
    "SCP-713" : 764,
    "SCP-715" : 688,
    "SCP-726" : 540,
    "SCP-732" : 215,
    "SCP-735" : 728,
    "SCP-736" : 613,
    "SCP-738" : 120,
    "SCP-743" : 550,
    "SCP-745" : 447,
    "SCP-748" : 543,
    "SCP-752" : 400,
    "SCP-753" : 655,
    "SCP-756" : 821,
    "SCP-765" : 562,
    "SCP-783" : 679,
    "SCP-784" : 731,
    "SCP-786" : 869,
    "SCP-795" : 782,
    "SCP-804" : 138,
    "SCP-807" : 765,
    "SCP-811" : 177,
    "SCP-823" : 176,
    "SCP-826" : 307,
    "SCP-835" : 96,
    "SCP-838" : 552,
    "SCP-846" : 324,
    "SCP-847" : 431,
    "SCP-860" : 240,
    "SCP-870" : 337,
    "SCP-871" : 67,
    "SCP-872" : 648,
    "SCP-877" : 669,
    "SCP-882" : 77,
    "SCP-884" : 180,
    "SCP-890" : 187,
    "SCP-895" : 24,
    "SCP-902" : 28,
    "SCP-909" : 727,
    "SCP-911" : 748,
    "SCP-914" : 9,
    "SCP-919" : 614,
    "SCP-920" : 456,
    "SCP-931" : 273,
    "SCP-939" : 101,
    "SCP-940" : 644,
    "SCP-946" : 182,
    "SCP-953" : 308,
    "SCP-956" : 321,
    "SCP-957" : 520,
    "SCP-962" : 162,
    "SCP-963" : 49,
    "SCP-966" : 135,
    "SCP-967" : 533,
    "SCP-970" : 198,
    "SCP-973" : 444,
    "SCP-978" : 279,
    "SCP-988" : 676,
    "SCP-990" : 41,
    "SCP-993" : 42,
    "SCP-999" : 12#,

    }

#END



if __name__ == "__main__":
    print "popular_scps.py\ninfo on SCPs from the SCP Foundation's 'Highest Rated SCPs' page.\n"
    print "%s 'popular' SCPs known about." % len(POPULAR_SCPS_DICT.keys())
    print
    print "TOP 20 MOST POPULAR SCPS:"
    print
    for f in range(1,21):
        #print "	%2d : %s" % (f, POPULAR_SCPS_DICT[f])
        print "	%2d : %s\t (%s)" % (f, POPULAR_SCPS_DICT[f], POPULAR_SCPS_DICT_FULL[f]["document_name"])
    print

