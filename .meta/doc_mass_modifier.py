#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make changes in bulk by regex... USE WITH CAUTION!!!"""

import os
import re

# set the language of the docs through which you would like to iterate <python|javascript|java|resp_api>
docs_lang = "python"
test_run = True

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

                # write the update content to the file
                with open(full_file_path, 'w') as f:
                    f.write(file_text)
            else:
                print("Would make change in {}: {}".format(full_file_path, matches))
        else:  # if the number of matches is unexpected, print a warning
            print("{} matches found in {}".format(len(matches), full_file_path))
