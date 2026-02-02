if __name__ == "__main__":
    n = int(input())
    integers = map(int, input().split())
    t = tuple(integers)
    print(hash(t))
