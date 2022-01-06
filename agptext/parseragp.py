import re
from collections import defaultdict
from parser.textparser import RemoveWhiteSpace, SplitSpaceColon, ColonSplit

class AGP_OLD:

    def __init__(self, list_):

        self.LIST_RECEIVE = []
        self.result_list = []

        print(f'{len(list_)} files received')

        self.Get_Structure_List(list_)


    def Get_Structure_List(self, list_):
        """
        This function gets the structure of the file.
        """

        for file in list_:
            self.result_list.append(self.Sequence_AGP(file[1]))


    def Sequence_AGP(self, list_):

        # Enumera a lista Recebida
        list_ = list(enumerate(list_))
        # Cria uma lista vazia para receber as slices
        slices = []
        # Estabelece o índice 0
        index_ = [0]
        # Cria uma lista para receber pares de  sessões
        spampairs = []
        # Cria uma variável para receber a
        leng = len(list_)-1

        def linesearch(file):

            # Procura por linhas conten
            for line in file:
                # linha começa com --------
                line:str
                if line[1].startswith("-----------"):
                    index_.append(line[0])

        def indexspam(index_):

            pairs = list(zip(index_[::1], index_[1::]))
            spampairs.extend(pairs)
            return pairs

        def textslice(list_, pairs):

            for x in pairs:
                a = list_[x[0]:x[1]]
                slices.append(a)

        linesearch(list_)
        index_.insert(len(index_), leng)
        indexspam(index_)
        textslice(list_, spampairs)

        return slices


class SplitSlices:

    def __init__(self, list_) -> None:

        self.Striped_Slices = []
        self.Get_Split_List(list_)

    def TextStrip(self, list_,):
        """
        Essa função Split as fatias do textos e retorna
        as mesmas
        """
        result_list = []

        for section in list_:
            sections = []
            for it2 in section:
                line = SplitSpaceColon(it2[1])
                RemoveWhiteSpace(line)
                sections.append(line)
            result_list.append(sections)
        self.Striped_Slices.append(result_list)

    def Get_Split_List(self, list_):
        """
        Essa função executa o Tesxt_split_S em uma lista
        """
        return [self.TextStrip(line) for line in list_]


class UnidadesVerticais:
    def __init__(self, list_) -> None:

        # Listas para checar as unidades verticas e receber
        # As sessões que possuem "UNID"
        self.CheckList = []

        # - Lista para receber ERROR
        self.NONVERTICAL = []
        self.NONVERTICAL_INDEX = []
        self.ERROR_PARSED_VERT = []

        # Lista para Receber o Resultado
        # dos blocos verticais
        self.UNIDADES_VERTICAIS = []

        # Funções para executar:
        self.check_unid_vert(list_)
        self.Vertical_block(self.CheckList)

    def check_unid_vert(self, list_):
        """
        This function checks for the section UNIDADES VERTICAIS
        """

        for file_ in list_:
            # print(file_[3][1][1])
            try:

                if "UNID" in file_[3][1][1]:

                    self.CheckList.append(
                        (file_[0][0][1], file_[4][2:]))

                elif "UNID" in file_[5][1][1]:

                    self.CheckList.append(
                        (file_[0][0][1], file_[6][2:]))
                elif "UNID" in file_[7][1][1]:

                    self.CheckList.append(
                        (file_[0][0][1], file_[8][2:]))

                else:
                    self.NONVERTICAL.append((file_[0]))
                    print('UNIDADE VERTICAL NÃO ENCONTRADA')
                    print(file_[0][0])

            except IndexError:
                print('UNIDADE VERTICAL NÃO ENCONTRADA INDEX ERROR')
                print(file_[0])
                self.NONVERTICAL_INDEX.append(file_)

    def Vertical_block(self, list_):
        """
        Essa Funcao pega os blocos processados que possuem UNID VERITCALIZADAS
        E extrai informação das linhas.
        """
        resultSplited = []
        ERROR_LIST = []
        for sect in list_:

            pocoVertical = []

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
                        pocoVertical.append(sorted_uv)

                    except IndexError:

                        print("INDEX ERRO VERTICAL BLOCK")
                        ERROR_LIST.append((unid_split,tp_bs))

                if len(tp_bs) == 6:

                    try:
                        sorted_uv = (
                            ((unid_split[0]), [tp_bs[1], tp_bs[2], tp_bs[3], tp_bs[4]]))
                        pocoVertical.append(sorted_uv)

                    except IndexError:
                        print("INDEX ERRO VERTICAL BLOCK /6")
                        ERROR_LIST.append(list_)

                if len(unid_split) == 0:
                    ERROR_LIST.append(sect[0])

                tuple_result = (sect[0], pocoVertical)
            resultSplited.append(tuple_result)
        self.UNIDADES_VERTICAIS.append(resultSplited)
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

    def Get_Head(self, list_:list[str]):

        nlist = [line for line in list_[0] if line != []]
        
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
        return [self.Get_Head(item) for item in list_]


class UnidadesVerticaisDict:

    def __init__(self, list_) -> None:

        self.POCO_SESSION_DICT = []
        self.makedict(list_)

    def makedict(self, list_:list[str]):

        for poco in list_:

            splitedpoco = ColonSplit(poco[0])

            POCO = splitedpoco[1].lstrip()
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

            POCO_COMPLETE[POCO] = POCO_VERTICAL_FORM
            self.POCO_SESSION_DICT.append(POCO_COMPLETE)