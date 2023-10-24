#graph entity wil be made and maintained here

import rdflib
from src.singletons.logger import get_logger

logger = get_logger()

class Graph:
    def __init__(self, ttl_file):
        logger.info("Graph class instantiated")
        self.g = rdflib.Graph()
        self.g = self.g.parse(ttl_file, format="ttl")
        logger.debug(f"Graph: {self.g}")
        
    def get_graph(self):
        return self.g