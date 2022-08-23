from graphviz import Digraph

dot = Digraph('mlsetup',comment='Machine learning setup',format='png',node_attr={'shape': 'rectangle'})

dot.node('deltatrain','Laju perubahan suhu node dataset latihan')
dot.node('deltatest','Prediksi laju perubahan suhu node dataset ujian')
dot.node('paramtrain','Parameter termal node dataset latihan')
dot.node('paramtest','Parameter termal node dataset ujian')
dot.node('algo','Algoritma regresi linear OLS machine learning')
dot.node('coef','Matriks koefisien termal node')
dot.node('temptest','Prediksi suhu node dataset ujian')

dot.edge('paramtrain','algo')
dot.edge('deltatrain','algo')
dot.edge('algo','coef')
dot.edge('paramtest','coef')
dot.edge('coef','deltatest')
dot.edge('deltatest','temptest')

dot.render(filename='graph_mlsetup',directory='fig').replace('\\', '/')
