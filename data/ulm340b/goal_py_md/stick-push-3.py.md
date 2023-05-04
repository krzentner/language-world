

Please include comments describing your program, similar to the code above.

(Note: There may be some bugs in the code above! If there's a bug in a program
here, you'll have to write a program that avoids the bug.)

---

## Step 3

Please write a program to perform the last task, `stick-push`.
Begin with the text:

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
```

Please include comments describing your program, similar to the code above.

(Note: There may be some bugs in the code above! If there's a bug in a program
here, you'll have to write a program that avoids the bug.)


"""

class Robot(object):
    def __init__(self, sim):
        self.sim = sim
        self.gripper = self.sim.send_gripper(0)

    def move_gripper(self, direction, open_gripper=False, close_gripper=False):
        if open_gripper and close_gripper:
            raise Exception('open and close gripper')
        if direction == 'vertically aligned with the button':
            self.gripper.move_gripper_x_mm(x=10)
            self.gripper.move_gripper_z_mm(z=-41)
        elif direction == 'left of the button':
            self.gripper.move_gripper_x_mm(x=2)
            self.gripper.move_gripper_z_mm(z=-41)
            self.gripper.open_gripper()
        elif direction == 'around the drawer handle':
            self.gripper.move_gripper_x_mm(x=-15)
            self.gripper.move_gripper_z_mm(z=-29)
            self.gripper.open_gripper()
        elif direction == 'near the drawer handle':
            self.gripper.move_gripper_x_mm(x=13)
            self.gripper.move_gripper_z_mm(z=-29)
            self.gripper.close_gripper()
        elif direction == 'around the window handle':
            self.gripper.move_gripper_x_mm(x=-15)
            self.gripper.move_gripper_z_mm(z=-29)
            self.