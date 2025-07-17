"""
A gene string can be represented by an 8-character long string, with choices from 
'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene 
string endGene where one mutation is defined as one single character changed in 
the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene 
must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return 
the minimum number of mutations needed to mutate from startGene to endGene. If 
there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included 
in the bank.

Constraints:
- 0 <= bank.length <= 10
- startGene.length == endGene.length == 8
- startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Explanation: One mutation to change endGene[7] from 'T' to 'A'.

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Explanation: One mutation to change startGene[2] from 'C' to 'A' and one 
mutation to change startGene[6] from 'T' to 'A'.

Example 3:
Input: startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
Explanation: One mutation to change startGene[4] from 'A' to 'C', one mutation 
to change startGene[5] from 'A' to 'C', and one mutation to change startGene[6] 
from 'A' to 'C'.
"""

from typing import List, Set
from collections import deque

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    """
    Find the minimum number of mutations needed to transform startGene to endGene.
    
    Intuition:
    Start = 2:22PM
    End = 2:35PM

    1. create a get_neighbors function that handles the permutation logic
    2. create a BFS (we are about shortest amount of steps)
    3. return steps if start == end
    4. otherwise, for every neighbor, mark as visited and append queue.
    """
    valid_genes = set(bank)
    if endGene not in valid_genes:
        return -1
    def get_neighbors(gene):
        for i, ch in enumerate(gene):
            for nucleotide in ["A", "C", "G", "T"]:
                if nucleotide == ch:
                    continue
                new_gene = gene[:i] + nucleotide + gene[i+1:]
                if new_gene in valid_genes:
                    yield new_gene
    
    seen = set()
    queue = deque([(startGene, 0)])
    seen.add(startGene)

    while queue:
        curr_gene, steps = queue.popleft()
        if curr_gene == endGene:
            return steps
        
        for neighbor_mutation in get_neighbors(curr_gene):
            if neighbor_mutation not in seen:
                seen.add(neighbor_mutation)
                queue.append((neighbor_mutation, steps + 1))
        
    return -1  # Placeholder return for template

if __name__ == "__main__":
    # Define test cases as tuples: (name, startGene, endGene, bank, expected)
    test_cases = [
        ("Example 1", "AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("Example 2", "AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
        ("Example 3", "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3),
        ("Same gene", "AACCGGTT", "AACCGGTT", ["AACCGGTT"], 0),
        ("No path", "AACCGGTT", "AACCGGTA", [], -1),
        ("Empty bank", "AACCGGTT", "AACCGGTA", [], -1),
        ("Single mutation", "AAAAACCC", "AAAACCCC", ["AAAACCCC"], 1),
        ("Multiple steps", "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3),
        ("Direct path", "AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("Indirect path", "AACCGGTT", "AACCGGTA", ["AACCGCTA", "AACCGGTA"], 1),
        ("Long path", "AAAAAAAA", "CCCCCCCC", ["AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AAACCCCC","AACCCCCC","ACCCCCCC","CCCCCCCC"], 8),
        ("No valid mutations", "AACCGGTT", "AACCGGTA", ["AACCGCTA"], -1),
        ("Start not in bank", "AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("End not in bank", "AACCGGTT", "AACCGGTA", ["AACCGGTT"], -1),
        ("Circular path", "AACCGGTT", "AACCGGTT", ["AACCGCTA", "AACCGGTA", "AACCGGTT"], 0),
        ("Multiple valid paths", "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC","AACCCCCG"], 3),
        ("One character difference", "AACCGGTT", "AACCGGTC", ["AACCGGTC"], 1),
        ("All characters different", "AAAAAAAA", "CCCCCCCC", ["CCCCCCCC"], -1),
        ("Partial bank", "AACCGGTT", "AACCGGTA", ["AACCGGTA","AACCGCTA"], 1),
        ("Complex path", "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC","AACCCCCG","AACCCCCG"], 3),
    ]
    
    # Track test results
    test_results = []
    
    # Run all test cases
    for i, (name, startGene, endGene, bank, expected) in enumerate(test_cases, 1):
        result = minMutation(startGene, endGene, bank)
        passed = result == expected
        test_results.append((f"Test {i}: {name}", passed))
        
        print(f"Test {i}: {name}")
        print(f"Start Gene: {startGene}")
        print(f"End Gene: {endGene}")
        print(f"Bank: {bank}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Pass: {passed}")
        print()
    
    # Summary of test results
    passed_tests = [test_name for test_name, passed in test_results if passed]
    failed_tests = [test_name for test_name, passed in test_results if not passed]
    
    print("=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    if failed_tests:
        print(f"❌ {len(failed_tests)} test(s) failed:")
        for test_name in failed_tests:
            print(f"   - {test_name}")
        print(f"✅ {len(passed_tests)} test(s) passed")
    else:
        print(f"✅ All {len(passed_tests)} tests passed!")
    print("=" * 50) 