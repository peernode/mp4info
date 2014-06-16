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

filename="./data/mp4info_ct_beta_%s"%(date);
data=np.loadtxt(filename, usecols=(0, 1), dtype=[('flag', 'i4'), ('ct', 'i4')])

#
# figure1: get info cost time
#
pl.figure(1)

suc_data=get_intkey_valued_data(data, 'flag', 1, 'ct')
suc_cdf_data=calc_suc_CDF_data(suc_data) 
pl.plot(suc_cdf_data['x'], suc_cdf_data['y'], color="red", linewidth=1.0, label=(u"成功耗时-%d")%(len(suc_cdf_data))) 

fail_data=get_intkey_valued_data(data, 'flag', 0, 'ct')
fail_cdf_data=calc_suc_CDF_data(fail_data) 
pl.plot(fail_cdf_data['x'], fail_cdf_data['y'], color="blue", linewidth=1.0, label=(u"失败耗时-%d")%(len(fail_cdf_data))) 

plt.legend(loc="lower right",prop=zhfont1)

pl.xlim(0, 8000)
#pl.xticks(np.linspace(0, 8000, 5, endpoint=True))

pl.xlabel("get info costtime (ms)")

pl.ylim(0, 100)
pl.yticks(np.linspace(0, 100, 11, endpoint=True))
pl.ylabel("percentage(%)")

pl.title("[beta] get info costtime in %s"%date)
pl.grid()

pl.savefig("./png/cdf_of_get_info_costtime_in_%s.png"%date)

pl.show()

# stat p25, 50, 75, 90
p25=suc_cdf_data['x'][int(0.25*len(suc_cdf_data))]
p50=suc_cdf_data['x'][int(0.50*len(suc_cdf_data))]
p75=suc_cdf_data['x'][int(0.75*len(suc_cdf_data))]
p90=suc_cdf_data['x'][int(0.90*len(suc_cdf_data))]

output_filename="./data/mp4info_ct_daily_beta"
output = open(output_filename, 'a')
output.write("%s %d %d %d %d\n"%(date, p25, p50, p75, p90))
output.close()

#
# figure 2: daily sm
#
daily_data = np.loadtxt(output_filename, dtype=[('time','i8'),('p25','i4'),('p50','i4'),('p75','i4'),('p90','i4')])

data_len=len(np.atleast_1d(daily_data))
time_str=[]
if data_len==1:
    time_str.append(str(daily_data["time"])[4:8])
else:
    for i in range(data_len):
        time_str.append(str(daily_data["time"][i])[4:8])

fig=plt.figure(figsize=(10,6),dpi=120)

plt.plot(daily_data["p25"],"*-b",label=u"p25")
plt.plot(daily_data["p50"],"+-r",label=u"p50")
plt.plot(daily_data["p75"],"o-k",label=u"p75")
plt.plot(daily_data["p90"],"y",label=u"p90")
plt.ylabel(u"获取压缩头信息耗时(ms)",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)

ax1=plt.gca()
#ax1.set_ylim(0, 10000)
ax1.set_xlim(0, data_len)
ax1.set_xticks(np.linspace(0, data_len, data_len+1, endpoint=True))
ax1.set_xticklabels(time_str, rotation=75)

plt.grid()

plt.title(u"[beta] daily get info cost time",fontproperties=zhfont1)

plt.savefig("./png/daily_info_ct_beta_"+date)

