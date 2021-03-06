from dataclasses import dataclass
import pathlib

from dlisio import dlis
from pandas import DataFrame

from .dlisbelo import DlisBelo


@dataclass
class DlisPlaza:
    """
    This is the main class for dealing with multiple .Lis files
    It aims to improve the workflow, and integration
    with other frameworks such as Django or Flask.
    """

    DlisFileList: list[DlisBelo]

    def __init__(self, pathlist: list[pathlib.Path]) -> None:
        self.DlisFileList = []
        self.ErrorFileList = []
        self.OpenList(pathlist)

    def OpenList(self, pathlist: list[pathlib.Path]) -> None:
        """
        Open dlis files and stores them on a list.
        If any errors, the files will be appended in the Errorfilelist.
        """
        try:
            for path in pathlist:
                dl = dlis.load(f'{path}')
                dlbelo = DlisBelo(dl)
                self.DlisFileList.append(dlbelo)
                dl.close()
        except Exception as e:
            print(e)
            self.ErrorFileList.append(path)

    def GammaScan(self) -> list[DataFrame]:
        """ 
        Searches for dataframes that contains GR columns on it,
        and returns a list of dataframes.
        """
        GammaData = []
        for file in self.DlisFileList:
            for dataframe in file.DataDictList:
                if 'GR' in dataframe['DATAFRAME'].columns.values:
                    GammaData.append(dataframe)

        return GammaData
