#coding: utf8
def uf(codigo):
    estados =  {
        '51': 'MT Mato Groso' ,
        '12': 'AC (Acre)',
        '13': 'AM (Amazonas)', 
        '14': 'RR (Roraima)',
        '15': 'PA (Pará)'
    }
    return estados[codigo]

print uf('51')


pessoas = ['brono', '']
