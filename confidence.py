"""
This module will handle self-consistency sampling, entropy-based scoring, and temperature-scaled calibration.
It will return a normalised confidence score between 0 and 1.
"""

# if task is low risk:
#     raw score = lightweight uncertainty score
# else:
#     generate multiple plans
#     agreement score = measure agreement across plans
#     raw score = agreement score

# if logprobs available and task is not low risk:
#     measure entropy score
#     raw score = combine agreement score and entropy score

# if calibration available:
#     confidence score =  apply temperature scaling to raw score
# else:
#     confidence score = raw score

# return confidence score
