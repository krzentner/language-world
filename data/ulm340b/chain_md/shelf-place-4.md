
    Steps:  1. Place gripper above object  2. Drop gripper around object  3. Place object at target
    First, place the gripper above the block.
    - When the robot's gripper is not above object, the robot should place gripper above object.
    If the gripper is not around the block and the gripper is open, drop the gripper around the block.
    - When the robot's gripper is not around object and the robot's gripper is open, the robot should drop gripper around object.
    If the gripper is around the object and the object is above the target, place it at the target.
    - When the robot's gripper is around object and object is above target, the robot should place object at target.

The task `shelf-pick-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, what steps the robot should perform?
    Steps:  1. Place gripper above object  2. Drop gripper around object  3. Place object at target
    First, place the gripper above the block.
    - When the robot's gripper is not above object, the robot should place gripper above object.
    If the gripper is not around the block and the gripper is open, drop the gripper around the block.
    - When the robot's gripper is not around object and the robot's gripper is open, the robot should drop gripper around object.
    If the gripper is around the object and the object is above the target, place it at the target.
    - When the robot's gripper is around object and object is above target, the robot should place object at target.
"""
[eod] [code]import FWCore.ParameterSet.Config as cms

from RecoJets.JetAssociationProducers.ak5JTA_cff import *
ak5JetTracksAssociatorAtVertex = ak5JetTracksAssociatorAtVertex.clone(
    jets = cms.InputTag("ak5PFJetsCHS")
)
ak5JetExtender = ak5JetExtender.clone(
    jets = cms.InputTag("ak5PFJetsCHS"),
    jet2TracksAtVertices = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    coneSize = 0.3, 
    coneSizeAt2 = 1.0,
    trackClassifier = cms.InputTag("jetTracksClassifier1")
)
ak5JetTracksAssociator