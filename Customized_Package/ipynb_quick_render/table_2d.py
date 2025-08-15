#二维表在Jupyter Notebook输出单元的可视化

from IPython import display as ipydisp; 

import math; 
from collections.abc import Iterable, Iterator; 
from functools import reduce; 
import operator as op; 
from itertools import zip_longest; 

class Table2d(): 
    
    #对象初始化
    def __init__(self, tab: Iterable, multi_column=1): 
        #将二维表的每个单元格内对象转化为文本, 保持二维表前两层不变
        #已知的bugs: 
        #  1. 如果tab[i]是str或者bytes类, 会被拆分为字符序列
        #  2. 由于函数定义时使用了annotation, 本模块无法在python 2.x的解释器中导入
        if multi_column == 1: 
            tab_mc = tab; 
        else: 
            #以"分栏"模式显示表格前, 需要对表格内容重新整理
            max_rows = math.ceil(len(tab) / multi_column); 
            idx_starts = range(0, len(tab), max_rows); 
            #如果未分栏表格的行数无法被分栏的列数整除, 需要对表格追加包含空字符串的行
            num_elem_pad = max_rows * multi_column - len(tab); 
            tab_pad = tab.copy(); 
            tab_pad.extend(((str(), ) * len(tab[0]), ) * num_elem_pad); 
            #将原表格以max_rows行为单位拆分重组
            idx_slices = tuple(
                slice(idx, idx + max_rows, 1) for idx in idx_starts
            ); 
            tab_mc = tuple(
                reduce(op.add, 
                    tuple(tab_pad[idx_mc][idx_row] for idx_mc in idx_slices)
                ) for idx_row in range(0, max_rows)
            ); 
        self._textual = tuple(
            tuple(
                str(cell) for cell in row
            ) for row in tab_mc
        ); 
        #统计二维表行数
        self._nrows = len(tab_mc); 
        #统计二维表列数
        self._ncolumns = max(len(row) for row in tab_mc);
        #初始化列标题配置(如果所有列的标题均为空, 则标题行在后续操作中不予渲染)
        self.column_heading = [str() for i in range(self._ncolumns)]; 
    
    @property
    def textual(self): 
        return self._textual
    
    @property
    def rows(self): 
        return self._nrows; 
    
    @property
    def columns(self): 
        return self._ncolumns; 
    
    def _html_tab_body(self): 
        tab = str().join( #所有行的内容HTML连接在一起
            tuple( #每行表格的内容
                "<tr>%s</tr>" % str().join( #一行之内所有单元格的内容HTNL连接在一起
                    tuple("<td>%s</td>" % cell for cell in row) #每个单元格的内容
                ) for row in self._textual
            )
        ); 
        return tab; 
    
    def _html_tab_head(self): 
        tab = "<tr>%s</tr>" % str().join(
            tuple("<th>%s</th>" % cell for cell in self.column_heading)
        ); 
        return tab; 
            
    def render(self): 
        #生成表格正文HTML
        html_tab_body = self._html_tab_body(); 
        #生成表格标题HTML
        if any(cell != str() for cell in self.column_heading): 
            html_tab_head = self._html_tab_head(); 
        else: 
            html_tab_head = str(); 
        #组合表格HTML
        html_tab = "<table>%s<table>" % (html_tab_head + html_tab_body); 
        ipydisp.display_html(ipydisp.HTML(html_tab)); 