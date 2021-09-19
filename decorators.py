#pairnei mia function ws orisma kanei lock ton server antalasei munimata me ton client
#kai epistrefei thn function
def decorator_read(func):

  def inner(*args):
    args[0].lock.acquire()
    args[2].sendall('Type the code: '.encode('utf-8'))
    lista  = list(args)
    lista[1] = args[2].recv(1204).decode('utf-8')
    t = tuple(lista)
    
    return func(*t)
  return inner   

#pairnei mia function ws orisma kanei lock ton server antalasei munimata me ton client
#kai epistrefei thn function
def decorator_create(func):

  def inner(*args):
    
     
    lista = list(args)
    args[0].lock.acquire()
    args[1].sendall('Type the code: '.encode('utf-8'))
    lista[2] = args[1].recv(1204).decode('utf-8')
    args[1].sendall('Type the state: '.encode('utf-8'))
    lista[3] = args[1].recv(1204).decode('utf-8')
    args[1].sendall('Type the time: '.encode('utf-8'))
    lista[4] = args[1].recv(1204).decode('utf-8')
    t = tuple(lista)
    

    return func(*t)
  return inner  