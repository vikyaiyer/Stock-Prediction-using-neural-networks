import tensorflow as tf
sess = tf.Session()

alpha = 0.01
sector = 8
n_stocks = 2*5

#placeholder
X1 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X2 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X3 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
'''
X4 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X5 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X6 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X7 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
X8 = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) 
'''

Y = tf.placeholder(dtype=tf.float32, shape = [None])

sigma = 1
weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale =sigma)
#bias_initializer = tf.zeros_initializer()

layer1_w1 = 1
layer1_w2 = 1
ema = 15
layer2_z = 5

layer1_w3 = 1
'''
layer1_w4 = 1
layer1_w5 = 1
layer1_w6 = 1
layer1_w7 = 1
layer1_w8 = 1




n_target = 1
'''
#EMA = tf.Variable(weight_initializer(ema, layer2_z))
#bias_hidden = tf.Variable(bias_initializer([layer1_w8]))

W_hidden_1 =  tf.Variable(weight_initializer([n_stocks, layer1_w1])) #check this
W_hidden_2 =  tf.Variable(weight_initializer([n_stocks, layer1_w2]))
W_hidden_3 =  tf.Variable(weight_initializer([n_stocks, layer1_w3]))
'''
W_hidden_4 =  tf.Variable(weight_initializer([n_stocks, layer1_w4]))
W_hidden_5 =  tf.Variable(weight_initializer([n_stocks, layer1_w5]))
W_hidden_6 =  tf.Variable(weight_initializer([n_stocks, layer1_w6]))
W_hidden_7 =  tf.Variable(weight_initializer([n_stocks, layer1_w7]))
W_hidden_8 =  tf.Variable(weight_initializer([n_stocks, layer1_w8]))


'''
Z_hidden_1 =  tf.Variable(weight_initializer([layer1_w1, layer2_z ]))

#W_out =  tf.Variable(weight_initializer([layer2_z,1]))
#bias_out = tf.Variable(bias_initializer([1]))


hidden1_w1 = tf.nn.sigmoid(tf.add(tf.matmul(X1, W_hidden_1), W_hidden_1))
hidden1_w2 = tf.nn.sigmoid(tf.add(tf.matmul(X2, W_hidden_2), W_hidden_2))
hidden1_w3 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_3), W_hidden_3))
#hidden1_w4 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_4), W_hidden_4))
#hidden1_w5 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_5), W_hidden_5))
#hidden1_w6 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_6), W_hidden_6))
#hidden1_w7 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_7), W_hidden_7))
#hidden1_w8 = tf.nn.sigmoid(tf.add(tf.matmul(X3, W_hidden_8), W_hidden_8))

hidden2_z1 = tf.nn.sigmoid(tf.add(tf.matmul(hidden1_w1,Z_hidden_1 ), Z_hidden_1))
hidden2_z1 = tf.nn.sigmoid(tf.add(tf.matmul(hidden1_w2,Z_hidden_1 ), Z_hidden_1))
hidden2_z1 = tf.nn.sigmoid(tf.add(tf.matmul(hidden1_w3,Z_hidden_1 ), Z_hidden_1))
with tf.Session() as sess:
	writer = tf.summary.FileWriter("output", sess.graph)
	print(sess.run(tf.global_variables_initializer()))
	writer.close()
