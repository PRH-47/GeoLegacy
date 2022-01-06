
import pathlib


class Searcher:
    """
    Main class for Searching geo files.
    """

    @staticmethod
    def SearchLis(folder_path: pathlib.Path):
        '''
        Essa função pega um PATH e uma LISTA de extensões
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos da extensão encontrados.
        '''
        EXTENSIONS = {'.lis'}

        return [path for path in folder_path.glob(r'**/*') if path.suffix in EXTENSIONS]

    @staticmethod
    def SearchDlis(folder_path: pathlib.Path):
        '''
        Essa função pega um PATH e uma LISTA de extensões
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos da extensão encontrados.
        '''
        EXTENSIONS = {'.dlis'}

        return [path for path in folder_path.glob(r'**/*') if path.suffix in EXTENSIONS]

    @staticmethod
    def SearchLas(folder_path: pathlib.Path):
        '''
        Essa função pega um PATH e uma LISTA de extensões
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos da extensão encontrados.
        '''
        EXTENSIONS = {'.las'}

        return [path for path in folder_path.glob(r'**/*') if path.suffix in EXTENSIONS]

    @staticmethod
    def SearchCombo(folder_path: pathlib.Path):
        '''
        Essa função pega um PATH e uma LISTA de extensões
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos da extensão encontrados.
        '''
        EXTENSIONS = {'.dlis', '.lis', '.las'}

        return [path for path in folder_path.glob(r'**/*') if path.suffix in EXTENSIONS]


    @staticmethod
    def Search_Txt(folder_path:str, name_:str):
        """
        Essa função pega um PATH e uma LISTA de nomes
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos de nome encontrados.
        """
        folder_paths = pathlib.Path(folder_path)
        filelist_name = []
        name_ = name_.upper()
        EXTENSIONS = {'.txt'}
        for path in folder_paths.glob(r'**/*'):
            # De Pure Path para String
            pathname = str(pathlib.PurePath(path)).upper()
            if name_ in pathname and  path.is_file() and path.suffix in EXTENSIONS:
                filelist_name.append(path)

        return filelist_name
