# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:23:26 2023

@author: 0036YD744
"""

# importing library's
import numpy as np

class Dqn():
    def __init__(self,maxMemory, discount):
        self.maxMemory = maxMemory
        self.discount = discount
        
        self.memory = list()
    
    # Remembering Experiance
    def remember(self, transition, gameOver):
        self.memory.append([transition,gameOver])
        if len(self.memory) > self.maxMemory:
            del self.memory[0]
            
    # Getting batches of inputs and tragets
    
