#!/usr/bin/env python
# ----------------------------------------------------------------------------
# MIT License
# display random characters to the roomba display. Note, there are some that
# roomba can't print, those are changed to ' '

from __future__ import print_function
import pycreate2
import time
import string
import random


if __name__ == "__main__":
	# Create a Create2 Bot
	port = '/dev/tty.usbserial-DA01NX3Z'

	# setup create 2
	bot = pycreate2.Create2(port)
	bot.start()
	bot.safe()

	# get the set of all printable ascii characters
	char_set = string.printable

	print('WARNING: Not all of the allowed printable characters really look good on the LCD')

	while True:
		word = ''.join(random.sample(char_set, 4))
		print('phrase:', word)
		bot.digit_led_ascii(word)
		time.sleep(2)
