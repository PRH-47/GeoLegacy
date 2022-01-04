
import pathlib
from agp import *


class wellload:
    def __init__(self,path):
        

        #Abrindo os arquivos da pasta (folder_one)
        self.AGP_OPT = Open_Service._Tuples(Search_Path.Search_Files(path,("agp")))

        # A classe AGPOOL cuida de receber os textos abertos e os armazenar em sua POOL de Texto
        self.new_pool = AGPOOL(self.AGP_OPT)

        # A variavel txt_Pool recebe os valores da lista POOL de txt_Received
        self.txt_Pool = self.new_pool.POOL

        # Aplica a sequencia de identificação e Estruturação em arquivos AGP_OLD
        self.txt_list_AGP_OLD = AGP_OLD(self.txt_Pool)
        
        self.Striped_lists = Striped_Slice(self.txt_list_AGP_OLD.result_list)

        self.Head_list = AGP_HEAD(self.Striped_lists.Striped_Slices)
        self.latlonglist = LATLONG(self.Head_list.HEADPOOL)
        
        self.vert_uni = Unid_vertical(self.txt_list_AGP_OLD.result_list)

        self.unid = Unid_dict(self.vert_uni.Vertical_SPLITED[0]) 
        self.Head_list.UniqueResults()
        
        # - MERGED UNID ++ HEAD
        self.MERGED_HEAD_UNI = []
        self.Merge_dict()
     
    def Merge_dict(self,):
        """ 
        Merged head with vertical unity list!!!
        Some print functions to check if everything is working is
        just below
        """
        #head_iter= self.Head_list.HEADPOOL.__iter__()
        #unid_iter = self.unid.POCO_SESSION_DICT.__iter__()
        #print(list(a)[0],list(b)[0])

        zip_iter = list(zip(self.Head_list.HEADPOOL.__iter__(),self.unid.POCO_SESSION_DICT.__iter__()))
        
        for zz in zip_iter:
            didi = {}
            if list(zip_iter[0][0].values())[0] == list(zip_iter[0][1].keys())[0]:
                didi.update(zz[0])
                didi.update(zz[1])
                
                self.MERGED_HEAD_UNI.append(didi)

        