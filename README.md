# MM
# Language: Python
# Input: CSV (file containing multi-omics data)
# Output: NOA (file containing entities and -omics information)
# Tested with: PluMA 1.1, Python 3.6


This simple plugin accepts a CSV file with columns representing multi-omics data.
It then separates the data into various -omics and outputs a NOde Attribute file for Cytoscape.
This can be useful for visualizing multi-omics data using different colors for different -omics,
for example.

At the moment, this plugin supports metagenomics and metabolomics data and assumes
all metabolites start with the letter 'X'.  It will be extended in the future to handle other
types of -omics (i.e. metatranscriptomics).
