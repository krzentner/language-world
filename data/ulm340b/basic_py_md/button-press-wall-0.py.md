

In the program, you should use functions like `robot.check`.
You can learn more about how to write a program for the robot here:
[Programming a Robot in WebPPL](http://webppl.org/robot/0.1/tutorial/01_basics.html).

For example, here's a program for the first task, `window-close`:

```
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")
```

When you are finished, please submit the name of your program (e.g. `window_close`), but not the code.
"""
[eod] [code]"""
The :mod:`sklearn.metrics.cluster` module includes score functions that can be
used to evaluate the results of a clustering.
"""

# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck
#         Joel Nothman <joel.nothman@gmail.com>
#
# License: BSD 3 clause

from __future__ import division

import numpy as np

from ..base import _average_binary_score, _check_reg_targets
from ..utils.validation import _check_sample_weight, check_array
from ..utils import check_consistent_length
from ..metrics.pairwise import euclidean_distances

__all__ = ["adjusted_rand_score", "rand_score", "completeness_score",
           "homogeneity_score", "adjusted_mutual_info_score",
           "mutual_info_score", "normalized_mutual_info_score",
           "entropy", "davies_bouldin_score"]


def adjusted_rand_score(labels_true, labels_pred, \
                        labels_true_unique=None,
                        labels_pred_unique=None):
    """Adjusted Rand Index.

    .. versionadded:: 0.12

    Parameters
    ----------
    labels_true : array-like of shape (n_samples,)
        Ground truth class labels to be used