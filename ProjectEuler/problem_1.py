CHALLENGE = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

CORRECT_SOLUTIONS = {
        'control':  { 'inputs': (5, 3, 10),     'answer': 23 },
        'actual':   { 'inpits'; (5, 3, 1000),   'answer': 233168 },
}

# Date 18/04/2016
def solution_1(upper_limit, factors*):
    """Find the sum of all the multiples of 3 or 5 below 1000."""
    multiples = set()
    for i in (3, 5):
        for j in range(1, ((1000 - 1) // i) + 1):
            multiples.add(i * j)
    print(sum(multiples))

# Date 18/04/2016
def solution2():
    def arithmetic_sum(first_term, max_value):
        n           = ((max_value) % first_term)
        last_term   = first_term * n
        return n // 2 * (first_term + last_term)
    max_value       = (1000 - 1)
    print(  arithmetic_sum(3,   max_value=max_value)
    +       arithmetic_sum(5,   max_value=max_value)
    -       arithmetic_sum(15,  max_value=max_value)
    )
    

SOLUTIONS = (
    solution_1,
    solution_2
)
