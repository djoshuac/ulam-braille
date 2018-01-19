
def triangle(n):
    return n * (n + 1) // 2

def diagonal_iteration(width):
    row = [triangle(i + 1) for i in range(width)]
    yield row

def rotate(grid):
    rotated = []

if __name__ == "__main__":
    print(list(diagonal_iteration(5)))
