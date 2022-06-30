from graphviz import Digraph

dot = Digraph('workflow',comment='Thermal modelling workflow',format='png',node_attr={'shape': 'rectangle'})
dot.node('start','Start',style="rounded")
dot.node('end','End',style="rounded")
dot.node('gather','Gather data')
dot.node('create','Create dataset')
dot.node('split','Split to training & test set')
dot.node('train','Train linear regression machine learning model')
dot.node('get','Get temperature predictions')
dot.node('evaluate','Evaluate model performance')
dot.edge('start','gather')
dot.edge('gather','create')
dot.edge('create','split')
dot.edge('split','train')
dot.edge('train','get')
dot.edge('get','evaluate')
dot.edge('evaluate','end')

dot.render(filename='graph_workflow',directory='fig').replace('\\', '/')