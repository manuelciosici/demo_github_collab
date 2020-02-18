def expand_contractions(input: str) -> str:
    """
    Expands contractions in the given text based on an external dictionary
    :param input: text to expand contractions in
    :return: text with contractions expanded
    """
    with open("contractions.json", "r") as in_file:
        import json
        contractions = json.load(in_file)
    output = input
    for contraction, expansion in contractions.items():
        output = output.replace(contraction, expansion)
    return output
