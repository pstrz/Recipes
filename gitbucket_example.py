# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:32:30 2018

@author: philstrzelecki
"""
import numpy as np
from git import Repo

A = np.ones([3,3])
np.save('A', A)

repo = Repo("")

origin = repo.remote()
origin.pull()



origin.push()

#none of this works :) 