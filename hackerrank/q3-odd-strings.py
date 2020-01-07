import random
from textwrap import wrap
#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. INTEGER m
# 2. STRING_ARRAY s
#
def genRandString(string_length):
    long_test_string = ""
    for i in range(string_length):
       a = ord('a')
       z = ord('z')
       long_test_string+= chr(random.randint(a,z))
    return long_test_string.split(chr(random.randint(a,z)))

def solveOld(m, s):
# we can ignore m because an odd to any power is odd
# and an even to any power is even
    allOdd = True
    for a in s:
        wordOdd = True
        for c in a:
            wordOdd*= ord(c) % 2 # store the parity of the char
        allOdd = (allOdd + wordOdd) % 2
    isEven = not allOdd
    return "EVEN" if not isEven else "ODD"

def solveNew(m, s):
    """
    given without proof:
    we can ignore m because an odd to any power is odd (1)
    and an even to any power is even (2)
    """
    sumEven = True # the empty sum, 0, is even
    for a in s:
        wordOdd = True # the empty product is 1, which is odd
        for c in a:
            """
            mod 2 stores the parity of the char
            `&=` the word has odd product only if there are no evens
            evens are zero, so anding with that will permanently set
            the wordOdd bit to false, as desired
            """
            wordOdd &= ord(c) % 2
        """
        every time a word has an odd sum, it flips the sumEven bit,
        which is desired because it keeps the information about the
        parity of the sum: Let 1 be odd and 0 even
        (1^1) → (0) === (1+1) → (0)
        (0^0) → (0) === (0+0) → (0)
        (1^0) → (1) === (1+0) → (1)
        (0^1) → (1) === (0+1) → (1)
        """
        sumEven = (sumEven ^ wordOdd)
    return "EVEN" if sumEven else "ODD"
def runShortTests(tests):
    print("begin short tests")
    print("=================")
    for s in tests:
        m = random.randint(1,100000)
        print(s, solveOld(m,s) , solveNew(m,s), sep="\t")

def runRandomLongTests():
    print("begin long tests")
    print("=================")
    string_length = int(1e3)
    m=0

    for i in range(10):
        long_test_s_vector = genRandString(string_length)
        print("\n".join(wrap(str(long_test_s_vector), 70)),
            solveOld(m,long_test_s_vector),
            solveNew(m,long_test_s_vector),
            sep="\n")

def main():
    tests = [
        ['abc', 'abcd'],
        ['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh'],
        ['azbde', 'abcher', 'acegk'],
        ['austin', 'dallas', 'houston'],
        ['lorem', 'ipsum', 'dolor']
    ]

    runShortTests(tests)
    runRandomLongTests()


if __name__ == "__main__":
    main()

print()
main()
