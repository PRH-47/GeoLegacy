from __future__ import annotations
from typing import Annotated
import os
import pathlib
import re
import pandas as pd
import sqlite3
from collections import defaultdict
import json


# - AGP.PY -
# - 18/11/21 -
# - Pedro Cavalcanti
#

class Search_Path:
    def Search_Exten(folder_path, extension):
        """
        Essa função pega um PATH e uma LISTA de extensões
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos da extensão encontrados.
        """
        extension: str
        extensions = extension
        filelist = []
        print(extensions)
        for path in folder_path.glob(r'**/*'):
            if path.suffix in extensions:
                filelist.append(path)

        return filelist

    def Search_Files(folder_path: pathlib.Path, name_):
        """
        Essa função pega um PATH e uma LISTA de nomes
        e retorna uma lista contendo os arquivos que correspondem
        aos arquivos de nome encontrados.
        """
        name_: str.lower()
        name_: str.format()
        name_list = [name_]

        filelist_name = []

        for path in folder_path.glob(r'**/*'):

            if path.is_file():
                # Transformação para Pure Path
                sss = pathlib.PurePath(path)

                # De Pure Path para String
                pathname = str(sss).lower()

                # Check for Multipe arg
                if len(name_list) > 1:
                    for name in name_list:
                        if name in pathname:
                            filelist_name.append(path)

                else:
                    if name_ in pathname:
                        filelist_name.append(path)

        return filelist_name


class Open_Service:

    """
        This class is used to speed the opening and closing of .txt files
        using instance of with, to deal with the process.
        You can choose how you want to 'tag' your files.
        Tuples, Dict or none.
    """

    def _Tuples(list_):
        """
            This function the Tuple style Opening to a list.
            It takes a list, open the .TXT files,
            and returns a tuple, with (filename,lines of the file)
        """
        return Open_Service.List_Iter(list_, Open_Service.Open_style.Open_With_Tuple)

    def List_Iter(list_, func_):
        """
        This function applies a function to a list.
        It retunrns a list with the opend files.
        """
        op_list = []
        for x in list_:
            func_(x)
            op_list.append(func_(x))
        return op_list

    class Open_style:

        def Open(path: pathlib.Path):
            """
            Essa função pega um PATH  de arquivo TXT e retorna
            uma lista de LINHAS que o arquivo contem            
            """
            if path.is_file():
                with open(path, encoding="ISO-8859-1") as f:
                    lines = f.readlines()
                return lines

        def Open_With_Tuple(path: pathlib.Path):
            """
            Essa função pega um PATH  de arquivo TXT 
                e retorna uma TUPLA cujo X[0]= PATHNAME
                e X[1] uma lista de  LINHAS strings que o arquivo contem

            """
            # Transformação para Pure Path
            sss = os.path.split(path)[1]

            # print(sss)
            AGP_Tuple_list = []
            #ssss = str.join(sss)
            # De Pure Path para String
            pathname = str(sss).upper()
            if path.is_file():
                with open(path, encoding="ISO-8859-1") as f:
                    lines = f.readlines()
                AGP_TUPLE = (pathname, lines)

                return AGP_TUPLE

            else:
                print('Is not file')

        def Open_With_Tag(path):
            """ 
            Essa função pega um PATH e uma DICT de nomes de arquivos
            e retorna uma lista de string que o arquivo contem
            """
            # Transformação para Pure Path
            sss = os.path.split(path)[1]

            # print(sss)
            AGP_TAG = {}
            #ssss = str.join(sss)

            # De Pure Path para String
            pathname = str(sss).upper()
            with open(path, encoding="ISO-8859-1") as f:
                lines = f.readlines()
            AGP_TAG.setdefault(pathname, lines)
            return AGP_TAG


class TXT_POOL_SEARCH:

    def List_Search(list_, name_):
        """ 
        Essa função procura um nome em uma LISTA
        """
        name_ = str.upper(name_)
        print(name_)
        for file_ in list_:
            # print(file_)
            for line in file_:

                line = line.upper()
                # print(line)
                if name_ in line:
                    print(file_[0])

    def List_Search_T(list_, name_):
        """
        Essa função procura um nome em uma LISTA
        RETONA =
        """

        name_ = str.upper(name_)
        list_: list(tuple)
        # print(name_)
        result_list = []
        T = []

        for file_ in list_:

            for line in file_[1]:

                line = line.upper()
                # print(line)
                if name_ in line:
                    # print(file_[0])
                    result_list.append(file_)
                    T.append(file_[0])

        print(f"Achamos {len(result_list)} Arquivos AGP com {name_}")
        print(T)
        return result_list


class AGPOOL():
    """ 
        A classe AGPOOL cuida de receber a lista de textos abertos
        e os armazenar em sua POOL de Texto.
    """

    def __init__(self, text_list):

        self.POOL = []
        self.POOL: Annotated[list,
                             'Lista principal de Recebimento de arquivos']

        self.DEFEC_POOL = []
        self.DEFEC_POOL: Annotated[list,
                                   'Lista que contem os arquivos com defeito de Recebimento de arquivos']

        self.Text_Dive(text_list)

    def Text_Dive(self, txl_):
        """ 
        This function takes in a list of files.
        It adds the list to the POOL list.
        If the file is the OLD format, it will be added to DEFEC_POOL
        """
        print('Iniciando Recebimento dos ARQUIVOS')
        for x in txl_:

            if str('========') in str(x[1][0]):
                self.DEFEC_POOL.append(x)
            else:
                self.POOL.append(x)

        print(f'{len(self.POOL)} Pocos  Adicionados ao POOL')
        print(f'{len(self.DEFEC_POOL)} Pocos  Adicionados ao DEFEC_POOL')
        return

    def Print_index(self):
        """
            Displayer para tirar duvidas
        """

        print(f"___ Existem {len(self.POOL)} Arquivos __________________")
        print(f"__________________________________________")

        for x in self.POOL:
            print(f"__________________________________________")
            print((x[0]), " Com ", len(x[1]), " Linhas ")

    def Quick_litho(self):
        pass


class AGP_OLD:
    """
        This function takes care of the processing of
        old AGP files.
    """

    def __init__(self, list_):
        """
        Initial Sequence with Get_Structure_List
        """

        self.LIST_RECEIVE = []
        self.result_list = []

        print(f'{len(list_)} Arquivos Recebidos')

        self.Get_Structure_List(list_)

    def Check_(self):

        print(f'{len(self.result_list)} Arquivos Fatiados')
        print(f'{len(self.slices)} Fatias criadas')
        print(f'Primeira Fatia do primeiro Arquivo')

        print(f'{self.result_list[0][0]}')
        print(f"__________________________________________")
        print(f'{self.result_list[1][0]}')

    def list_describe(self):
        for _list in self.result_list:
            for poco in _list:
                print(f"__________________________________________")
                print(f'{poco}')

        #print(f'{self.result_list[0:3]} Primeiro Arquivo')

    def Get_Structure_List(self, list_):
        """
        This function gets the structure of the file.

        """

        for file in list_:
            """
            Printing the items of the list and applying the sequence al·go·rithm
            """
            # print("####################################################################")
            # print("# Cabeçalho recebido __________________________________________")
            # print(it[1][0])

            # Executa a função Sequence na lista Recebida
            temp = self.Sequence_AGP(file[1])

            # print("# Cabeçalho Lido __________________________________________")
            # print(temp)
            # print("####################################################################")
            self.result_list.append(temp)

        # Finaliza a sessão.
        print(f'{len(list_)} Arquivos Processados')
        # return self.result_list

    def Sequence_AGP(self, list_):

        # Enumera a lista Recebida
        list_ = list(enumerate(list_))

        # Cria uma lista vazia para receber as slices
        slices = []

        # Estabelece o índice 0
        indexx = [0]

        # Cria uma lista para receber pares de  sessões
        spampairs = []

        # Cria uma variável para receber a
        leng = len(list_)-1

        def linesearch(list_):
            """
            This function looks for lines that starts with -------
            """
            for x in list_:
                if x[1].startswith("-----------"):
                    indexx.append(x[0])

        def indexspam(indexx):

            pairs = list(zip(indexx[::1], indexx[1::]))
            spampairs.extend(pairs)
            return pairs

        def textslice(list_, pairs):

            for x in pairs:
                a = list_[x[0]:x[1]]
                slices.append(a)

        linesearch(list_)
        indexx.insert(len(indexx), leng)
        indexspam(indexx)
        textslice(list_, spampairs)

        return slices


class Striped_Slice:
    def __init__(self, list_) -> None:

        self.Striped_Slices = []

        self.Get_Split_List(list_)
        print(len(self.Striped_Slices))
        # print(self.Striped_Slices[0])

    def Text_Strip_S(self, list_,):
        """
        Essa função Split as fatias do textos e retorna
        as mesmas
        """
        result_list = []

        for section in list_:
            sections = []
            for it2 in section:
                line = re.split(r'\s{5,}|:', it2[1])
                while "" in line:
                    line.remove("")
                sections.append(line)
            result_list.append(sections)
        self.Striped_Slices.append(result_list)

    def Get_Split_List(self, list_):
        """
        Essa função executa o Tesxt_split_S em uma lista
        as mesmas
        """

        return [self.Text_Strip_S(it) for it in list_ ]


class Unid_vertical:
    def __init__(self, list_) -> None:

        # Listas para checar as unidades verticas e receber
        # As sessões que possuem "UNID"

        self.UNIDADES_VERTICAIS = []

        # - Lista para receber ERROR
        self.NONVERTICAL = []
        self.NONVERTICAL_INDEX = []
        self.ERROR_PARSED_VERT = []

        # Lista para Receber o Resultado
        # dos blocos verticais

        self.Vertical_SPLITED = []

        # Funções para executar:
        self.setup(list_)
        self.Vertical_block(self.UNIDADES_VERTICAIS)

    def setup(self, list_):
        self.check_unid_vert(list_)

    def check_unid_vert(self, list_):
        """
        This function checks for the section UNIDADES VERTICAIS

        """

        for file_ in list_:
            # print(file_[3][1][1])
            try:

                if "UNID" in file_[3][1][1]:
                    # print(file_[0][0],"#3")
                    self.UNIDADES_VERTICAIS.append(
                        (file_[0][0][1], file_[4][2:]))

                elif "UNID" in file_[5][1][1]:
                    # print(file_[0][0],"#5")
                    self.UNIDADES_VERTICAIS.append(
                        (file_[0][0][1], file_[6][2:]))
                elif "UNID" in file_[7][1][1]:
                    # sprint(file_[0][0],"#7")
                    self.UNIDADES_VERTICAIS.append(
                        (file_[0][0][1], file_[8][2:]))

                else:
                    self.NONVERTICAL.append((file_[0]))
                    print('UNIDADE VERTICAL NÃO ENCONTRADA')
                    print(file_[0])
            except IndexError:
                print('UNIDADE VERTICAL NÃO ENCONTRADA INDEX ERROR')
                print(file_[0])
                self.NONVERTICAL_INDEX.append(file_)

    def Vertical_block(self, list_):
        """
        Essa Funcao pega os blocos processados que possuem UNID VERITCALIZADAS
        E extrai informação das linhas.

        """
        SPLITED_VERTICAL = []
        ERROR_LIST = []
        for sect in list_:

            # print("_____________________________________________________________________")
            # print(sect[0])
            POCO_VERTICAL = []

            for lin in sect[1]:
                # - Finding the groups Strings ex: G BALSAS
                unid_split = re.findall(
                    r'(\s{1,5}\w{1,}\s{1,7}[.A-Z.\-]{3,8}\s{1,3})', lin[1])

                # SPlIT TOPO(COTA) / BASE (COTA)
                tp_bs = re.findall(r'([0-9\.\-\/]{2,})', lin[1])

                if len(tp_bs) == 4:

                    try:
                        sorted_uv = (
                            ((unid_split[0]), [tp_bs[1], tp_bs[2], "null", "null"]))
                        POCO_VERTICAL.append(sorted_uv)

                    except IndexError:

                        print("INDEX ERRO VERTICAL BLOCK")
                        # ERROR_LIST.append((unid_split,tp_bs))

                if len(tp_bs) == 6:
                    # print(sect[0])
                    # print(lin[0],lin[1])
                    try:
                        sorted_uv = (
                            ((unid_split[0]), [tp_bs[1], tp_bs[2], tp_bs[3], tp_bs[4]]))

                        POCO_VERTICAL.append(sorted_uv)
                    except IndexError:
                        print("INDEX ERRO VERTICAL BLOCK /6")
                        # ERROR_LIST.append(list_)

                if len(unid_split) == 0:
                    ERROR_LIST.append(sect[0])

                liii = (sect[0], POCO_VERTICAL)
            SPLITED_VERTICAL.append(liii)
        self.Vertical_SPLITED.append(SPLITED_VERTICAL)
        self.ERROR_PARSED_VERT.append(ERROR_LIST)


class AGP_HEAD:
    """"
        Classe responsavel pelo tratamento e classifacao 
        do HEAD.
        HEADPOOL = lista de Dict
        UNIQUEDICT = Lista de todos os possiveis resultados

    """

    def __init__(self, list_):

        # Listas de Recebimento
        ###$$###

        self.HEADPOOL = []

        self.UNIQUEDICT = {}

        # - Sequencia Principal
        self.Get_HEAD_List(list_)

    def UniqueResults(self,):

        KEY_V_RESULT = []
        for dict_ in self.HEADPOOL:
            for k, v in dict_.items():
                # - Chamando todos os valores
                result = dict_[k]
                # - Criando uma Tupla com a chave do dict e os resultados
                Tuple_result = (k, result)
                KEY_V_RESULT.append(Tuple_result)

        # - Criando um dicionaro default
        d = defaultdict(list)
        for k, v in KEY_V_RESULT:
            d[k].append(v)

        self.UNIQUE_RESULT_LIST = list(d.items())
        # - Criando um dict unico para session
        SESSION_UNIQUEDICT = {}
        for x, y in d.items():

            SESSION_UNIQUEDICT[x] = set(y)

        # - Tornando o dict da session em dict default
        self.UNIQUEDICT.update(SESSION_UNIQUEDICT)
        # print(self.UNIQUEDICT)

    def Get_Head(self, list_):
        # print(list)
        nlist = [x for x in list_[0] if x != []]
        pair_list = []
        cabecalho = {}
        for p in nlist:

            # print(p,len(p))
            if len(p) == 2:

                pair = (p[0].lstrip().rstrip(), p[1].lstrip().rstrip())
                pair_list.append(pair)

            if len(p) == 4:
                pairone = (p[0].lstrip().rstrip(), p[1].lstrip().rstrip())
                pairtwo = (p[2].lstrip().rstrip(), p[3].lstrip().rstrip())
                pair_list.append(pairone)
                pair_list.append(pairtwo)
        for k, v in pair_list:

            head = {}
            head[k] = v
            cabecalho.update(head)
        self.HEADPOOL.append(cabecalho)

        return cabecalho

    def Get_HEAD_List(self, list_):
        result_list = []

        for it in list_:

            temp = self.Get_Head(it)
            # print(temp)
            result_list.append(temp)
        return result_list


class LATLONG:
    """'
        Pega a lista gerada pelo HEAD list e transforma em uma lista
        COntendo LAT E LONG
    """

    def __init__(self, list_) -> None:

        self.LATLIST = []
        self.LONGLIST = []
        self.XY_NORM = []

        self.PureName = []

        self.LatLong(list_)
        # print(self.XY_NORM)

    def describe(self):
        print(len(self.LATLIST))
        print(len(self.LATLIST))

        for item_ in self.LATLIST, self.LONGLIST:
            pass

    def LatLong(self, list_):

        NEW_LAT_LIST = []
        NEW_LONG_LIST = []

        XY_NORM = []
        XY_DMS = []

        for x in list_:

            poco = x['POCO']
            self.PureName.append(poco)
            lat = x['LATITUDE']
            long_ = x['LONGITUDE']

            LATLONGLIST = []

            lat_split = re.findall(r'[^()]+', lat)
            long_split = re.findall(r'[^()]+', long_)

            new_lat = (poco, (lat_split[0], lat_split[1]))
            new_long = (poco, long_split[0], long_split[1])

            self.LATLIST.append(new_lat)
            self.LONGLIST.append(new_long)

            xy_One = (poco, lat_split[0], long_split[0])
            self.XY_NORM.append(xy_One)
            xy_Parenteses = (lat_split[1], long_split[1])


class Unid_dict:

    def __init__(self, list_) -> None:

        self.POCO_SESSION_DICT = []
        self.makedict(list_)

    def makedict(self, list_:list[str]):

        for poco in list_:

            pPOCO = re.split(" : ", poco[0])

            POCO = pPOCO[1].lstrip()
            POCO = POCO.rstrip()

            POCO_COMPLETE = {}
            POCO_VERTICAL_FORM = {}

            for form_topo_base in poco[1]:

                FORM = form_topo_base[0].lstrip()
                TOPO = form_topo_base[1][0].lstrip()
                TOPO_COTA = form_topo_base[1][1].lstrip()
                BASE = form_topo_base[1][2].lstrip()
                BASE_COTA = form_topo_base[1][3].lstrip()

                FORM_DICT = {}
                mini_form = {}

                mini_form['TOPO'] = TOPO
                mini_form['TOPO COTA'] = TOPO_COTA
                mini_form['BASE'] = BASE
                mini_form['BASE COTA'] = BASE_COTA

                FORM_DICT[FORM] = mini_form

                POCO_VERTICAL_FORM.update(FORM_DICT)

                # print(FORM_DICT)
            POCO_COMPLETE[POCO] = POCO_VERTICAL_FORM
            self.POCO_SESSION_DICT.append(POCO_COMPLETE)


class dataframes_vert_uni:

    def __init__(self, list_) -> None:
        self.DF_COLLECTION_VERTICAL_UNIT = []
        self.makeDataframe(list_)

    def DF_check(self):
        print(len(self.DF_COLLECTION_VERTICAL_UNIT))

    def makeDataframe(self, list_):
        for dict_ in list_:

            poco_df = pd.concat(
                {k: pd.DataFrame(v).T for k, v in dict_.items()}, axis=0)
            #tag = (dict_[0])
            self.DF_COLLECTION_VERTICAL_UNIT.append(poco_df)
            # print(poco_df.head(10))

    def DF_to_EX(self, path_):

        for df in self.DF_COLLECTION_VERTICAL_UNIT:
            tag = df.index[0][0]
            ptag = path_+f'/{tag}.xlsx'

            df.to_excel(ptag, index=True, header=True)
