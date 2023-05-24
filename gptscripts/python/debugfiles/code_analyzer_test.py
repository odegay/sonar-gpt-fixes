from tree_sitter import Parser
from tree_sitter_languages import get_language
import os

class CodeAnalyzer:
    def __init__(self, language, source_code_path):
        self.parser = Parser()
        self.parser.set_language(language)
        with open(source_code_path, 'rb') as f:
            self.source_code = f.read()
        self.tree = self.parser.parse(self.source_code)
        self.root_node = self.tree.root_node
        # Dictionary mapping entity serial number to updated code
        self.updated_entities = {}

    def update_entity_code(self, entity_serial_number, updated_code):
        """Updates the code of an entity with a given serial number"""
        self.updated_entities[entity_serial_number] = updated_code

    def get_entity_by_line(self, line_number):
        line_to_node = self.map_lines_to_level2_nodes()
        entity_dict = line_to_node.get(line_number)
        if not entity_dict:
            return None, None

        return self._get_entity(entity_dict)

    def get_entity_by_serial_number(self, serial_number):
        if serial_number >= len(self.root_node.children):
            return None, None
        entity_node = self.root_node.children[serial_number]
        return self._get_entity({"node": entity_node, "index": serial_number})

    def _get_entity(self, entity_dict):
        entity_node = entity_dict["node"]
        entity_serial_number = entity_dict["index"]

        entity_code = self.source_code[entity_node.start_byte:entity_node.end_byte].decode()
        start_line, _ = entity_node.start_point
        end_line, _ = entity_node.end_point
        entity_with_line_numbers = "\n".join(
            f"{i+1}: {line}" for i, line in enumerate(entity_code.split("\n"), start=start_line)
        )

        return entity_with_line_numbers, entity_serial_number    

    def map_lines_to_level2_nodes(self):
        line_to_node = {}
        for i, child in enumerate(self.root_node.children):
            start_line, _ = child.start_point
            end_line, _ = child.end_point
            for line_number in range(start_line, end_line + 1):
                line_to_node[line_number] = {"node": child, "index": i}
        return line_to_node

    def extract_entities(self):
        return self._extract_entities(self.root_node)

    def _extract_entities(self, node):
        entities = []

        if node.type in ['function_definition', 'class_definition']:
            entities.append(self.source_code[node.start_byte:node.end_byte].decode())
        
        for child in node.children:
            entities.extend(self._extract_entities(child))
        
        return entities
    
    def get_source_code_as_string(self):
        """
        Returns the whole source code file as a string.
        Substitutes the original entities with their updated code if available.
        """
        # Reconstruct the code from the entities
        updated_source_code_lines = []
        for i, entity_node in enumerate(self.level2_nodes):
            # Check if this entity has been updated
            if i in self.updated_entities:
                updated_source_code_lines.append(self.updated_entities[i])
            else:
                # Get the lines of code for this entity
                entity_code = self.source_code[entity_node.start_byte:entity_node.end_byte].decode()
                updated_source_code_lines.append(entity_code)

        # Join the lines of code and return
        return "\n".join(updated_source_code_lines)


# Load the Python language grammar
PY_LANGUAGE = get_language('python')
print(os.getcwd())

# Path to the source code file
# SOURCE_CODE_FILE_PATH = "/python/gptscripts/python/debugfiles/sonar_fixes.py"
SOURCE_CODE_FILE_PATH = "gptscripts/python/debugfiles/sonar_fixes.py"

analyzer = CodeAnalyzer(PY_LANGUAGE, SOURCE_CODE_FILE_PATH)

issue_line_number = 36  # Replace with actual line number from SonarScan
entity_with_line_numbers, entity_serial_number = analyzer.get_entity_by_line(issue_line_number)
print(f"Entity for line {issue_line_number}: {entity_with_line_numbers}")