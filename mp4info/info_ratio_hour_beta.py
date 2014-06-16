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
filename="./data/info_ratio_hour_beta_"+filetime

data = np.loadtxt(filename, dtype=[('time','i4'),('total','i4'),('fail','f4')])


fig=plt.figure(figsize=(10,6),dpi=120)
ax1=fig.add_subplot(111)

plt.plot(data["time"],data["total"],"*-b",label=u"压缩头信息请求数")
plt.xlabel(u"单位： Hour ",fontproperties=zhfont1)
plt.ylabel(u"压缩头信息请求数",fontproperties=zhfont1)
plt.legend(loc="upper left",prop=zhfont1)
plt.grid()

ax2=ax1.twinx()
plt.plot(data["time"],data["fail"]/(data["total"]),"*-r",label=u"获取失败率")
plt.ylabel(u"信息获取失败率",fontproperties=zhfont1)
plt.ylim(0, 0.1)
ax2.set_yticks(np.linspace(0, 0.1, 11))
plt.legend(loc="upper right",prop=zhfont1)
plt.grid()

plt.xlim(0,24)
plt.xticks(range(24))
plt.title(u"【Beta版本】信息获取失败率"+filetime,fontproperties=zhfont1)

plt.savefig("./png/info_ratio_hour_beta_"+filetime)

print "draw"+filetime+" ratio hour beta png"
