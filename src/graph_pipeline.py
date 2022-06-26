from graphviz import Digraph

dot = Digraph('pipeline',comment='Dataset creation pipeline',format='png',graph_attr={'splines': 'line'},node_attr={'shape': 'rectangle'})
dot.node('input','Input',shape='parallelogram')
dot.node('output','Output',shape='parallelogram')
dot.node('prepare','Prepare base dataset')

dot.node('eclipse','Calculate nodes\' eclipse factor')
dot.node('vf','Calculate nodes\' view factor to Earth')

dot.node('solar','Calculate nodes\' Solar heat term')
dot.node('earth','Calculate nodes\' Earth heat term')
dot.node('albedo','Calculate nodes\' albedo heat term')
dot.node('filter','Filter dataset')
dot.node('clean','Clean?',shape='diamond')

dot.edge('input','prepare')

dot.edge('prepare','eclipse')
dot.edge('prepare','vf')

dot.edge('eclipse','solar')

dot.edge('vf','earth')

dot.edge('vf','albedo')
dot.edge('eclipse','albedo')

dot.edge('solar','filter')
dot.edge('earth','filter')
dot.edge('albedo','filter')
dot.edge('filter','clean')
dot.edge('clean','output',label='Yes')

dot.edge('clean:e','filter:se',label='No')

dot.render(filename='graph_pipeline',directory='fig').replace('\\', '/')
