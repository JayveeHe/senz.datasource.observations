# -*- coding: utf-8 -*-

"""模型比较"""

from generate_observations import *
from generate_observations import sound_type, motion_type, location_type
from ghmm import *

# hmm model init
total_type = len(sound_type) * len(motion_type) * len(location_type)
sigma = IntegerRange(0, total_type)

## 转移矩阵，发射矩阵的初始化
N = 4
A = []
B = []
for looper in xrange(N):  # N个隐状态
    A.append([0.5, 0.5])
    B.append([1.0/total_type for i in xrange(total_type)])
pi = [1.0/N] * N

m = HMMFromMatrices(sigma, DiscreteDistribution(sigma), A, B, pi)
print('Init hmm model:')
print(m)

# hmm train
print('Train...')
train_seq = SequenceSet(sigma, generate_studying_senz_list(list_count=10))
m.baumWelch(train_seq)

# score test seq
print('same source:')
test_seq = SequenceSet(sigma, generate_studying_senz_list())
m.loglikelihoods(test_seq)

print('other source:')
test_seq = SequenceSet(sigma, generate_dining_senz_list())
m.loglikelihoods(test_seq)
