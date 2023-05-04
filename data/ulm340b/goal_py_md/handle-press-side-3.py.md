

Steps:
  1. Put gripper above the handle
  2. Line up gripper with the handle as viewed from above
  3. Push down on the handle
```

```python
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Line up gripper with the handle as viewed from above
    #  3. Push down on the handle
    # As long as the robot's gripper is vertically aligned with handle we can
    # move it above the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is above the handle, it can be lined up with handle
    # without danger of hitting the handle from the side.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("vertically aligned with handle", close_gripper=True)
    # As long as the gripper is aligned with the handle, it can push down on the
    # handle without danger of hitting it from the side.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle", close_gripper=True)
```
[eod] [code]'''
Given two strings, return True if either of the strings appears at the very end of the other string,
unless it appears only as a prefix of the other string. In other words,
a string appears as a suffix of the other string,
unless it is a prefix of the other string.


end_other("Hiabc", "abc") → True
end_other("AbC", "HiaBc") → True
end_other("abc", "abXabc") → True
end_other("abc", "abXabXabc") → False
end_other("abc", "HiaBabc") → False
end_other("abc", "abc") → False
'''


def end_other(a, b):
    a_len = len(a)
    b_len = len(b)

    b_as_suf = a[-b_len:] == b
    b_as_pref = b[:a_len] == a

    if not b_as_pref:
        # we could also use else
        return