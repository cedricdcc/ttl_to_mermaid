import argparse
import rdflib
import os

from src.singletons.logger import get_logger
from src.models.graph import Graph
from src.models.diagram import DiagramManager

logger = get_logger()

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("ttl_file", help="path to the TTL file")
args = parser.parse_args()

logger.info(f"ttl_file: {args.ttl_file}")

# Check if the TTL file exists
if not os.path.exists(args.ttl_file):
    logger.error(f"TTL file not found: {args.ttl_file}")
    exit(1)

# Create a graph instance
graph = Graph(args.ttl_file)

# Make a diagram instance
diagram = DiagramManager(graph.g)