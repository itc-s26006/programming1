import pickle
with open('test.pkl','rb') as f:
    result=pickle.load(f)
    print(result)
