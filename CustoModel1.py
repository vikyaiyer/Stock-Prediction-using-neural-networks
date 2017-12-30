import tensorflow as tf
import pandas as pd
import numpy as np


sector = 8

#data input
data1 = pd.read_csv('fileRO-1.csv')
data1 = data1.drop(['open'], 1)
data1 = data1.drop(['volume'], 1)
data1 = data1.drop(['low'], 1)
data1 = data1.drop(['high'], 1)
data1 = data1.drop(['Date'], 1)
data1 = data1.values

data2 = pd.read_csv('fileRO-2.csv')
data2 = data2.drop(['open'], 1)
data2 = data2.drop(['volume'], 1)
data2 = data2.drop(['low'], 1)
data2 = data2.drop(['high'], 1)
data2 = data2.drop(['Date'], 1)
data2 = data2.values

list1=[]
list2=[]
n = data1.shape[0]
p = data1.shape[1]

i=0
flg=0  
while(i<n):
        #print(i)
        if((i+1)%5==0 and i!=0):
            i=i+6
            flg=1
        else:
            list1.append(((data1[i+1]-data1[i])/data1[i]).tolist())
            list2.append(((data2[i+1]-data2[i])/data2[i]).tolist())
                
        if(i>100):
            break
        if(flg==0):
            i=i+1
        flg=0

sigma = 1
n_stocks = 10
X1 = tf.constant(list1,dtype=tf.float32)
X2 = tf.constant(list2,dtype=tf.float32)
print(X1)
'''
X3 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X4 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X5 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X6 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X7 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X8 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
Y = tf.placeholder(dtype=tf.float32, shape = [None])
'''

weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale =sigma)
#bias_initializer = tf.zeros_initializer()

layer1_w = 1
layer2_z = 5

'''
ema = 15
n_target = 1
'''

W_hidden_1 =  tf.Variable(tf.random_normal([(n_stocks*4),layer1_w]))
W_hidden_2 =  tf.Variable(tf.random_normal([(n_stocks*4),layer1_w]))


Z_hidden =  tf.Variable(tf.random_normal([2,layer2_z]))

W_out =  tf.Variable(tf.random_normal([5,1]))

'''
W_hidden_3 =  tf.Variable(weight_initializer([n_stocks, layer1_w3]))
bias_hidden_3 = tf.Variable(bias_initializer([layer1_w3]))

W_hidden_4 =  tf.Variable(weight_initializer([n_stocks, layer1_w4]))
bias_hidden_4 = tf.Variable(bias_initializer([layer1_w4]))

W_hidden_5 =  tf.Variable(weight_initializer([n_stocks, layer1_w5]))
bias_hidden_5 = tf.Variable(bias_initializer([layer1_w5]))

W_hidden_6 =  tf.Variable(weight_initializer([n_stocks, layer1_w6]))
bias_hidden_6 = tf.Variable(bias_initializer([layer1_w6]))

W_hidden_7 =  tf.Variable(weight_initializer([n_stocks, layer1_w7]))
bias_hidden_7 = tf.Variable(bias_initializer([layer1_w7]))

W_hidden_8 =  tf.Variable(weight_initializer([n_stocks, layer1_w8]))
bias_hidden_8 = tf.Variable(bias_initializer([layer1_w8]))

#
#bias_out = tf.Variable(bias_initializer([1]))
'''

alpha=[[0.01]]
sess = tf.Session()
sess.run(tf.global_variables_initializer())

hidden1_w1 = tf.nn.sigmoid(tf.matmul(tf.transpose(X1),W_hidden_1))
hidden1_w2 = tf.nn.sigmoid(tf.matmul(tf.transpose(X2),W_hidden_2))
print(hidden1_w1)
print(hidden1_w2)

m1=sess.run(hidden1_w1)
m2=sess.run(hidden1_w2)

list_hidden_1=[]
list_hidden_1.append(m1[0].tolist())
list_hidden_1.append(m2[0].tolist())

list_hidden=tf.constant(list_hidden_1,dtype=tf.float32)

print(list_hidden)
hidden2_z = tf.nn.sigmoid(tf.matmul(tf.transpose(list_hidden),Z_hidden))

out_layer = tf.nn.sigmoid(tf.matmul(hidden2_z,W_out))
#a1 = tf.transpose(tf.constant(alpha,dtype=tf.float32))
#hidden1_w1 = tf.nn.sigmoid(tf.add(tf.matmul(X1,a1), W_hidden_1))

#print(sess.run(hidden1_w1))
#print(sess.run(hidden1_w2))
#print(sess.run(hidden2_z))
print(sess.run(out_layer))
tf.summary.FileWriter("output", sess.graph)
