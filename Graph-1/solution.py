# Python 2.7.10

import sys 
# collections module optimizes queues
import collections


USAGE = """Usage: {script} sitemap_file *args
    sitemap_file: .txt file containing known page links.
    *args: any number of page names to check links for
""".format(script=sys.argv[0])

def parse(path):
    """parse(str) -> dict

    Given a path to a sitemap file, parses links from the file.
    Returns dictionary of start pages and associated linked pages.
    """
    with file(path) as f:
        lines = [line.rstrip().split(' ') for line in f.readlines()]
    # TODO: assert words[1] == '->' for each line in lines!
    return {words[0]: words[2:] for words in lines}

def query(d, pages):
    """query(dict, list) -> list

    Queries known sitemap with list of page names. 
    Returns list of strings of all links reachabe from given starting pages.
    """
    out     =   []
    que     =   collections.deque(pages)
    # breadth-first search
    while len(que) > 0:
        node = que.popleft()
        if d.has_key(node):
            que.extend(filter(lambda x: x not in que and x not in out, d.get(node)))
        out.append(node)
    return out[len(pages):]
 

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print USAGE
        sys.exit()
    pages = query(parse('sample_input.txt'), sys.argv[2:])
    if len(dependencies) == 0:  print 'unknown'
    else:                       print pages

# NOTE: Alternatively, use `networkx`
