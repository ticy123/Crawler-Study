from multiprocessing import  Process

def test(name):
    print("hello",name)

if __name__ == '__main__':
    name_list=['a','b','c','d']
    for name in name_list:
        t = Process(target=test,args=(name,))
        t.start()
        t.join()