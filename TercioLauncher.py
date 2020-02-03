"""

This script is simply a launcher for the game.

Using this makes it easier when loading files 
and relative paths and such. If we were to
simply load the GameManager.py, it would
require us to have "../../" at the start of
every file path. Using this, we can instead
use "./"

"""

from Assets.Scripts import GameManager

GameManager.main()