from graphviz import Digraph

dot = Digraph('dataset',comment='Dataset creation pipeline',format='png',graph_attr={'splines': 'line'},node_attr={'shape': 'rectangle'})
dot.node('input','Input',shape='parallelogram')
dot.node('output','Output',shape='parallelogram')
dot.node('prepare','Prepare base dataset')
dot.node('eclipse','Calculate node eclipse factor')
dot.node('vf','Calculate node view factor to Earth')
dot.node('albedo','Calculate satellite albedo factor')

dot.node('solar', 'Calculate solar heat factor')
dot.node('earth', 'Calculate Earth heat factor')
dot.node('albedoheat', 'Calculate albedo heat factor')
dot.node('filter','Filter dataset')



dot.edge('input','prepare')

dot.edge('prepare','eclipse')
dot.edge('prepare','vf')
dot.edge('prepare','albedo')

dot.edge('eclipse','solar')

dot.edge('vf','albedoheat')
dot.edge('albedo','albedoheat')

dot.edge('vf','earth')

dot.edge('solar','filter')
dot.edge('earth','filter')
dot.edge('albedoheat','filter')

dot.edge('filter','output')

dot.render(filename='graph_dataset',directory='fig').replace('\\', '/')
