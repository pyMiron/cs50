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
    res_dict = {}
    for i in corpus:
        res_dict[i] = 0
    if len(corpus[page]) == 0:
        for i in corpus:
            res_dict[i] = 1/len(corpus)
    else:
        prob = damping_factor / len(corpus[page])
        for i in corpus:
            res_dict[i] += (1 - damping_factor)/len(corpus)
            if i in corpus[page]:
                res_dict[i] += prob
    return res_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    lst = []
    lst_links = list(corpus.keys())

    start_page = lst_links[random.randrange(len(lst_links))]
    lst.append(start_page)
    res_dict = transition_model(corpus, start_page, damping_factor)
    for _ in range(n):
        links_from_page = list(corpus.get(start_page))
        proba = random.randint(1, 100)
        if proba / 100 <= damping_factor and len(links_from_page) > 0:
            start_page = links_from_page[random.randrange(len(links_from_page))]
        elif proba / 100 > damping_factor or len(links_from_page) == 0:
            start_page = lst_links[random.randrange(len(lst_links))]
        lst.append(start_page)
    for i in corpus:
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
    start_prob = 1 / len(corpus)
    for el in corpus:
        res_dict[el] = start_prob

    def linked_pages(page):
        lst = []
        for links in corpus:
            if page in corpus[links] or len(corpus[links]) == 0:
                lst.append(links)
        return lst

    max_diff = 1
    while max_diff > 0.001:
        cur_diff = 0
        for el in corpus:
            res = 0
            for i in linked_pages(el):
                numlinks = len(corpus[i])
                if numlinks == 0:
                    numlinks = len(corpus)
                res += (res_dict[i] / numlinks)*damping_factor
            res += (1 - damping_factor) / len(corpus)
            cur_diff = max(cur_diff, res_dict[el]-res)
            res_dict[el] = res
        max_diff = min(cur_diff, max_diff)
    return res_dict


if __name__ == "__main__":

    main()
