from pandas import DataFrame


class MnemonicFix:
    """
    Main class for fixing mnemonics.
    Searches for column values and replaces them.
    """

    @staticmethod
    def DepthRename(df:DataFrame) -> DataFrame:
        """
        Depth rename utility.
        Searches for columns values with whitespaces and renames them.
        """
        if 'DEPT(0)' in df.columns.values:
            df.rename(columns={'DEPT(0)': 'DEPT'}, inplace=True)

        if 'DEPT ' in df.columns.values:
            df.rename(columns={'DEPT ': 'DEPT'}, inplace=True)

        return df

    @staticmethod
    def GammaRename(df: DataFrame) -> DataFrame:
        """
        GR rename utility.
        Searches for columns values with whitespaces and renames them.
        """

        if 'GR  ' in df.columns.values:
            df.rename(columns={'GR  ': 'GR'}, inplace=True)

        if 'GR ' in df.columns.values:
            df.rename(columns={'GR ': 'GR'}, inplace=True)

        if ' GR ' in df.columns.values:
            df.rename(columns={' GR ': 'GR'}, inplace=True)

        if 'RGR  ' in df.columns.values:
            df.rename(columns={'RGR  ': 'RGR'}, inplace=True)

        if 'RGR ' in df.columns.values:
            df.rename(columns={'RGR ': 'RGR'}, inplace=True)

        if ' RGR ' in df.columns.values:
            df.rename(columns={' RGR ': 'RGR'}, inplace=True)

        return df

    @staticmethod
    def IndexToDept(df) -> DataFrame:
        """
        This function is specially usefull for Dlis files
        that have index in place of depth.
        """
        for col in df.columns.values:
            if 'INDEX' in col:
                target = col
                df.rename(columns={target: 'DEPT'}, inplace=True)

        return df
