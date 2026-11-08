from fractions import Fraction


for blocks in (2, 4, 8, 16):
    private_bits = blocks
    positions = blocks * (private_bits + 1)
    joint_support = 2 ** (blocks * private_bits + 1)
    marginal_support = 2 ** (private_bits + 1)
    joint_entropy = joint_support.bit_length() - 1
    summed_entropy = blocks * (marginal_support.bit_length() - 1)
    correction = summed_entropy - joint_entropy
    assert correction == blocks - 1
    print(f"{blocks:2d} blocks: correction={correction:2d}, correction/size={Fraction(correction, positions)}")
