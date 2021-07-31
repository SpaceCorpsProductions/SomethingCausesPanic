#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Collects our error clases together:

Used by scp_widgets.py:
    ObjectClassError, DisruptionClassError, RiskClassError

used by make_area_signs.py
    SecurityError

used by map_prototype.py/site_map.py
    FormatError, CenterError
"""

#Content relating to the SCP Foundation, including the SCP Foundation
#logo, is licensed under Creative Commons Sharealike 3.0 and all
#concepts originate from http://www.scpwiki.com and its authors.
#This file, being derived from this content, is hereby
#also released under Creative Commons Sharealike 3.0.

#See http://www.scpwiki.com/licensing-guide and
#http://creativecommons.org/licenses/by-sa/3.0/ for more information.

VERSION = "0.9.0a"
__VERSION__ = VERSION



#used by scp_widgets.py
class ObjectClassError(Exception):
    """Used when an unknown OBJECTCLASS is passed to our DangerDiamond widget"""
    pass

class DisruptionClassError(Exception):
    """Used when an unknown DISRUPTIONCLASS is passed to our DangerDiamond widget"""
    pass

class RiskClassError(Exception):
    """Used when an unknown RISKCLASS is passed to our DangerDiamond widget"""
    pass


#used by make_area_signs.py
class SecurityError(Exception):
    """Used when the colour or other data is wrong with a security level or clearance"""
    pass


#used by map_prototype.py/site_map.py
class FormatError(Exception):
    """Used when an unknown image format is specified for map output"""
    pass

class CenterError(Exception):
    """Used when an unknown shape specified for central area"""
    pass

