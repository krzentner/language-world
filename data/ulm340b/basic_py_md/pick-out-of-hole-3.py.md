

Please make sure that your program works by clicking the `Test` button.
"""

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Your code here
    pass[eod] [code]import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("G4PrintGeometry")

#process.load('Configuration.Geometry.GeometryExtended2021_cff')
#process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')


process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        enable = cms.untracked.bool(False)
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    )
)

process.Timing = cms.Service("Timing")

#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    oncePerEventMode = cms.untracked.bool(True),
#    showMallocInfo = cms.untracked.bool(True),
#    dump = cms.untracked.bool(True),
#    ignoreTotal = cms.untracked.int32(1)
#)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Geometry.MuonNumbering.muonGeometryConstants_cff')

#from Geometry.CSCGeometryBuilder.cscGeometry_cfi import cscGeometry
#from Geometry.DTGeometryBuilder.dtGeometry_cfi import dtGeometry

#process.myprint = cms.EDAnalyzer("SimG4PrintGeometry",
#                                 dumpPosInfo = cms.untracked.bool(True),
#                                 dumpSpecs = cms.untracked.bool(True),
#                                 dumpGeoHistory = cms.untracked.