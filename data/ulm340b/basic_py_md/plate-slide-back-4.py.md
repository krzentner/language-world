
"""

# Instructions:
# Please write a program to perform the last task, `plate-slide-back`.


def plate_slide_back(robot):
    if check(
        "the robot's gripper is not above the plate handle and the robot's gripper is not vertically aligned with the plate handle"
    ):
        robot.put("the gripper above the plate handle")
    if check(
        "the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not near the plate handle"
    ):
        robot.push("the gripper into the plate handle")
    if check(
        "the robot's gripper is near the plate handle and the plate handle is below the robot's gripper"
    ):
        robot.slide("the plate back to the goal")
[eod] [code]from tensorflow.keras import Model
from tensorflow.keras.layers import (
    Input,
    Dense,
    Activation,
    concatenate,
    Lambda,
    TimeDistributed,
    LSTM,
    Bidirectional,
    GRU,
    GlobalAveragePooling1D,
    Dropout,
)


def build_lstm_network(config, model_name):
    input_shape = config.getint("data", "input_dim")
    input_data = Input(shape=input_shape)

    x = Bidirectional(LSTM(units=32, return_sequences=True))(input_data)
    x = GlobalAveragePooling1D()(x)

    prediction = Dense(units=1, activation="sigmoid")(x)

    model = Model(input_data, prediction)
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return model


def build_gru_network(config, model_name):
    input_shape = config.getint("data", "input_dim")
    input_data = Input(shape=input_shape)

    x = Bidirectional(GRU(units=32, return_sequences=True))(input_data)
    x = GlobalAveragePooling1D()(x)

    prediction = Dense(units=1, activation="sigmoid")(x)

    model = Model(input_data, prediction)
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return model
[eod] 