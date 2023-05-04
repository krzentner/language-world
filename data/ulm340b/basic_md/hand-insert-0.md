
- I'm not sure yet, please show me examples.


I'm not sure yet, please show me examples.

The task `hand-insert` requires the robot to pick up the puck and move it to the target location.
To pick up the puck and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with puck, the robot should put gripper above puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should grab puck.
    - When the robot's gripper is near the puck and the robot's gripper is closed, the robot should place puck at goal.
"""
[eod] [code]# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
"""Tests for `tf.data.experimental.make_batched_features_dataset()`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from tensorflow.core.example import example_pb2
from tensorflow.core.example import feature_pb2
from tensorflow.python.data.kernel_tests import test_base
from tensorflow.python.data.ops import dataset_ops
from tensorflow.python.feature_column import make_parse_example_spec_op
from tensorflow.python.ops import parsing_ops
from tensorflow.python.ops import variables
from tensorflow.python.platform import test


class MakeBatchedFeaturesDatasetTest(test_base.DatasetTestBase):

  @test_base.run_all_in_graph_and_eager_modes
  def testMakeBatchedFeaturesDataset(self):
    example1 = example_pb2.Example(
        features=feature_pb2.Features(
            feature={
                "int64_feature":
                    feature_pb2.Feature(int64_list=feature_pb2