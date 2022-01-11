import pathlib
import os


class OpenServices:

    @staticmethod
    def Open_With_Tuple(path: pathlib.Path) -> tuple[str,list[str]]:
        """
        Essa função pega um PATH  de arquivo TXT 
        e retorna uma TUPLA cujo X[0]= PATHNAME
        e X[1] uma lista de  LINHAS strings que o arquivo contem
        """
        # Transformação para Pure Path
        pathname = str(os.path.split(path)[1]).upper()
        if path.is_file():
            with open(path, encoding="ISO-8859-1") as f:
                lines = f.readlines()
                openTuples = (pathname, lines)

            return openTuples

        else:
            print('Is not file')

    @staticmethod
    def List_Iter(list_: list, func_) -> list:

        return [func_(path) for path in list_]

    @staticmethod
    def OpenList_Tuples(list_: list) -> list:
        return OpenServices.List_Iter(list_, OpenServices.Open_With_Tuple)
