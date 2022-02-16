from dlisio import lis
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from lisbelo.utils import feetMeter
from lisbelo.mnemonicfix import MnemonicFix


@dataclass
class LisBelo:
    """
    Main class for dealing with .Lis files
    """

    LIS_SOUL: lis.PhysicalFile
    DATAFRAME_LIST: list[DataFrame]
    Logical_Dict_List: list[dict]

    def __init__(self, physical_file: lis.PhysicalFile) -> None:
        """
        This object takes a loaded LIS file , Merge its logical files
        And serialize them in a List of dicts
        """
        self.LIS_SOUL = physical_file

        self.Merged_Logical_Files = []
        self.Logical_Dict_List = []
        self.DATAFRAME_LIST = []

        self.Merge_Files(physical_file)
        self.Logical_Persona()

    def Merge_Files(self, physicalfile: lis.PhysicalFile) -> None:
        """
        Merging all Logical Files inside the Physical file.
        """
        *tail, = physicalfile
        self.Merged_Logical_Files.extend(tail)

    def Logical_Persona(self) -> None:
        """
        Processing each Logical file of the Phsycal FIle
        """
        # - Loop over all Logical files
        for f in self.Merged_Logical_Files:
            # - Creates a dict
            Merged_Logical_Files_DICT = {}
            # - Loops over the Wellsite data
            for x in f.wellsite_data():
                a = x.components()
                Welldict = {c.mnemonic.lstrip().rstrip()
                                              : c.component for c in a}
                Merged_Logical_Files_DICT.update(Welldict)
            # - Format specs for the curves
            formatspecs = f.data_format_specs()
            # - It can have more than one spec
            format_spec = formatspecs[0]
            data_specs = {spec.mnemonic.lstrip().rstrip(
            ): spec.units for spec in format_spec.specs}
            # - Creates a key for the specs
            # - Collect the curves and units
            Merged_Logical_Files_DICT['SPEC'] = data_specs
            # - Retrieving the curve data
            data = lis.curves(f, format_spec, strict=False)
            # - Apending the dataframe
            df = pd.DataFrame(data[::-1])
            df = MnemonicFix.DepthRename(df)
            df = MnemonicFix.GammaRename(df)
            self.DATAFRAME_LIST.append(df)
            # - Stting the KEY data in the dict
            Merged_Logical_Files_DICT['DATA'] = data[::-1]
            self.Logical_Dict_List.append(Merged_Logical_Files_DICT)

    @property
    def DepthCheck(self):
        """
        Returns a Tuple of (max,min)
        """
        return[(df['DEPT'].min(), df['DEPT'].max()) for df in self.DATAFRAME_LIST]

    @property
    def DataLenght(self):
        """
        Return the number of Lis files in the current session
        """
        return len(self.DATAFRAME_LIST)

    def GammaCheck(self) -> list[dict]:
        return [dict_ for dict_ in self.Logical_Dict_List if 'GR' in dict_['SPEC']]

    def GammaDataframe(self):
        return [df for df in self.DATAFRAME_LIST if df['GR'] in df[0]]
