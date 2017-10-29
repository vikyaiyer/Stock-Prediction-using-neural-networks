import math
class MathFun:
	def __init__(self):
		pass
		
	def IntraInterval(self,High,Low,Open,Close):
		a = High - Open
		b = Open - Close
		c = Close - Low
		d = High - Low
			
		Q = [(a/d),(b/d),(c/d)]
		return Q

	def InputX(self,new,old):
		return (new - old)/old

	def ActivationFunc(self,x):
		return (1- math.exp(-x))/(1 + math.exp(-x))


x = MathFun()        
print("IntraInterval: ",x.IntraInterval(230,210,215,225))
print("InputX: ",x.InputX(17,20))    
print("Activation Fuction: ",x.ActivationFunc(0.56))        
