

In the rest of this document, I'll give you more details about how the robot can be controlled.

You can see the full set of example programs in the file `scripts/robot_examples.py`.
You can add the following code to your program to run any of the examples
(e.g. if you add the code to run `door_open`, you should run `door_open` instead
of the default `push-wall`):

```
def run_program(robot, program):
    def check(condition):
        return check_robot(robot, condition)
    program(robot)

def run_drawer_open(robot):
    run_program(robot, drawer_open)

def run_drawer_close(robot):
    run_program(robot, drawer_close)

def run_door_open(robot):
    run_program(robot, door_open)

def run_peg_insert_side(robot):
    run_program(robot, peg_insert_side)

def run_window_open(robot):
    run_program(robot, window_open)

def run_window_close(robot):
    run_program(robot, window_close)

def run_reach(robot):
    run_program(robot, reach)

def run_pick_place(robot):
    run_program(robot, pick_place)

def run_push(robot):
    run_program(robot, push)
```

To run one of these examples, add the following code to your program and then
run your program:

```
run_program(robot, door_open)
```

To run your `push-wall` code, add the following code:

```
run_program(robot, push_wall)
```

If you want to see an animation of what the robot should do, you can add the following code:

```
animate(robot)
```

If you want to get advice on what your program should do next, you can add the following code:

```
recommendation = advice(robot)
```

`recommendation` will be a string with some text about what the robot should do,
such as `"Try: `"the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck`".`

You can print a message describing the robot's state with the following code:

```
show(robot)
```

To run your program, make sure that your file