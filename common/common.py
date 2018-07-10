#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse


class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


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


def read_from_cmd():
    pass


if __name__ == '__main__':
    read_from_cmd()
