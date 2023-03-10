#!/usr/bin/python3
def multiple_returns(sentence):
    """My multiple return values function

    Args:
        sentence: To be checked for length and first character

    Returns:
        The length and first character of provided string
    """
    len_s = len(sentence)
    if len_s == 0:
        return (len_s, None)
    return (len_s, sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
