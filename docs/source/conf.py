# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
os.environ['SPHINX_BUILD'] = '1'

import sys
sys.path.insert(0, os.path.abspath('../../back'))


project = 'guardias'
copyright = '2024, Enrique Cillero Dorado'
author = 'Enrique Cillero Dorado'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'docxbuilder'

]

docx_documents = [
    ('index', 'output', {
        'title': 'Guardias',
        'author': 'Enrique Cillero Dorado',
    }, True),
]

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{graphicx}
        % Otros paquetes necesarios pueden ser añadidos aquí
    ''',
    'figure_align': 'htbp',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
