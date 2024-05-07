import os
import nltk


def create_cell(first, second):
    """
    creates set of string from concatenation of each character in first
    to each character in second
    :param first: first set of characters
    :param second: second set of characters
    :return: set of desired values
    """
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f + s)
    return res


def read_grammar(filename):
    """
    reads the rules of a context free grammar from a text file
    :param filename: name of the text file in current directory
    :return: two lists. v_rules lead to variables and t_rules
    lead to terminals.
    """
    filename = os.path.join(os.curdir, filename)
    with open(filename) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []

        for rule in rules:
            left, right = rule.split(" -> ")  # Det -> a returns left = Det & right = a

            # for two or more results from a variable
            """
            * Tendency to result right = '' 
            Solution: add single whitespace after the last word of a sentence
            ex: agawed kax where x is white space
            """
            right = right[:-1].split(" | ")  #
            for ri in right:

                # it is a terminal
                if str.islower(ri):
                    t_rules.append([left, ri])

                # it is a non-terminal
                else:
                    v_rules.append([left, ri])
        return v_rules, t_rules


def read_input(filename):
    """
    reads the inputs from a text file
    :param filename: name of the text file in current directory
    :return: list of inputs
    """
    filename = os.path.join(os.curdir, filename)
    res = []
    with open(filename) as inp:
        inputs = inp.readlines()
        for i in inputs:
            res.append(i)
    return res


def cyk_alg(varies, terms, inp):
    """
    implementation of CYK algorithm
    :param varies: rules related to variables
    :param terms: rules related to terminals
    :param inp: input string
    :return: resulting table
    """
    length = len(inp)
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]

    # table on which we run the algorithm
    table = [[set() for _ in range(length - i)] for i in range(length)]

    # Deal with variables
    for i in range(length):
        for te in terms:
            if inp[i] == te[1]:
                table[0][i].add(te[0])

    # Deal with terminals
    # its complexity is O(|G|*n^3)
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = create_cell(table[k][j], table[i - k - 1][j + k + 1])
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])

    """
    if the last element of table contains the highest level structure (i.e., not set()) 
    of the input belongs to the grammar
    """
    return table


def show_result(tab, inp):
    """
    this function prints the procedure of cyk.
    in the end there is a message showing if the input
    belongs to the grammar
    :param tab: table
    :param inp: input
    :return: None
    """
    for c in inp:
        print("\t{}".format(c), end="\t")
    print()
    for i in range(len(inp)):
        print(i + 1, end="")
        for c in tab[i]:
            if c == set():
                print("\t{}".format("_"), end="\t")
            else:
                print("\t{}".format(c), end=" ")
        print()

    if tab[len(inp) - 1][0] != set():
        print("The input belongs to this context free grammar!")
    else:
        print("The input does not belong to this context free grammar!")


def ilocano_to_english_translator(x):
    ilocano_english_mapping = {
        'agawid ka': "you are going home",
        'agawid ka jay balayen': "go home to the house"
    }
    for i in range(0, len(x)):
        y = ilocano_english_mapping.get(x[i].strip())
        print(y)


if __name__ == '__main__':
    ilocano_cfg_file_path = "ilocano_cfg.txt"
    ilocano_imperative_file_path = "ilocano_imperative.txt"
    v, t = read_grammar(ilocano_cfg_file_path)
    ilocano_sentence = read_input(ilocano_imperative_file_path)
    for i in range(0, len(ilocano_sentence)):
        ilocano_tokens = nltk.word_tokenize(ilocano_sentence[i])
        ta = cyk_alg(v, t, ilocano_tokens)
        show_result(ta, ilocano_tokens)
        print()

    print()

    english_cfg_file_path = "english_cfg.txt"
    english_imperative_file_path = "english_imperative.txt"
    v, t = read_grammar(english_cfg_file_path)
    english_sentence = read_input(english_imperative_file_path)
    for i in range(0, len(english_sentence)):
        english_tokens = nltk.word_tokenize(english_sentence[i])
        ta = cyk_alg(v, t, english_tokens)
        show_result(ta, english_tokens)
        print()

    ilocano_to_english_translator(ilocano_sentence)
