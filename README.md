# pyracer
Pyracer is a simple bot for typeracer written in Python.

# Installation

First, install python if you haven't already. You can do it [here](https://www.python.org/downloads/)
Second, download this repository.
Lastly, go into CMD/Terminal (make sure you're in project directory) and type `pip install -r requirements.txt`. This will install dependencies required by this program.

After installing dependencies the only thing you need is the `main.py` file. You can move it wherever you want.

# Usage

`python main.py` will run the script. It will run endlessly, so eventually you'll have to stop it manually.
If you want to increase, or decrease typing speed, just change the value of TYPE_PAUSE variable (it will always be just below imports). Note that if you set it below 0.03 (time is stored in seconds) typeracer will probably detect that you're not really typing.

Have fun with destroying all 200WPM noobs.