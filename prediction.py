import tensorflow as tf
sess = tf.Session()

n_stocks = 79*5

#placeholder
#input (t to t+5)
X = tf.placeholder(dtype=tf.float32, shape = [None, n_stocks]) #chane shape as needed
#target data (t+10)
Y = tf.placeholder(dtype=tf.float32, shape = [None])

sigma = 1
weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale =sigma)
bias_initializer = tf.zeros_initializer()

#Model architecture parameters

#hidden
n_neurons_1 = 20
n_neurons_2 = 8

n_target = 1

#Hidden weights initialize
W_hidden_1 =  tf.Variable(weight_initializer([n_stocks, n_neurons_1]))
bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))

W_hidden_2 =  tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))

#output weiights
W_out =  tf.Variable(weight_initializer([n_neurons_2,1]))
bias_out = tf.Variable(bias_initializer([1]))


hidden_1 =  tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
hidden_2 =  tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))

out = tf.transpose(tf.add(tf.matmul(hidden_2, W_out), bias_out))

with tf.Session() as sess:
	writer = tf.summary.FileWriter("output", sess.graph)
	print(sess.run(tf.global_variables_initializer()))
	writer.close()



