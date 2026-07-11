import re


def extract_score(evaluation):

    match = re.search(r"Score:\s*(\d+)", evaluation)

    if match:

        return int(match.group(1))

    return 0