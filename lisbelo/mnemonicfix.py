from pandas import DataFrame


class MnemonicFix:

    @staticmethod
    def depthrename(df) -> DataFrame:
        if 'DEPT(0)' in df.columns.values:
            df.rename(columns={'DEPT(0)': 'DEPT'}, inplace=True)

        if 'DEPT ' in df.columns.values:
            df.rename(columns={'DEPT ': 'DEPT'}, inplace=True)

        return df

    @staticmethod
    def gammarename(df: DataFrame) -> DataFrame:

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
        
        for col in df.columns.values:
            if 'INDEX' in col :
                target = col
                df.rename(columns={target: 'DEPT'}, inplace=True)

        return df