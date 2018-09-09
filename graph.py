#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : first_code.py
# @Author: wxc
# @Date  : 2018/9/8

import tensorflow as tf
#取消额外的输出（...compiled to use: AVX2）
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

g1 = tf.Graph()
with g1.as_default():
    #在计算图g1中定义变量‘’v“，并设置初始值为0
    v = tf.get_variable(
        "v", shape=[1], initializer=tf.zeros_initializer)

g2 = tf.Graph()
with g2.as_default():
    #在计算图g1中定义变量‘’v“，并设置初始值为0
    v = tf.get_variable(
        "v", shape=[1], initializer=tf.ones_initializer)

#在计算图g1中读取变量”v”的取值
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        #在计算图g1中，变量“v”的取值应该是0，所以下面这行会输出[0.]
        print (sess.run(tf.get_variable("v")))

#在计算图g2中读取变量”v”的取值
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        #在计算图g1中，变量“v”的取值应该是0，所以下面这行会输出[0.]
        print (sess.run(tf.get_variable("v")))
