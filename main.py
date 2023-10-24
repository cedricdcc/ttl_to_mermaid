import argparse
import rdflib
import os

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("ttl_file", help="path to the TTL file")
args = parser.parse_args()

# Read the TTL file and parse it using rdflib
g = rdflib.Graph()
g.parse(args.ttl_file, format="ttl")

# Traverse the graph and extract the necessary information to create the Mermaid markdown
mermaid_markdown = "graph TD\n"
for s, p, o in g:
    #clean the s o first by removing "" and > < " " by _
    s = s.n3()
    clean_s = s.replace('"', '')
    clean_s = clean_s.replace('>', '')
    clean_s = clean_s.replace('<', '')
    clean_s = clean_s.replace(' ', '_')
    o = o.n3()
    clean_o = o.replace('"', '')
    clean_o = clean_o.replace('>', '')
    clean_o = clean_o.replace('<', '')
    clean_o = clean_o.replace(' ', '_')
    mermaid_markdown += f"{clean_s} --> {clean_o}\n"

# Print the Mermaid markdown
print(mermaid_markdown)