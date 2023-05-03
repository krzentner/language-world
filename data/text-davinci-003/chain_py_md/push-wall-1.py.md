

The following steps are needed to complete this task:

1. Put gripper above wall
2. Align gripper with top of wall
3. Push gripper into top of wall
4. Line up gripper above puck 
5. Push gripper into the puck
6. Line up the puck and wall with gripper 
7. Slide puck away from wall to goal
 

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above wall
    #  2. Align gripper with top of wall
    #  3. Push gripper into top of wall
    #  4. Line up gripper above puck 
    #  5. Push gripper into the puck
    #  6. Line up the puck and wall with gripper 
    #  7. Slide puck away from wall to goal
    # First, put the gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # If the gripper is not lined up with the top of the wall, line it up.
    if check("the robot's gripper is not vertically aligned with top of wall"):
        robot.align("gripper with top of wall")
    # The wall is likely lower than the puck, so we should push down on the wall
    # to make sure we have control.
    if check("the robot's gripper is vertically aligned with top of wall"):
        robot.push("gripper into top of wall")
    # Move the gripper above the puck before we can catch it.
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    # Push down on the puck to make sure we have it and line it up with the wall.
    if check("the robot's gripper is above puck"):
        robot.push("gripper into the puck")
    # If the puck and the wall aren't lined up with the gripper, line them up.
    # This can be done by moving either the puck or the wall while keeping them
    # aligned with each other.
    if check("the puck and wall are not horizontally aligned with the robot's gripper"):
        robot.align("puck and wall with gripper")
    # Slide the puck away from the wall if it's still lined up with the wall and
    # the gripper still has control.
    if check("the puck and wall are horizontally aligned with the robot's gri