#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Nucleus class -- Version 1.1
Last edit:  2024/03/15
Author:     Geysen, Steven (SG)
Notes:      - Nucleus class to build NeuroGraph
            - Release notes:
                * Fix presentation
To do:      - Information in nodes
            - Filters
            - Plotting
Comments:   
Sources:    Python 3 Object-Oriented Programming (Phillips, 2018)
            https://python-course.eu/applications-python/graphs-python.php
"""



#%% ~~ Imports ~~ %%#


import abc

from collections.abc import Container



#%% ~~ Nucleus class ~~ %%#
###########################


class Nucleus():
    """Nucleus node, containing all information for filtering and plotting."""

    _nucleus_keys = [
        'OfficialName', 'Lobe', 'Subregion', 'Network', 'Connections',
        'SignalTo', 'SignalFrom', 'Neurotransmitters', 'Functions', 'Sources'
        ]

    def __init__(self, nucleus_dict=None):
        # Create nucleus data dictionary
        if nucleus_dict == None:
            nucleus_dict = {keyi: set() for keyi in Nucleus._nucleus_keys}
        ## Add missing keys
        missing_dict = {
            keyi: set() for keyi in Nucleus._nucleus_keys - nucleus_dict.keys()
            }
        if not len(missing_dict.keys()) == 0:
            nucleus_dict = nucleus_dict | missing_dict
        self._nucleus_dict = nucleus_dict
    
    
    def connections(self, _nucleus_dict):
        return [
            nami['OfficialName'] for nami in _nucleus_dict['Connections']
            ]
    
    
    def add_to_subregion(self, subregion):
        self._nucleus_dict['Subregion'] = subregion
    
    
    def add_connection(self, brain_part):
        self._nucleus_dict['Connections'].add(brain_part)
        
        #TODO: Update 'Connections' of both brain parts
    
    
    def __repr__(self):
        return f'Nucleus ({self._nucleus_dict["OfficialName"]})'
    
    
    def __str__(self):
        return self._nucleus_dict['OfficialName']



# ------------------------------------------------------------------------- End
