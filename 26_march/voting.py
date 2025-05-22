# Q2) Problem Statement: Instant Runoff Voting (IRV)
# There are 5 candidates (A, B, C, D, E) in an election.
# Each voter ranks all 5 candidates in order of preference (e.g., ACBED).

# The election follows the Instant Runoff Voting (IRV) system:

# ✅ IRV Rules:
# Each voter’s first preference vote is counted initially.

# If any candidate gets more than 50% of the total votes, they are declared the winner.

# If no one has >50%, the candidate with the fewest first-choice votes is eliminated.

# Votes for the eliminated candidate are redistributed to the next preferred candidate (who is still in the race).

# This process repeats until one candidate has more than 50% of the votes.

# Input Format:
# First line: Two integers N (number of voters) and M (number of candidates, always 5).

# Next N lines: Each line is a string of length 5 containing unique uppercase letters from A to E, representing one voter's ranking from most to least preferred.

# Output Format:
# Print the name of the winning candidate (a single uppercase letter).

# Constraints:
# 1
# ≤
# 𝑁
# ≤
# 1001
# 1≤N≤1001

# 𝑀
# =
# 5
# M=5

# Each vote contains all 5 candidates exactly once and uses only uppercase letters A–E.

# Example:
# Input:

# 4 5
# ABCDE
# BCDAE
# ACBED
# CBDEA
# Output:
# A


