from spent_category import *


class SpentCategoryNode:
    def __init__(self, spent_on_category: SpentOnCategory, left_child=None, right_child=None):
        self.spent_on_category = spent_on_category
        self.left_child = left_child
        self.right_child = right_child


class SpentCategoryTree:
    def __init__(self):
        self.root_node = None

    def build_tree(self, spent_dict: dict[int, SpentOnCategory]):
        for key, value in spent_dict.items():
            self.insert(value)

    def get_highest_spent_category(self):
        return self._find_maximum(self.root_node).spent_on_category if self.root_node else None

    def insert(self, item: SpentOnCategory):
        self.root_node = self._place_item(self.root_node, item)

    def _place_item(self, node: SpentCategoryNode, item: SpentOnCategory):
        if node is None:
            return SpentCategoryNode(item)
        if item.amount > node.spent_on_category.amount:
            node.right_child = self._place_item(node.right_child, item)
        elif item.amount < node.spent_on_category.amount:
            node.left_child = self._place_item(node.left_child, item)
        return node

    def find_spent_amount(self, category_id: int):
        return self._find_node_by_category_id(self.root_node, category_id)

    def increase_amount(self, amount: float, category_id: int):
        return self._change_amount(amount, category_id)

    def decrease_amount(self, amount: float, category_id: int):
        return self._change_amount(-amount, category_id)

    def _change_amount(self, amount: float, category_id: int):
        item = self._find_node_by_category_id(self.root_node, category_id)
        if item:
            item.amount += amount
            return True
        return False

    def _find_node_by_category_id(self, node: SpentCategoryNode, category_id: int):
        if node is None:
            return None
        if category_id == node.spent_on_category.category_id:
            return node.spent_on_category
        found_in_left = self._find_node_by_category_id(
            node.left_child, category_id)
        if found_in_left:
            return found_in_left
        return self._find_node_by_category_id(node.right_child, category_id)

    def get_all_items(self):
        return self._in_order_traversal(self.root_node)

    def _in_order_traversal(self, node: SpentCategoryNode):
        result = []
        if node is None:
            return result
        result.extend(self._in_order_traversal(node.left_child))
        result.append(node.spent_on_category)
        result.extend(self._in_order_traversal(node.right_child))
        return result

    def delete(self, value: SpentOnCategory):
        self.root_node = self._delete_recursive(self.root_node, value)

    def _delete_recursive(self, node: SpentCategoryNode, value: SpentOnCategory):
        if node is None:
            return None
        if value.amount < node.spent_on_category.amount:
            node.left_child = self._delete_recursive(node.left_child, value)
        elif value.amount > node.spent_on_category.amount:
            node.right_child = self._delete_recursive(node.right_child, value)
        else:
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            next_node = self._find_minimum(node.right_child)
            node.spent_on_category = next_node.spent_on_category
            node.right_child = self._delete_recursive(
                node.right_child, next_node.spent_on_category)
        return node

    def find_minimum(self):
        return self._find_minimum(self.root_node).spent_on_category if self.root_node else None

    def _find_minimum(self, node: SpentCategoryNode):
        current = node
        while current and current.left_child:
            current = current.left_child
        return current

    def _find_maximum(self, node: SpentCategoryNode):
        current = node
        while current and current.right_child:
            current = current.right_child
        return current
