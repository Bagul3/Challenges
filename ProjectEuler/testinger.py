import problem_1

PROBLEMS = [problem_1, problem_1, problem_1]

def check_solution(solution, kwargs, answer):
    """Return's True if solution's answer is correct."""
    s = solution(**kwargs)
    return s.answer() == answer

def evaluate_problem(problem):
    """Evaluates whether or not the problem has been solved, or is pending."""
    pass
    

def main():
    for problem in PROBLEMS:
        print(problem.__name__)
    
        for solution in problem.SOLUTIONS:
            print('\t', solution.__name__, end=": ")
    
            status = all(check_solution(solution, **params) for name, params in problem.TEST_CASES.items())
            print('correct' if status else 'incorrect')
    
            # ALTERNATIVE: 
            # for name, params in problem.TEST_CASES.items():
            #     print('\t' * 2, name, end=': ')
            #     print(check_solution(solution, **params))

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------

# import os
# import fnmatch

# NOTE: for some reason works incorrectly; * matches 1 or more occurences here
#       while + doesn't work
# PROBLEM_FILE_PATTERN    = r'problem_[0-9]*.py'
# SOLUTION_CLASS_PATTERN  = 'Solution_[0-9]*'

# for f in os.listdir('.'):
#     if fnmatch.fnmatchcase(f, PROBLEM_FILE_PATTERN):
#         print(f[:-3])
