#secret.py
import hashlib

def dataProcess(data):#bububu输入字典，输出密码值
    key0 = list(data.keys())[0]
    value = data[key0] + key0
    valueProcess = hashlib.md5()
    valueProcess.update(value.encode("utf8"))
    data = valueProcess.hexdigest()
    return data

def verification(storeDic,verifDic):#输入储存的字典，应验证的字典
    verifDic[username] = dataProcess(verifDic)
    if storeDic[username] == verifDic[username]:
        return True
    else:
        return False

if __name__ == '__main__':
    store = {}
    username = input('Set your username:')
    store[username] = input('Set your password:')
    store[username] = dataProcess(store)
    beVerification = {}
    username = input('Enter your username:')
    beVerification[username] = input('Enter your password:')
    if verification(store,beVerification):
        print('Get it.')
    else:
        print('Your username or password is incorrect.')
