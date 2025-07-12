from collections import Counter, deque


def predictPartyVictory(senate: str) -> str:
    """
    In each round, every senator can exercise one of the two rights:
    1. Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
    2. Announce the victory: If this senator found the senator who still has rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
    
    The voting procedure is given in the form of a string senate. Each character is either 'R' (Radiant) or 'D' (Dire).
    """
    # TODO: Implement solution
    # Hint: Consider using queues to track senators from each party
    # Think about the order of operations when senators ban each other
    
    return ""


if __name__ == "__main__":
    test_cases = {
        "RD": "Radiant",
        "RDD": "Dire",
        "DDRRR": "Dire",
        "DRRD": "Dire",
        "DRRDRDRDRDDRDRDR": "Radiant"
    }
    
    for senate, expected in test_cases.items():
        result = predictPartyVictory(senate)
        print(f"Senate: {senate} -> Expected: {expected}, Got: {result}")
        # assert(result == expected)  # Uncomment when solution is implemented 

    