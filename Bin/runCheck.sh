#!/bin/bash

echo $1 | thraxrewrite-tester --far=corrector.far --rules=corrector
