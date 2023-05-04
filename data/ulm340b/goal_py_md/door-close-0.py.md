

Write a program using these instructions:

- check: Check if a condition is true or false. The condition is provided in English.
- move_gripper: Move the robot's gripper towards a target location. The target location is provided in English.
  - The robot's gripper will continue moving towards the target location until the condition is true.
  - Optional: Provide `close_gripper=True` to close the gripper.
"""


# door-close: push the door closed to the target location
def door_close(robot):
    # We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")

    # Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")

    # Once the gripper is around the door handle, we can just pull the drawer open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")


# Please press 'Submit' to continue.
[eod] [code]import os

from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-geocoder-tgos',
    version='0.1',
    description='TGOS geocoder for django-geocoder',
    author='Mikko Hellsing',
    author_email='mikko@opensourcehacker.com',
    url='https://github.com/miohtama/django-geocoder-tgos',
    license='BSD',
    package_dir={'': 'src'},
    packages=['geocoder_tgos',],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming