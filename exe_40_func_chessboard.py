def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def chessboard(n=8):
    i = 1
    while i <= n:
        if is_even(i):
            print('# ' * int(n / 2))
        else:
            print(' #' * int(n / 2))
        i += 1

chessboard()
