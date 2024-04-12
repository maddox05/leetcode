int check_if_node_in_BST(struct TreeNode* root, int key){
  if(root == NULL){
    return 0;
  }
  struct TreeNode * current = root;
  if(current->val == key){
    return 1;
  }
  else if(key < current->val){
    return check_if_node_in_BST(current->left, key);
  }
  else{
    return check_if_node_in_BST(current->right, key);
  }
}

struct TreeNode* find_succesor(struct TreeNode* root, int key) {
  struct TreeNode * current = root;
  if(current->left == NULL){
    return current->right;
  }
  else if(current->right == NULL){
    return current->left;
  }
  else{
    current = current->right;
    struct TreeNode * last = current;
    while(current->left != NULL){
      last = current;
      current = current->left;
    }
    last->left = current->right; // needs current right as if the successor has a right, we need to save the right (we know the successor has no left)
    return current;
  }

}


struct TreeNode* rec_deleteNode(struct TreeNode* root, int key) {
  struct TreeNode * current = root;
  if(current->val == key){
    
    // delete current and find successor;
    struct TreeNode * successor = find_succesor(root, key);
    if(current->left != NULL && successor->val != current->left->val){
      successor->left = current->left;
    }
    if(current->right != NULL && successor->val != current->right->val){
      successor->right = current->right;
    }
    return successor;
  }
  else if(key < current->val){
    current->left = rec_deleteNode(current->left, key);
    // go lefty
  }
  else if(key > current->val){
    current->right = rec_deleteNode(current->right, key);
    // go right
  }
  return current;
}

 
struct TreeNode* deleteNode(struct TreeNode* root, int key) {
  if(root == NULL){
    return NULL;
  }
  if(check_if_node_in_BST(root, key) == 0){
    return root;
  }
  root = rec_deleteNode(root, key);
  return root;

}
