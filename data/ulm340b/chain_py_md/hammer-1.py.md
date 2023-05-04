

The robot is given the `gripper` which is a pair of grippers at the end of the arm. It can:

- `put(object1 on object2)`
- `pull(object1 towards object2)`
- `push(object1 towards object2)`
- `align(object1 to object2)`
- `insert(object1 into object2)`
- `grab(object1)`
- `drop(object1)`
- `close(object1)`
- `slide(object1 to object2)`
- `reach(to object1)`
- `open(object1)`
- `grab(object1)`
- `place(object1)`

```
hammer(robot)
```
"""
# hammer: hit the nail with the hammer
def hammer(robot):

    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")

    if check("the robot's gripper is above hammer"):
        robot.grab("hammer")

    if check("the robot's gripper is below hammer"):
        robot.push("hammer downwards")

    if check("the robot's gripper is above hammer"):
        robot.grab("hammer")

    if check("the robot's gripper is below hammer"):
        robot.push("hammer downwards")

hammer(robot)
[eod] [code]"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# s = "A man, a plan, a canal: Panama"
s = "race a car"
# s = "0p"


class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalnum(char):
            if '0' <= char <= '9' or 'a' <= char <= 'z' or 'A