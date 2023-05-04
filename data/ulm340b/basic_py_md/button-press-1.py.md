

and then include a `check` statement and a command as seen above in the code examples, that make the `button-press` task work.

```
if check("the robot's gripper is not horizontally aligned with the button"):
```



```python
# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.align("gripper to button")
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.push("the button")
```

[eod] [code]from ..core import *
from ..graph import *
from .utils import *


def add_conv_layer(prev, n, k=3, s=1, p='SAME', use_bias=True, relu=True, **kwargs):
    if 'padding' in kwargs:
        p = kwargs['padding']
    layer = conv_layer(prev, n, k, s, p, use_bias, relu, **kwargs)
    return layer

def add_deconv_layer(prev, n, k=4, s=2, p='SAME', use_bias=True, relu=True, **kwargs):
    if 'padding' in kwargs:
        p = kwargs['padding']
    layer = deconv_layer(prev, n, k, s, p, use_bias, relu, **kwargs)
    return layer

def add_max_pool_layer(prev, k=2, s=2, padding='SAME', **kwargs):
    if 'padding' in kwargs:
        padding = kwargs['padding']
    layer = max_pool_layer(prev, k, s, padding)
    return layer

def add_fc_layer(prev, n, relu=True, use_bias=True, **kwargs):
    layer = fc_layer(prev, n, use_bias, relu, **kwargs)
    return layer

def add_batch_norm_layer(prev, training=True, **kwargs):
    layer = batch_norm_layer(prev, training)
    return layer


def add_conv_trans_layer(prev, n, k=3, s=2, p='SAME', use_bias=True, relu=True, **kwargs):
    if 'padding' in kwargs:
        p = 