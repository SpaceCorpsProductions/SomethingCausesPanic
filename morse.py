#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

VERSION = "0.4a"
__VERSION__ = VERSION

"""Various routines related to Morse code. Can convert Morse code to
text, text to Morse code and check if an SCP is one that is known to
use Morse code."""

#morse.py
#May be useful where an SCP uses Morse code to communicate...
#(future enhancement... have some method of producing Morse code as audio?)

from types import IntType, FloatType, NoneType, StringType

#uses some code from Samual Sam's "Morse Code Translator in Python"
#https://www.tutorialspoint.com/morse-code-translator-in-python

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'
					}

def morse(message):
	"""Guesses whether to encrypyt (convert English -> Morse) or decrypt
	(convert Morse -> English) the incoming message and calls appropriate routine.
	(Returns None if input is None)."""
	if message in [None, ""]:
		return None
	elif message[0] in ("-", "."):
		return decryption(message)
	else:
		return encryption(message)

def encryption(message):
    "Converts English to Morse code."
    message = message.upper()
    my_cipher = ''
    for myletter in message:
        if myletter != ' ':
            if myletter in MORSE_CODE_DICT.keys():
                my_cipher += MORSE_CODE_DICT[myletter] + ' '
            else:
                pass # silently ignore characters that aren't in our code chart, rather than giving a key error.
        else:
            my_cipher += ' '
    return my_cipher

def decryption(message):
    "Converts Morse code to English."
    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:
        # checks for space
        if (myletter != ' '):
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mycitext)]
            mycitext = ''
    return decipher



MORSE_USING_SCPS = [

	# Morse code is used by the following SCPs...

	"SCP-264",
	# SCP-264("Skeleton Temple"): "SCP-264 is sentient, communicating
	#   through several non-verbal forms, including... Morse code."

	"SCP-270",
	# SCP-270("Secluded Telephone"): "For the most part, SCP-270-1
	#   consists of a mildly distorted human female voice... The following
	#   have also been recorded:... Morse code..."

	"SCP-304",
	# SCP-304("The Signal"): "The signal begins in Morse Code with "King
	#   William IV" and proceeds down a list of English monarchs, American presidents 
	#   and other leaders. SCP-304's format changes from Morse Code to ASCII upon 
	#   reaching "President Lyndon B Johnson". "

	"SCP-480",
	# SCP-480("Recurring Nightmare Field"): "Potential test subjects are
	#   to be enrolled in an intensive Morse code training course. All
	#   requests made by potential test subjects (e.g. food, water, any
	#   other necessities) will only be fulfilled after a correct request
	#   given in Morse code by tapping an index finger against any of the
	#   multiple purpose-built sensors throughout the holding facility."

	"SCP-680",
	# SCP-680("Clockwork Skull"): "Studies performed on SCP-680 have
	#   revealed that the “clicks” emitted by the SCP are actually
	#   messages communicated in Morse Code describing the  “studied”
	#   item’s properties..."

	"SCP-1073",
	# SCP-1073("Computing Microbes"): "Following the initial recovery in
	#   19██ it was believed that the waves were meaningless until Dr.
	#   ██████, an amateur radio operator, found that the small waves
	#   (averaging eight (8) cm in diameter) and the large waves
	#   (averaging sixteen (16) cm in diameter) respectively correspond to
	#   the dots and dashes of Morse code."

	"SCP-1174",
	# SCP-1174("The Wreck of the Edmund Fitzgerald"): "Upon coming into
	#   visual range of any vessel traveling through Lake Superior,
	#   SCP-1174-1 will attempt to establish communication by means
	#   appropriate to the period and capabilities of the vessel
	#   appearing, including... Morse code..."

	"SCP-1245",
	# SCP-1245("Whaling Ship"): "On ██/██/████, SCP-1245 transmitted a
	#   message in Morse code to staff at Site-412."

	"SCP-1246",
	# SCP-1246("Stone Spiral"): "SCP-1246 will emit a series of noises,
	#   designated SCP-1246-3... Addendum: Transcript of SCP-1246-3...
	#   13:14 to 13:30: A sequence of eight digits as expressed in Morse
	#   code via telegraph key, varying for each iteration."

	"SCP-1382",
	# SCP-1382("Save Our Souls"): "In dark weather or night conditions,
	#   SCP-1382-1 flashes the international Morse code distress signal
	#   "S.O.S." at ten-second intervals."

	"SCP-1414",
	# SCP-1414("Passive-Aggressive Radio"): "SCP-1414-1 is SCP-1414's
	#   "owner"... SCP-1414 is able to detect commands from SCP-1414-1 in
	#   a variety of formats, including... having third parties relay the
	#   command in Morse code by clapping their hands."

	"SCP-1480",
	# SCP-1480("Bus #64"): "Periodically, flashing lights can be seen
	#   emanating from the windows of SCP-1480... These flashes can be
	#   deciphered into Morse code messages; how the entity is familiar
	#   with Morse code protocols is unknown."

	"SCP-1531",
	# SCP-1531("Perfect Lie Detector"): "SCP-1531 is a standard issue
	#   polygraph of indeterminate make.... When a subject... has its
	#   sensors affixed to their skin and is asked a question they are
	#   able to understand, the following happens: Subject answers the
	#   question, usually orally, but when that method is restricted,
	#   writing... or blinking in Morse code have been used."

	"SCP-1535",
	# SCP-1535("Purgatory"): "Entities present within SCP-1535 after it
	#   has been sealed gain the ability to reason... and knowledge of
	#   Morse code."

	"SCP-1640",
	# SCP-1640("Lunar Leporine"): "SCP-1640 emits a frequency modulated
	#   radio broadcast on the ██.███ frequency band, and may
	#   occasionally broadcast sounds of a repeated thumping noise, which
	#   has been determined to be Morse code."

	"SCP-1723",
	# SCP-1723("Radio Intercepting Woman"): "SCP-1723 can understand
	#   messages sent in ... Morse code."

	"SCP-1809",
	# SCP-1809("Microscopic Cellular Housing Enthusiasts"): "extensive
	#   observation reveals SCP-1809-1 to be constantly communicating via
	#   morse code."

	"SCP-1852",
	# SCP-1852("Dictus Ultima"): "Testing is to be conducted by no fewer
	#   than two personnel... fully trained in communicating in Morse
	#   code.... SCP-1852-2 is activated when a person uses the telegraph
	#   key to type a question in English, using Morse code, and pulls
	#   the lever.... the speaker installed within the statue will
	#   produce an answer to the question posed to it, in the form of an
	#   English language statement in Morse code."

	"SCP-2129",
	# SCP-2129("Hot-Blooded Snake"): "This is evidenced by its ability to
	#   modulate the strength and length of the detonations it emits to
	#   communicate in Portuguese using a rough, sometimes inexact
	#   version of morse code"

	"SCP-2132",
	# SCP-2132("Most Dangerous Fighting Exhibition and Obstacle Resort"):
	#   "SCP-2132's numbers station transmitted the following message in
	#   Morse code:
	#   I CANNOT THINK OF ANYTHING ELSE STOP I AM SORRY STOP YOU USED
	#   THEM ALL STOP"

	"SCP-2306",
	# SCP-2306("Revenant AI"): "SCP-2306 has... demonstrated limited
	#   capacity to function on other electronic devices that contain a
	#   USB port, with SCP-2306-1 communicating through other means
	#   including: Morse code on an electronic music keyboard..."

	"SCP-2598",
	# SCP-2598("Traveling Moth Salesman"): "SCP-2598 is able to
	#   communicate with humans by colliding with their heads in a pattern
	#   consistent with American Morse Code."

	"SCP-2728",
	# SCP-2728("On the Barcelona Skyline"): "a bright flashing light
	#   shone through the windows of SCP-2728 at 21:00. After initial
	#   observation, it was shortly discovered to be Morse code. The
	#   following is a transcription of the Morse code, beginning shortly
	#   after the light started flashing"

	"SCP-2749",
	# SCP-2749("It's Just Business"): "(Several instances of SCP-2749-A
	#   are seen gathered on the large table communicating with a series of
	#   taps which were translated from Morse code.)"

	"SCP-2819",
	# SCP-2819("Bond Beetles"): "High-power microphones located in both
	#   containment units detected a rhythmic clicking originating from
	#   SCP-2819-1 and -2's mandibles—analysis determined this to be
	#   Morse code."

	"SCP-2844",
	# SCP-2844("Gary of the Paperclips"): "Afterwards, another Faraday
	#   Cage was placed over the original cage and SCP-2844-A, which
	#   resulted in another message from SCP-2844-A after roughly a week,
	#   this time in Morse Code."

	"SCP-3044",
	# SCP-3044("Evolution In A Bottle"): "Later analysis revealed the
	#   flashes to be Morse Code, and translated to "HELP" repeated over
	#   and over. It is currently unknown how the lifeforms learned Morse
	#   Code, or how they were aware that there was anyone to communicate
	#   with outside of SCP-3044."

	"SCP-3082",
	# SCP-3082("Neverland's Lost Boys and Girls"): "SCP-3082-2's Morse
	#   code-based alphabet written in crayon on birch bark... Letters,
	#   dots, and dashes, a facsimile of Morse code, are written in black
	#   and blue crayon on the birch bark."

	"SCP-3127",
	# SCP-3127("Nineteen Year Old Jessica Lambert And A Female Pig Of
	#   Abnormal Size, Forever"): "Analysis of SCP-3127's screaming
	#   patterns has shown that the gaps between its vocalizations are
	#   consistent and can be translated into Morse code (a method of
	#   communication the original SCP-3127 had limited knowledge of)."

	"SCP-3281",
	# SCP-3281("[REDACTED BY AARS538]"): "The afflicted individual blinks
	#   their eyelids to form a pattern in morse code encoding [REDACTED
	#   BY AARS538]."

	"SCP-3538",
	# SCP-3538("The Greatest Carabiner Ever"): "Foundation personnel
	#   planted within local police forces later found and identified the
	#   source of the clicking to be SCP-3538 sending out a Morse code
	#   SOS signal... It’s opening and closing in a pattern… the pattern
	#   almost looks like… Morse code. One second.... this interview has
	#   been translated from the original Morse code SCP-3538 produces."

	"SCP-3658",
	# SCP-3658("The Time Walker"): "SCP-3658 seems to be highly
	#   intelligent as it encodes its transmissions in Binary, Morse
	#   code, etc."

	"SCP-3770",
	# SCP-3770("One Thousand Footsteps Towards The Promised Land"):
	#   "GP-0001-D began to create loud respiratory "hisses" (as is
	#   common in the species) at short intervals translated to Latin
	#   morse code."

	"SCP-3798",
	# SCP-3798("There Are Flowers There"): "all signals received are to
	#   be digitally stored and copied, with copies of short-timeframe
	#   signals translated into the ISO basic Latin alphabet from
	#   standard Morse code.... Signals emitted by SCP-3798 are relayed
	#   in short bursts of 0.25 seconds and 1.02 seconds, which together
	#   correspond to letters and numbers in Morse code (0.25-second
	#   signal representing “dots” and 1.02-second signals representing
	#   “dashes”). In short timeframes, these codes have been shown to
	#   translate to English language sentences."

	"SCP-3840",
	# SCP-3840("We Stand On Guard For Thee"): "Analysis has found that
	#   the timing of each collision corresponds to a Morse code
	#   message... A repeating monotone buzzing sequence, forming the
	#   following message in Morse code..."

	"SCP-3842",
	# SCP-3842("Life-Emitting Diode"): "This appears to be Morse code
	#   that translates to "DOT BOY AND DASH MAN KEEPING EVERYONE SAFE FROM
	#   THE EVIL DR. ELECTRON"."

	"SCP-4099",
	# SCP-4099("We Die in the Dark"): "Other auditory phenomena
	#   include... morse code and radio transmissions..."

	"SCP-4215",
	# SCP-4215("The Inkredible 51st Squiddy Squaddy"): "This interview
	#   was performed entirely through Morse, with Researcher Klatz
	#   flashing a light to communicate as non-anomalous instances of
	#   Sepia lycidas would."

	"SCP-4523",
	# SCP-4523("Cave Story"): "Low-pitch tones audible in the background
	#   were later interpreted as the following morse code message: DON'T
	#   CUT THE FEEDS. I MISS WATCHING YOU."

	"SCP-4936",
	# SCP-4936("Summer Vacation ??"): "On 2018/09/03 04:16 PM, JRTF Phi-4
	#   detected a radio message emitting from SCP-4936 while it
	#   hibernated. Notably, the message was relayed in Morse code, similar
	#   to interstellar radio messages sent from Earth to deep space."

	"SCP-5111"#,
	# SCP-5111("Fermi, Exterminated"): "Autonomous data analysis programs
	#   isolated the signal and found that it consisted of messages in
	#   Morse code, translating to sentences in English.... As Farer 1
	#   exits the chamber, a series of electronic beeps are audible,
	#   spelling out a message in English Morse Code."

	#Morse code is also mentioned in...
	# SCP-537("Singing Gramophone"): "Attempts to teach SCP-537 Morse code
	#   as a way of accelerating communications have failed, owing to
	#   SCP-537's inability to read or spell."
	# SCP-2181("Little Lock-a-Doors"): "Inscribed into the dorsal surface
	#   of the forearm was a message in Morse code, translated below.
	#   that is not the print"
	# SCP-2423("Site-██"): "The musical tone heard near the beginning has
	#   been identified as a harpsichord, and it may have been spelling out
	#   the morse code "error" message."
	# SCP-2853("From Dust to Dawn"): "Control notes that this is Morse
	#   code for "SOS" but does not tell the subject."
	# SCP-2886("Planet-Hopping Volcano"): "Section is a recording of
	#   morse code."
	# SCP-3119("Lord of the Dance"): "All attempts to communicate with
	#   SCP-3119 by e.g. dancing using Morse code or semaphore flags have
	#   failed."
	# SCP-3258("God Killers"): "Due to an unprompted personal initiative
	#   on the part of Dr. ███████, a simple binary language similar to
	#   Morse code has been discovered in the arrangement of noncoding
	#   segments of SCP-3258’s DNA."
	# SCP-3349("Printing EKG"): "Dr. Whote and his staff initiate
	#   messages (“Hello”, “Greetings”, “What is your name?”) coded in
	#   Morse and delivered by (1) playing the auditory sequence near the
	#   ear of the patient, (2) manual percussion at the sternum, and (3)
	#   electrical impulses via transvenous pacing."
	# SCP-4568("Dilemma of the Twin Serpents"): "analysis by Foundation
	#   cryptologists and linguists determined it to be an attempt at
	#   comunication via a binary encoding of Mapudungun similar to Morse
	#   code."
	# SCP-5180("The Federation Awaits, Anomalous Apes"): "The Corvid and
	#   Troodontid both possessed a small ceramic device with a single
	#   button that produced a clicking noise when pressed. This is
	#   believed to have been used for communication between the organisms
	#   in a method similar to Morse code."

]


def IaAMorseUser(SCP=None):
    """Given an SCP-number, will return True if it is an SCP that is
    known to use Morse code, False otherwise."""
    #print "SCP:", SCP
    thisSCP = None
    if type(SCP) == NoneType:
        return False
    if type(SCP) == IntType:
        thisSCP = "SCP-%s" % SCP
    if type(SCP) == FloatType:
        thisSCP = "SCP-%s" % int(SCP)
    if type(SCP) == StringType:
        thisSCP = SCP
    try:
        #eg if passed string "2081" for SCP-2081
        thisSCP = "SCP-%s" % int(SCP)
    except:
        pass    # haven't been passed a number as a string then
        
    if thisSCP == None:
        return False

    thisSCP = thisSCP.upper()
    #print "thisSCP:", thisSCP
    if thisSCP in MORSE_USING_SCPS:
        return True
    else:
        return False



def demo1(plaintext=""):
    print "plaintext = '%s'" % plaintext
    print "encryption(plaintext) - ie converting text to Morse Code:"
    print encryption(plaintext)
    print "decryption(encryption(plaintext)) - ie converting Morse Code to text:"
    print decryption(encryption(plaintext))
    print

def demo2(plaintext=""):
    print "plaintext = '%s'" % plaintext
    print "morse(plaintext) - try converting text to Morse Code:"
    print morse(plaintext)
    print "morse(morse(plaintext)) - try converting Morse Code to text:"
    print morse(morse(plaintext))
    print


if __name__ == "__main__":
    print "morse.py \n(Version %s)" % (__VERSION__)
    print "%s Morse code-using SCPs known about.\n" % (len(MORSE_USING_SCPS))

    plaintext = "morse.py (Version %s)" % (__VERSION__)
    demo1(plaintext)
    plaintext = "this is a test. does it include spaces and punctuation?"
    demo2(plaintext)

