class Solution:
  def __init__(self,x,exprFun,partition):
    self.x=x
    self.exprFun=exprFun
    self.partition=partition
    self.funVal=[]
    self.calculate()

  def calculate(self):
    for i in range(len(self.x)):
      exec("x{0}={1}".format(i+1,self.x[i]))

    for i in range(len(self.x)):
      self.funVal.append(eval("{0}".format(self.exprFun[i])))

  def __str__(self):
    string="";
    for i in range(len(self.x)):
      string=string+"x{0}: {1:.2f}\t".format(i+1,self.x[i])
    for i in range(len(self.funVal)):
      string=string+"f{0}: {1:.2f}\t".format(i+1,self.funVal[i])
    string=string+"Partition: {0}\t Assigned_fitness: {1:.2f}".format(self.partition,self.funVal[self.partition])    
    return string



#from petia import Solution
funs=['x1','(1+x2)/x1']
A=[]
A.append(Solution([0.31, 0.89],funs,1))
A.append(Solution([0.43, 1.92],funs,1))
A.append(Solution([0.22, 0.56],funs,2))
A.append(Solution([0.59, 3.63],funs,2))
A.append(Solution([0.66, 1.41],funs,1))
A.append(Solution([0.83, 2.51],funs,2))

for i in range(len(A)):
  A[i].calculate()
  print(A[i])
