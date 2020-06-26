from collections import defaultdict
import sys


class Node:
    def __init__(self, char, value):
        self.left = None
        self.right = None
        self.char = char
        self.value = value

    def set_right_child(self, right):
        self.right = right

    def set_left_child(self, left):
        self.left = left


class Tree:
    def __init__(self, node):
        self.root = node


def huffman_encoding(data):
    if not data:
        return "", None
    frequencies = get_characters_frequencies(data)
    tree = create_huffman_tree(frequencies)
    coding = encode(tree)
    return code_data(data, coding), tree


def huffman_decoding(data, tree):
    if not data:
        return ""

    decoded_string = ""
    node = tree.root
    for char in data:
        if char == "0":
            node = node.left
        else:
            node = node.right
        if not node.left and not node.right:
            decoded_string += node.char
            node = tree.root
    return decoded_string


def get_characters_frequencies(string):
    frequencies = defaultdict(int)
    for char in string:
        frequencies[char] += 1
    return sorted(frequencies.items(), key=lambda item: item[1])


def create_huffman_tree(frequencies):
    if len(frequencies) == 1:
        left = Node(char=frequencies[0][0], value=None)
        root = Node(char=None, value=frequencies[0][1])
        root.set_left_child(left)
        tree = Tree(root)
        return tree

    if len(frequencies) == 2:
        left = Node(char=frequencies[0][0], value=None)
        right = Node(char=frequencies[1][0], value=None)

        root = Node(char=None, value=frequencies[0][1] + frequencies[1][1])
        root.set_left_child(left)
        root.set_right_child(right)

        tree = Tree(root)
        return tree

    last_element = frequencies[-1]
    rest_data = frequencies[:-1]
    tree = create_huffman_tree(rest_data)

    left = Node(char=last_element[0], value=None)
    new_root = Node(char=None, value=tree.root.value + last_element[1])
    new_root.set_left_child(left)
    new_root.set_right_child(tree.root)

    tree.root = new_root

    return tree


def encode(tree):
    root = tree.root
    if not root.left and not root.right:
        return {root.value: "0"}
    return encode_recursive(root, "")


def encode_recursive(root, current_code):
    if root is None:
        return {}

    codes = {}
    if root.char:
        codes[root.char] = current_code

    codes.update(encode_recursive(root.left, current_code + "0"))
    codes.update(encode_recursive(root.right, current_code + "1"))
    return codes


def code_data(data, codes):
    coding = ""
    for char in data:
        coding += codes[char]
    return coding


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    empty_sentence = ""

    encoded_data, tree = huffman_encoding(empty_sentence)
    print(encoded_data)
    # should return empty string

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    # decoded data should also be empty string

    only_one_letter_sentence = "AAAAAAAAAA"

    encoded_data, tree = huffman_encoding(only_one_letter_sentence)
    print(encoded_data)
    # should return empty string

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data)
    # decoded data should be "AAAAAAAAAA"