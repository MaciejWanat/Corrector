# Corrector
This program corretcs errors in a given polish word using finite state automaton. It's using [Polimorf](http://zil.ipipan.waw.pl/PoliMorf) as a source dictionary, and [Thrax](http://www.openfst.org/twiki/bin/view/GRM/ThraxQuickTour) as a tool to build and process automaton.
Files:
* corrector.grm - file containing Thrax code to build automaton
* run.py - python file that is working basicly as interface for program
* Bin/runCheck.sh - helper script for python interface
* Bin/corrector.far.tar.gz - binary file containing built automaton
* Dictionaries/polimorfNorm.txt.tar.gz - normalized Polimorf dictionary containing only words
* README.md -  this file
