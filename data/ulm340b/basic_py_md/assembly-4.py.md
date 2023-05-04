
"""

from language import ProgramRunner

assembly_program = '''
# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("wrench is not around the peg"):
        robot.drop("wrench around peg")
'''


def test_assembly():
    env = ProgramRunner()
    env.program = assembly_program

    assert env.run()

    for t in env.observations:
        env.render(t)
[eod] [code]import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


if __name__ == "__main__":
    # For webcam input:
    camera = cv2.VideoCapture(0)

    with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            frame.flags.writeable = False
            results = hands.process(frame)

            frame.flags.writeable = True
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=hand_landmarks,
                        connections=mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles
                        .get_default_hand_landmarks_style())
            cv2.imshow('MediaPipe Hands', frame)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        camera.release()
        cv2.destroy