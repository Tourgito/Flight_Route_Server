import threading
import time 
import socket
import random 
from route import Route
from decorators import decorator_create,decorator_read 

k1 = 'What do you want to do?'
k2 ='Write: 1, Read: 2, Update: 3, Delete: 4, Exit: 5'
k3 = 'Route does not exist!!!'
k4 = 'Give a number of the options!!!'

 

class Server(object):
    
    def __init__(self):
        self.ip = 'localhost'
        self.port_number = 8999
        self.lock = threading.Lock()
        self.list = []

    #Dimiourgei ena Route kai to apothikeuei  
    @decorator_create 
    def create(self,conn,*args):
      for route in self.list:
          if route.getCode() == args[0]:
              conn.sendall('Already exist!!!.\n{}\n{}'.format(k1,k2).encode('utf-8'))
              break
      else:        
       route = Route()
       route.setcode(args[0])
       route.setstate(args[1])
       route.setTime(args[2])
       self.list.append(route)
       random_number = random.randint(5,10) 
       time.sleep(random_number)
       print('client {} waited to create the route {} seconds'.format(args[3],random_number))
       conn.sendall('Saved succesfully.\n{}\n{}'.format(k1,k2).encode('utf-8'))

      self.lock.release()


    #Anazhti ama uparxei ena sugekrimeno Route kai to emfanizei
    @decorator_read
    def search(self,code,conn,ip):
     
     fly = self.search_list(code,1)
     random_number = random.randint(2,4)
     time.sleep(random_number)
     print('client {} waited to read the route {} seconds'.format(ip,random_number))
     if fly is not None:
       conn.sendall('Found succesfully: {} {} {}\n{}\n{}'.format(fly.getCode(),fly.getState(),fly.getTime(),k1,k2).encode('utf-8'))
     else:
       conn.sendall('{}\n{}\n{}'.format(k3,k1,k2).encode('utf-8'))

     self.lock.release()
     

    #Diagrafei ena Route ama uparxei
    def delete_fly(self,conn,ip):

      self.lock.acquire()

      conn.sendall('dwse code: '.encode('utf-8'))          
      code = conn.recv(1204).decode('utf-8')
      fly = self.search_list(code,2)
      random_number = random.randint(5,10)
      time.sleep(random_number)
      print('client {} waited to delete the route {} seconds'.format(ip,random_number))
      if fly:
        conn.sendall('Route deleted succesfully!!!\n{}\n{}'.format(k1,k2).encode('utf-8'))         
      else:
        conn.sendall('{}\n{}\n{}'.format(k3,k1,k2).encode('utf-8'))

      self.lock.release()              


    #kanei update sugekrimeno Route
    def update(self,conn,ip):
        self.lock.acquire()

        conn.sendall('Type the code of the Route you want to update!!!'.encode('utf-8'))
        code = conn.recv(1204).decode('utf-8')
        fly, index = self.search_list(code,3)
        if fly is None:
         conn.sendall('{}'.format(k3).encode('utf-8'))
        else:

          conn.sendall('What do you want to update??\nCode: 1, State: 2, Time: 3'.encode('utf-8'))
          while True: 

            reply = conn.recv(1204).decode('utf-8')
            if reply.__eq__('1'):
                self.update_field(conn,fly,index,'code',ip)
                break
            elif reply.__eq__('2'):
              self.update_field(conn,fly,index,'state',ip)
              break
            elif reply.__eq__('3'):
              self.update_field(conn,fly,index,'time',ip)
              break
            else:
              conn.sendall('{}'.format(k4).encode('utf-8'))

        self.lock.release()    

    #apothikeuei Route sthn list
    def update_field(self,conn,fly,index,i,ip):
             conn.sendall('Give the new {}:'.format(i).encode('utf-8'))
             update = conn.recv(1204).decode('utf-8')
             if i == 'code':
               fly.setcode(update)
             elif i == 'state':
               fly.setstate(update)
             else:
               fly.setTime(update)
             self.list[index] = fly
             random_number = random.randint(5,10)      
             time.sleep(random_number)
             print('client {} waited to update the route {} seconds'.format(ip,random_number))
             conn.sendall('Updated sucesfully!!!\n{}\n{}'.format(k1,k2).encode('utf-8'))


    #anazhtei ama uparxei sugekrimeno route sthn lista
    def search_list(self,code,i):

       if i == 1: 
        for route in self.list:
            if route.getCode() == code:
                return route
        else:
             return None
       elif i == 2:
         for route in self.list:
            if route.getCode() == code:
                self.list.remove(route)
                return True
         else:
             return False
       else:   
            for index,route in enumerate(self.list):
              if route.getCode() == code:
                return route, index
            return None,-1 
              


    #Analogos me to ti thelei na kanei o client ektelei thn katallhlh methodo
    def options(self,conn,ip):
      
     while True:       
     
       reply = conn.recv(1204).decode('utf-8')
       
              
       if reply == '2':
          self.search(None,conn,ip) 
       elif reply == '1':
           
           self.create(conn,None,None,None,ip)
       elif reply == '4':
            self.delete_fly(conn,ip)
       elif reply == '3':
            self.update(conn,ip)
       elif reply == '5':
            print('client {} close the connection!!!'.format(ip))
            break     
       else:
           conn.sendall('{}'.format(k4).encode('utf-8'))            
     conn.close()      

    #Dimiourgei sundesei me ton client kai dimiourgei to thread
    def connect_to_client(self):
        conne_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conne_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conne_socket.bind((self.ip, self.port_number))
        conne_socket.listen(5)

        while True:
          conn, ip = conne_socket.accept()
          print('client {} connect with your server'.format(ip))
          threading.Thread(target=self.options,args=(conn,ip,)).start()
        conne_socket.close()

             
       


    





if __name__  == "__main__":
    server = Server()
    server.connect_to_client()


