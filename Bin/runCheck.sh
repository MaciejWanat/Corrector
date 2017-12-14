#!/bin/bash

echo $1 | thraxrewrite-tester --far=./Bin/corrector.far --rules=corrector
