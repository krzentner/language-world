

## Test Cases

Your code should pass these tests:

```
> python hello-robot.py
> hello-robot.py --task box-close
```
'''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Move the robot's gripper towards the lid
    #  2. Grab the lid
    #  3. Put the lid on top of the box
    #  4. Move the robot's gripper away from the lid
    # First, we want to move the robot's gripper towards the lid, so it
    # can grab the lid
    if check("the robot's gripper is not close to the lid"):
        robot.move("gripper towards lid")
    # Next, we want to grab the lid.
    # To do this, we close the gripper and see if we are able to pick up the lid
    if check("the robot's gripper is near the lid and the robot's gripper is open"):
        robot.close("gripper around the lid")
    # Once the robot has closed the gripper around the lid,
    # we want to make sure it is holding onto the lid
    if check("the robot's gripper is near the lid and the robot's gripper is closed"):
        robot.place("gripper above the lid")
    # Finally, now that the gripper is closed around the lid,
    # we want to make sure that we are no longer near the lid
    # so that the robot is out of the way
    if check("the robot's gripper is near the lid"):
        robot.move("the robot away from the lid")


def main():
    from hello_robot import Robot, check_task
    robot = Robot()
    if check_task():
        task_fns = [box_close]
    else:
        task_fns = [
            door_open,
            reach,
            window_close,
            button_press_topdown,
            drawer_close,
            drawer_open,
            push,
            window_open,
            peg_insert_side,
            pick_place,
            box_close,
        ]
    robot.run(task_fns)


if __name__ == '__main__':
 