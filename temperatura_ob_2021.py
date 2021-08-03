# gráfico de temperatura em ouro branco, MG
import csv
from matplotlib import pyplot as plt
from datetime import datetime


base_de_dados = 'history_data.csv'
temp_maxima, tem_minima, data = [], [], []
temp_maximaC, tem_minimaC = [], []
# abrir o arquivo
with open(base_de_dados) as f:
    tabela = csv.reader(f)
    cabecalho = next(tabela)
    for linhas in tabela:
        try:
            temp_maxima.append(float(linhas[2]))
            tem_minima.append(float(linhas[3]))
            data.append(datetime.strptime(str(linhas[1]), "%m/%d/%Y"))
        except ValueError:
            print('Erro ao armazenar na lista, talvez, falta de dados')
        except TypeError:
            print('formato,type, incorreto')

# converter a temperatura maxima para C:
for temperaturas in temp_maxima:
    c = (temperaturas - 32) / 1.8
    temp_maximaC.append(c)
# converter a temperatura mínima para C:
for temperaturas in tem_minima:
    c = (temperaturas - 32) / 1.8
    tem_minimaC.append(c)
# plotando o gráfico:
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(data, temp_maximaC, c='red', linewidth=3, alpha=0.5)
plt.plot(data, tem_minimaC, c='blue', linewidth=3, alpha=0.5)
plt.fill_between(data, temp_maximaC, tem_minimaC, facecolor='green', alpha=0.1)
plt.title('Temperaturas máximas e mínimas em Ouro Branco MG', fontsize=24)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Temperatura', fontsize=14)
fig.autofmt_xdate()  # desenha rótulo com a data na diagonal
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
