

If you would like to use a particular action, it can be done via:

```
robot.<action>("<argument>")
```

The available actions and their arguments are listed below:

```
action: put
arguments: [gripper] near [object],
           [gripper] below [object],
           [gripper] above [object],
           [gripper] behind [object],
           [gripper] in front of [object],
           [gripper] to left of [object],
           [gripper] to right of [object]

action: slide
arguments: [object] left,
           [object] right,
           [object] up,
           [object] down,
           [object] forward,
           [object] backward,
           [object] away from [object],
           [object] towards [object]

action: close
arguments: [gripper] around [object]

action: open
arguments: [gripper] away from [object],
           [gripper] above [object]

action: grab
arguments: [object],
           [object] near [gripper],
           [object] below [gripper],
           [object] above [gripper],
           [object] behind [gripper],
           [object] in front of [gripper],
           [object] to left of [gripper],
           [object] to right of [gripper]

action: align
arguments: [object] to [object],
           [object] with [object]

action: drop
arguments: [gripper] near [object],
           [gripper] below [object],
           [gripper] above [object],
           [gripper] behind [object],
           [gripper] in front of [object],
           [gripper] to left of [object],
           [gripper] to right of [object]

action: insert
arguments: [object] into [object],
           [object] on top of [object],
           [object] into [location],
           [object] at [location],
           [object] below [object],
           [object] on [object],
           [object] above [object],
           [object] behind [object],
           [object] in front of [object],
           [object] to left of [object],
           [object] to right of [object]

action: pull
arguments: [object] forward,
           [object] backward,
           [object] away from [object],
           [object] towards [object]

action: push
arguments: [gripper] into [object],