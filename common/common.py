#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
from collections import OrderedDict


class Queue:
    def __init__(self):
        self._value = []
        self.length = 0

    def enqueue(self, value):
        self._value.append(value)
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            value = self._value[0]
            self._value = self._value[1:]
            self.length -= 1
            return value


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

        self.left_height = 0
        self.right_height = 0


class Stack:
    def __init__(self):
        self._value = []
        self.length = 0

    def push(self, value):
        self._value.append(value)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self._value.pop()


def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)


def levelorder(root):
    if root == None:
        print("null")
        return

    node_stack = [root]
    while len(node_stack) > 0:
        node = node_stack.pop(0)
        print(node.val)
        if node.left:
            node_stack.append(node.left)
        else:
            print("null")

        if node.right:
            node_stack.append(node.right)
        else:
            print("null")


class MinHeapNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None


class MinHeap:
    """
    最小堆
    """

    def __init__(self):
        """
        数组存放节点
        """
        # 存放一个占位节点，使得有效值的下标从1开始， 方便计算
        self._value = [None]
        self.length = 0

    def insert(self, val):
        """
        插入节点构成完全二叉树
        """
        self._value.append(val)
        self.length += 1

    def percDown(self, i):
        left_node_index = i*2
        right_node_index = left_node_index+1

        # 有子节点
        while left_node_index <= self.length:
            left_node = self._value[left_node_index]
            # 有两个子节点
            if right_node_index <= self.length:
                right_node = self._value[right_node_index]
                if self._value[i].freq < left_node.freq and self._value[i].freq < right_node.freq:
                    break
                else:
                    if left_node.freq < right_node.freq:
                        self._value[i], self._value[left_node_index] = left_node, self._value[i]
                        i = left_node_index
                    else:
                        self._value[i], self._value[right_node_index] = right_node, self._value[i]
                        i = right_node_index

                    left_node_index = 2*i
                    right_node_index = left_node_index+1
            else:
                if self._value[i].freq < left_node.freq:
                    break
                else:
                    self._value[i], self._value[left_node_index] = left_node, self._value[i]
                    i = left_node_index

                left_node_index = 2*i
                right_node_index = left_node_index + 1

    def percUp(self, i):
        """
        调整为最小堆
        """
        while i//2 > 0:
            if self._value[i].freq < self._value[i//2].freq:
                self._value[i], self._value[i //
                                            2] = self._value[i//2], self._value[i]

                i = i//2
            else:
                break

    def rootPath(self, i):
        """
        指定位置元素到root节点的路径打印，下表从1开始
        """
        while i > 0 and i <= self.length:
            print(self._value[i].val)
            i = i // 2

    def deleteMinNode(self, i):
        """
        删除指定位置i的节点
        """
        # 使用树中最后一个节点填充被删除节点的位置，保证删除后仍然是一棵完全二叉树
        if i > self.length:
            return

        deleted_node = self._value[i]

        replace_node = self._value[-1]
        self._value[i] = replace_node
        self._value = self._value[:-1]
        self.length -= 1

        # 与父节点比较
        parent_node_index = i//2
        # 替换节点位置为根节点或者值比父节点小
        if i == 1 or replace_node.freq < self._value[parent_node_index].freq:
            self.percDown(i)
        else:
            self.percUp(i)

        return deleted_node


def buidMinHeap(seq):
    h = MinHeap()
    for i, v in enumerate(seq):
        h.insert(v)
        h.percUp(i+1)

    return h


def leftRotate(z):
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2

    z.left_height = z.left.left_height + 1
    z.right_height = z.right.right_height + 1

    y.left_height = y.left.left_height + 1
    y.right_height = y.right.right_height + 1

    return y


def rightRotate(z):
    y = z.left
    t3 = y.right

    y.right = z
    z.left = t3

    z.left_height = z.left.left_height + 1
    z.right_height = z.right.right_height + 1

    y.left_height = y.left.left_height + 1
    y.right_height = y.right.right_height + 1

    return y


def PreOrderTree(tree):
    if tree == None:
        return

    print(tree.value)
    PreOrderTree(tree.left)
    PreOrderTree(tree.right)


def buildTree():
    # 从文件中读取
    node_input_list = read_from_file()

    # print(node_input_list)
    result = []

    for node_input in node_input_list:
        # 使用数组来实现链表
        tree = []
        node_num = int(node_input[0][0])

        # 标志tree中的节点是否有其他节点指向，如果没有就是root节点
        check = [0]*node_num
        root = None

        for i in range(1, node_num+1):
            node_list = node_input[i]

            node_value = node_list[0]
            node_left = node_list[1]
            node_right = node_list[2]

            if node_left != "-":
                node_left = int(node_left)
                check[node_left] = 1
            else:
                node_left = -1

            if node_right != "-":
                node_right = int(node_right)
                check[node_right] = 1
            else:
                node_right = -1

            node = TreeNode(node_value, node_left, node_right)
            tree.append(node)

        result.append(tree)

        for k, v in enumerate(check):
            if v == 0:
                root = tree[k]
                result.append(root)
                break

    return result


def read_from_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help="file name")
    args = parser.parse_args()

    tree_list = []
    with open(args.f, "r") as f:
        node_input = []
        for i in f:
            if i.strip() == "?":
                tree_list.append(node_input)
                node_input = []
                continue
            node_input.append(i.strip().split(' '))

        return tree_list


def buildTree_listLeaves():
    # 从文件中读取
    node_input_list = read_from_file()

    # print(node_input_list)
    result = []

    for node_input in node_input_list:
        # 使用数组来实现链表
        tree = []
        node_num = int(node_input[0][0])

        # 标志tree中的节点是否有其他节点指向，如果没有就是root节点
        check = [0]*node_num
        root = None

        for i in range(1, node_num+1):
            node_list = node_input[i]

            node_value = i - 1
            node_left = node_list[0]
            node_right = node_list[1]

            if node_left != "-":
                node_left = int(node_left)
                check[node_left] = 1
            else:
                node_left = -1

            if node_right != "-":
                node_right = int(node_right)
                check[node_right] = 1
            else:
                node_right = -1

            node = TreeNode(node_value, node_left, node_right)
            tree.append(node)

        result.append(tree)

        for k, v in enumerate(check):
            if v == 0:
                root = tree[k]
                result.append(root)
                break

    return result


def buildTestTree(level_order_seq):
    """
    根据层序遍历序列生成对应的二叉树
    [1,2,None,3,None,4,...]
    """
    len_seq = len(level_order_seq)
    level_order_map = {}
    root = None
    for i in range(1, len_seq+1):
        if level_order_seq[i-1] == None:
            continue

        left = None
        right = None

        if 2*i-1 < len_seq and level_order_seq[2*i-1]:
            left = level_order_map.setdefault(
                2*i, TreeNode(level_order_seq[2*i-1]))

        if 2*i < len_seq and level_order_seq[2*i]:
            right = level_order_map.setdefault(
                2*i+1, TreeNode(level_order_seq[2*i]))

        if i == 1:
            root = TreeNode(level_order_seq[i-1])
            root.left = left
            root.right = right
        else:
            parent = level_order_map[i]
            parent.left = left
            parent.right = right

    return root


def buildHuffmanTree(alphabet_map):
    """
    """
    pass


def sortMapByValue(origin_map):
    return OrderedDict(sorted(origin_map.items(), key=lambda kv: kv[1]))


if __name__ == '__main__':
    pass
