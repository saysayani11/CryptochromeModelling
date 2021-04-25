from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='5T5X')
aln.append_model(mdl, align_codes='5T5X')
aln.append(file='hcry1.seq', align_codes=('blbp'))
aln.align(gep_penalties_1d=(-600,-400))
aln.write(file='hcry1-5T5X.ali', alignment_format='PIR')
aln.write(file='hcry1-5T5X.pap', alignment_format='PAP')
