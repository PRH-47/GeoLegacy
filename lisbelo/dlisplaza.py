from dataclasses import dataclass
import pathlib

from dlisio import dlis

from .dlisbelo import DlisBelo


@dataclass
class LisPlaza:
    """
    This is the main class for dealing with multiple .Lis files
    It aims to improve the workflow, and integration
    with other frameworks such as Django or Flask.
    """

    DlisFileList: list[DlisBelo]

    def __init__(self, pathlist: list[pathlib.Path]) -> None:
        self.DlisFileList = []
        self.OpenList(pathlist)

    def OpenList(self, pathlib: list[pathlib.Path]) -> None:
        try:
            for path in pathlib:
                dl = dlis.load(f'{path}')
                dlbelo = DlisBelo(dl)
                self.DlisFileList.append(dlbelo)
                dl.close()
        except Exception as e:
            print(e)

    def GammaScan(self):
        GammaData = []
        for file in self.DlisFileList:
            for dataframe in file.DATAFRAMELIST:
                if 'GR' in dataframe['DATAFRAME'].columns.values:
                    GammaData.append(dataframe)

        return GammaData
