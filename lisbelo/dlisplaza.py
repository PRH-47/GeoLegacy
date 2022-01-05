from logging import exception
from .dlisbelo import DlisBelo
from dlisio import dlis
import pathlib


class LisPlaza:

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
