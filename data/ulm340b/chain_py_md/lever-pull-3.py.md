

You will need to fill in the code to perform the task, and document it.
You can use the following commands:

 - `robot.put`
 - `robot.slide`
 - `robot.push`
 - `robot.align`
 - `robot.insert`
 - `robot.reach`
 - `robot.grab`
 - `robot.drop`
 - `robot.close`
 - `robot.pull`
 - `robot.move`
 - `check`
 - `get_position`
 - `get_angle`

If you want to test your code before you submit it, copy and paste this command in a Python interpreter:

```python
import gym
env = gym.make("gym_robot_manipulation:RobotManipulation-v0")
env.reset()
env.eval("""

def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
  