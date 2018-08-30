#!/usr/bin/env pytest

import template as app
 
def test_app (capsys):
  # variável com a letra do arquivo de testes
  number = 1
  
  while True:
    try:
      # abre um arquivo de entrada e lê o conteúdo
      with open('input-{}'.format(number), 'r') as f:
        input_values = f.read().split('\n')

      # abre um arquivo de entrada e lê o conteúdo
      with open('output-{}'.format(number), 'r') as f:
        expected_output = f.read() + '\n'

      # função que substitui o input do código
      def mock_input(s = ''):
        if s: print(s)
        # transforma IndexError em EOFError
        try:
          return input_values.pop(0)
        except IndexError:
          raise EOFError('EOF when reading a line')
      app.input = mock_input

      # executa o código e verifica a saída
      app.main()
      output, error = capsys.readouterr()

      # analisa se a saída foi igual à esperada
      assert output == expected_output
      assert error == ''

      # procura a próxima entrada de teste
      number += 1
    
    # para o loop se não encontrar um arquivo de testes
    except FileNotFoundError:
      break
