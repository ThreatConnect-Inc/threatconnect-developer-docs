import os
import re
import subprocess
import sys

replacement_config = """
try:
    import ConfigParser
except:
    import configparser as ConfigParser
import sys

from threatconnect import ThreatConnect

config = ConfigParser.RawConfigParser()
config.read("./tc.conf")

try:
    api_access_id = config.get('threatconnect', 'api_access_id')
    api_secret_key = config.get('threatconnect', 'api_secret_key')
    api_default_org = config.get('threatconnect', 'api_default_org')
    api_base_url = config.get('threatconnect', 'api_base_url')
except ConfigParser.NoOptionError:
    print('Could not read configuration file.')
    sys.exit(1)"""

default_file = "./test.py"


def get_code_snippets(file_text):
    """Identify all of the code snippets in the documentation."""
    code_block_pattern = "\.\. code-block:: python\n((.*\n)*?)[\S]"

    code_blocks = re.findall(code_block_pattern, file_text)

    return [codeblock[0] for codeblock in code_blocks]


def test_snippets():
    """Test all of the code snippets in the python SDK docs."""
    counter = {
        'expected_error': 0,
        'success': 0,
        'unexpected_error': 0,
    }

    for path, dirs, files in os.walk("../docs/python/"):
        for file_ in files:
            code_blocks = None

            # parse the code blocks from the file
            with open(os.path.join(path, file_), 'r') as f:
                # get the code blocks
                code_blocks = get_code_snippets(f.read())

            # test each of the code blocks
            for code_block in code_blocks:
                # if this code block is not meant to run as a stand-alone file, skip it
                if ":no-test:" in code_block:
                    continue

                # pattern for ":linenos:" and ":emphasize-lines:"
                line_num_pattern = ":.*?:.*"

                # replace the appropriate sections of the code block
                code_block = re.sub(line_num_pattern, "", code_block)
                code_block = re.sub("\n    ", "\n", code_block)
                code_block = code_block.replace("...", replacement_config)

                # write the python snippet to a file
                with open(default_file, 'w+') as f:
                    f.write(code_block)

                try:
                    # run the file
                    subprocess.check_output(["python", "{}".format(default_file)])
                    counter['success'] += 1
                except subprocess.CalledProcessError:
                    # if there is an exception, get the output
                    error_output = subprocess.getoutput("python {}".format(default_file))

                    # if the output was not an expected error, make a not of it
                    if "ConfigParser.NoSectionError: No section: 'threatconnect'" not in error_output:
                        print("\n\n{}:\n{}".format(os.path.join(path, file_), error_output))
                        counter['unexpected_error'] += 1
                    else:
                        counter['expected_error'] += 1

    # report the damage
    print("Successes: {}\nExpected Errors: {}\nUnexpected Errors: {}".format(counter['success'],
                                                                             counter['expected_error'],
                                                                             counter['unexpected_error']))

    # exit with a partial failure if there were unexpected errors
    if counter['unexpected_error'] > 0:
        sys.exit(3)
