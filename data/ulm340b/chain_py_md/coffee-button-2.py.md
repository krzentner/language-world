

When you are finished, write `coffee_button(`, then click the button.

"""

import pandas as pd
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def check(statement):
    return statement

def robot(verb):
    verb = verb.lower()
    verb = verb.replace(' ', '_')
    verb = verb.replace('-', '_')
    global verbs
    global objects
    global prepositions

    verb = verb.replace(verb, verbs[verb][1:])
    pre = verbs[verb].split('-')
    if len(pre) > 1:
        obj = pre[1]
        verb = pre[0]
        pre = prepositions[obj][pre[1]]
    else:
        obj = None
        pre = None
    if verb == 'move':
        return 'move the gripper {0}'.format(pre)
    if verb == 'push':
        return 'push {0} {1}'.format(pre, obj)
    if verb == 'pull':
        return 'pull {0} {1}'.format(pre, obj)
    if verb == 'slide':
        return 'slide {0} {1}'.format(pre, obj)
    if verb == 'drop':
        return 'drop {0} {1}'.format(pre, obj)
    if verb == 'place':
        return 'place {0} {1}'.format(pre, obj)
    if verb == 'align':
        return 'align {0} {1}'.format(pre, obj)
    if verb == 'insert':
        return 'insert {0} {1}'.format(pre, obj)
    if verb == 'reach':
        return 'reach towards the target'
    if verb == 'grab':
        return 'grab {0}'.format(obj)
    if verb == 'close':
        return 'close the gripper around {0}'.format(obj)
    if verb == 'put':
        return 'put {0} {1}'.format(obj, pre)

class World:
    def __init__(self, verb