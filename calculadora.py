# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JCb6DKwCly38RT85zadyN0FwXq9rh9GE
"""
def calculadora():
  opcao = 1
  while (opcao != '0'):
    try:
      print()
      print("------------------------------")
      opcao = input(f"1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n")
      if (opcao == '1'):
        valor_1 = float(input('Valor 01:' ))
        valor_2 = float(input('Valor 02:' ))
        resultado = valor_1 + valor_2
        print(f'Resultado: {valor_1} + {valor_2} = {resultado}')
      elif (opcao == '2'):
        valor_1 = float(input('Valor 01:' ))
        valor_2 = float(input('Valor 02:' ))
        resultado = valor_1 - valor_2
        print(f'Resultado: {valor_1} - {valor_2} = {resultado}')
      elif (opcao == '3'):
        valor_1 = float(input('Valor 01:' ))
        valor_2 = float(input('Valor 02:' ))
        resultado = valor_1 * valor_2
        print(f'Resultado: {valor_1} * {valor_2} = {resultado}')
      elif (opcao == '4'):
        valor_1 = float(input('Valor 01:' ))
        valor_2 = float(input('Valor 02:' ))
        resultado = valor_1 / valor_2
        print(f'Resultado: {valor_1} / {valor_2} = {resultado}')
      elif (opcao == '0'):
        pass
      else:
        print('Essa opção não existe!')
    except:
      print("Por favor insira valores válidos.")

	

"""
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite  o número para a operação correspondente e caso o usuário introduza
qualquer outro, o sistema deve mostrar a mensagem “Essa opção não  existe” e 
voltar ao menu de opções.

Após a  seleção, o sistema deve pedir para o usuário inserir o primeiro e 
segundo valor, um de cada. Depois precisa executar a operação e mostrar o
resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema  irá 
parar.

É necessário que o sistema mostre as opções sempre que finalizar
uma operação e mostrar o resultado. 
"""
