# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 18:23:29 2013

@author: xujy
"""

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import sys
from pylab import *

from tool_funs import *

reload(sys)
sys.setdefaultencoding("utf-8")
zhfont1=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/TrueType/ukai.ttf')

date = sys.argv[1]

filename="./data/uncompress_ct_beta_%s"%(date);
data=np.loadtxt(filename, dtype=[('ct', 'i4')])

#
# figure1: get info cost time
#
pl.figure(1)

ct_cdf_data=calc_suc_CDF_data(data['ct']) 
pl.plot(ct_cdf_data['x'], ct_cdf_data['y'], color="red", linewidth=1.0, label=(u"解压耗时-%d")%(len(ct_cdf_data))) 

plt.legend(loc="lower right",prop=zhfont1)

pl.xlim(0, 50)
pl.xticks(np.linspace(0, 50, 11, endpoint=True))

pl.xlabel("uncompress costtime(ms)")

pl.ylim(0, 100)
pl.yticks(np.linspace(0, 100, 11, endpoint=True))
pl.ylabel("percentage(%)")

pl.title("[beta] uncompress costtime(ms) in %s"%date)
pl.grid()

pl.savefig("./png/cdf_of_uncompress_ct_in_%s.png"%date)

pl.show()

