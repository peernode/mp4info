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

filename="./data/task_size_beta_%s"%(date);
data=np.loadtxt(filename, usecols=(0, 1), dtype=[('original', 'i4'), ('compress', 'i4')])

#
# figure1: get info cost time
#
pl.figure(1)

original_cdf_data=calc_suc_CDF_data(data['original']) 
pl.plot(original_cdf_data['x']/1024, original_cdf_data['y'], color="red", linewidth=1.0, label=(u"原始头大小-%d")%(len(original_cdf_data))) 

compress_cdf_data=calc_suc_CDF_data(data['compress']) 
pl.plot(compress_cdf_data['x']/1024, compress_cdf_data['y'], color="blue", linewidth=1.0, label=(u"压缩头大小-%d")%(len(compress_cdf_data))) 

plt.legend(loc="lower right",prop=zhfont1)

pl.xlim(0, 1000)
pl.xticks(np.linspace(0, 1000, 11, endpoint=True))

pl.xlabel("original/compress head size (KB)")

pl.ylim(0, 100)
pl.yticks(np.linspace(0, 100, 11, endpoint=True))
pl.ylabel("percentage(%)")

pl.title("[beta] original/compress head size in %s"%date)
pl.grid()

pl.savefig("./png/cdf_of_original_compress_head_size_in_%s.png"%date)

pl.show()

