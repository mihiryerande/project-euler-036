# Problem 36:
#     Double-Base Palindromes
#
# Description:
#     The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#
#     Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#     (Please note that the palindromic number, in either base, may not include leading zeros.)

def main(n):
    """
    Returns a list of all numbers less than `n` which are palindromes in base-10 and base-2,
      as well as the sum of those numbers.

    Args:
        n (int): Natural number

    Returns:
        (Tuple[List[int], int]):
            Tuple of ...
              * List of all palindromes in base-10 and base-2, less `n`
              * Sum of those numbers

    Raises:
         AssertError: if incorrect args are given
    """
    palindromes = []
    total = 0
    for x in range(1, n):
        s10 = str(x)
        s2 = bin(x)[2:]
        if s10[::-1] == s10 and s2[::-1] == s2:
            palindromes.append(x)
            total += x
    return palindromes, total


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    double_base_palindromes, palindromes_sum = main(num)
    print('Palindromes in base-10 and base-2:')
    print('  Base-10      Base-2')
    for double_base_palindrome in double_base_palindromes:
        print('  {:<10d} = {:<}'.format(double_base_palindrome, bin(double_base_palindrome)[2:]))
    print('Sum of those:')
    print('  {}'.format(palindromes_sum))
