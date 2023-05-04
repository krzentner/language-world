

You may use the following predicates:

|Predicate|Example|
|---|---|
|`the robot's gripper is vertically aligned with soccer ball`|`the robot's gripper is not vertically aligned with soccer ball`|
|`the robot's gripper is right of soccer ball`|`the robot's gripper is not right of soccer ball`|
|`the robot's gripper is left of soccer ball`|`the robot's gripper is not left of soccer ball`|
|`the robot's gripper is forward aligned with soccer ball`|`the robot's gripper is not forward aligned with soccer ball`|
|`the robot's gripper is around soccer ball`|`the robot's gripper is not around soccer ball`|
|`the robot's gripper is near soccer ball`|`the robot's gripper is not near soccer ball`|
|`the robot's gripper is almost vertically aligned with soccer ball`|`the robot's gripper is not almost vertically aligned with soccer ball`|
|`soccer ball is horizontally aligned with target location`|`soccer ball is not horizontally aligned with target location`|
|`soccer ball is vertically aligned with target location`|`soccer ball is not vertically aligned with target location`|
|`soccer ball is behind target location`|`soccer ball is not behind target location`|
|`soccer ball is almost vertically aligned with target location`|`soccer ball is not almost vertically aligned with target location`|
|`the robot's gripper is near target location`|`the robot's gripper is not near target location`|

To run your code, press `Submit` and then `Run`.
'''
# -*- coding: utf-8 -*-


# soccer: push the soccer ball into the target location
def soccer(robot):
    """
    Steps:
      1. Put gripper above soccer ball
      2. Push down on soccer ball
      3. Slide soccer ball to target location
    The robot can slide the soccer ball by pushing down on it from above.
    If the ball isn't below the gripper as seen from above, move the gripper
    above the soccer ball.
    If the gripper is aligned with the soccer ball but not near it, move the
    gripper down to the soccer ball to slide it.
    If the gripper is near the soccer ball, we've probably pushed the ball down
    and can slide it to the target location.
    Close the gripper to make sure we keep control of the soccer ball.
    """
    if check("