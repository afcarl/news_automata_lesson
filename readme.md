some simple examples for learning programming with python

all the `*_repl.py` files are guides for what to show in the Python REPL.

the sequence, from easier to harder:

* `tipper.py`, `tipper_repl.py` - a simple tip calculator
* `strings_repl.py` - quick intro to string manipulation
* `counter.py`, `counter_repl.py` - a word counter
* `flipper.py`, `flipper_repl.py` - word flipping in text

if you're using a computer where you do not have sudo privileges (say in a computer
lab), the `setup.sh` script will setup `pip` for your user.

then you have to install packages using `pip` with the `--user` flag, e.g.:

    pip install --user requests


note: right now `readability-lxml` is used but it's tricky to install that without sudo
privileges since it requires `lxml`, which requires the xcode command line tools.