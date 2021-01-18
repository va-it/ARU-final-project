# Calculate BLEU score

from nltk.translate.bleu_score import sentence_bleu

scores = []

for generated_gui in os.listdir('generated_code'):
    if generated_gui.find('.gui') != -1:
	generated_gui_uid = Path(generated_gui).stem
	# store tokens for generated gui inside candidate array
	candidate = []
	for line in file:
		line = line.replace(',', ' ,').replace('\n', ' \n')
		tokens = line.split(' ')
		for token in tokens:
			# The candidate sentence is as a list of tokens.
			candidate.append(token)

	for original_gui in os.listdir('original_code'):
		if original_gui.find('.gui') != -1:
			original_gui_uid = Path(original_gui).stem
			if original_gui_uid == generated_gui_uid:
				# store tokens for original gui inside array
				original_token_sequence = []
				for line in original_gui:
					line = line.replace(',', ' ,').replace('\n', ' \n')
					tokens = line.split(' ')
					for token in tokens:
						original_token_sequence.append(token)
				
				reference = []
				# The reference is expected to be a list of sentences
				reference.append(original_token_sequence)
				score = sentence_bleu(reference, candidate)
				scores.append(score)

# calculate the average BLEU score and print it
print(sum(scores)/len(scores))
        	



