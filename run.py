#!/usr/bin/env python

import subprocess

print('Witaj w korektorze!')
print('Wpisz exit aby wyjść.\n')

exit = False
while (exit == False):

	print('--------------------')
	inputWord = input('\nWpisz słowo które chcesz poprawić: ')

	if(inputWord == 'exit'):
		exit = True
	else:
		print('Moment, sprawdzam Twoje słowo!')
		result = subprocess.run(['bash', './Bin/runCheck.sh', inputWord], stdout=subprocess.PIPE)

		rawText = result.stdout.decode('utf-8')
		outputWord = rawText[29:-14].strip()

		if (outputWord != ''):
			print("\nTwoje poprawione słowo: " + outputWord + "\n")
		else:
			print("\nNiestety, nie znalazłem poprawnej formy tego słowa!\n")