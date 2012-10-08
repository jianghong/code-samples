package a0;

import a0.BinaryTree.Node;
import junit.framework.TestCase;

public class BinaryTreeTest extends TestCase {
    /**
     * Test the Node constructor with a basic string value.
     */
    public void testNodeConstructorString() {
        Node newNode = new Node("Alpha");
        assertEquals(newNode.value, "Alpha");
    }

    /**
     * Test the Node constructor with a null value.
     */
    public void testNodeConstructorNull() {
        Node newNode = new Node(null);
        assertEquals(newNode.value, null);
    }
    
    /**
     * Test BT's setRoot method.
     */
    public void testSetRootNewNode() {
        BinaryTree bt = new BinaryTree();
        Node newNode = new Node("Alpha");
        Node oldRoot = bt.setRoot(newNode);
        assertEquals(bt.getRoot(), newNode);
    }
    /** 
     * Test BT's setRoot method's behaviour when replacing the node.
     */
    public void testSetRootReplaceRoot() {
        BinaryTree bt = new BinaryTree();
        Node newNode = new Node("Alpha");
        Node newNode2 = new Node("Beta");
        Node oldRoot = bt.setRoot(newNode);
        oldRoot = bt.setRoot(newNode2);
        assertEquals(bt.getRoot(), newNode2);
    }
    
    /**
     * 
     */
    public void testNodeSwapBasic() {
        /* Initialise a pair of trees (without a BinaryTree object)
         * 
         *      1       3
         *     /         \
         *    2           4
         * 
         */
        Node newNode1 = new Node("1");
        Node newNode2 = new Node("2");
        Node newNode3 = new Node("3");
        Node newNode4 = new Node("4");

        newNode1.attachLeft(newNode2);
        newNode3.attachRight(newNode4);
        
        // Perform a swap of the children nodes...
        newNode2.swap(newNode4);
        
        /* So we expect
         * 
         *      1       3
         *     /         \
         *    4           2
         * 
         */
        
        // ... ensuring that the nodes' values are unchanged ...
        assertEquals(newNode1.value, "1");
        assertEquals(newNode2.value, "2");
        assertEquals(newNode3.value, "3");
        assertEquals(newNode4.value, "4");
        
        // ... and ensure the resulting structure is correct
        // first verifying the tree containing the "4"
        assertEquals(newNode4.parent, newNode1);
        assertEquals(newNode4.leftChild, null);
        assertEquals(newNode4.rightChild, null);
        
        assertEquals(newNode1.parent, null);
        assertEquals(newNode1.rightChild, null);
        assertEquals(newNode1.leftChild, newNode4); 
        
        // then verifying the tree containing the "2"
        assertEquals(newNode2.parent, newNode3);
        assertEquals(newNode2.leftChild, null);
        assertEquals(newNode2.rightChild, null);
        
        assertEquals(newNode3.parent, null);
        assertEquals(newNode3.rightChild, newNode2);
        assertEquals(newNode3.leftChild, null);     
    }
     /** 
     * We have a BT that looks like this
     *             1
     *         /        \
     *        2          4
     *          \       /
     *           3     5
     *                /
     *               6
     * Test swapping on node2 and node5.
     * 
     * We expect a new BT that looks like this
     *             1
     *         /        \
     *        5          4
     *          \       /
     *           3     2
     *                /
     *               6
     */
     public void testSwapMore() {
        BinaryTree bt = new BinaryTree();
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        bt.setRoot(node1);
        node1.attachLeft(node2);
        node2.attachRight(node3);
        node1.attachRight(node4);
        node4.attachLeft(node5);
        node5.attachLeft(node6);
        // Swap node2 and node 5
        node2.swap(node5);
        // Ensure values of nodes are unchanged
        assertEquals(node2.getValue(), 2);
        assertEquals(node5.getValue(), 5);
        // Verify tree structure for node5
        assertEquals(node1.leftChild, node5);
        assertEquals(node5.parent, node1);
        assertEquals(node5.rightChild, node3);
        assertEquals(node5.leftChild, null);
        assertEquals(node3.parent, node5);
        // Verify tree structure for node2;
        assertEquals(node4.leftChild, node2);
        assertEquals(node2.parent, node4);
        assertEquals(node2.leftChild, node6);
        assertEquals(node2.rightChild, null);
        assertEquals(node6.parent, node2);
    }
     /**
      * Test swap when swapping root with a child node
      * We have initial tree of
      *                    1
      *                      \
      *                        2
      *                      /   
      *                    3
      *                  /   \
      *                4       5
      * 
      * Swap root with node3 and new tree should be
      *                 3
      *                   \
      *                    2
      *                   /
      *                  1
      *                /   \ 
      *               4      5
      */
     
     public void testSwapRoot() {
        BinaryTree bt = new BinaryTree();
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        node1.attachRight(node2);
        node2.attachLeft(node3);
        node3.attachLeft(node4);
        node3.attachRight(node5);
        bt.setRoot(node1);
        // Swap root with node3
        node1.swap(node3);
        // Verify tree structure of node3
        assertEquals(node3.parent, null);
        assertEquals(node3.rightChild, node2);
        assertEquals(node3.leftChild, null);
        assertEquals(node2.parent, node3);
        // Verify tree structure of node1;
        assertEquals(node1.parent, node2);
        assertEquals(node1.rightChild, node5);
        assertEquals(node1.leftChild, node4);
        assertEquals(node4.parent, node1);
        assertEquals(node5.parent, node1);
     }
    /**
     * Return a string representation of a node's left child, parent,
     * and right child, each separated by a space.
     * @param node The string representation of a node's connections
     * @return
     */
    public String lprValue(Node node) {
        return (node.leftChild == null ? "null" : node.leftChild.value.toString()) + " " +
               (node.parent == null ? "null" : node.parent.value.toString()) + " " +
               (node.rightChild == null ? "null" : node.rightChild.value.toString());
    }
    
    public void testContainsRoot() {
        BinaryTree bt = new BinaryTree();
        Node node1 = new Node(1);
        Node node2 = new Node("test");
        bt.setRoot(node1);
        // Test if contains works with a root containing an int
        assertEquals(bt.contains(1), node1);
        bt.setRoot(node2);
        // Test if contains works with a root containing a string
        assertEquals(bt.contains("test"), node2);
        // Test if contains works with a root without children and cannot 
        // find the value
        assertEquals(bt.contains("not in here"), null);
    }
    
    public void testContainsMore() {
        BinaryTree bt = new BinaryTree();
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        bt.setRoot(node1);
        node1.leftChild = node2;
        node2.rightChild = node3;
        node1.rightChild = node4;
        node4.leftChild = node5;
        node5.leftChild = node6;
        // Test if value can be found at various levels of the BT
        assertEquals(bt.contains(2), node2);
        assertEquals(bt.contains(3), node3);
        assertEquals(node4, bt.contains(4));
        assertEquals(bt.contains(5), node5);
        assertEquals(bt.contains(6), node6);
        assertEquals(null, bt.contains("not in here"));
                }
}
