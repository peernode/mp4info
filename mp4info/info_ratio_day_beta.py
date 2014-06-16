# -*- coding: utf-8 -*-
"""
Created on 2013/10/31

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
zhfont1=matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/TrueType/ukai.ttf')

filetime=sys.argv[1]
filename="./data/info_ratio_day_beta"

data = np.loadtxt(filename, dtype=[('time','i4'),('total','i4'),('fail','f4')])

data_len=len(np.atleast_1d(data))
time_str=[]
if data_len==1:
    time_str.append(str(data["time"])[4:8])
else:
    for i in range(data_len):
        time_str.append(str(data["time"][i])[4:8])

fig=plt.figure(figsize=(10,6),dpi=120)

plt.plot(data["total"],"*-b",label=u"信息请求数")
plt.ylabel(u"信息请求数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)

ax1=plt.gca()
ax1.set_xlim(0, data_len)
ax1.set_xticks(np.linspace(0, data_len, data_len+1, endpoint=True))
ax1.set_xticklabels(time_str, rotation=75)

ax2=ax1.twinx()
plt.plot(data["fail"]/(data["total"]),"*-r",label=u"获取失败率")
plt.ylabel(u"信息获取失败率",fontproperties=zhfont1)
plt.ylim(0,0.1)
ax2.set_yticks(np.linspace(0, 0.1, 11))
plt.legend(loc="upper right",prop=zhfont1)
plt.grid()

plt.title(u"【Beta版本】信息获取失败率 by day",fontproperties=zhfont1)

plt.savefig("./png/info_ratio_day_beta_"+filetime)

print "draw"+filetime+" beta date png"
