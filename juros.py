# Programa para Cálculo de Empréstimo e Financiamentos
# Fórmula usada pelo Banco Central
# Os nomes das varias iniciais seguem o padrão da fórmula da matemática financeira
# A variável de amortização ela pode ser digitada pelo usuário conforme instituição bancária, senão assume o valor padrão
# O valor do IOF é fixo em 0,38% com base no Banco Central
# A variável parcelas_em_dias não está considerando anos bissextos
###########################################################################3
import os

decisao = True

while decisao:
    os.system('clear')

    print('#' * 100)
    pv = float(input("Digite o valor a ser emprestado: ")) #usar ponto ao invés de vírgula na separação dos centavos
    i = float(input("Digite o valor dos juros: ")) # não usar %
    n = int(input("Digite a quantidade de parcelas: "))
    entrada = input("Digite, se for o caso, o valor da entrada R$: ")
    amortizacao_diaria = float(0.156630137)
    iof = float(0.38)
    parcelas_em_dias = (n / 12) * 365

    if entrada:
        pv = pv - float(entrada)
    else:
        entrada = None

    if pv and i and n:
        #quebrando a fórmula
        i = (i/100) #dividir o juro inteiro por 100
        formula_1 = ((1 + i)**n)-1
        formula_2 = ((1 + i)**n)*i
        r = formula_1 / formula_2
        pmt = pv / r
        # fim da quebra de fórmula

        valor_total = (pmt * n) - pv #valor total de juros acrescidos
        total_divida = (pmt * n) # somatória do valor emprestado mais juros acrescidos
        valor_iof = (pv * iof) / 100 #descobrir o IOF da operação sobre o valor emprestado

        #calcular o IOF diario
        iof_diario = (pv * parcelas_em_dias * amortizacao_diaria) / 100
        
        #regra do BC se passar de 300 o valor é fixo em 300, senão verifica o real valor
        if iof_diario >= 300:
            valor_final_iof = valor_iof + 300.00
        else:
            valor_final_iof = valor_iof + iof_diario

        #preparar para exibir na tela
        print('-' * 100)
        if entrada:
            print(f'Você deu de entrada o valor de R$: {float(entrada):.2f}')
        print(f'Você pegou emprestado R$ {pv:.2f}')
        print(f'Você irá pagar {n} parcelas de R$ {pmt:.2f}')
        print(f'No total você pagará de juros R$ {valor_total:.2f}')
        print('-' * 100)
        print(f'Total da sua dívida será de R$ {total_divida:.2f}')
        print(f'O valor do IOF da operação será de R$ {valor_final_iof:.2f}')
    else:
        print("É necessário digitar TODOS os valores!")
    
    print('-' * 100)
    resposta = input('Deseja efetuar um novo cálculo? (S/N): ')
    
    if resposta.lower().startswith == 's':
        decisao = True
    else:
        break

print('Fim do cálculo')
