with open('test.dat','wb') as f:
    f.write(b'012345')
    
with open('test.dat','rb') as f:
    data = f.read(6)
    print(data)
    
f = open('test.dat','rb')
f.tell()

f.read(2)

f.tell()

f.seek(2)

f.tell()

f.read(2)

f.close()

import pickle
sample_num = 100
with open('sample.pkl','rb') as f:
    pickle.dump(sample_num,f)

import pickle
with open('sample.pkl','rb') as f:
    load_num = pickle.load(f)
    print(load_num)
    
