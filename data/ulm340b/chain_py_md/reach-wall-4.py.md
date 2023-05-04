

You may need to do the following actions:

  - `if check("the robot's gripper is not vertically aligned with puck"): robot.put("gripper above puck")`
  - `if check("the robot's gripper is not above puck"): robot.place("gripper above puck")`
  - `if check("the robot's gripper is not vertically aligned with the puck"): robot.put("the gripper above the puck")`
  - `if check("the robot's gripper is not above puck"): robot.place("gripper above puck")`
  - `if check("the robot's gripper is not near reach target"): robot.reach("to goal")`
  - `if check("the robot's gripper is not vertically aligned with reach target"): robot.put("gripper above reach target")`
  - `if check("the robot's gripper is not above reach target"): robot.place("gripper above reach target")`

You will know you've got it when the task is solved.
""".trimIndent(),

"12": """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# window-open: slide