from mock import patch
from io import StringIO
 
with patch('builtins.input', side_effect=["0"]):
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        print(input())