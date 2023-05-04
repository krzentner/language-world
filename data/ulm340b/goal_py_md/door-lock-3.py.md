

Use `check("the robot's gripper is ...")` to verify that the gripper is in the correct position before moving it with `robot.move_gripper("...")`.

To see all the steps in the `door-lock` task, use the simulator:

```
simulator.visualize_program("door-lock")
```

"""

# TODO: write this function
def door_lock(robot):
    pass


# TODO: write this function
def run_program():
    pass


def run_simulator(program, display_image):
    import simulator

    def get_action(robot, world, program):
        """Takes the action chosen by the program."""
        action = program[robot.program_counter](robot)
        robot.program_counter += 1
        return action

    def program_done(robot):
        return robot.program_counter >= len(program)

    simulator.simulate_world(
        program,
        get_action,
        program_done,
        display_image,
    )


def visualize_program(program_name):
    display_image = "rgb"
    run_simulator(programs[program_name], display_image)


def main():
    while True:
        print(
            """
door-lock: use the robot's gripper to turn the dial on the door
button-press-side: press the button from the side
drawer-close: push the drawer closed
drawer-open: pull the drawer open
door-close: push the door closed
door-lock: turn the dial on the door
door-open: pull the door open
peg-insert-side: insert the peg into the hole
pick-place: pick up the puck and hold it at the target location
push: slide the puck to the target location
reach: reach to the target location
window-close: slide the window closed to the right
window-open: slide the window open to the left
visualize_program: visualize one of the programs

What would you like to do?
"""
        )
        command = input()
        if command == "door-lock":
            run_program()
        elif command == "button-press-side":
            visualize_program("button-press-side")
        elif command == "drawer-close":
            visualize_program("drawer-close")
        elif command == "drawer-open":
            visualize_program("drawer-open")
        elif command == "door-close":
            visualize_program("door-close")
        elif command ==