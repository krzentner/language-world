

"""
[eod] [code]import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("mnist_data",one_hot=True)

training_iters = 1000000
batch_size = 128
display_step = 10

# 定义两个placehodlder
x = tf.placeholder(tf.float32, [None, 784]) # 28*28
y = tf.placeholder(tf.float32, [None, 10])

# 创建一个简单的神经网络，输入层包含784个神经元，输出层包含10个神经元，中间有一个隐藏层
W1 = tf.Variable(tf.truncated_normal([784,200],stddev=0.1))
b1 = tf.Variable(tf.zeros([200]))
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)

W2 = tf.Variable(tf.truncated_normal([200,10],stddev=0.1))
b2 = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax(tf.matmul(L1,W2)+b2)

# 二次代价函数
# loss = tf.reduce_mean(tf.square(y-prediction))
# cross_entropy = -tf.reduce_sum(y*tf.log(prediction))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=prediction))
# 使用梯度下降法来最小化代价函数
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 开始一个会话
with tf.Session() as sess:
    sess.run(init)

    for i in range(training_iters):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        if i%display_step==0:
            loss_val = sess.run(loss,feed_dict={x:batch_xs,y:batch_ys})
