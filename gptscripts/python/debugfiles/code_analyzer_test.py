from tree_sitter import Parser
from tree_sitter_languages import get_language

def extract_entities(node, source_code):
    print("****extract_entities ENTITY TYPE: ********:\n", node.type)
    entities = []

    if node.type == 'function_definition':
        entities.append(source_code[node.start_byte:node.end_byte].decode())
    elif node.type == 'class_definition':
        entities.append(source_code[node.start_byte:node.end_byte].decode())
    
    for child in node.children:
        entities.extend(extract_entities(child, source_code))
    
    return entities

# Load the Python language grammar
PY_LANGUAGE = get_language('python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

# Path to the source code file
SOURCE_CODE_FILE_PATH = "/python/gptscripts/python/debugfiles/sonar_fixes.py"

# Read the source code from the file
with open(SOURCE_CODE_FILE_PATH, 'rb') as f:
    source_code = f.read()

# Parse the source code
tree = parser.parse(source_code)

# Traverse the syntax tree and extract entities
root_node = tree.root_node
entities = extract_entities(root_node, source_code)

for entity in entities:
    print("****Entity********:\n", entity) 