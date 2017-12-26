#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

fig = plt.figure(figsize=(8, 6), dpi=100)
axes = fig.add_subplot(1, 1, 1)
axes.step(x, y)
plt.show()
