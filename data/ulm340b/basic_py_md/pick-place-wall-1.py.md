

**Hint:** Your program will need to pick up the puck first and then place it near the target location.
"""

pick_place_wall = """
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")
"""

######################
## Problem Statement ##
######################

def _task(func, robot):
  """Return true if 'func' executes successfully on 'robot'."""
  try:
    exec(func) in robot.controller.namespace
    return True
  except:
    print(traceback.format_exc())
    return False

def door_close(robot):
  """Close the door. The task is successful if the gripper is near the door handle."""
  return _task('''
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")''', robot)


########################
## Hidden test functions ##
########################

def _test_door_close():
  """Can the robot close the door?"""
  robot = WorldModel()
  door_close(robot)
  return robot.gripper_near_handle('door')


######################
## Unit tests for you ##
######################

def test_door_close():
  assert _test_door_close() is True, "You should close the door."

[eod] [code]import sqlite3

con=sqlite3.connect("bank.s3db")

cr=con.