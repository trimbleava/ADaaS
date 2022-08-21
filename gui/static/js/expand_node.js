function expandNode(node, depth) {
  // Expand this node
  // node.setExpanded(true);
  // Reduce the depth count
  depth--;
  // If we need to go deeper
  if (depth > 0) {
      for (var i = 0; i < node.children.length; i++) {
          // Go recursive on child nodes
          expandNode(node.children[i], depth);
      }
  }
}
