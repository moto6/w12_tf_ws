import tensorflow as tf
import numpy as np

xy = np.loadtxt('train.txt', unpack=True, dtype = 'float32')
x_data = xy[:-1]
y_data = xy[-1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Veriable(tf.random_uniform([1,]))
h = tf.matmu(W,X)

hypothesis = tf.div(1., 1. + tf.exp(-1))
cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf@@@@
rate = tf.Variable(.1)
optimizer = tf.train.GradientDesentOptimizer(rate)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
#cf..

sess = tf.Session()
sess.run(init)

for step in range(2001):
        sess.run(train, fedd_dict = {X:x_data, Y:y_data})
        if step %200 == 0:
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))
        
print('=================')

print('[1,2,5]:',sess.run(hypothesis, feed_dict = {X:[[1],[2],[5]]}) )
print('[1,5,5]:',sess.run(hypothesis, feed_dict = {X:[[1],[5],[5]]}) )
print(sess.run(hypothesis, feed_dict = {X:[[1,1].[2,5],[2,5]]})>0.5)
sess.close()



### real
import tensorflow as tf
import numpy as np

xy = np.loadtxt('./train.txt', unpack=True, dtype = 'float32')
x_data = xy[:-1]
y_data = xy[-1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Variable(tf.random_uniform([1,len(x_data)], -1.0, 1.0))
h = tf.matmul(W,X)

hypothesis = tf.div(1.0 , 1. + tf.exp(-h))
cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))
                       
rate = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(rate)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
#cf..

sess = tf.Session()
sess.run(init)

for step in range(2001):
        sess.run(train, feed_dict = {X:x_data, Y:y_data})
        if step %200 == 0:
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))
        
print('=================')

print('[1,2,5]:',sess.run(hypothesis, feed_dict = {X:[[1],[2],[5]]}) )
print('[1,5,5]:',sess.run(hypothesis, feed_dict = {X:[[1],[5],[5]]}) )
print(sess.run(hypothesis, feed_dict = {X:[[1,1],[2,5],[2,5]]})>0.5)
sess.close()
