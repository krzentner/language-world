
"""

class Robot:
    def __init__(self, position_data):
        """Position data is an array of all positions of objects in the workspace."""
        self.position_data = position_data
        self.gripper_distance_moved = 0
        self.gripper_is_closed = False
        self.gripper_target = None

    def move_gripper(self, new_location, close_gripper=False):
        """Moves the gripper to the location, optionally closing it as well.

        You can use the following kinds of relative directions as locations:
         - left of the peg
         - left of the peg as viewed from the side
         - below the peg as viewed from the side
         - above the peg as viewed from the side
         - vertically aligned with the peg as viewed from the front
         - vertically aligned with the peg as viewed from above
         - forward aligned with the peg as viewed from the side
         - horizontally aligned with the peg as viewed from the side

        You can also use the names of objects as locations:
         - the peg
         - the hole
         - reach target
         - target location

        Or a combination of the two:
         - near the peg
         - above the hole
         - right of the peg as viewed from above
         - above the reach target
         - left of the target location

        To close the gripper, set the `close_gripper` parameter to `True`.
        """
        self.gripper_target = {
            "the peg": "peg",
            "peg": "peg",
            "the hole": "hole",
            "hole": "hole",
            "target location": "goal",
            "target": "goal",
            "reach target": "reach",
            "reach": "reach",
            "window handle": "handle2",
            "handle": "handle2",
            "window": "handle2",
            "window handle": "handle2",
            "drawer handle": "handle",
            "handle": "handle",
            "drawer": "handle",
            "drawer handle": "handle",
            "door handle": "handle3",
            "handle": "handle3",
            "door": "handle3",
            "door handle": "handle3",
            "puck": "puck",
            "button": "button",
        }.get(new_location.lower(), new_location)
        self.gripper_is_closed = close_gripper


# ================================================================
# Tasks
# ================================================================

# You can