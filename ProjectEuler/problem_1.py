CHALLENGE = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

TEST_CASES = {
    'control': {
        'kwargs': { 'factors': (3, 5), 'upper_boundary': 10 },
        'answer':23
    },
    'actual': { 
        'kwargs': {'factors': (3, 5), 'upper_boundary': 1000 },
        'answer': 233168
    }
}

# ----------------------------------------------------------------------

# Date 2016-05-24
class Solution1(object):
    """Find the the sum of all values that are multiples of the two factors below 
    an upper limit for natural numbers."""

    def __init__(self, factors, upper_boundary):
        self.factors        = factors
        self.upper_limit    = upper_boundary - 1
        self.date           = '2016-05-27'              # NOTE: date of completion
    
    def __arithmetic_sum(self, first_term, no_of_terms):
        """Calculate and return sum or arithmetic sequence."""
        # TODO: assert that natural numbers are supplied
        # TODO: assert that upper boundary is greater than each factor
        # TODO: answer should be integer! how to track?
        summation = no_of_terms * first_term * (1 + no_of_terms) // 2    
        return summation

    def answer(self):
        """Return the answer."""         
        # NOTE; unsure how to doc string this; it makes sense in context
        # TODO: refactor to generalise for more than 2 factors

        # combine arithmetics sums of factors
        factor_summations   = sum(self.__arithmetic_sum(f, self.upper_limit // f)
                for f in self.factors)
        # compensate for repeated values
        union               = self.factors[0] * self.factors[1]
        union_summations    = self.__arithmetic_sum(union, self.upper_limit // union)
        answer              = factor_summations - union_summations

        # TODO: answers is always >= 0, test
        return answer


SOLUTIONS = [Solution1]
