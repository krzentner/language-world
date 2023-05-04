
    - First, move the robot's gripper until the robot's gripper is left of the handle and the robot's gripper is closed
    - Then, move the robot's gripper until the robot's gripper is near the handle
"""

# This is the full language.
_LANGUAGE_SPECIFICATION = (
    [_WORD_TYPES]
    + [_RELATION_TYPES]
    + [_PREDICATE_TYPES]
    + [_TYPE_HIERARCHY]
    + [_OBJECTS_BY_TYPE]
    + [_FUNCTIONS_BY_TYPE]
    + [_POSSIBLE_ACTION_PARAMS_BY_TYPE]
    + [_TASK_LIST]
    + _TUTORIAL_TEXT.split("\n")
)

_LANGUAGE_SPECIFICATION_WITH_DEFAULTS = [
    "Default starting state:",
    "{} (the robot's gripper is open and not holding anything)",
    "",
    _WORD_TYPES,
    _RELATION_TYPES,
    _PREDICATE_TYPES,
    _TYPE_HIERARCHY,
    _OBJECTS_BY_TYPE,
    _FUNCTIONS_BY_TYPE,
    _POSSIBLE_ACTION_PARAMS_BY_TYPE,
    "{} (the object is on the ground and the robot's gripper is not on the object)",
    "{} (the robot's gripper is above the object and the robot's gripper is closed)",
    "{} (the robot's gripper is forward aligned with the object and the robot's gripper is closed)",
    "{} (the robot's gripper is below the object and the robot's gripper is closed)",
    "{} (the robot's gripper is above the object and the robot's gripper is closed)",
    "{} (the robot's gripper is almost vertically aligned with the object and the robot's gripper is closed)",
    "{} (the robot's gripper is vertically aligned with the object and the robot's gripper is closed)",
    "{} (the robot's gripper is near the object and the robot's gripper is closed)",
    "{} (the object is below the robot's gripper and the robot's gripper is closed)",
    "{} (the robot's gripper is forward aligned with the object and the robot's gripper is closed)",
    "{} (the robot's gripper is horizontally aligned with the object and the robot's gripper is closed)",
    _TASK_LIST,
    _TUTORIAL_TEXT,
]
[eod] [code]import json

# json模块