#!/bin/bash

cat odm.txt | tr , '\n'  | sed -r '/[^A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+/d' > odmNorm.txt
