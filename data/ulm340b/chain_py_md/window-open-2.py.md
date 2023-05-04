

The `robot` object has the following methods:

* `move(text)`: Move the gripper toward the target location specified by `text`.
* `put(text)`: Move the gripper above the target location specified by `text`.
* `drop(text)`: Move the gripper below the target location specified by `text`.
* `slide(text)`: Push the target object specified by `text` to the side.
* `slide_to(text)`: Slide the gripper towards the target location specified by `text`.
* `push(text)`: Push the gripper forward towards the target specified by `text`.
* `push_to(text)`: Push the target object specified by `text`.
* `pull(text)`: Pull the target object specified by `text`.
* `pull_back(text)`: Pull the gripper back towards the target location specified by `text`.
* `close(text)`: Close the gripper around the target specified by `text`.
* `close_at(text)`: Close the gripper near the target specified by `text`.
* `grab(text)`: Close the gripper around the target specified by `text`.
* `grab_at(text)`: Close the gripper near the target specified by `text`.
* `open(text)`: Open the gripper when at the target location specified by `text`.
* `open_at(text)`: Open the gripper near the target location specified by `text`.
* `pick_up(text)`: Pick up the target object specified by `text`.
* `put_down(text)`: Place down the target object specified by `text`.
* `release(text)`: Release the gripper while holding the target object specified by `text`.
* `insert(text)`: Insert the target object specified by `text`.
* `align(text)`: Adjust the alignment of the target object specified by `text`.
* `align_to(text)`: Adjust the gripper's position to the target object specified by `text`.
* `align_with(text)`: Adjust the gripper's alignment to the target object specified by `text`.
* `place(text)`: Move the gripper to the target location specified by `text`.
* `remove(text)`: Move the gripper to the target location specified by `text`.

The `robot` object also has the `check(text)` method, which returns a `True`
or `False` depending on the result of the logical expression described by
`text`. For example, in the following example `check(text