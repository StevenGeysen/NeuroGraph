#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Regions - Prefrontal cortex -- Version 1
Last edit:  2024/03/15
Author:     Geysen, Steven (SG)
Notes:      - Brain regions in the prefrontal cortex
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


from src.Nucleus import Nucleus



#%% ~~ Prefrontal cortex ~~ %%#
###############################


dlPFC = Nucleus({
    'OfficialName': 'dorsolateral prefrontal cortex',
    'Lobe': 'frontal', 'Subregion': 'prefrontal cortex',
    'Functions': {'self control'},
    'Sources': {'Dantas et al., (2023)'}
    })


vmPFC = Nucleus({
    'OfficialName': 'ventromedial prefrontal cortex',
    'Lobe': 'frontal', 'Subregion': 'prefrontal cortex',
    'Connections': {dlPFC}, 'Functions': {'reward valuation'},
    'Sources': {'Dantas et al., (2023)'}
    })


dlPFC.add_connection(vmPFC)



# ------------------------------------------------------------------------- End
