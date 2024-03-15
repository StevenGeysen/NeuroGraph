#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Regions - Insula -- Version 1
Last edit:  2024/03/15
Author:     Geysen, Steven (SG)
Notes:      - Brain regions in the insula
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



#%% ~~ Insula ~~ %%#
####################


anterior_insula = Nucleus({
    'OfficialName': 'anterior insula',
    'Lobe': 'insular', 'Functions': {'homeostasis'},
    'Sources': {'Menz et al., (2012)'}
    })



# ------------------------------------------------------------------------- End
