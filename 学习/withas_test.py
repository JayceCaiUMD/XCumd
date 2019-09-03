class WithTest:
    def __init__(self, name):
        self.name = name
        pass

    def __enter__(self):
        print('__enter__ executed')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ executed')

    def pocess(self):
        print('pocessing')

with WithTest("cxy") as nametest:     #with-open steps:
    print(nametest.name)                #1.run __enter__
    nametest.pocess()                   #2.return the result of __enter__to 'nametest'
print('end')                            #3.run the code below with-as
                                        #4.run __exit__
