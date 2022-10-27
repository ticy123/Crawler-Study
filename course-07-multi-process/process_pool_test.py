from multiprocessing import Pool

def test(p):
    return p

if __name__ == '__main__':
    res=[]
    with Pool(5) as p:
        res.append(p.map(test,['a','b','c']))
    for re in res:
        print(re)

