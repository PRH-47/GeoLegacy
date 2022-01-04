from dlisio import lis
from .lisbelo import LisBelo
import pathlib


class Lis_Plaza:
    '''
    Lis_Plaza is the main list to hold the physical files.
    '''
    logicalfileslist:list[LisBelo]

    def __init__(self, pathlist: list[pathlib.Path]) -> None:
        '''
        This object needs an list of paths, so it can take care of the IO of .lis files
        '''
        self.pathlist = pathlist
        self.logicalfileslist=[]
        self.OpenList()

    def OpenList(self) -> None:

        for path in self.pathlist:
            # - Loading individual files
            pn = pathlib.PurePath(path)
            # - Creating a Physical FIle
            l_ = lis.load(f'{pn}')
            # - Lisbelo OBJ
            lb = LisBelo(l_)
            # - Appending to the
            self.logicalfileslist.append(lb)
            # - Closing the file.
            l_.close()

    @property
    def FileLenght(self) -> int:
        return len(self.logicalfileslist)
