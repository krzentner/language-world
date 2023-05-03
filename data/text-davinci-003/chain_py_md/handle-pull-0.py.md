

Steps:
  1. Put gripper above handle
  2. Grab handle with gripper
  3. Pull handle up 

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # To start, put the gripper above the handle to get a better grip on it.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper isn't around the handle, grab it with the gripper.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.grab("handle")
    # If the gripper is around the handle and closed, pull it up.
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.pull("handle up")        
``