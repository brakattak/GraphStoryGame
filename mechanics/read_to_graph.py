import networkx as nx
import re

LINE_COUNT = 0
def check_line(line,count):
    if(not re.match('\([0-9,]+\)::.*',line)
       and not re.match('\d+\([0-9,]+\)::.*::.*',line)
       and not re.match('\d+\([0-9,]+\)\([0-9,]+\)::.*',line)):
        raise ValueError('Line {} is formated incorrectly. The line read: \n{}'.format(count,line))

def read_to_graph(filename,split_string):
    G = nx.DiGraph()
    G.add_edge(0,0,text='')
    line_count = -1
    for line in open(filename,'r'):
        line_count += 1
        if line[0]=='#' or line.strip() == '':
            continue
        check_line(line,line_count)
        l = line.split(split_string)
        if(re.match('\([0-9,]+\)::.*',line)):
            edge = l[0][1:-1].split(',')
            text = l[1][:-1]
            G.add_edge(int(edge[0]),int(edge[1]),text=text)
        else:
            node = re.search('(\d+)\(',l[0]).group(0)[:-1]
            choice_num = [int(i) for i in re.search('\(([0-9,]+)\)',l[0]).group(0)[1:-1].split(',')]
            text = l[1]
            if(re.match('\d+\([0-9,]+\)::.*::.*',line)):
                choice_text = [i.lower() for i in l[2][:-1].split('|')]
                G.add_node(int(node),text=text,choice_text=choice_text,choice_num=choice_num)
            else:
                choice_prob = [int(i) for i in re.search('\)\(([0-9,]+)\)',l[0]).group(0)[2:-1].split(',')]
                G.add_node(int(node),text=text,choice_num=choice_num,choice_prob=choice_prob)
    return G
