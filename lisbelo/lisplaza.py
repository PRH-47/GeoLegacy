import pathlib

from dlisio import lis
from pandas import DataFrame

from .lisbelo import LisBelo


class Lis_Plaza:
    '''
    Lis_Plaza is the main list to hold the physical files.
    And dealing with multiple files.
    '''
    LisFileList: list[LisBelo]

    def __init__(self, pathlist: list[pathlib.Path]) -> None:
        '''
        This object needs an list of paths, so it can take care of the IO of .lis files
        '''
        self.pathlist = pathlist
        self.LisFileList = []
        self.ErrorFileList = []
        self.OpenList()

    def OpenList(self) -> None:

        for path in self.pathlist:
            try:
                # - Loading individual files
                pn = pathlib.PurePath(path)
                # - Creating a Physical FIle
                l_ = lis.load(f'{pn}')
                # - Lisbelo OBJ
                lb = LisBelo(l_)
                # - Appending to the
                self.LisFileList.append(lb)
                # - Closing the file.
                l_.close()

            except Exception as e:
                print(e)
                error_tuple = (e,path)
                self.ErrorFileList.append(error_tuple)

    @property
    def FileLenght(self) -> int:
        return len(self.LisFileList)

    def GammaScan(self) -> list[DataFrame]:
        """ 
        Searches for dataframes that contains GR columns on it,
        and returns a list of dataframes.
        """
        GammaData = []
        for file in self.LisFileList:
            for dataframe in file.DATAFRAME_LIST:
                if 'GR' in dataframe.columns.values:
                    GammaData.append(dataframe)

        return GammaData

    def printcheck(self):
        """
        Prints file by file in LisFile list
        """
        check = f"There are {len(self.LisFileList)} files in the LisFileList"
        print(check)
        for file in self.LisFileList:
            print(file)

    def printcheck_error(self):
        """
        Prints file by file in LisFile list
        """
        check = f"There are {len(self.ErrorFileList)} files in the ErrorFileList"
        print(check)
        for file in self.ErrorFileList:
            print(file)
