#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse


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

    def percUp(self, i):
        """
        调整为最小堆
        """
        i = self.length
        while i/2 > 0:
            if self._value[i] < self._value[i/2]:
                self._value[i], self._value[i /
                                            2] = self._value[i/2], self._value[i]

                i = i/2
            else:
                break

    def rootPath(self, i):
        """
        指定位置元素到root节点的路径打印，下表从1开始
        """
        while i > 0 and i <= self.length:
            print(self._value[i])
            i = i / 2


def buidMinHeap(seq):
    h = MinHeap()
    for i in seq:
        h.insert(i)
        h.percUp(i)

    return h


def Insert(tree, v):
    if tree.value == None:
        tree.value = v
        return
    else:
        node = TreeNode(v)
        while tree.value != None:
            if v > tree.value:
                tree.right_height += 1

                if tree.right != None:
                    tree = tree.right
                else:
                    tree.right = node
                    return
            else:
                tree.left_height += 1
                if tree.left != None:
                    tree = tree.left
                else:
                    tree.left = node
                    return

            if tree.right_height-tree.left_height > 1:
                if v > tree.right.value:
                    # RR rotate
                    tree = leftRotate(tree)
                else:
                    # RL rotate
                    rightRotate(tree.right)
                    tree = leftRotate(tree)

            if tree.left_height - tree.right_height > 1:
                if v < tree.left.value:
                    # LL rotate
                    tree = rightRotate(tree)
                else:
                    # LR rotate
                    leftRotate(tree.left)
                    tree = rightRotate(tree)


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
                2*i, TreeNode(level_order_seq[2*i-1], None, None))

        if 2*i < len_seq and level_order_seq[2*i]:
            right = level_order_map.setdefault(
                2*i+1, TreeNode(level_order_seq[2*i], None, None))

        if i == 1:
            root = TreeNode(level_order_seq[i-1], left, right)
        else:
            parent = level_order_map[i]
            parent.left = left
            parent.right = right

    return root


if __name__ == '__main__':
    read_from_cmd()
