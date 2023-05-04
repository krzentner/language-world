

You can use the same statements shown in the other programs.

If you don't know what to do, you can give the robot a `robot.hint()`
message with your best guess about what it should do next.

If the robot performs a task other than the one you want, you can tell
it to cancel with the `robot.cancel()` message.

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not around stick"):
        robot.grab("stick")
    if check("the robot's gripper is around stick"):
        robot.place("stick in front of thermos")
    if check("stick is in front of thermos"):
        robot.push("thermos")
    if check("thermos is near thermos goal"):
        robot.cancel()
```
"""
def stick_push(robot):
    if check("the robot's gripper is not around stick"):
        robot.grab("stick")
    if check("the robot's gripper is around stick"):
        robot.place("stick in front of thermos")
    if check("stick is in front of thermos"):
        robot.push("thermos")
    if check("thermos is near thermos goal"):
        robot.cancel()
[eod] [code]# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""Script to validate the accuracy of a model on ImageNet.

This script requires a trained model.  To train a model please see:

  https://www.tensorflow.org/hub/common_usages/image_classification_with_hub

  and specifically use the imagenet_preprocessing.py script.

This will validate the model on validation set (or user-specified data
directory), computing the top-1 accuracy of the model.   If you have