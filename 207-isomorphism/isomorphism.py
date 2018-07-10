#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from common.common import TreeNode, buildTree


def sub_tree_num(root):
    num = 0
    if root.left != -1:
        num += 1
    if root.right != -1:
        num += 1

    return num


def isomorphism(tree1, root1,  tree2, root2):
    # 根节点不同
    if root1.value != root2.value:
        return False

    tree1_sub_num = sub_tree_num(root1)
    tree2_sub_num = sub_tree_num(root2)

    # 子树数量不同
    if tree1_sub_num != tree2_sub_num:
        return False

    # 只有根节点
    if tree1_sub_num == 0:
        return True

    # 只有一棵子树
    if tree1_sub_num == 1:
        tree1_sub_index = root1.left if root1.left != -1 else root1.right
        tree2_sub_index = root2.left if root2.left != -1 else root2.right

        return isomorphism(tree1, tree1[tree1_sub_index], tree2, tree2[tree2_sub_index])

    # 都有两棵子树
    if tree1_sub_num == 2:
        return (isomorphism(tree1, tree1[root1.left], tree2, tree2[root2.left]) and isomorphism(tree1, tree1[root1.right], tree2, tree2[root2.right])) or (isomorphism(tree1, tree1[root1.left], tree2, tree2[root2.right]) and isomorphism(tree1, tree1[root1.right], tree2, tree2[root2.left]))


if __name__ == '__main__':
    tree1, root1, tree2, root2 = buildTree()
    print(root1.value, root2.value)

    print(isomorphism(tree1, root1, tree2, root2))
