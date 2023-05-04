

The robot is looking at the plate from the side:

```
    # Steps:
    #  1. Put the gripper in front of the plate
    #  2. Move the gripper into the plate to pick it up
    #  3. Push the plate sideways to the target location
    #  4. Drop the plate at the target location
```

I can't give you an example for how to do the task itself, because that's what I'd like to ask you to write!

Here's some example code using the robot's commands, `put`, `grab`, `align`, and `insert`:

```
robot.grab("peg")
robot.align("peg to hole")
robot.insert("peg into hole")
```

Please write a program to perform the last task, `peg-insert-side`.
Begin with the text:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
```

The robot is looking at the peg from the side:

```
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
```

I can't give you an example for how to do the task itself, because that's what I'd like to ask you to write!

Here's some example code using the robot's commands, `grab`, `align`, and `insert`:

```
robot.grab("peg")
robot.align("peg to hole")
robot.insert("peg into hole")
```

Please write a program to perform the last task, `plate-slide-top`.
Begin with the text:

```
# plate-slide-top: slide the plate into the target location
def plate_slide_top(robot):
```

The robot is looking at the plate from the top:

```
    # Steps:
    #  1. Put the gripper in front of the plate
    #  2. Move the gripper into the plate to pick it up
    #  3. Push the plate to the target location
    #  4. Drop the plate at the target location
```

I can't give you an example for how to do the task itself, because that's what I'