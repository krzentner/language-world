

You can also write a comment describing the steps required to complete the task.
'''

# YOUR CODE HERE
def plate_slide(robot):
    # Steps:
    #  1. Move robot gripper to above plate.
    #  2. Drop gripper down onto plate.
    #  3. Push plate onto target location
    # move gripper above plate
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate")
    # Drop gripper down onto plate
    if check("the robot's gripper is not on plate"):
        robot.move_gripper("on plate")
    # Push plate onto target location
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above target location")

'''You can now use the command `execute` to ask the robot to perform any task! For example,

```python
execute(button_press_topdown)
```

or

```python
execute(reach)
```

or even

```python
execute(plate_slide)
```

Now try to complete the following tasks:

'''

execute(plate_slide)
execute(push)
execute(reach)
execute(pick_place)
execute(window_open)
execute(window_close)
execute(drawer_close)
execute(drawer_open)
execute(door_open)
execute(peg_insert_side)
execute(button_press_topdown)
[eod] [code]import cv2

def change_img_format(filename, format_to_change):
    im = cv2.imread(filename)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    cv2.imwrite("output_images/{}.{}".format(filename.split('.')[0], format_to_change), im)

change_img_format("data/cat.jpg", "bmp")
change_img_format("data/cat.jpg", "png")[eod] [code]# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор',
                               null=True, blank=True, related_name='comments')
    text = models.TextField(verbose_name='Комментарий', blank