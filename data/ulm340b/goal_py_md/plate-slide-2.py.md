

To do this, you should use the `robot` object.

The robot has a `move_gripper` function that takes a `direction` string and
an optional `close_gripper` boolean.

If `close_gripper` is `True`, the robot will close the gripper to try to grab
an object.

The `move_gripper` function only needs to be called once.
It is recommended to call it in an `if` statement.

Here are the `direction`s that you can choose from:

`near the plate` : Move the robot's gripper near the plate (the side near the robot).
`near the target location` : Move the robot's gripper near the plate's target location.
`almost vertically aligned with the plate` : Move the robot's gripper to line up roughly vertically with the plate (the plate is closer to the robot).
`vertically aligned with the plate` : Move the robot's gripper to line up vertically with the plate (the plate is closer to the robot).
`horizontally aligned with the plate` : Move the robot's gripper to line up horizontally with the plate (the plate is closer to the robot).
`forward aligned with the plate` : Move the robot's gripper to line up forward with the plate (the plate is closer to the robot).
`around the plate` : Move the robot's gripper around the plate (the plate is closer to the robot).
`above the plate` : Move the robot's gripper above the plate (the plate is closer to the robot).
`left of the plate` : Move the robot's gripper to the left of the plate (the plate is farther from the robot).
`in front of the plate` : Move the robot's gripper in front of the plate (the plate is farther from the robot).
`right of the plate` : Move the robot's gripper to the right of the plate (the plate is farther from the robot).
`below the plate` : Move the robot's gripper below the plate (the plate is farther from the robot).
"""
[eod] [code]from pathlib import Path

from setuptools import setup


# read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ms_deisotope',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Mass Spectrometry deisotoping utilities',