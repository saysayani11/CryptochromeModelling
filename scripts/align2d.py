from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='5T5X', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5T5X', atom_files='5T5X.pdb')
aln.append(file='target.ali', align_codes='target')
aln.align2d(max_gap_length=50)
aln.write(file='1.ali', alignment_format='PIR')
aln.write(file='1.pap', alignment_format='PAP')
