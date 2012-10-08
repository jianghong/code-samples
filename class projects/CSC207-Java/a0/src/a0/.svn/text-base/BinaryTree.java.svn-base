package a0;

/**
 * A binary tree.
 */
public class BinaryTree {
    
    /**
     * A Node in BinaryTree that keeps track of its parent, left child, and
       right child, and its value.
     */
    public static class Node {
        Node parent;
        Node leftChild;
        Node rightChild;
        Object value;
        
        /**
         * Constructor for a new Node object with an initial value.
         * This node has no parents or children when initialized.
         * 
         * @param value The value of this node
         */
        Node(Object value) {
            this.value = value;
        }
        
        /**
         * Make child this node's left child if this node does not have 
         * a left child. Otherwise, attach to the first node that is the left
         * child of this node's left child, etc., that had no left child.
         * Precondition: child is not already attached to another node.
         * 
         * @param Child The node to be attached
         */
        void attachLeft(Node child) {
            if (this.leftChild != null) {
                this.leftChild.attachLeft(child);
                return;
            }
           
            this.leftChild = child;
            this.leftChild.parent = this;
        }
       
        /**
         * Make child this node's right child if this node does not have 
         * a right child. Otherwise, attach to the first node that is the right
         * child of this node's right child, etc., that had no right child.
         * Precondition: Child is not already attached to another node.
         *  
         * @param child The node to be attached
         */
        void attachRight(Node child) {
            if (this.rightChild != null) {
                this.rightChild.attachRight(child);
                return;
            }
            
            this.rightChild = child;
            this.rightChild.parent = this;
        }
        
                
        /**
         * Determine if Node node is the right child or left child of this node
         * Return 1 if node is a right child and return 0 if node is left
         * @param node
         * @return 1 or 0
         */
        public int rightOrLeftChild(Node node) {
            
            int bool;

                if (this.rightChild == node) {
                    bool = 1;
                }
                else {
                    bool = 0;
                }

            return bool;
            
        }
        /**
         * Swap this node with another node.
         * The parents and children of these two nodes should be swapped and
         * the corresponding references swapped as well.
         * 
         * E.g., starting from
         * 
         *      0   3
         *     /     \
         *    1       4
         *   /         \
         *  2           5
         *
         *  and swapping the 1 and 4 nodes should result in the following:
         *  
         *      0   3
         *     /     \
         *    4       1
         *   /         \
         *  2           5
         *
         * @param node The node to be swapped.
         */
        public void swap(Node node) {
            // Store reference to this node's parent and children
            Node thisParent = this.parent;
            Node thisLeftChild = this.leftChild;
            Node thisRightChild = this.rightChild;
            
            // Store references to the other node's parents and children
            Node otherParent = node.parent;
            Node otherLeftChild = node.leftChild;
            Node otherRightChild = node.rightChild;
            
            // Make the other node take the original place of this node
            node.parent = this.parent;
            node.leftChild = this.leftChild;
            node.rightChild = this.rightChild;
            
            // Make this node take the other node's original place
            this.parent = otherParent;
            this.leftChild = otherLeftChild;
            this.rightChild = otherRightChild;
            
            // Make this node's children refer to other node as parent
            if (thisLeftChild != null) 
                thisLeftChild.parent = node;
            if (thisRightChild != null) 
                thisRightChild.parent = node;
            
            // Make other node's children refer to this node as parent
            if (otherLeftChild != null)
                otherLeftChild.parent = this;
            if (otherRightChild != null)
                otherRightChild.parent = this;
            
            // Handle special case of swapping root
            // Determine if this node is a right or left child of orignal parent
            // Determine if node is a right or left child of its original parent
            // Make the parents refer to correct nodes after the swap
            if (thisParent == null) {
                node.parent = null;
                int otherRightorLeft = otherParent.rightOrLeftChild(node);
                if (otherRightorLeft == 1)
                    otherParent.rightChild = this;
                else
                    otherParent.leftChild = this;     
         }
            else if (otherParent == null) {
                this.parent = null;
                int thisRightorLeft = thisParent.rightOrLeftChild(this);
                if (thisRightorLeft == 1)
                    thisParent.rightChild = node;
                else
                    thisParent.leftChild = node;
        }
            else {
            int otherRightorLeft = otherParent.rightOrLeftChild(node);
            int thisRightorLeft = thisParent.rightOrLeftChild(this);
            if (thisRightorLeft == 1)
                thisParent.rightChild = node;
            else
                thisParent.leftChild = node;
            if (otherRightorLeft == 1)
                otherParent.rightChild = this;
            else
                otherParent.leftChild = this;
            }
            
        }
        

        /**
         * Return the value of this node.
         * @return The value of this node.
         */
        public Object getValue() {
            return this.value;
        }
    }

    /** The root of this binary tree. */
    private Node root;
    
    /**
     * Make root the new root of this tree and return the old root.
     * 
     * @param root The node to be made root.
     * @return The old root
     */
//    public BinaryTree setRoot(Node root) {
    public Node setRoot(Node root) {
        Node oldRoot = this.root;
        this.root = root;
        return oldRoot;
    }

    /**
     * Return the root of this tree.
     * @return the root
     */
    public Node getRoot() {
        return root;
    }

    /**
     * Return a node whose value matches the provided value.
     * If no such node is found, return null.
     * 
     * @param value The value of the node to be found
     * @return The found node
     */
    public Node contains(Object value) {
        Node targetNode = null;
        if (this.root.getValue() == value) {
            return this.root;
        }
        if (this.root.leftChild != null){
            BinaryTree leftBT = new BinaryTree();
            leftBT.setRoot(this.root.leftChild);
            targetNode = leftBT.contains(value);
            if (targetNode != null) {
                return targetNode;
            }
        }
        if (this.root.rightChild != null) {
            BinaryTree rightBT = new BinaryTree();
            rightBT.setRoot(this.root.rightChild);
            targetNode = rightBT.contains(value);
        }
     
        return targetNode;
    }
}
