from hasse import display_hasse_diagram

# Divisibility poset of the divisors of 60.
# Elements are divisors of 60 ordered by divisibility (a divides b).
poset_div_60 = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 10), (1, 12), (1, 15), (1, 20), (1, 30), (1, 60),
    (2, 2), (2, 4), (2, 6), (2, 10), (2, 12), (2, 20), (2, 30), (2, 60),
    (3, 3), (3, 6), (3, 12), (3, 15), (3, 30), (3, 60),
    (4, 4), (4, 12), (4, 20), (4, 60),
    (5, 5), (5, 10), (5, 15), (5, 20), (5, 30), (5, 60),
    (6, 6), (6, 12), (6, 30), (6, 60),
    (10, 10), (10, 20), (10, 30), (10, 60),
    (12, 12), (12, 60),
    (15, 15), (15, 30), (15, 60),
    (20, 20), (20, 60),
    (30, 30), (30, 60),
    (60, 60)
]

# "Diamond"-shaped poset with 9 elements.
# A small example with elements 0 to 8 and a complex ordering pattern.
poset_diamond = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
    (1, 1), (1, 2), (1, 4), (1, 5), (1, 7), (1, 8),
    (2, 2), (2, 5), (2, 8),
    (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
    (4, 4), (4, 5), (4, 7), (4, 8),
    (5, 5), (5, 8),
    (6, 6), (6, 7), (6, 8),
    (7, 7), (7, 8),
    (8, 8)
]

# Subgroup lattice of the dihedral group D8 (order 8).
# Elements represent subgroups; ordering given by subgroup inclusion.
poset_D8 = [
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
    (2, 8), (3, 8), (4, 9), (5, 9), (6, 10), (7, 10),
    (8, 10), (9, 10)
]

# Chain of size 10.
# Totally ordered set with elements 1 to 10.
poset_chain_10 = [(i, j) for i in range(1, 11) for j in range(i, 11)]

# Boolean lattice of subsets of a 3-element set.
# Elements are numbers 0 to 7 representing subsets; ordered by subset inclusion.
poset_boolean_3 = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
    (1, 1), (1, 3), (1, 5), (1, 7),
    (2, 2), (2, 3), (2, 6), (2, 7),
    (3, 3), (3, 7),
    (4, 4), (4, 5), (4, 6), (4, 7),
    (5, 5), (5, 7),
    (6, 6), (6, 7),
    (7, 7)
]

# Divisibility poset on divisors of 30.
# Ordered by divisibility relation.
poset_div_30 = [
    (1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (1, 10), (1, 15), (1, 30),
    (2, 2), (2, 6), (2, 10), (2, 30),
    (3, 3), (3, 6), (3, 15), (3, 30),
    (5, 5), (5, 10), (5, 15), (5, 30),
    (6, 6), (6, 30),
    (10, 10), (10, 30),
    (15, 15), (15, 30),
    (30, 30)
]


# Divisor lattice of 12.
# Divisors of 12 ordered by divisibility.
poset_div_12 = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 12),
    (2, 2), (2, 4), (2, 6), (2, 12),
    (3, 3), (3, 6), (3, 12),
    (4, 4), (4, 12),
    (6, 6), (6, 12),
    (12, 12)
]

# Poset of partitions of 4 (simplified example).
# Elements represent partitions indexed 1 to 5 ordered by refinement.
poset_partitions_4 = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 2), (2, 4), (2, 5),
    (3, 3), (3, 5),
    (4, 4), (4, 5),
    (5, 5)
]

# Task dependency poset (7 elements).
# Directed acyclic graph representing prerequisites in tasks.
poset_tasks = [
    (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
    (0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)
]


display_hasse_diagram(poset_tasks, title="My Poset", node_color = "lightblue")