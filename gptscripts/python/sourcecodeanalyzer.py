import tree_sitter

def extract_entities(node, source_code):
    entities = []
    if node.type == 'function_definition':
        entities.append(source_code[node.start_byte:node.end_byte].decode())
    elif node.type == 'class_definition':
        entities.append(source_code[node.start_byte:node.end_byte].decode())
    
    for child in node.children:
        entities.extend(extract_entities(child, source_code))
    
    return entities

# Load the Python language grammar (replace "path/to/tree-sitter-python" with the actual path)
PY_LANGUAGE = tree_sitter.Language('path/to/tree-sitter-python', 'python')
parser = tree_sitter.Parser()
parser.set_language(PY_LANGUAGE)

# Parse the source code
source_code = b"""
class ExampleClass:
    def example_method(self):
        print('Hello, world!')

def example_function():
    print('Hello, world!')
"""
tree = parser.parse(source_code)

# Traverse the syntax tree and extract entities
root_node = tree.root_node
entities = extract_entities(root_node, source_code)

for entity in entities:
    print("Entity:\n", entity)