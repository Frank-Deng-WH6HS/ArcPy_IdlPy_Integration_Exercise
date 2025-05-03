#二维表在Jupyter Notebook输出单元的可视化

from IPython import display as ipydisp; 

from collections.abc import Iterable, Iterator; 

class Table2d(): 
    
    #对象初始化
    def __init__(self, tab: Iterable): 
        #将二维表的每个单元格内对象转化为文本, 保持二维表前两层不变
        #已知的bug: 如果tab[i]是str或者bytes类, 会被拆分为字符序列
        self.__textual = tuple(
            tuple(
                str(cell) for cell in row
            ) for row in tab
        ); 
        #统计二维表行数
        self.__nrows = len(tab); 
        #统计二维表列数
        self.__ncolumns = max(len(row) for row in tab);
        #初始化列标题配置(如果所有列的标题均为空, 则标题行在后续操作中不予渲染)
        self.column_heading = [str() for i in range(self.__ncolumns)]; 
    
    @property
    def textual(self): 
        return self.__textual
    
    @property
    def rows(self): 
        return self.__nrows; 
    
    @property
    def columns(self): 
        return self.__ncolumns; 
    
    def __html_tab_body(self): 
        tab = str().join( #所有行的内容HTML连接在一起
            tuple( #每行表格的内容
                "<tr>%s</tr>" % str().join( #一行之内所有单元格的内容HTNL连接在一起
                    tuple("<td>%s</td>" % cell for cell in row) #每个单元格的内容
                ) for row in self.__textual
            )
        ); 
        return tab; 
    
    def __html_tab_head(self): 
        tab = "<tr>%s</tr>" % str().join(
            tuple("<th>%s</th>" % cell for cell in self.column_heading)
        ); 
        return tab; 
            
    def render(self): 
        #生成表格正文HTML
        html_tab_body = self.__html_tab_body(); 
        #生成表格标题HTML
        if any(cell != str() for cell in self.column_heading): 
            html_tab_head = self.__html_tab_head(); 
        else: 
            html_tab_head = str(); 
        #组合表格HTML
        html_tab = "<table>%s<table>" % (html_tab_head + html_tab_body); 
        ipydisp.display_html(ipydisp.HTML(html_tab)); 