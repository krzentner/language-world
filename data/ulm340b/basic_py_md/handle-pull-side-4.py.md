

# --hints--

The code must be a function definition for handle_pull_side.

```js
assert(
  code.includes('def handle_pull_side(robot):\n') &&
    code.includes('pass') &&
    code.includes('\\n')
);
```

The code must use the robot library correctly to pass the evaluation.

```js
assert(robotEval.call(robot) === true);
```

# --seed--

## [webdriver - write code](https://docs.codecademy.com/courses/learn-programming/lessons/webdriver-practice/challenges/write-code)

```js
const robot = {
  align: function(p) {
    console.log(`robot.align(${p})`);
  },
  drop: function(p) {
    console.log(`robot.drop(${p})`);
  },
  grab: function(p) {
    console.log(`robot.grab(${p})`);
  },
  insert: function(p) {
    console.log(`robot.insert(${p})`);
  },
  move: function(p) {
    console.log(`robot.move(${p})`);
  },
  place: function(p) {
    console.log(`robot.place(${p})`);
  },
  put: function(p) {
    console.log(`robot.put(${p})`);
  },
  push: function(p) {
    console.log(`robot.push(${p})`);
  },
  pull: function(p) {
    console.log(`robot.pull(${p})`);
  },
  reach: function(p) {
    console.log(`robot.reach(${p})`);
  },
  slide: function(p) {
    console.log(`robot.slide(${p})`);
  },
  close: function(p) {
    console.log(`robot.close(${p})`);
  },
  open: function(p) {
    console.log(`robot.open(${p})`);
  },
  type: function(p) {
    console.log(`robot.type(${p})`);
  }
};
const check = function(p) {
  console.log(`check(${p})`);
};

var code =
  '// handle-pull-side: pull up the handle from