from graphviz import Digraph

dot = Digraph('algoritma',comment='Algoritma pembuatan dataset',format='png',graph_attr={'splines': 'line'},node_attr={'shape': 'rectangle'})
dot.node('input','MASUKAN',shape='parallelogram')
dot.node('output','KELUARAN',shape='parallelogram')
dot.node('prepare','Menyiapkan dataset dasar')
dot.node('eclipse','Menghitung faktor gerhana node')
dot.node('vf','Menghitung view factor node')
dot.node('albedo','Menghitung faktor albedo satelit')

dot.node('solar', 'Menghitung faktor panas Matahari')
dot.node('earth', 'Menghitung faktor panas Bumi')
dot.node('albedoheat', 'Menghitung faktor panas albedo')
dot.node('filter','Menyaring dataset')



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

dot.render(filename='graph_algoritma',directory='fig').replace('\\', '/')
