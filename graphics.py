import matplotlib.pyplot as plt

def main():
    tp50 = [208 for i in range(20)]
    tn50 = [208 for i in range(20)]
    tp60 = [208 for i in range(20)]
    tn60 = [208 for i in range(20)]
    tp70 = [132, 138, 124, 129, 138, 131, 127, 117, 128, 129, 130, 131, 126, 137,
            125, 127, 136, 123, 134, 126]
    tn70 = [208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208,
            208, 208, 208, 208, 208, 208]
    tp80 = [0 for _ in range(20)]
    tn80 = [175, 162, 123, 165, 167, 168, 131, 157, 160, 166, 148, 160, 174, 173,
            123, 158, 135, 175, 159, 149]
    tp90 = [0 for _ in range(20)]
    tn90 = [73, 57, 64, 68, 58, 72, 53, 61, 69, 65, 62, 62, 67, 65, 63, 65, 55,
            71, 56, 70]
    tp100 = [0 for _ in range(20)]
    tn100 = [1, 1, 0, 0, 2, 1, 0, 0, 3, 2, 0, 0, 1, 0, 2, 0, 1, 4, 1, 1]
    calcula_percentual = lambda x: 100*x/208
    p_tp70 = [calcula_percentual(_) for _ in tp70]
    print(p_tp70)
    p_tn80 = [calcula_percentual(_) for _ in tn80]
    p_tn90 = [calcula_percentual(_) for _ in tn90]
    p_tn100 = [calcula_percentual(_) for _ in tn100]
    percentual_tp = [100, 100, sum(p_tp70)/20, 0, 0, 0]
    percentual_tn = [100, 100, 100, sum(p_tn80)/ 20, sum(p_tn90) / 20, sum(p_tn100)/ 100]
    print(sum(tn80)/20 / 208)
    print(f'Percentual true positive {percentual_tp}')
    print(f'Percentual true negative {percentual_tn}')
    print(f'Length tp50 {len(tp50)}')
    print()
    print(f'Lenght tn50 {len(tn50)}')

    plt.plot([50, 60, 70, 80, 90, 100],percentual_tp, label='Verdeiros positivos', color='green', )
    plt.plot([50, 60, 70, 80, 90, 100],percentual_tn, label='Falsos positivos', color='red')
    plt.legend()
    plt.title('CLASSIFICAÇÃO DE RANSOMWARE COM NSA')
    plt.xlabel('% de Semelhança entre vetores')
    plt.ylabel('Percentual % de classificação')
    plt.grid()
    plt.show()
    #plt.savefig('/home/rui/Área de Trabalho/projeto/dataset/teste/classificacao_nsa.png')

if __name__ == '__main__':
    main()

