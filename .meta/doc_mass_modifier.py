#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make changes in bulk by regex... USE WITH CAUTION!!!"""

import os
import re

# set the language of the docs through which you would like to iterate <python|javascript|java|resp_api>
docs_lang = "python"
test_run = True


def update_emphasized_lines(file_text, delta):
    """Change the emphasize lines headings in the file_text by the delta."""
    if delta == 0:
        print("The delta is zero. No changes will be made to the file text.")
    else:
        # find the emphasize lines
        matches = re.findall(':emphasize-lines: (.*)', file_text)

        # increment them appropriately
        for match in matches:
            emphasis_intervals = list()

            for range_ in match.split(","):
                new_nums = list()

                for num in range_.split("-"):
                    if int(num) > 3:
                        new_nums.append(str(int(num) + delta))
                    else:
                        new_nums.append(num)

                emphasis_intervals.append("-".join(new_nums))

            # replace the old interval with the updated one
            file_text = re.sub(match, ",".join(emphasis_intervals), file_text)

    # return the file_text with the updated emphasized line numbers
    return file_text


# iterate through the docs
for path, dirs, files in os.walk("../docs/".format(docs_lang)):
    # iterate through the files
    for file_ in files:
        file_text = None
        full_file_path = os.path.join(path, file_)

        # read the file's content
        with open(full_file_path, 'r') as f:
            file_text = f.read()

        # find something in the current file
        pattern = "# instantiate (.*) object"
        matches = re.findall(pattern, file_text)
        expected_matches = 1

        if not matches:  # if there are no matches, move on
            pass
        elif len(matches) == expected_matches:  # if the number of matches is expected, make appropriate changes
            if not test_run:
                # replace the matched content with something else
                file_text = re.sub(pattern, "# instantiate some {}".format(matches[0]), file_text)

                file_text = update_emphasized_lines("", 0)

                # write the update content to the file
                with open(full_file_path, 'w') as f:
                    f.write(file_text)
            else:
                print("Would make change in {}: {}".format(full_file_path, matches))
        else:  # if the number of matches is unexpected, print a warning
            print("{} matches found in {}".format(len(matches), full_file_path))
