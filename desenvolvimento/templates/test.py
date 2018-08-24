import template as app
 
def test_app (capsys):
  input_values = [0]
  expected_output = ['']

  def mock_input(s = ''):
    if s: print(s)
    return str(input_values.pop(0))
  app.input = mock_input

  app.main()
  output, error = capsys.readouterr()

  assert output == '\n'.join(expected_output + [''])
  assert error == ''
