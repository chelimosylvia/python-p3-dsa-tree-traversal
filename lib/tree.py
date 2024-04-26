class Tree:
    def __init__(self, data):
        self.data = data

    def get_element_by_id(self, target_id):
        return self._get_element_by_id_recursive(self.data, target_id)

    def _get_element_by_id_recursive(self, node, target_id):
        if 'id' in node and node['id'] == target_id:
            return node
        for child in node.get('children', []):
            result = self._get_element_by_id_recursive(child, target_id)
            if result:
                return result
        return None
