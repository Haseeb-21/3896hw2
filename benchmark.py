import random
import statistics
import sys
import time
import urllib.request 

def make_random_int_list(maxint, size):
    '''
    Returns an unsorted list L, with len(L) == size, of integers, with each integer randomly selected from 1 to maxint.

    May be helpful for testing.
    '''
    return list([random.randint(1, maxint) for i in range(size)])


def make_random_word_list(size):
    '''
    Returns an unsorted list L, with len(L) == size, of words, with the words selected from Cicero

    May be helpful for testing.
    '''
    _lorem = '''Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis
    et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia
    voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui
    ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia
    dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora
    incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima
    veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut
    aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui
    in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui
    dolorem eum fugiat quo voluptas nulla pariatur?
    I also -- add ?!?  in some 13.5 stuff that isn't words but +_+ you can still sort it
    '''.split()
    lorem = _lorem * (size // len(_lorem) + 1)
    random.shuffle(lorem)
    return lorem[:size]


def validate_sort(sort_module):
    test_sizes = [10, 100, 1000]
    int_tests = [make_random_int_list(10*i, i) for i in test_sizes]
    word_tests = [make_random_word_list(i) for i in test_sizes]
    test_suite = int_tests + word_tests

    # test_suite = test_suite[:1]

    test_results = [[sort_module.sort(case), sorted(case)] for case in test_suite]
    # print(test_results)
    test_successes = [res[0] == res[1] for res in test_results]
    return {
        'success': len([x for x in test_successes if x]),
        'total': len(test_results),
        'successes': test_successes,
        'details': test_results,
    }


def benchmark_sort(sort_function_dict, iteration_count, data):
    iteration_count = int(iteration_count)
    filenames = list(sort_function_dict.keys())
    times = {fn: [] for fn in filenames}
    pick_order = list(range(len(times))) * iteration_count
    random.shuffle(pick_order)
    for i in range(iteration_count * len(times)):
        random.shuffle(data)
        # print(data[:20])
        filename = filenames[pick_order[i]]
        func = sort_function_dict[filename]
        t0 = time.time()
        func(data)
        t1 = time.time()
        times[filename].append((t1 - t0) * 1000)
    for name, numbers in times.items():
        print('FUNCTION:', name, 'Used', len(numbers), 'times')
        print('\tMEDIAN %0.4f' % (statistics.median(numbers)))
        print('\tMEAN  %0.4f' % (statistics.mean(numbers)))
        print('\tSTDEV %0.4f' % (statistics.stdev(numbers)))
    


def main(sort_file_names, iteration_count=100, data_url="http://www.gutenberg.org/files/98/98-0.txt", array_size_cap=-1):
    from importlib import import_module

    modules = {}
    for sfn in sort_file_names:
        try: 
            if sfn.endswith('.py'):
                sfn = sfn[:-3]        # strip off .py so that the next line works
            student_sort_module = import_module(sfn)

            valid_results = validate_sort(student_sort_module)
            if valid_results['success'] != valid_results['total']:
                print("%s : SORT DID NOT VALIDATE (passed %d of %d tests)" % (sfn, valid_results['success'], valid_results['total']))
                if not valid_results['successes'][0]:
                    print("wat: ", valid_results['details'][0])
            else:
                print("%s : sort validated (passed %d of %d tests)" % (sfn, valid_results['success'], valid_results['total']))
                modules[sfn] = student_sort_module.sort
        except Exception as e:
            print("%s not processed successfully %s" % (sfn, e))
            raise e

    data = urllib.request.urlopen(data_url).read().decode('utf-8').split()[:int(array_size_cap)]
    print("beginning time trials", flush=True)
    benchmark_results = benchmark_sort(modules, iteration_count, data)


if __name__ == "__main__":
    '''

    To just call this on your_code.py, try
       $ python3 benchmark.py your_code.py

    To adjust the number of runs, or the source URL, try
       $ python3 benchmark.py your_code.py 15 http://www.gutenberg.org/cache/epub/7256/pg7256.txt

    To run it on a bunch of methods projects, try
       $ time python3 benchmark.py -- 2 https://www.gutenberg.org/files/98/98-0.txt 25000 < all_sorts.list
    
    '''
    targetfile = sys.argv[1]
    if targetfile == '--':
        multifiles = [line.strip() for line in sys.stdin.readlines()]
        main(multifiles, *sys.argv[2:])
    else:
        main([targetfile], *sys.argv[2:])


