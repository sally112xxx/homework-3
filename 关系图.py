#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:25:53 2021

@author: sally
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:05:18 2021

@author: sally
"""
from pyecharts import options as opts
from pyecharts.charts import Graph

##--- 第0步：准备工作
# 输入文件
node_file_name = '/Users/sally/Desktop/Concurrence 平凡的世界 3/output/平凡的世界-人物节点.csv'
link_file_name = '/Users/sally/Desktop/Concurrence 平凡的世界 3/output/平凡的世界-人物连接.csv'
# 输出文件
out_file_name = '/Users/sally/Desktop/Doc2.html'


##--- 第1步：从文件读入节点和连接信息
node_file = open(node_file_name, 'r')
node_line_list = node_file.readlines()
node_file.close()
del node_line_list[0]  # 删除标题行

link_file = open(link_file_name, 'r')
link_line_list = link_file.readlines()
link_file.close()
del link_line_list[0]  # 删除标题行

##--- 第2步：解析读入的信息，存入列表
node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    node_in_graph.append(opts.GraphNode(
            name=one_line_list[0], 
            value=int(one_line_list[1]), 
            symbol_size=int(one_line_list[1])/20))  # 手动调整节点的尺寸
#print('-'*20)  # 测试点
link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    link_in_graph.append(opts.GraphLink(
            source=one_line_list[0], 
            target=one_line_list[1], 
            value=int(one_line_list[2])))


##--- 第3步：画图
c = Graph()
c.add("", 
      node_in_graph, 
      link_in_graph, 
      edge_length=[10,50], 
      repulsion=5000,
      layout="force",  # "force"-力引导布局，"circular"-环形布局
      )
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图-平凡的世界"))
c.render(out_file_name)
