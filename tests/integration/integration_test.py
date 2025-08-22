import io
from contextlib import redirect_stdout
from unittest.mock import patch
from main import main

def test_as_command_line_call():
    f = io.StringIO()
    with redirect_stdout(f):
        with patch('sys.argv', ['movie_analyzer', './sample_data/movies.csv']):
            main()
        out = f.getvalue()
  
    assert out == """Starting...
Suggested Movies:
01 | Brazil                                   | Rating: 10.0 | Certified Fresh: True | 002
02 | Blade Runner                             | Rating:  9.9 | Certified Fresh: True | 001
03 | Russian Ark                              | Rating:  9.8 | Certified Fresh: True | 017
04 | 2001 A Space Oddisey                     | Rating:  9.8 | Certified Fresh: True | 031
05 | The Sacrifice                            | Rating:  9.7 | Certified Fresh: True | 004
06 | The Seven Samurai                        | Rating:  9.5 | Certified Fresh: True | 029
07 | Once Upon A Time In Hollywood            | Rating:  9.4 | Certified Fresh: True | 006
08 | An American Werewolf in London           | Rating:  9.4 | Certified Fresh: True | 023
09 | 12 Monkeys                               | Rating:  9.3 | Certified Fresh: True | 005
10 | Time Bandits                             | Rating:  9.3 | Certified Fresh: True | 014
"""
