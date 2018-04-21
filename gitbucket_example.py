# -*- coding: utf-8 -*-
"""
I would like to nominate GitPython for the Single Worst Tutorial Ever Written

@author: philstrzelecki
"""
import numpy as np
from git import Repo

A = np.ones([3,3])
np.save('A', A)

repo = Repo("")
origin = repo.remote('origin')

repo.index.add(["A.npy"])
repo.index.commit("test")

origin.push()

B = 2 * np.ones([3,3])
np.save('A', B)

origin.pull

C = np.load('A.npy')
print(C)