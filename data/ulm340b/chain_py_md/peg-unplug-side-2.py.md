

"""

print("We'll be waiting to make sure you don't accidentally run the program too early.  Hit enter when you're ready.")
input()





# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull peg away from hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")[eod] [code]
# coding: utf-8

# ### 1.
# ### Import the required libraries

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

def get_age(date_column, age_column, bdate_column='date_of_birth', format='%Y%m%d'):
    '''
    Generates the age of individuals based on the date of birth.

    Parameters:
        date_column (str): Name of the data column containing the event's date
        age_column (str): Name of the data column where the generated ages will be stored
        bdate_column (str,