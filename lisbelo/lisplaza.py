from dlisio import lis
from .lisbelo import LisBelo
import pathlib


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
                self.ErrorFileList.append(path)

    @property
    def FileLenght(self) -> int:
        return len(self.FileList)
