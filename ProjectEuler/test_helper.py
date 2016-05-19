# TODO: refactor module importing
import problem_1 as p

for i, s in enumerate(p.SOLUTIONS):
    print('solution_%s' % i)
    for name, params in p.TEST_CASES.items():
        answer = s(**params['kwargs'])
        if answer == params['answer']:  status = 'pass'
        else:                           status = 'fail' 

        print(name, '\t\t%s' % status, 'actual: %s \n expected: %s' % (answer, params['answer']))


# for m in MODULES:
#     for s in m.SOLUTIONS:
#         for case, arguments in m.CORRECT_SOLUTIONS:
#             # check if solutions correct
#             kwargs = m.format_inputs( arguments['inputs'] )
#             # TODO assert equal here v['answer'] s(**kwargs)
#             # TODO: count h`ere

# NOTES:
# count correct solutions (per problem individually)
# change text colour of output
# notify of incorrect solutions (how?)
# TODO: detect if no solutions have been attmpted for a problem

# SAMPLE OUTPUT:

#   # Problem 1
#       # solution_1
#           # contorl:  pass
#           # actual:   fail    output: X expected: Y
#       # solution_2
#           # contorl:  pass
#           # actual:   pass

#   # Problem 2
#       # solution_1
#           # contorl:  fail    output: X expected: Y
#           # actual:   fail    output: X expected: Y

# You have 1 correct csolution to 2 problems


# for problem_file in project_directory:
#     print('#', problem_file.name)
#     for solution  in problem_file:
#         print('\t #', solution_name)
#         for test_case in test_cases:
#             if it_passed: print( test_case.name + ':\t pass')   # in green
#             else: print(test_case.name + ':\t fail')            # in red

    
