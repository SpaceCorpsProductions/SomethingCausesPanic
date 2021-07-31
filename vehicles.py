#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Contains information about vehicle SCPs (only anything about them
specifically being vehicles - for anything else see objects.py).

Includes info on cars (anything capable of being parked in a garage,
including trucks and vans) and aircraft (anything stored in a
hangar, including aircraft-shaped living SCPs).

"Cars" only includes vehicles held in containment by the SCP, not
vehicles-type anomalies observed in the wild (such as SCP-5141 -
"Studebaker Special Six", which is observed to travel between North
Carolina and Tennessee). If you can't find it in an SCP garage or
Anomalous Vehicle Containment Bay, you won't find it in the CAR_SCPS
list.
"""

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.


VERSION = "0.0.4b"
__VERSION__ = VERSION

# 26 vehicle-type SCPs known about:
# 18 car-type SCPs known about.
# 11 aircraft-type SCPs known about.

##THIS FILE IS UNFINISHED!

import string, random
from types import IntType, FloatType, NoneType, StringType


# "CAR" SCPs = Vehicle-type SCPs stored in garages

CAR_SCPS = [

    "SCP-115",  # "Miniature Dump Truck"
    "SCP-490",  # "Ice Cream Truck"
    "SCP-708",  # "The Big Orange Forklift"
    "SCP-907",  # "An Exploratory Vehicle
    #"SCP-941",  # "Sick of Motion"     # TO-DO
    "SCP-1061", # "The Accidental Car"
    "SCP-1187", # "Stationary ATV"
    "SCP-1221", # "Unidentified Bus"
    "SCP-1492", # "Ill-Begotten Gains"
    "SCP-1894", # "Crash Course Diet"
    "SCP-1946", # "Diner Mimics"
    "SCP-2320", # "A Trolley"
    "SCP-2445", # "Wondertainment Logistics"
    "SCP-2538", # "The Perfect Escape"
    "SCP-2830", # "The Knowledge"
    "SCP-3707", # "Fly By Night Only"
    "SCP-3763", # "A Piece of Him is Still Around"
    "SCP-3913", # "Keep on Trucking"
    "SCP-4137", # "Hyper-Axial Nintendocore Overdose"

    ]

CAR_SCPS_DICT = {

    "SCP-115":     {
        "name"  :       "SCP-115",          # Miniature Dump Truck
        "designation":  "SCP-115",
        "make":         "dump truck",
        "colour":       None,
        "year":         None#,
        # SCP-115-1 is a toy dump truck, with no identifying markers or labels
        # to identify its original manufacturer. Unlike regular toy dump trucks,
        # SCP-115-1 weighs as much as the actual vehicle it represents, roughly
        # 90 tons. SCP-115-1 is also capable of motorized movement and can
        # function exactly like a normal dump truck, excepting the fact that it
        # is several magnitudes smaller. SCP-115-1 also has a similar carrying
        # capacity as its larger counterparts, being able to carry or tow roughly
        # 120 tons of cargo. SCP-115-1 apparently needs diesel fuel to run properly.
        # There is a small port in its left side that allows fueling. It stores and 
        # consumes as much fuel as a regular dump truck.
        },

    #SCP-490 - "Ice Cream Truck"
    "SCP-490":     {
        "name"  :       "SCP-490",          # Ice Cream Truck
        "designation":  "SCP-490",
        "make":         "ice cream truck",
        "colour":       None,
        "year":         "196█"#,
        # SCP-490 is an ice cream truck dating to the 1960s
        # constructed by [REDACTED]. It seems to be mechanically standard except
        # for the audio system, which does not respond to operators, though
        # it appears to be in working order.
        },

    #SCP-708 - "The Big Orange Forklift"
    "SCP-708":     {
        "name"  :       "SCP-708",          # The Big Orange Forklift
        "designation":  "SCP-708",
        "make":         "Toyota Model 7FDU80 7-Series Forklift",
        "colour":       "orange",
        "year":         None#,
        # SCP-708 is an orange Toyota Model 7FDU80 7-Series Forklift with a
        # typical lift capacity of 8 metric tonnes. Records indicate it was
        # purchased by [REDACTED] on 7/13/████ and delivered 7/30/████.
        },

    #SCP-907 - "An Exploratory Vehicle"
    "SCP-907":     {
        "name"  :       "SCP-907",          # An Exploratory Vehicle
        "designation":  "SCP-907",
        "make":         "VW van",
        "colour":       None,
        "year":         "196█"#,
        # SCP-907 is a 196█ VW van bearing no internal or external structural
        # anomalies. The vehicle had received a new coat of paint shortly before
        # recovery, but otherwise all modification to the vehicle has been
        # carried out by the Foundation. Said modification includes the removal
        # of all seats in the vehicle and the addition of testing and research
        # equipment. SCP-907 is outfitted as a mobile research station. 
        },

##    #SCP-941 - "Sick of Motion"
##    "SCP-941":     {
##        "name"  :       "SCP-941",          # Sick of Motion
##        "designation":  "SCP-941",
##        "make":         None,
##        "colour":       None,
##        "year":         None#,
##        },

   #TO DO
##    #SCP-941 - "Sick of Motion"
##    "SCP-941":     {"name"  :              "SCP-941",
##                 "item_name" :              "SCP-941",
##                 "document_name" :          '"Sick of Motion"',
##                 "filename" :               "SCP_0941.txt",
##                 "object_class" :           "Euclid",
##                 "disruption_class" :       None,
##                 "risk_class" :             None,
##                 "containment" :            None
##                 },

    #SCP-1061 - "The Accidental Car"
    "SCP-1061":     {
        "name"  :       "SCP-1061",          # The Accidental Car
        "designation":  "SCP-1061",
        "make":         "Pontiac Grand Am",
        "colour":       "dark red",
        "year":         "1992"#,
        # SCP-1061 is a dark red 1992 Pontiac Grand Am with severe collision
        # damage, including a large hole in its driver's-side front windshield.
        # It manifests three distinct anomalous properties; these properties are
        # considered to be linked, in that they seem to be caused by the same
        # anomalous entity.
        # SCP-1061 should be kept in a secured, climate-controlled garage. Its
        # tires have been removed and should not be replaced for any reason. Its
        # doors should be locked at all times and its windshield boarded up,
        # unless testing is in progress.
                 },

    #SCP-1187 - "Stationary ATV"
    "SCP-1187":     {
        "name"  :       "SCP-1187",          # Stationary ATV
        "designation":  "SCP-1187",
        "make":         "Kazuma 150cc All Terrain Vehicle",
        "colour":       "blue",
        "year":         "2006"#,
        # SCP-1187 is a blue 2006 Kazuma 150cc All Terrain Vehicle. It was sold
        # and delivered to ██████ ████ of ████████, South Carolina via an
        # anonymous online merchant site.
        # SCP-1187 is to be stored in a remote, above-ground enclosure 5km from
        # Site 19 with a staff of 2 armed guards and 1 Level 1 researcher.
        },

    #SCP-1221 - "Unidentified Bus"
    "SCP-1221":     {
        "name"  :       "SCP-1221",          # Unidentified Bus
        "designation":  "SCP-1221",
        "make":         "Mercedes-Benz O405 single-decker bus",
        "colour":       None, #none given
        "year":         "1989"#,
        # SCP-1221 is a Mercedes-Benz O405 single-decker bus manufactured at the
        # company's Mannheim plant in 1989. It was purchased by the ██████
        # Transit Authority and had an uneventful 10-year career.
        # SCP-1221 is non-hazardous and contained in a Anomalous Vehicle
        # Containment Bay at Site-██.
        },

    #SCP-1492 - "Ill-Begotten Gains"
    "SCP-1492":     {
        "name"  :       "SCP-1492",          # Ill-Begotten Gains
        "designation":  "SCP-1492",
        "make":         "civilian-model armored car",
        "colour":       None,
        "year":         None#,
        # SCP-1492 is currently impounded in the Site-47 
        # Anomalous Vehicle Containment Bay with tires and battery removed.
        # SCP-1492 is a civilian-model armored car which has been modified for
        # use in anomalous larceny.
        # The passenger's seat has been replaced with an 
        # experimental target acquisition and teleportation device that Foundation 
        # technicians have thus far failed to replicate. 
        },

    #SCP-1676 - "Customer Loyalty Program"
    "SCP-1676":     {
        "name"  :       "SCP-1676",          # Customer Loyalty Program
        "designation":  "SCP-1676",
        "make":         "Chevrolet S-10 Blazer LS",
        "colour":       "white",
        "year":         "2001"#,
        # SCP-1676-1 is contained in a secure vehicle bay at Humanoid
        # Containment Site-06-3, with its keys contained in a separate secure
        # locker except as needed for vehicle maintenance or experimentation.
        # SCP-1676-1 is a white, two-door 2001 Chevrolet S-10 Blazer LS
        # consistent with those produced at the assembly plant in Linden, New
        # Jersey. SCP-1676-1's components lack any identifying serial numbers or
        # Vehicle Identification Numbers (VINs), and where the driver's-side
        # windshield VIN plate would normally be, there is instead a sterling
        # silver plaque with the words "Customer Loyalty Program". When fueled,
        # SCP-1676-1 starts and operates normally.
        },

    #SCP-1676 - "Customer Loyalty Program"
    "SCP-1676-1":     {
        "name"  :       "SCP-1676-1",          # Customer Loyalty Program
        "designation":  "SCP-1676-1",
        "make":         "Chevrolet S-10 Blazer LS",
        "colour":       "white",
        "year":         "2001"#,
        # SCP-1676-1 is contained in a secure vehicle bay at Humanoid
        # Containment Site-06-3, with its keys contained in a separate secure
        # locker except as needed for vehicle maintenance or experimentation.
        # SCP-1676-1 is a white, two-door 2001 Chevrolet S-10 Blazer LS
        # consistent with those produced at the assembly plant in Linden, New
        # Jersey. SCP-1676-1's components lack any identifying serial numbers or
        # Vehicle Identification Numbers (VINs), and where the driver's-side
        # windshield VIN plate would normally be, there is instead a sterling
        # silver plaque with the words "Customer Loyalty Program". When fueled,
        # SCP-1676-1 starts and operates normally.
        },

    #SCP-1894 - "Crash Course Diet"
    "SCP-1894":     {
        "name"  :       "SCP-1894",          # Crash Course Diet
        "designation":  "SCP-1894",
        "make":         "van",
        "colour":       None,
        "year":         None#,
        # SCP-1894 is a mid-sized van, with vanity license plate, reading
        # "CRSHCRS". All identifying marks, such as brand names or serial
        # number, have been removed.
        # SCP-1894 is to be held in a secured garage, located within Site-77.
        },

    #SCP-1946 - "Diner Mimics"
    "SCP-1946":     {
        "name"  :       "SCP-1946",          # Diner Mimics
        "designation":  "SCP-1946",
        "make":         "Airstream Excella-II trailer",
        "colour":       None,
        "year":         1986#,
        # SCP-1946 is contained at Site-116 in its AVB (Anomalous Vehicle Bay),
        # on lot #1542/A.
        # SCP-1946 is a 1986 Airstream Excella-II trailer, converted into a
        # small mobile diner. It is fully furnished, with a 3 m x 1.5 m kitchen
        # area situated in the back, containing (amongst others) a dishwasher, a
        # deep fryer, a grill and a stove. In addition, this area also contains
        # SCP-1946-1, SCP-1946-3 and SCP-1946-5. Towards the front of SCP-1946
        # is a ten-person seating area in a traditional American diner style,
        # with red leather upholstered bar stools positioned next to a high
        # wall-mounted table running along the left side of SCP-1946. This also
        # contains SCP-1946-2, SCP-1946-4, SCP-1946-6, SCP-1946-7 and
        # SCP-1946-10. Also in the front of SCP-1946 is the trailer's toilet. It
        # contains both a chemical toilet and SCP-1946-11. The kitchen and
        # seating area are separated by a small counter on which a cash register
        # and SCP-1946-9 sit.
        # SCP-1946-1 through -11 are subjects previously exposed to SCP-1946's
        # anomalous effect. All but SCP-1946-8 remain inside SCP-1946.
        # SCP-1946-8 is deceased.
        },

    #SCP-2320 - "A Trolley"
    "SCP-2320":     {
        "name"  :       "SCP-2320",          # A Trolley
        "designation":  "SCP-2320",
        "make":         "PCC streetcar",
        "colour":       "red and white",
        "year":         1938#,
        # SCP-2320 is a refurbished PCC streetcar, originally manufactured by
        # the St. Louis Car Company in 1938. SCP-2320 is capable of operating
        # without access to electrical power and is capable of off-rail travel,
        # but otherwise does not bear any outward mechanical or structural
        # anomalies. The vehicle is painted with a red and white color scheme,
        # typical of the Pittsburgh Railways streetcar fleet.
        # SCP-2320 is currently contained within Garage 01 at Site-45.
        },

    #SCP-2445 - "Wondertainment Logistics"
    "SCP-2445":     {
        "name"  :       "SCP-2445",          # Wondertainment Logistics
        "designation":  "SCP-2445",
        "make":         "tractor trailer",
        "colour":       "white",
        "year":         None#, None given
        # SCP-2445 is a white, mostly unmarked tractor trailer. Of note is the
        # inclusion of a label on the bottom right of the rightmost back door,
        # which reads:
        # Wondertainment Logistics Co. 
        # A Division of Dr. Wondertainment Inc. 
        # Beneath the engine hood of SCP-2445's truck section is a modified
        # engine component, designated SCP-2445-1, capable of producing
        # significantly more power than that of a standard semi-truck.
        # SCP-2445-2 is a black, metallic cube, measuring at 0.6m x 0.6m x 0.6m,
        # that sits between the driver's and passenger's seat in the cab of
        # SCP-2445. Two large cables connect SCP-2445-1 to SCP-2445-2
        # through the dashboard of the cab. Eight smaller cables run from the
        # SCP-2445-2 into the dashboard, on which sits a large touchscreen.
        # Across the top of this screen are the words "WonderVision". 
        },

    #SCP-2538 - "The Perfect Escape"
    "SCP-2538":     {
        "name"  :       "SCP-2538",          # The Perfect Escape
        "designation":  "SCP-2538",
        "make":         "large van",
        "colour":       None,
        "year":         None#,
        # SCP-2538 is a large van with a set of seats in the back, along with
        # several containers. The vehicle has several crude steel plates
        # attached to the sides and windows. SCP-2538 has no visible license
        # plating and manufacturer labels. Due to this, manufacturer and
        # previous owner of SCP-2538 are unknown. The left side of the vehicle
        # has a spray painted rectangular symbol with the letters "R. S."
        # written below.
        },

    #SCP-2830 - "The Knowledge"
    "SCP-2830":     {
        "name"  :       "SCP-2830",          # The Knowledge
        "designation":  "SCP-2830",
        "make":         "Austin FX4 London taxi",
        "colour":       "black",
        "year":         None # None given
        # SCP-2830-1-A through -O are to be secured in Foundation Garage
        # 020-2830. 
        # SCP-2830 is the collective designation for a series of objects related
        # to a formerly-operating anomalous luxury transportation collective,
        # known as "the Knowledge," believed to be operational from the
        # mid-1960s to 2005.
        # - SCP-2830-1-A through -O are a series of fifteen Austin FX4 hackney
        #   carriages (Also called cabs or London taxis) which have been modified
        #   via extranormal means.
        },

    #SCP-3707 - "Fly By Night Only"
    "SCP-3707":     {
        "name"  :       "SCP-3707",          # Fly By Night Only
        "designation":  "SCP-3707",
        "make":         "Toyota Camry",
        "colour":       None, # none given
        "year":         2002#,
        # SCP-3707 is kept at Site-81's anomalous motor pool and maintained as
        # necessary to ensure drivability.
        # SCP-3707 is a 2002 Toyota Camry with Minnesota plates. Anomalous
        # properties manifest when occupied by exactly one human, who is driving
        # it between 12 AM and 3 AM local time.
        },

    #SCP-3763 - "A Piece of Him is Still Around"
    "SCP-3763":     {
        "name"  :       "SCP-3763",          # A Piece of Him is Still Around
        "designation":  "SCP-3763",
        "make":         "Chevrolet Biscayne sedan",
        "colour":       None, # none given
        "year":         1964#,
        # SCP-3763 is a 1964 Chevrolet Biscayne sedan. The vehicle is installed
        # with a "Thalbrum Vehicle Security System", believed to be the source
        # of its anomalous effects.
        # SCP-3763 is to be stored in the Anomalous Vehicle Containment Center
        # at Site-48.
        },

    #SCP-3913 - "Keep on Trucking"
    "SCP-3913":     {
        "name"  :       "SCP-3913",          # Keep on Trucking
        "designation":  "SCP-3913",
        "make":         "Kenworth W900A semi-trailer truck",
        "colour":       None,
        "year":         1979#,
        # SCP-3913 is to be kept in Site-88's above-ground anomalous vehicle bay. A GPS 
        # tracking device is to be installed inside SCP-3913's cab. Obstructions between 
        # SCP-3913 and public roadways must be removable in case of an SCP-3913 breach. 
        # SCP-3913 is a Kenworth W900A 1979 model semi-trailer truck. If more
        # than 2.56 kilometers from the corpse of Jedediah Phillips (hereafter
        # referred to as SCP-3913-1) SCP-3913 will begin independent operation
        # and move towards SCP-3913-1. SCP-3913 does not require fuel to operate
        # in this manner.
        },

    #SCP-4137 - "Hyper-Axial Nintendocore Overdose"
    "SCP-4137":     {
        "name"  :       "SCP-4137",          # Hyper-Axial Nintendocore Overdose
        "designation":  "SCP-4137",
        "make":         "Ford Transit 100 Campervan",
        "colour":       None,
        "year":         1975#,
        # SCP-4137 is a 1975 Ford Transit 100 Campervan, possessing an interior
        # pocket dimension (SCP-4137-Z) in which subjects can perform unbounded
        # movement through four-dimensional space.
        },

    }


# "AIRCRAFT" SCPs = Vehicle-type SCPs stored in hangars.

AIRCRAFT_SCPS = [
    "SCP-556",  # "Painted Aircraft"
    "SCP-616",  # "The Vessel and the Gate"
    "SCP-787",  # "The Plane That Never Was"
    "SCP-1387", # "Giant Seagull Airlines"
    "SCP-1759", # "Lovely Lucy"
    "SCP-1850", # "Accipiter sopwithii"
    "SCP-2473", # "Better Hide, Better Run"
    "SCP-2725", # "Akron and Nemesis"
    "SCP-2918", # "A Post-Traumatic Predator"
    "SCP-3531", # "Skyfood"
    "SCP-4927", # "Have a Nice Flight"
    ]

AIRCRAFT_SCPS_DICT = {

    #SCP-556 - "Painted Aircraft"
    "SCP-556":     {
        "name"  :       "SCP-556",          # Painted Aircraft
        "designation":  "SCP-556",
        "make":         "Boeing 707-323C (wreckage)",
        "colour":       None,
        "year":         1979#,
        # SCP-556 is the recovered wreckage of Varig cargo flight PP-VLU, a
        # Boeing 707-323C that crashed approximately 320 km east-northeast of
        # Tokyo, Japan on January 30, 1979. 
        # SCP-556 is stored in a secure hangar at Site ██.
        },

    #SCP-616 - "The Vessel and the Gate"
    "SCP-616":     {
        "name"  :       "SCP-616",          # The Vessel and the Gate
        "designation":  "SCP-616",
        "make":         "Boeing ███-███",
        "colour":       None,
        "year":         "1966"#,
        # SCP-616 is a prototype Boeing ███-███, designed by █████ █████████ and
        # constructed on 16/06/1966 to specifications. Though superficially
        # similar to the Boeing 737 which went into service shortly afterwards,
        # SCP-616's model had various internal alterations, including [DATA
        # EXPUNGED]. Despite the various alterations, the most important feature
        # of SCP-616 is the center left emergency door, which has been dubbed
        # SCP-616-1. SCP-616-1 is a standard emergency door, though partially
        # covered in extensive markings associated with Satanic cults adhering
        # to [REDACTED]. 
        },

    #SCP-787 - "The Plane That Never Was"
    "SCP-787":     {
        "name"  :       "SCP-787",          # The Plane That Never Was
        "designation":  "SCP-787",
        "make":         "Boeing 747-200",
        "colour":       None,
        "year":         None#,
        # SCP-787 is a Boeing 747-200 airliner of unknown manufacturing date and
        # call sign. The exterior of SCP-787 has been painted over, including
        # all passenger windows: Paint was wet upon recovery, drying soon after.
        # The mechanical components of SCP-787 are all undamaged and functional,
        # and show no signs of use. Nonmechanical components of SCP-787,
        # including carpeting, upholstery, and luggage, are in an advanced state
        # of decay. The pilot and co-pilot’s seats have been removed, replaced
        # with two piles of computer components arranged in the shape of chairs.
        },

    #SCP-1387 - "Giant Seagull Airlines"
    "SCP-1387":     {
        "name"  :       "SCP-1387",          # Giant Seagull Airlines
        "designation":  "SCP-1387",
        "make":         "large avian creature",
        "colour":       None,
        "year":         None#,
        # SCP-1387 is a very large avian creature similar in appearance to a
        # seagull, measuring approximately 20m in length, with a wingspan of
        # approximately 25m. SCP-1387 lacks a heart, respiratory system, or
        # digestive system, as its body cavity instead contains a space closely
        # resembling the cabin of a passenger aircraft. This space is 2.5m x 15m
        # in area, with exactly 40 seats and 20 windows (though none are visible
        # from the outside). 
        # SCP-1387 is currently contained in Area-55. Primary containment
        # consists of a 100m x 100m x 30m steel reinforced concrete hangar.
        # SCP-1387 is to be restrained in this hangar with 30 high tension steel
        # cables at all times, and is to be under constant surveillance.
        },

    #SCP-1759 - ""Lovely Lucy""
    "SCP-1759":     {
        "name"  :       "SCP-1759",          # Lovely Lucy
        "designation":  "SCP-1759",
        "make":         "Douglas A-20 Havoc",
        "colour":       "olive drab",
        "year":         1942#,
        # SCP-1759 is a 1942 Douglas A-20 Havoc bomber aircraft. The craft meets
        # standard specifications. 4 guns are mounted in the nose, 2 in the rear
        # section, and one mounted ventrally. Painted on the left side of the
        # plane is a blonde figure with the text "Lovely Lucy" written below
        # her. 
        # SCP-1759 is to be locked in its guarded hangar at all times.
        },

    #SCP-1850 - "Accipiter sopwithii"
    "SCP-1850":     {
        "name"  :       "SCP-1850",          # Accipiter sopwithii
        "designation":  "SCP-1850",
        "make":         "Sopwith Triplane",
        "colour":       "olive drab",
        "year":         1917#,
        # SCP-1850 is an anomalous organism in the exact shape of a full-size 
        # 1917 Sopwith Triplane aircraft. 
        # SCP-1850 is to be kept in an aircraft hangar at Site 6.
        # SCP-1850 EATS ANYONE WHO ENTER THE COCKPIT!
        },

    #SCP-2473 - "Better Hide, Better Run"
    "SCP-2473":     {
        "name"  :       "SCP-2473",          # Better Hide, Better Run
        "designation":  "SCP-2473",
        "make":         "atmospheric re-entry vehicle",
        "colour":       None,
        "year":         None#,
        # SCP-2473 is an atmospheric re-entry vehicle of anomalous origins. It
        # has the following approximate specifications: a 51-meter length, a
        # 30-meter wingspan, a 65-meter height, and a total weight of
        # approximately 110,000 kilograms.
        # SCP-2473 has no external marks, and possesses a form of ion
        # propulsion. Hardware for docking onto another spacecraft is present. A
        # living quarters/cockpit has been identified. Much of SCP-2473's
        # interior is filled with computer hardware, apparatus for recycling air
        # and human waste, and a retractable photovoltaic panel. All hardware
        # within SCP-2473 appears to have suffered several centuries of
        # oxidization. 
        },

    #SCP-2725 - "Akron and Nemesis"
    "SCP-2725":     {
        "name"  :       "SCP-2725",          # Akron and Nemesis
        "designation":  "SCP-2725",
        "make":         "USS Akron",
        "colour":       None,
        "year":         1933#,
        # SCP-2725 is the salvaged remains of the USS Akron, a helium-filled
        # rigid airship formerly belonging to the U.S. Navy. The vehicle has
        # been extensively repaired and modified with scrap material and organic
        # matter to permit continued function after its destruction in 1933.
        # SCP-2725 is kept anchored in a reinforced hangar at Site-88.
        },

    #SCP-2918 - "A Post-Traumatic Predator"
    "SCP-2918":     {
        "name"  :       "SCP-2918",          # A Post-Traumatic Predator
        "designation":  "SCP-2918",
        "make":         "MQ-1 Predator",
        "colour":       None,
        "year":         None#,
        # SCP-2918 is an incomplete MQ-1 Predator unmanned aerial vehicle suite,
        # consisting of one airframe, one ground control system (GCS) and one
        # primary satellite link communications suite (currently disabled). 
        },

    #SCP-3531 - "Skyfood"
    "SCP-3531":     {
        "name"  :       "SCP-3531",          # Skyfood
        "designation":  "SCP-3531",
        "make":         "Boeing 737",
        "colour":       None,
        "year":         None#,
        # SCP-3531 is a Boeing 737 airliner. SCP-3531 is unremarkable in both
        # exterior and interior appearance, and is non-anomalous when not in
        # flight. 
        },

##    #SCP-4927 - "Have a Nice Flight"
##    "SCP-4927":     {
##        "name"  :       "SCP-4927",          # Have a Nice Flight
##        "designation":  "SCP-14927",
##        "make":         None, #varies
##        "colour":       None, #varies
##        "year":         "between 1945 and 1990"#,
##        # SCP-4927 is a phenomenon that occurs between 2:00 AM and 4:00 AM in
##        # derelict airports and those with less than 100 annual flights.
##        # SCP-4927 begins with the appearance of fog, followed by the landing of
##        # a commercial aircraft, designated as SCP-4927-1. SCP-4927-1 instances
##        # are discontinued models manufactured between 1945 and 1990.
##        # Upon landing, SCP-4927-1 will open its gate, disembarking passengers
##        # and staff (SCP-4927-2 and SCP-4927-3 respectively). SCP-4927-2
##        # instances are dressed in clothing typical of 1945 to 1990. SCP-4927-3
##        # are airport employees.
##        },

    }






def IsACar(SCP=None, Extended=0):
    """Given an SCP-number, will return True if it is a car-type SCP, False otherwise.
If given the optional argument "Extended=1", will return a tuple.
If the given SCP is a car, will return True and a brief description of the car,
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
    if thisSCP in CAR_SCPS:
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in CAR_SCPS_DICT.keys():
                this_desc = ""
                if CAR_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["colour"])
                if CAR_SCPS_DICT[thisSCP]["year"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["year"])
                    else:
                        this_desc = "%s %s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["year"])
                if CAR_SCPS_DICT[thisSCP]["make"] != None:
                    if this_desc == "":
                        this_desc = "%s"  % (CAR_SCPS_DICT[thisSCP]["make"])
                    else:
                        this_desc = "%s %s" % (this_desc, CAR_SCPS_DICT[thisSCP]["make"])
                elif CAR_SCPS_DICT[thisSCP]["make"] == None:
                    this_desc = "%s" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                desc = "%s." % (desc)
            return (True, desc)
        else:
            return True

    elif thisSCP in CAR_SCPS_DICT.keys():
        #failsafe - should be found by above
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in CAR_SCPS_DICT.keys():
                this_desc = ""
                if CAR_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["colour"])
                if CAR_SCPS_DICT[thisSCP]["year"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["year"])
                    else:
                        this_desc = "%s %s"  % (this_desc, CAR_SCPS_DICT[thisSCP]["year"])
                if CAR_SCPS_DICT[thisSCP]["make"] != None:
                    if this_desc == "":
                        this_desc = "%s"  % (CAR_SCPS_DICT[thisSCP]["make"])
                    else:
                        this_desc = "%s %s" % (this_desc, CAR_SCPS_DICT[thisSCP]["make"])
                elif CAR_SCPS_DICT[thisSCP]["make"] == None:
                    this_desc = "%s" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                desc = "%s." % (desc)
            return (True, desc)
        else:
            return True

    else:
        if Extended==1:
            return (False, None)
        else:
            return False


def IsAnAircraft(SCP=None, Extended=0):
    """Given an SCP-number, will return True if it is an aircraft-type SCP, False otherwise.
If given the optional argument "Extended=1", will return a tuple.
If the given SCP is an aircraft, will return True and a brief description of the aircraft,
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
    if thisSCP in AIRCRAFT_SCPS:
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in AIRCRAFT_SCPS_DICT.keys():
                this_desc = ""
                if AIRCRAFT_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["colour"])
                if AIRCRAFT_SCPS_DICT[thisSCP]["year"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["year"])
                    else:
                        this_desc = "%s %s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["year"])
                if AIRCRAFT_SCPS_DICT[thisSCP]["make"] != None:
                    if this_desc == "":
                        this_desc = "%s"  % (AIRCRAFT_SCPS_DICT[thisSCP]["make"])
                    else:
                        this_desc = "%s %s" % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["make"])
                elif AIRCRAFT_SCPS_DICT[thisSCP]["make"] == None:
                    this_desc = "%s" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                desc = "%s." % (desc)
            return (True, desc)
        else:
            return True

    elif thisSCP in AIRCRAFT_SCPS_DICT.keys():
        #failsafe - should be found by above
        if Extended==1:
            desc = "%s is a" % (thisSCP)
            if thisSCP in AIRCRAFT_SCPS_DICT.keys():
                this_desc = ""
                if AIRCRAFT_SCPS_DICT[thisSCP]["colour"] != None:
                    this_desc = "%s%s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["colour"])
                if AIRCRAFT_SCPS_DICT[thisSCP]["year"] != None:
                    if this_desc == "":
                        this_desc = "%s%s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["year"])
                    else:
                        this_desc = "%s %s"  % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["year"])
                if AIRCRAFT_SCPS_DICT[thisSCP]["make"] != None:
                    if this_desc == "":
                        this_desc = "%s"  % (AIRCRAFT_SCPS_DICT[thisSCP]["make"])
                    else:
                        this_desc = "%s %s" % (this_desc, AIRCRAFT_SCPS_DICT[thisSCP]["make"])
                elif AIRCRAFT_SCPS_DICT[thisSCP]["make"] == None:
                    this_desc = "%s" % (this_desc)
                desc = "%s %s." % (desc, this_desc)
            else:
                desc = "%s." % (desc)
            return (True, desc)
        else:
            return True

    else:
        if Extended==1:
            return (False, None)
        else:
            return False


def IsAVehicle(SCP=None, Extended=0):
    car,desc = IsACar(SCP=SCP, Extended=1)
    if car == 1:
        if Extended in (1, "1"):
            return (True, desc)
        else:
            return True
    plane,desc = IsAnAircraft(SCP=SCP, Extended=1)
    if plane == 1:
        if Extended in (1, "1"):
            return (True, desc)
        else:
            return True
    if car == 0 and plane == 0:
        if Extended in (1, "1"):
            return (False, None)
        else:
            return False
        

##def demo():
##    book = random.choice(BOOK_SCPS)
##    desc = IsABook(book,1)[1]
##    print desc

def demoCars():
    "print out the description for a random car-type SCP"
    car = random.choice(CAR_SCPS)
    desc = IsACar(car,1)[1]
    print desc

def demoAircraft():
    "print out the description for a random aircraft-type SCP"
    plane = random.choice(AIRCRAFT_SCPS)
    desc = IsAnAircraft(plane,1)[1]
    print desc


#CAR_SCPS
#CAR_SCPS_DICT = {

#AIRCRAFT_SCPS = [
#AIRCRAFT_SCPS_DICT = {


if __name__ == "__main__":
    print "vehicles.py\n(Version: %s)" % VERSION
    print "%s vehicle-type SCPs known about:" % (len(CAR_SCPS)+len(AIRCRAFT_SCPS))
    print "\t%s car-type SCPs known about." % len(CAR_SCPS)
    print "\t%s aircraft-type SCPs known about.\n" % len(AIRCRAFT_SCPS)
    print "random car:"
    demoCars()
    print "\nrandom aircraft:"
    demoAircraft()
    print
    