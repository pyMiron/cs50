import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    print(corpus)
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = 0
    res_dict = {}
    lst = []
    rand_set = corpus.keys()
    rand_set = list(rand_set)
    start_dir = corpus.get(page)
    start_page = start_dir[random.randrange(len(start_dir))]
    lst.append(start_page)
    while N < SAMPLES:
        new_dir = corpus[start_page]
        proba = random.randint(1, 100)
        if start_page == None:
            start_page = rand_set[random.randrange(len(rand_set))]
        if proba / 100 <= damping_factor:
            start_page = new_dir[random.randrange(len(new_dir))]
        elif proba / 100 > damping_factor:
            start_page = rand_set[random.randrange(len(rand_set))]
        lst.append(start_page)
        N += 1
    for i in rand_set:
        fin_prob = lst.count(i)/len(lst)
        res_dict[i] = fin_prob

    return res_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    res_dict = {}
    lst = []
    N = 0
    rand_set = corpus.keys()
    rand_set = list(rand_set)

    start_page = rand_set[random.randrange(len(rand_set))]
    lst.append(start_page)
    while n > N:
        new_dir = corpus.get(start_page)
        new_dir = list(new_dir)
        proba = random.randint(1, 100)
        if proba / 100 <= damping_factor and len(new_dir) > 0:
            start_page = new_dir[random.randrange(len(new_dir))]
        elif proba / 100 > damping_factor or len(new_dir) == 0:
            start_page = rand_set[random.randrange(len(rand_set))]
        lst.append(start_page)
        N += 1
    for i in rand_set:
        fin_prob = lst.count(i) / len(lst)
        res_dict[i] = fin_prob
    print(res_dict)
    return res_dict





def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    res_dict = {}
    rand_set = corpus.keys()
    rand_set = list(rand_set)
    start_prob = 1 / len(rand_set)
    for el in rand_set:
        res_dict[el] = start_prob


    def pages(page):
        lst = []
        for i in rand_set:
            if page in corpus[i] or len(corpus[i]) == 0:
                lst.append(i)
        return lst


    max_diff = 1
    while max_diff > 0.001:
        cur_diff = 0
        for el in rand_set:
            res = 0
            for i in pages(el):
                numlinks = len(corpus[i])
                if numlinks == 0:
                    numlinks = len(rand_set)
                res += (res_dict[i] / numlinks)*damping_factor
            res += (1 - damping_factor) / len(rand_set)
            if res_dict[el]-res > cur_diff:
                cur_diff = res_dict[el]-res
            res_dict[el] = res
        max_diff = min(cur_diff, max_diff)
    return res_dict
if __name__ == "__main__":
    main()
