
import pathlib


class Searcher:

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
        EXTENSIONS = {'.dlis','.lis','.las'}

        return [path for path in folder_path.glob(r'**/*') if path.suffix in EXTENSIONS]
