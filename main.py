# Задача №1

def dig_pow(n, p):
    text = str(n)
    total = 0
    for i in range(len(text)):
        digit = int(text[i])
        power = p + i
        total = total + (digit ** power)
    if total % n == 0:
        return total // n
    else:
        return -1
        
print(dig_pow(89, 1)) 
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
print(dig_pow(92, 1)) 
print()

# Задача №2

def get_sum(a,b):
    if a > b:
        a, b = b, a 
        return sum(range(a, b + 1))
print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
print()

# Задача  №3

def binary_array_to_number(arr):
    return int ("".join(str(bit) for bit in arr), 2)

print(binary_array_to_number([0, 0, 0, 1]))  
print(binary_array_to_number([0, 0, 1, 0]))  
print(binary_array_to_number([0, 1, 0, 1]))  
print(binary_array_to_number([1, 0, 0, 1]))  
print()

# Задача №4

def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    
    if h < 10:
        h_str = "0" + str(h)
    else:
        h_str = str(h)
        
    if m < 10:
        m_str = "0" + str(m)
    else:
        m_str = str(m)
        
    if s < 10:
        s_str = "0" + str(s)
    else:
        s_str = str(s)
        
    return h_str + ":" + m_str + ":" + s_str
print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
print()

# Задача №5

def valid_braces(string):
    stack = []
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if len(stack) == 0:
                return False
            last = stack.pop()
            if last != brackets[char]:
                return False
                
    if len(stack) == 0:
        return True
    else:
        return False
print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("(}"))
print(valid_braces("[(])"))
print(valid_braces("[({})](]"))
print()

# Задача №6

def product_fib(prod):
    a = 0
    b = 1 
    while a * b < prod:
        next_val = a + b 
        a = b 
        b = next_val
    return [a, b, a * b == prod]
print(product_fib(714))
print(product_fib(800))
print()

# Задача #7

def delete_nth(order,max_e):
    result = []
    counts = {}
    
    for num in order:
        if num not in counts:
            counts[num] = 0
            
        if counts[num] < max_e:
            result.append(num)
            counts[num] = counts[num] + 1
            
    return result
print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
print(delete_nth([20, 37, 20, 21], 1))
print()

# Задача №8 

def find_nb(m):
    total = 0
    n = 0
    while total < m:
        n = n + 1
        total = total + n ** 3
    if total == m:
        return n
    else:
        return -1
print(find_nb(1071225))
print(find_nb(91716553919377))
print()

# Задача №9

def domain_name(url):
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    return url.split(".")[0]     
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print()

# Задача №10

def move_zeros(lst):
    result = []
    zeros_count = 0
    
    for item in lst:
        if item == 0 and type(item) is not bool:
            zeros_count = zeros_count + 1
        else:
            result.append(item)
            
    for i in range(zeros_count):
        result.append(0)
        
    return result
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3]))
print()

# Задача №11

def get_pins(observed):
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    if len(observed) == 0:
        return []
        
    result = ['']
    for digit in observed:
        current_variants = adjacent[digit]
        next_result = []
        for prefix in result:
            for char in current_variants:
                next_result.append(prefix + char)
        result = next_result
        
    return result
print(get_pins('8'))
print(get_pins('11'))
print(get_pins('369'))
print()

# Задача №12

import re

def validate_password(password):
    if len(password) < 6:
        return False
        
    has_lower = False
    has_upper = False
    has_digit = False
    
    for char in password:
        if not char.isalnum():
            return False
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
            
    if has_lower and has_upper and has_digit:
        return True
    else:
        return False


regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z0-9]{6,}$"
test_password = "Password123"
print(validate_password.__name__, test_password, validate_password(test_password))
print()

# Задача #13

def dirReduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    
    stack = []
    
    for direction in arr:
        if stack and stack[-1] == opposites.get(direction):
            stack.pop()
        else:
            stack.append(direction)
            
    return stack
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]))
print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))

# Задача №14

def pick_peaks(arr):
    pos = []
    peaks = []
    
    if not arr:
        return {"pos": pos, "peaks": peaks}
    
    potential_pos = -1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            potential_pos = i
        elif arr[i] < arr[i - 1]:
            if potential_pos != -1:
                pos.append(potential_pos)
                peaks.append(arr[potential_pos])
                potential_pos = -1
                
    return {"pos": pos, "peaks": peaks}
print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
print(pick_peaks([1, 2, 2, 2, 1]))
print(pick_peaks([1, 2, 2, 2, 3]))
print() 

# Задача №15

def loop_size(node):
    slow = node
    fast = node
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
            
    current = slow.next
    count = 1
    while current != slow:
        count += 1
        current = current.next
        
    return count
print(loop_size.__name__, loop_size)
print()

# Задача №16

def first_non_repeating_letter(s):
    from collections import Counter
    
    counts = Counter(s.lower())
    
    for char in s:
        if counts[char.lower()] == 1:
            return char
            
    return ""
print(first_non_repeating_letter.__name__, "stress", first_non_repeating_letter("stress"))
print(first_non_repeating_letter.__name__, "sTreSS", first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter.__name__, "@#@@*", first_non_repeating_letter("@#@@*"))
print(first_non_repeating_letter.__name__, "かか何", first_non_repeating_letter("かか何"))
print(first_non_repeating_letter.__name__, "🐐🦊🐐", first_non_repeating_letter("🐐🦊🐐"))
print()

# Задача №17

def int32_to_ip(int32):
    return ".".join(str((int32 >> (24 - i * 8)) & 255) for i in range(4))
print(int32_to_ip.__name__, 2149583361, int32_to_ip(2149583361))
print(int32_to_ip.__name__, 32, int32_to_ip(32))
print(int32_to_ip.__name__, 0, int32_to_ip(0))
print()

#  Задача №18

def zeros(n):
    count = 0
    while n >= 5:
        count += n // 5
        n //= 5
    return count
print(zeros.__name__, 1000, zeros(1000))
print(zeros.__name__, 5, zeros(5))
print(zeros.__name__, 10, zeros(10))
print()

# Задача №19

def solve_puzzle (clues):
    from itertools import permutations

    perms = list(permutations([1, 2, 3, 4]))

    def count_visible(line):
        visible = 0
        max_h = 0
        for h in line:
            if h > max_h:
                visible += 1
                max_h = h
        return visible

    def check(grid):
        for c in range(4):
            col = [grid[r][c] for r in range(4)]
            if clues[c] != 0 and count_visible(col) != clues[c]:
                return False
            if clues[11 - c] != 0 and count_visible(col[::-1]) != clues[11 - c]:
                return False

        for r in range(4):
            row = grid[r]
            if clues[15 - r] != 0 and count_visible(row) != clues[15 - r]:
                return False
            if clues[4 + r] != 0 and count_visible(row[::-1]) != clues[4 + r]:
                return False

        return True

    def solve(r=0, grid=[]):
        if r == 4:
            return tuple(grid) if check(grid) else None

        for p in perms:
            valid = True
            for c in range(4):
                col = [grid[row][c] for row in range(r)] + [p[c]]
                if len(set(col)) != len(col):
                    valid = False
                    break
            if not valid:
                continue

            res = solve(r + 1, grid + [p])
            if res:
                return res
        return None

    return solve()
print(solve_puzzle.__name__, solve_puzzle([
    0, 0, 1, 2,
    0, 0, 0, 2,
    0, 3, 0, 0,
    0, 1, 0, 0
]))
print()

# Задача №20

def solution(args):
    result = []
    i = 0
    n = len(args)
    
    while i < n:
        start = i
        while i + 1 < n and args[i + 1] == args[i] + 1:
            i += 1
            
        length = i - start + 1
        if length >= 3:
            result.append(f"{args[start]}-{args[i]}")
        elif length == 2:
            result.append(str(args[start]))
            result.append(str(args[i]))
        else:
            result.append(str(args[start]))
            
        i += 1
        
    return ",".join(result)
print(solution.__name__, solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print()

# Задача №21

def balanced_parens(n):
    if n == 0:
        return [""]
    
    result = []
    
    def generate(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
            
        if open_count < n:
            generate(current + "(", open_count + 1, close_count)
            
        if close_count < open_count:
            generate(current + ")", open_count, close_count + 1)
            
    generate("", 0, 0)
    return result

func_name = balanced_parens.__name__
print("balanced_parens(0) -> " + str(balanced_parens(0)))
print("balanced_parens(1) -> " + str(balanced_parens(1)))
print("balanced_parens(2) -> " + str(balanced_parens(2)))
print("balanced_parens(3) -> " + str(balanced_parens(3)))
print()

# Задача №22

def sudoku(puzzle):
    def is_valid(board, row, col, num):
        if num in board[row]:
            return False
            
        for r in range(9):
            if board[r][col] == num:
                return False
                
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(3):
            for c in range(3):
                if board[start_row + r][start_col + c] == num:
                    return False
                    
        return True

    def solve(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            
                            if solve(board):
                                return True
                                
                            board[r][c] = 0
                    return False
        return True

    solve(puzzle)
    return puzzle
    print("sudoku: " + sudoku.__name__)
print("-" * 40)

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = sudoku(puzzle)
for row in solved:
    print(str(row))
print()

#  Задача №23

def exp_sum(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
            
    return dp[n]
print("exp_sum(1) -> " + str(exp_sum(1)))
print("exp_sum(2) -> " + str(exp_sum(2)))
print("exp_sum(3) -> " + str(exp_sum(3)))
print("exp_sum(4) -> " + str(exp_sum(4)))
print("exp_sum(5) -> " + str(exp_sum(5)))
print("exp_sum(10) -> " + str(exp_sum(10)))
print()

# Задача №24

def path_finder(maze):
    grid = [list(row) for row in maze.split('\n')]
    n = len(grid)
    
    if grid[0][0] == 'W' or grid[n-1][n-1] == 'W':
        return False
        
    visited = [[False] * n for _ in range(n)]
    queue = [(0, 0)]
    visited[0][0] = True
    
    while queue:
        r, c = queue.pop(0)
        
        if r == n - 1 and c == n - 1:
            return True
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 'W':
                visited[nr][nc] = True
                queue.append((nr, nc))
                
    return False
print("path_finder: " + path_finder.__name__)
print("-" * 40)

maze = ".W.\n.W.\n..."
print("path_finder(maze) -> " + str(path_finder(maze)))
print()


# Задача №25

def closest_pair(points):
    import math
    
    def dist(p1, p2):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])
        
    def closest_util(px, py):
        n = len(px)
        if n <= 3:
            min_d = float('inf')
            best_pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    d = dist(px[i], px[j])
                    if d < min_d:
                        min_d = d
                        best_pair = [px[i], px[j]]
            return min_d, best_pair
            
        mid = n // 2
        mid_point = px[mid]
        
        pyl = [p for p in py if p[0] < mid_point[0] or (p[0] == mid_point[0] and p[1] <= mid_point[1])]
        pyr = [p for p in py if p not in pyl]
        
        dl, pair_l = closest_util(px[:mid], pyl)
        dr, pair_r = closest_util(px[mid:], pyr)
        
        if dl < dr:
            d = dl
            best_pair = pair_l
        else:
            d = dr
            best_pair = pair_r
            
        strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
        
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= d:
                    break
                dt = dist(strip[i], strip[j])
                if dt < d:
                    d = dt
                    best_pair = [strip[i], strip[j]]
                    
        return d, best_pair

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    _, result = closest_util(px, py)
    return result
print("closest_pair: " + closest_pair.__name__)
print("-" * 40)

points = (
    (2, 2),
    (2, 8),
    (5, 5),
    (6, 3),
    (6, 7),
    (7, 4),
    (7, 9)
)

print("closest_pair(points) -> " + str(closest_pair(points)))
print()