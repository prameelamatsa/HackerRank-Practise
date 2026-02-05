def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase
    
    # width of the rangoli
    width = 4 * size - 3
    
    lines = []
    
    for i in range(size):
        # descending part + ascending part
        left = alpha[size-1 : size-1-i : -1]
        right = alpha[size-1-i : size]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))
    
    # upper + lower (mirror)
    print("\n".join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
