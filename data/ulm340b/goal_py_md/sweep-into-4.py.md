

The robot has some pre-written subroutines:

    - `check(statement)` checks whether the statement is true.
        - `check("the robot's gripper is open")`
        - `check("the robot's gripper is not around the puck")`
    - `robot.move_gripper(goal, close_gripper=True)` moves the robot's gripper towards the goal.
        - `robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)`
        - `robot.move_gripper("near the puck", close_gripper=True)`

For more info, run `python3 ./subroutines/subroutines.py`.

"""

import util

##################################################
# Helper functions and classes


def check(statement):
  """ Checks whether a statement about the world is true. """
  # print(statement)
  return util.parse_statement(statement)


class Robot:
  def __init__(self):
    self.gripper_x = 0.500
    self.gripper_y = 0.200
    self.gripper_closed = False

  def move_gripper(self, goal, close_gripper=False):
    """
    Moves the robot's gripper towards the goal.
    - close_gripper: if True, closes the gripper while moving
    """
    if close_gripper:
      self.gripper_closed = True
    if goal == "to the left":
      self.gripper_x -= 0.010
    elif goal == "to the right":
      self.gripper_x += 0.010
    elif goal == "up":
      self.gripper_y += 0.010
    elif goal == "down":
      self.gripper_y -= 0.010
    elif goal == "above the puck":
      if self.gripper_x < 0.490:
        self.gripper_x += 0.005
    elif goal == "near the puck":
      if self.gripper_x > 0.505:
        self.gripper_x -= 0.005
    elif goal == "left of the puck":
      if self.gripper_y > 0.190:
        self.gripper_y -= 0.005
    elif goal == "right of the puck":
      if