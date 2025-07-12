class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            num, count = self.stack.pop()
            counter += count
        self.stack.append((price, counter))
        return counter

if __name__ == "__main__":
    # Test case from the problem
    stockSpanner = StockSpanner()
    
    # Test the sequence of prices
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    
    print("Testing StockSpanner:")
    print("Prices:", prices)
    print("Expected:", expected)
    print("Actual:  ", end="")
    
    results = []
    for price in prices:
        result = stockSpanner.next(price)
        results.append(result)
        print(f"{result}", end=" ")
    
    print()
    print("Test passed!" if results == expected else "Test failed!")
    print(f"Results: {results}")
    