# https://towardsdatascience.com/build-a-keyword-extraction-api-with-spacy-flask-and-fuzzywuzzy-4909d7ffc105
# https://gist.github.com/cdpierse/1b1e3ae23bbb6c9b7b2e70ac066f4e60
import spacy
import subprocess
from string import punctuation


def extract_keywords(nlp, sequence, special_tags: list = None):
    """
    Takes a Spacy core language model,
    string sequence of text and optional
    list of special tags as arguments.

    If any of the words in the string are
    in the list of special tags they are immediately
    added to the result.

    Arguments:
        sequence {str} -- string sequence to have keywords extracted from

    Keyword Arguments:
        tags {list} -- list of tags to be automatically added (default: {None})

    Returns:
        {list} -- list of the unique words extracted from a string
    """
    result = []

    # custom list of part of speech tags we are interested in
    # we are interested in proper nouns, nouns, and adjectives
    #
    # EDIT this list of 'parts of speech' tags
    pos_tags = ['PROP_N', 'N', 'ADJ', 'V']

    # create a spacy doc object by calling the nlp object on the input sequence
    doc = nlp(sequence.lower())

    # if special tags are given and exist in the input sequence
    # add them to results by default
    if special_tags:
        tags = [tag.lower() for tag in special_tags]
        for token in doc:
            if token.text in tags:
                result.append(token.text)

    for chunk in doc.noun_chunks:
        final_chunk = ""
        for token in chunk:
            if token.pos_ in pos_tags:
                final_chunk += token.text + " "
        if final_chunk:
            result.append(final_chunk.strip())

    for token in doc:
        if token.text in nlp.Defaults.stop_words or token.text in punctuation:
            continue
        if token.pos_ in pos_tags:
            result.append(token.text)

    return list(set(result))


if __name__ == "__main__":
    """
    install the language model using the subprocess package
    useful when hosting the service in the cloud as it prevents against
    us forgetting to do this via the CLI
    """
    # load the (small/large) engine language model
    model_size = 'sm'  # (sm/lg)
    language_model = "en_core_web_" + model_size
    subprocess_call = "python -m spacy download " + language_model
    subprocess.call(subprocess_call, shell=True)
    nlp = spacy.load(language_model)
    print("Loaded language vocabulary")

    title = "Why projects being built on Ethereum don't need Silicon Valley"
    content = """
    this type of behavior is going to disrupt more than just silicon valley - i look forward to the days where the average family can be invested like the billionaires; owning a % of an apartment complex, or commercial property - making passive income each year from these holdings - crypto will not only eliminate the need for most middle man, it'll put the power into the hands of the governed.. they say you don't attempt to take down the current system, you just build one parallel and slowly migrate. this is happening naturally in our reality - you gotta love the collective consciousness of humans
    The state isn't even needed. You can already nowadays buy tokens of an electronic device and earn a share of its profits, along with other investors and the proximity manager of the electronic device. All of this on the blockchain, through a DAO, without requiring any trust (unlike centralized markets like the stocks).

So, sure, the manager could take the device and quit it all to install and manage it elsewhere without sharing anything. But then, it would be the only trade he'd do: he'd bare himself from future trades where he could handle more than an electronic device, as well as cutting him off the network of other devices that may be needed for "his" device to properly work.

For a market to be efficient and people to behave between themselves, you only need transactions to be small enough so that no one can reasonably profit from being dishonest, due to the future profit they'd lose.

Besides, most states do recognize contracts of shared ownership or shared profit. The fact the contract is automatically enforced through a token has nothing to do with the validity of the contract in the eyes of the law.
    In 2014, I moved to the bay ready to be engulfed in the overload of brilliance that the genius minds of the great Silicon Valley would bestow upon me.

Didn’t take long to see the old decrepit man behind the curtain, playing the organ.

It’s just dumb billionaires who got lucky once or twice and have been dining out on those winnings. Now they spend their time kissing each others’ asses, kissing their own asses, and gambling on unnecessary products & services to strike it richer.

‘Our service is called BallWashr. We come to your office parking lot and a robot washes your balls!’ ‘I’ll pay $100,000,000 for it! But let’s try to make it a PAAS play to get ELAs!’

This place is a beached whale carcass with just blubber hanging off of bones. The rest is liquefying into oil. The gulls have dispersed.
    """

    print(extract_keywords(nlp, title + content))
