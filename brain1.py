# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:04:43 2023

@author: 0036YD744
"""

# Imporing Library's
import keras 
from keras.models import Sequential
from keras.layes import Dense
from keras.optimizers import Adam
import pandas
import numpy



# creating Brain class
class Brain():
    
    def __init__(self, num_inputs,num_outputs, learning_rate):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.lr = learning_rate
        
        # creating the Nural Nwtwork
        self.model = Sequential()
        self.model.add(Dense(units=32, activation='relu', input_shape= (self.num_inputs,)))
        self.model.add(Dense(units=16, activation='relu'))
        self.model.add(Dense(units=self.num_outputs))
        
        self.model.compile(optimizer=Adam(learning_rate=self.lr),loss='mean_squared_error')
        
        
        
        
        
        
        
        