import itertools
import enchant

# From the 2020-05-03 puzzle section, "Building Blocks"

d = enchant.Dict("en_US")

# starters = ['bam', 'ina', 'pet', 'bob', 'too', 'alc', 'rep', 'car']
# position = 'first'
# blocks = [
#     'ant', 'boo', 'che', 'dge', 'eum', 'igh', 'lic', 'oho', 'oke', 'ral', 'rol',
#     'sle', 'taj', 'tha', 'tri', 'ugn', 'ugu', 'wha', 'zle'
# ]

starters = ['est', 'ali', 'dsc', 'ivo', 'rit', 'pev', 'erl', 'sce']
position = 'middle'
blocks = [
    'anc', 'lav', 'lan', 'equ', 'rew', 'gra', 'int', 'cre', 'ral', 'ere',
    'ape', 'cal', 'ten', 'ine', 'ock', 'ndo', 'nyn', 'ose', 'run'
]

# starters = ['tch', 'orm', 'ter', 'wer', 'xin', 'ion', 'ast', 'nce']
# position = 'last'
# blocks = [
#     'ant', 'cri', 'cun', 'eif', 'ela', 'flo', 'fre', 'ito', 'kil', 'may', 'ned',
#     'oli', 'pwa', 'sim', 'sta', 'sto', 'ter', 'ulc', 'ytu'
# ]


def solve(starters, position, blocks):
    block_perms = list(itertools.permutations(blocks, r=2))
    block_starter_combs = []
    for starter in starters:
        if position == 'last':
            block_starter_combs.extend(
                [
                    {
                        'string': x[0] + x[1] + starter,
                        'is_word': d.check(x[0] + x[1] + starter)
                    }
                    for x in block_perms
                ]
            )
        elif position == 'middle':
            block_starter_combs.extend(
                [
                    {
                        'string': x[0] + starter + x[1],
                        'is_word': d.check(x[0] + starter + x[1])
                    }
                    for x in block_perms
                ]
            )
        else:
            block_starter_combs.extend(
                [
                    {
                        'string': starter + x[0] + x[1],
                        'is_word': d.check(starter + x[0] + x[1])
                    }
                    for x in block_perms
                ]
            )

    found_words = [x for x in block_starter_combs if x['is_word']]
    return found_words
