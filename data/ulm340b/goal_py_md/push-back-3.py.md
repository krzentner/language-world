

"""
import sys

def robot_position(robot):
  return 1.0 if (robot.y - robot.y_min) / robot.y_range >= 0.5 else -1.0

def robot_angle(robot):
  return robot.z_min * 0.5


def check(condition):
  assert eval(condition)
  return True


def move_gripper(command, close_gripper=False):
  command = command.replace("robot's gripper", "position")
  command = command.replace("the", "")
  command = command.replace("object", "objects[0]")
  parts = command.split(" ")
  if close_gripper and parts[-1] == "open":
    command = "open"
  elif close_gripper and parts[-1] == "closed":
    command = "closed"
  elif parts[-1] == "open":
    command = "closed"
  elif parts[-1] == "closed":
    command = "open"
  if command == "around":
    command = "near"
  if command == "to the left":
    command = "left"
  if command == "to the right":
    command = "right"
  if command == "to the side":
    command = "side"
  if command == "front":
    command = "in front"
  if command == "behind":
    command = "left of"
  if command == "leftmost":
    command = "left of"
  if command == "forward":
    command = "in front"
  if command == "backward":
    command = "left of"
  if command == "above":
    command = "above"
  if command == "below":
    command = "under"
  if command == "aligned":
    command = "aligned"
  if command == "in line":
    command = "aligned"
  if command == "inside":
    command = "inside"
  if command == "not in line":
    command = "aligned"
  if command == "almost":
    command = ""
  if command == "not in line":
    command = "aligned"
  if command == "left":
    command = "left of"
  if command == "right":
    command = "right of"
  if command == "vertically":
    command = "vertically"
  if command == "horizontally":
    command = "horizontally"
  if command == "not vertically":
    command = "vertical