class TxtPool:
    def __init__(self, text_list):

        self.Pool = []
        self.NotOpenedPool = []

        self.Text_Dive(text_list)

    def Text_Dive(self, txl_):

        print('Initiating the file list')
        for file in txl_:

            if '========'  in str(file[1][0]):
                self.NotOpenedPool.append(file)
            else:
                self.Pool.append(file)

        print(f'{len(self.Pool)} Files added to the Pool')
        print(f'{len(self.NotOpenedPool)} Files added to the NotOpenedPool')