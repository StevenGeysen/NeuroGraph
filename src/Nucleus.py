#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Nucleus class -- Version 1
Last edit:  2024/01/28
Author:     Geysen, Steven (SG)
Notes:      - Nucleus class to build NeuroGraph.
            - Release notes:
                * Initial commit
To do:      - Information in nodes
            - Filters
            - Plotting
Comments:   
Sources:    Python 3 Object-Oriented Programming (Phillips, 2018)
            https://python-course.eu/applications-python/graphs-python.php
"""



#%% ~~ Imports and directories ~~ %%#


from pathlib import Path


# Directories
SPINE = Path.cwd()



#%% ~~ Nucleus class ~~ %%#
###########################


class Nucleus(object):
    """Nucleus node, containing all information for filtering and plotting."""

    _nucleus_keys = [
        'OfficialName', 'Lobe', 'Subregion', 'Network', 'Connections',
        'SignalTo', 'SignalFrom', 'Neurotransmitters', 'Functions', 'Sources'
        ]

    def __init__(self, nucleus_dict=None):
        if nucleus_dict == None:
            nucleus_dict = {keyi: None for keyi in Nucleus._nucleus_keys}
        self._nucleus_dict = nucleus_dict
    
    def connections(self, _nucleus_dict):
        return [
            nami['OfficialName'] for nami in _nucleus_dict['Connections']
            ]
    
    def add_to_subregion(self, subregion):
        self._nucleus_dict['Subregion'] = subregion



# ------------------------------------------------------------------------- End
