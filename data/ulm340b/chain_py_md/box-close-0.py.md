

As you might guess, to close the box you should:

1. Line up the robot's gripper with the box lid.
2. Move the gripper over the box lid.
3. Move the gripper down to grip the box lid.
4. Move the gripper, holding the lid, over the box.
5. Drop the lid on the box.


<button class="Skip_p">Skip</button>

# Question 3

Thank you for helping me teach the robot how to do these tasks!

Please watch the following video, which is an overview of our study,
in which we ask you to teach the robot some additional tasks.
After the video, you will be asked to write programs for those tasks,
as you did in this HIT.

<div id="iframe_container">
<iframe width="750px" height="420px" src="https://www.youtube.com/embed/kY8e3o70e9M?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<script>
    if (window.innerWidth <= 900) {
        const iframes = document.querySelectorAll('iframe');
        for (let i = 0; i < iframes.length; i++) {
            iframes[i].setAttribute('width', '100%')
            iframes[i].setAttribute('height', 'calc(100vh - 80px)')
        }
    }
</script>


<button class="Skip_p">Skip</button>

# Question 4


The video described how to complete the first task, _peg-insert-side_, which is:

 1. Move the gripper over the peg.
 2. Lower the gripper so it is around the peg.
 3. Push the peg up so it is vertically aligned.
 4. Slide the peg to the hole.
 5. Push the peg in the hole.

Please write a program for the _peg-insert-side_ task that matches this procedure:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    # 