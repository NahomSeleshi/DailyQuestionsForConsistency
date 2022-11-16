from collections import Counter


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    '''
    Function to find Huffman Code
    '''
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    '''
    Function to make tree
    :param nodes: Nodes
    :return: Root of the tree
    '''
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


if __name__ == '__main__':
    
    text =  open(r"G:\GW\COURSES\DESIGN & ANALYSIS OF ALGORITHM\Assignments\P2\Huffman_sample_text.txt.txt", "r+")
        
    string = text.read()
    freq = dict(Counter(string))
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    # print("e: ", encoding, "f: ", freq)

    bits_after_huffman = 0
    for i in range(len(freq)):
        bits_after_huffman += freq[i][1] * len(encoding[freq[i][0]])

    # for i in encoding:
    #     print(f'{i} : {encoding[i]}')
    
    print("Number of bits used before Huffman: ", len(string)*8)
    print("Number of bits used after Huffman: ", bits_after_huffman)
