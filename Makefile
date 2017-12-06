corrector.far: corrector.grm ./Dictionaries/odmNorm.txt
	thraxcompiler --input_grammar=$< --output_far=$@

clean:
	rm -f 
