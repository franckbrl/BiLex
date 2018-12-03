import sys

def process(inFile, vocabFile, embeddingFile):
	'''Split @inFile generated by BilBOWA into @vocabFile and @embeddingFile.'''
	with open(inFile, 'r', encoding='utf-8', errors='ignore') as fin, \
		open(vocabFile, 'w', encoding='utf-8') as fVocab, \
		open(embeddingFile, 'w', encoding='utf-8') as fEmbedding:
		lines = fin.readlines()
		lines = lines[1:]
		for line in lines:
			parts = line.split()
			fVocab.write(parts[0] + '\n')
			fEmbedding.write(' '.join(parts[1:]) + '\n')

if __name__ == '__main__':
	process(sys.argv[1], sys.argv[2], sys.argv[3])