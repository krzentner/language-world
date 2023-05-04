
""".trimIndent()

        assertEquals(
            """
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("robot gripper is not forward aligned with handle"):
        robot.grab("handle")
    if check("robot gripper is forward aligned with handle"):
        robot.push("handle down")
    """.trimIndent(),
            expectedOutput.trim()
        )
    }

    @Test
    fun `test_sample_output_4`() {
        val task = getTask()
        val program = task.toCode(Language.PYTHON)
        val (_, expectedOutput) = task.runProgram(program)

        assertEquals(
            """
# push-into: push the object into the goal
def push_into(robot):
    if check("the robot's gripper is not above object and the robot's gripper is not vertically aligned with object"):
        robot.move("gripper above object")
    if check("the robot's gripper is above object and the robot's gripper is not near object and the robot's gripper is not vertically aligned with object"):
        robot.put("gripper into object")
    if check("the robot's gripper is near object and the robot's gripper is not vertically aligned with object"):
        robot.push("gripper into object")
    if check("the robot's gripper is vertically aligned with object"):
        robot.push("object into goal")
        """.trimIndent(),
            expectedOutput.trim()
        )
    }
}
[eod] [code]package ru.fors.navigation.interfaces

interface ActivityResultListener {
    fun onActivityResult(resultCode: Int, requestCode: Int)
}[eod] [code]package `in`.co.akgroups.apnaClinic.Adapter

import `in`.co.akgroups.apnaClinic.Modal.CategoryModel
import `in`.co.akgroups.apnaClinic.R
import android.content.Context
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.cardview.widget.CardView
import androidx.recyclerview.widget.RecyclerView
import com.github.marlonlom.utilities.timeago.TimeAgo
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.activity