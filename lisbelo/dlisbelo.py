from dataclasses import dataclass
from dlisio import dlis
import pandas as pd


@dataclass
class DlisBelo:

    MergedLogicalFiles: list[dlis.LogicalFile]

    def __init__(self, dlisfile: dlis.PhysicalFile) -> None:

        self.MergedLogicalFiles = []
        self.MergedFrames = []
        self.DATAFRAMELIST = []

        self.MergeFiles(dlisfile)
        self.GetFrames()
        self.MakeDataDict()

    def MergeFiles(self, dlisfile: dlis.PhysicalFile) -> None:

        *files, = dlisfile
        self.MergedLogicalFiles.extend(files)

    def GetFrames(self, ):
        for file in self.MergedLogicalFiles:
            self.MergedFrames.extend(file.find('FRAME'))

    def MakeDataDict(self):
        DataDict = {}
        for frames in self.MergedFrames:
            self.DataDict(frames)

    def DataDict(self, frame):

        DataDict = {}
        DataDict['NAME'] = frame.name
        DataDict['CURVES'] = [ch.name for ch in frame.channels]
        DataDict['UNIT'] = [ch.units for ch in frame.channels]
        df = pd.DataFrame(frame.curves())
        DataDict['DATAFRAME'] = df
        self.DATAFRAMELIST.append(DataDict)
