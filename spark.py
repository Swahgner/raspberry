#!/usr/bin/python
#
# pi-sense-rainbow.py
#
# Paints a scrolling rainbow of colours on the sense-hat display. Based on the
# sense-hat example script 'colour_cycle.py'.
#
# This  program  is  free software: you can redistribute it and/or  modify  it
# under  the terms of the GNU General Public License as published by the  Free
# Software  Foundation,  either version 3 of the License, or (at your  option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but  WITHOUT
# ANY  WARRANTY;  without  even  the implied warranty  of  MERCHANTABILITY  or
# FITNESS  FOR A PARTICULAR PURPOSE.  See the GNU General Public  License  for
# more details.
#
# You  should  have  received a copy of the GNU General  Public License  along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sense_hat
import random
import time
import signal

# Signal handler to trap Ctrl_C events.
def signal_handler(signal, frame):

  _sense.clear([0, 0, 0])
  raise SystemExit

def next_colour(_colour):
  if (_colour[0] == 192 and _colour[1] < 192 and _colour[2] == 0):
    _colour[1] += 48
  if (_colour[1] == 192 and _colour[0] > 0 and _colour[2] == 0):
    _colour[0] -= 48
  if (_colour[1] == 192 and _colour[2] < 192 and _colour[0] == 0):
    _colour[2] += 48
  if (_colour[2] == 192 and _colour[1] > 0 and _colour[0] == 0):
    _colour[1] -= 48
  if (_colour[2] == 192 and _colour[0] < 192 and _colour[1] == 0):
    _colour[0] += 48
  if (_colour[0] == 192 and _colour[2] > 0 and _colour[1] == 0):
    _colour[2] -= 48
  return _colour

# Instantiate sense object before setting up signal handler as the 
# signal handler uses it to clear all the pixels.
_sense = sense_hat.SenseHat() 

# Set up signal handler to catch Ctrl-C.
signal.signal(signal.SIGINT, signal_handler)

# Dim the display.
_sense.low_light = True

# Rotate the display so it is the 'right' way up.
_sense.set_rotation(0)

# Instantiate list of lists (to hold pixel values).
_pixels = [[0, 0, 0] for _range in range(64)]

_colour = [192, 0, 0]
while True:
  for _count in range(56,64):
    _pixels[_count] = [_colour[0], _colour[1], _colour[2]]

  for _count in range(56):
    _pixels[_count] = _pixels[_count + 8]

  _colour = next_colour(_colour)

  # Update the display.
  _sense.set_pixels(_pixels)

  # Pause briefly, then do it all again!
  time.sleep(0.04) 
