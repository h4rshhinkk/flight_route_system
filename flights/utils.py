from collections import deque

def nth_node(root, n, direction):
    current = root
    for _ in range(n):
        current = getattr(current, direction)
        if current is None:
            return None
    return current


def longest_path(root):
    if not root:
        return (0, None)

    left_len, left_node = longest_path(root.left)
    right_len, right_node = longest_path(root.right)

    if left_len >= right_len:
        return (left_len + (root.left.duration if root.left else 0),
                left_node or root.left)
    else:
        return (right_len + (root.right.duration if root.right else 0),
                right_node or root.right)


def shortest_between(start, goal):
    if not start or not goal:
        return (None, [])

    visited = set()
    queue = deque([(start, [start], 0)])

    while queue:
        node, path, dur = queue.popleft()
        if node == goal:
            return (dur, path)
        visited.add(node)

        for child in [node.left, node.right]:
            if child and child not in visited:
                queue.append((child, path + [child], dur + child.duration))
        for rel in ["left_parent", "right_parent"]:
            for parent in getattr(node, rel).all():
                if parent not in visited:
                    queue.append((parent, path + [parent], dur + node.duration))
    return (None, [])
