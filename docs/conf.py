# -*- coding: utf-8 -*-

from recommonmark.parser import CommonMarkParser

from tcex import __version__

# Add the path to the tcex code so the module documentation can be created
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
# napoleon_include_private_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
# napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
# napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True

# set version and release values used in tcex documentation
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# viewcode module - http://www.sphinx-doc.org/en/1.5.1/ext/viewcode.html
viewcode_import = True

templates_path = ['/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx', 'templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']     
source_parsers = {      
            '.md': CommonMarkParser,        
        }
master_doc = 'index'
project = u'ThreatConnect Developer Docs'
copyright = u'2017'
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'threatconnect-threatconnect-developer-docs'
html_theme = 'sphinx_rtd_theme'
# file_insertion_enabled = False
latex_documents = [
  ('index', 'threatconnect-threatconnect-developer-docs.tex', u'ThreatConnect Developer Docs Documentation',
   u'', 'manual'),
]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True
