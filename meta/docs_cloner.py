#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clone the documentation for one item (group or indicator) into documentation for another item by replacing all references to the old item with the appropriate version of the new item's name."""

# define the file you would like to update
file_ = "../docs/python/groups/campaigns/crud/update.rst"

# define the lower-case name of the object for which we are updating the documentation
new_object_name = "campaign"  # must be LOWER-CASE!

"""The keys in the mappings below specify words we want to replace and their corresponding values are the words, based on the new_object_name, we will use to replace the key. In the example below, all instances of 'Adversary' will be replaced with 'Campaign' and 'adversaries' would become 'campaigns'."""
replacements = {
    'Adversary': new_object_name.title(),
    'Adversaries': new_object_name.title() + "s",
    'adversary': new_object_name,
    'adversaries': new_object_name + "s",
}

text = None

# read the file we are going to update
with open(file_, 'r') as f:
    text = f.read()

# make all of the specified replacements
for replacement in replacements:
    text = text.replace(replacement, replacements[replacement])

# write the updated text to the file
with open(file_, 'w') as f:
    f.write(text)
