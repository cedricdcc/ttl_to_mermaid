import os

#all diagram functions and instances here
import graphviz
from src.singletons.logger import get_logger
import rdflib

logger = get_logger()

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

class DiagramManager:
    
    def __init__(self, graph):
        logger.info("Diagram class instantiated")
        self.graph = graph
        self.make_diagram()
        self.view_diagram()
        self.save_diagram()
    
    def make_legend(self):
        logger.info("Making legend")
        #make a subgraph for the legend
        with self.diagram.subgraph(name="legend") as legend:
            legend.attr(style="filled", color="lightgrey")
            legend.attr(label="Legend")
            #classes will be a yellow filled box with a black border and black text 
            legend.node("class", label="Class", shape="box", style="filled", fillcolor="yellow", color="black", fontcolor="black")
            #class restriction is a light yellow filled box with a dotted border and black text
            legend.node("class_restriction", label="Class Restriction", shape="box", style="filled", fillcolor="lightyellow", color="black", fontcolor="black")
            #a lightgreen filled parallellogram for datatypes
            legend.node("datatype", label="Datatype", shape="parallelogram", style="filled", fillcolor="lightgreen", color="black", fontcolor="black")
            #a lightblue filled box for object properties
            legend.node("object_property", label="Object Property", shape="box", style="filled", fillcolor="lightblue", color="black", fontcolor="black")
            #a grey filled box for concepts
            legend.node("concept", label="Concept", shape="box", style="filled", fillcolor="grey", color="black", fontcolor="black")
            
    def make_ontology(self):
        logger.info("Making ontology")
        
        #make subgraph for ontology
        with self.diagram.subgraph(name="ontology") as ontology:
            ontology.attr(style="filled", color="lightgrey")
            ontology.attr(label="Ontology")
        
            #go over all the triples in the graph
            for subject, predicate, object in self.graph:
                #logger.debug(f"Subject: {subject} | Predicate: {predicate} | Object: {object}")
                
                #if predicate is rdf-syntax type, then log the object
                if predicate == rdflib.RDF.type:
                    logger.debug(f"Object: {object}")
                    
                    # check if the object is skos:concept,owl:Class, owl:DatatypeProperty, owl:ObjectProperty
                    if object == rdflib.OWL.Class:
                        #make a node for the class
                        ontology.node(str(subject), label=str(subject), shape="box", style="filled", fillcolor="yellow", color="black", fontcolor="black")
                    elif object == rdflib.OWL.DatatypeProperty:
                        #make a node for the datatype
                        ontology.node(str(subject), label=str(subject), shape="parallelogram", style="filled", fillcolor="lightgreen", color="black", fontcolor="black")
                    elif object == rdflib.OWL.ObjectProperty:
                        #make a node for the object property
                        ontology.node(str(subject), label=str(subject), shape="box", style="filled", fillcolor="lightblue", color="black", fontcolor="black")
                    elif object == rdflib.SKOS.Concept:
                        #make a node for the concept
                        ontology.node(str(subject), label=str(subject), shape="box", style="filled", fillcolor="grey", color="black", fontcolor="black")
                    elif object == rdflib.OWL.Restriction:
                        #make a node for the class restriction
                        ontology.node(str(subject), label=str(subject), shape="box", style="filled", fillcolor="lightyellow", color="black", fontcolor="black")
                    else:
                        logger.debug(f"Object: {object} is not a class, datatype, object property, or concept")
            
              
            
                    
            
        
    def make_diagram(self):
        logger.info("Making diagram")
        self.diagram = graphviz.Digraph(
            name="diagram",
            filename="diagram",
            format="png",
            graph_attr={"rankdir": "LR"},
        )
        
        self.make_legend()
        self.make_ontology()
        
    def view_diagram(self):
        logger.info("Viewing diagram")
        self.diagram.view()
    
    def save_diagram(self):
        logger.info("Saving diagram")
        self.diagram.render()