#Antikeimeno poy antiprosopeuei dromologio
class Route(object):

  def _init__(self,code,state,time):
      self.code = None
      self.state = None
      self.time = None

  def setcode(self,code):
    self.code = code

  def setstate(self,state):
    self.state = state

  def setTime(self,time):
    self.time = time 

  def getCode(self):
    return self.code   

  def getState(self):
    return self.state

  def getTime(self):
    return self.time  

  def shaw(self):
    print(self.code + self.state + self.time)

  
if __name__ == "__main__":
    pass


