from dataclasses import dataclass
from dlisio import dlis
import pandas as pd

from .mnemonicfix import MnemonicFix


@dataclass
class DlisBelo:

    MergedLogicalFiles: list[dlis.LogicalFile]

    def __init__(self, dlisfile: dlis.PhysicalFile) -> None:
        self.MergedLogicalFiles = []
        self.MergedFrames = []
        self.DataDictList = []

        self.MergeFiles(dlisfile)
        self.GetFrames()
        self.GetOrigins()
        self.MakeDataDict()

    def MergeFiles(self, dlisfile: dlis.PhysicalFile) -> None:
        """
        Merges all the logical files inside a physucal file.
        """
        *files, = dlisfile
        self.MergedLogicalFiles.extend(files)

    def GetFrames(self, ):
        """
        Merges
        """
        self.origins = []
        for file in self.MergedLogicalFiles:
            for origin in file.origins:
                self.origins.extend(origin.file_id)
            self.MergedFrames.extend(file.find('FRAME'))

    def GetOrigins(self):
        self.origins = []
        for file in self.MergedLogicalFiles:
            for origin in file.origins:
                self.origins.append(origin.file_id)

    def MakeDataDict(self):
        for frames in self.MergedFrames:
            self.DataDict(frames)

    def DataDict(self, frame: dlis.Frame):

        DataDict = {}
        DataDict['WELL'] = self.origins[0]
        DataDict['FRAME'] = frame.name
        DataDict['CURVES'] = [ch.name for ch in frame.channels]
        DataDict['UNIT'] = [ch.units for ch in frame.channels]

        df = pd.DataFrame(frame.curves(strict=False))
        df = MnemonicFix.IndexToDept(df)
        df = MnemonicFix.GammaRename(df)

        df['WELL'] = self.origins[0]
        DataDict['DATAFRAME'] = df
        self.DataDictList.append(DataDict)
