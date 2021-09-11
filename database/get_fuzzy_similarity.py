# https://towardsdatascience.com/build-a-keyword-extraction-api-with-spacy-flask-and-fuzzywuzzy-4909d7ffc105
# https://gist.github.com/cdpierse/a0ca013fe037b04423e554ffc940cea6

from fuzzywuzzy import process
from fuzzywuzzy.fuzz import ratio


def get_fuzzy_similarity(token=None, dictionary=None):
    """
    Returns similar words and similarity scores for a given token
    from a provided dictionary of words

    :param token : {str} the referenced word (default: {None})
    :param dictionary : {list} the list of target words
    :return: {list} a list of tuples in the form (matched_word, similarity score)
    """

    if token and dictionary:
        return process.extractBests(token, dictionary, scorer=ratio, score_cutoff=70)
    else:
        return []


if __name__ == "__main__":
    # test dictionary
    word_dictionary = ['medium', 'twitter', 'google', 'linkedIn', 'facebook']

    # results from fuzzy match search
    print(get_fuzzy_similarity('FaceBoo', word_dictionary))
