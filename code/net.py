from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import numpy as np 
import pandas as pd

zxc = pd.read_excel('/users/xuguodong/desktop/data1/result1.xls');
z = np.array(zxc.ix[:,'data'])

X = np.arange(194)[:,None]
y = z

temp = pd.read_excel('/users/xuguodong/desktop/2016/1/temp.xlsx')

net =buildNetwork(8,50,30,20,1,bias=True)

ds = SupervisedDataSet(8,1)

for i in range(170):
	ds.addSample((y[i],y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6],y[i+7]),y[i+8])

trainers = BackpropTrainer(net, ds, momentum=0.1,verbose = True, weightdecay=0.01)
trainers.trainEpochs(epochs=15)
out = []
for i in range(8):
	out.append(net.activate((y[178+i],y[178+i+1],y[178+i+2],y[178+i+3],y[178+i+4],y[178+i+5],y[178+i+6],y[178+i+7])))
print out






