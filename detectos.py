import platform
import getpass

def detect():
    user = getpass.getuser()
    my_os = platform.system()
    if my_os == 'Linux':
        path = '/home/'+user+'/Documentos/mypass'
    else:
        path = 'C:/Users/'+user+'/Documents/mypass'
    return path