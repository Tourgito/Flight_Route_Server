import socket
import sys
import time

class Client(object):
    
    def __init__(self):
        self.adress = 'localhost'
        self.port_number = 8999
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        

    #Dhmiourgei sundesei me ton server, antalasei mhnumata kai telos aposundeaite
    def connect(self):
      self.socket.connect(('localhost',8999))
      while True:
        
         option = input('Type: ')
         self.socket.sendall(option.encode('utf-8'))
         if option == '5':
             sys.exit()
         reply = self.socket.recv(1204).decode('utf-8')
         print(reply)
        
        
      self.socket.close()


   
    

def message():
    print('Hello CLient!!!')
    print('What do you want to do?')
    print('Write: 1, Read: 2, Update: 3, Delete: 4, Exit: 5')

if __name__ == "__main__":
    message()
    client = Client()
    client.connect()
