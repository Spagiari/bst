import logging

RED = True
BLACK = False

class BST:
    class Node:
        def __init__(self, key, value, color, size, skey = None):
            self.key = key
            if skey == None:
                self.value = value
            else:
                self.value = dict()
                self.value[skey] = value
            self.color = color
            self.size = size
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    ##########################################
    # Node helper methods
    ##########################################
    @staticmethod
    def __isRed(x):
        if x == None:
            return False
        return x.color == RED

    @staticmethod
    def __size(x):
        if x == None:
            return 0
        return x.size

    def size(self):
        return BST.__size(self.root)

    def isEmpty(self):
        return self.root == None

    ########################################
    # Standard BST search
    ########################################
    @staticmethod
    def __get(x, key):
        while x != None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def get(self, key):
        if (key == None):
            raise ValueError
        return BST.__get(self.root, key)

    def contains(self, key):
        return self.get(key) != None

    #######################################
    # Red-black tree insertion
    #######################################
    @staticmethod
    def __put(h, key, val, skey = None):
        if h == None:
            return BST.Node(key, val, RED, 1, skey)

        if key < h.key:
            h.left = BST.__put(h.left, key, val, skey)
        elif key > h.key:
            h.right = BST.__put(h.right, key, val, skey)
        else:
            if skey == None:
                h.value = val
            else:
                h.value[skey] = val

        # fix-up
        if BST.__isRed(h.right) and not BST.__isRed(h.left):
            h = BST.rotate_left(h)
        if BST.__isRed(h.left) and BST.__isRed(h.left.left):
            h = BST.rotate_right(h)
        if BST.__isRed(h.left) and BST.__isRed(h.right):
            BST.flip_colors(h)
        h.size = BST.__size(h.left) + BST.__size(h.right) + 1

        return h

    def put(self, key, val, skey = None):
        if key == None:
            raise ValueError
        if val == None:
            self.delete(key)

        self.root = BST.__put(self.root, key, val, skey)
        self.root.color = BLACK

    #######################################
    # Red-black tree deletion
    #######################################
    def delete_min(self):
        if self.isEmpty():
            raise ValueError

        if not BST.__isRed(self.root.left) and not BST.__isRed(self.root.right):
            self.root = RED

        self.root = BST.__delete_min(self.root)
        if not self.isEmpty():
            self.root = BLACK

    @staticmethod
    def __delete_min(h):
        if h.left == None:
            return None

        if not BST.__isRed(h.left) and not BST.__isRed(h.left.left):
            h = BST.move_red_left(h)

        h.left = BST.__delete_min(h.left)
        return BST.balance(h)

    def delete_max(self):
        if self.isEmpty():
            raise ValueError

        if not BST.__isRed(self.root.left) and not BST.__isRed(self.root.right):
            self.root.color = RED

        self.root = BST.__delete_max(self.root)
        if not self.isEmpty():
            root.color = BLACK

    @staticmethod
    def __delete_max(h):
        if BST.__isRed(h.left):
            h = BST.rotate_right(h)

        if h.right == None:
            return None

        if not BST.__isRed(h.right) and not BST.__isRed(h.right.left):
            h = BST.move_red_right(h)

        h.right = BST.__delete_max(h.right)

        return BST.balance(h)

    def delete(self, key):
        if key == None:
            raise ValueError
        if not self.contains(key):
            return

        if not BST.__isRed(self.root.left) and not BST.__isRed(self.root.right):
            self.root.color = RED

        self.root = BST.__delete(self.root, key)
        if not self.isEmpty():
            self.root.color = BLACK

    @staticmethod
    def __delete(h, key):
        if key < h.key:
            if not BST.__isRed(h.left) and not BST.__isRed(h.left.left):
                h = BST.move_red_left(h)
            h.left = BST.__delete(h.left, key)
        else:
            if BST.__isRed(h.left):
                h = BST.rotate_right(h)
            if key == h.key and h.right == None:
                return None
            if not BST.__isRed(h.right) and not BST.__isRed(h.right.left):
                h = BST.move_red_right(h)
            if key == h.key:
                x = BST.__get_min(h.right)
                h.key = x.key
                h.value = x.value
                h.right = BST.__delete_min(h.right)
            else:
                h.right = BST.__delete(h.right, key)

        return BST.balance(h)

    ##############################################
    # Red-black tree helper functions
    ##############################################
    @staticmethod
    def rotate_right(h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = x.right.color
        x.right.color = RED
        x.size = h.size
        h.size = BST.__size(h.left) + BST.__size(h.right) + 1
        return x

    @staticmethod
    def rotate_left(h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = x.left.color
        x.left.color = RED
        x.size = h.size
        h.size = BST.__size(h.left) + BST.__size(h.right) + 1
        return x

    @staticmethod
    def flip_colors(h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    @staticmethod
    def move_red_left(h):
        BST.flip_colors(h)
        if BST.__isRed(h.right.left):
            h.right = BST.rotate_right(h.right)
            h = BST.rotate_left(h)
            BST.flip_colors(h)
        return h

    @staticmethod
    def move_red_right(h):
        BST.flip_colors(h)
        if BST.__isRed(h.left.left):
            h = BST.rotate_right(h)
            BST.flip_colors(h)
        return h

    @staticmethod
    def balance(h):
        if BST.__isRed(h.right):
            h = BST.rotate_left(h)
        if BST.__isRed(h.left) and BST.__isRed(h.left.left):
            h = BST.rotate_right(h)
        if BST.__isRed(h.left) and BST.__isRed(h.right):
            BST.flip_colors(h)

        h.size = BST.__size(h.left) + BST.__size(h.right) + 1
        return h

    #################################################
    # Utility functions
    #################################################
    def height(self):
        return BST.__height(self.root)

    @staticmethod
    def __height(h):
        if h == None:
            return -1
        return 1 + max(BST.__height(x.left), BST.__height(x.right))

    #################################################
    # Ordered symbol table methods.
    #################################################
    def get_min(self):
        if self.isEmpty():
            raise ValueError
        return BST.__get_min(self.root).key

    @staticmethod
    def __get_min(x):
        if x.left == None:
            print ('min', x)
            return x
        else:
            return BST.__get_min(x.left)

    def get_max(self):
        if self.isEmpty():
            raise ValueError
        return BST.__get_max(self.root).key

    @staticmethod
    def __get_max(x):
        if x.right == None:
            return x
        else:
            return BST.__get_max(x.right)

    def floor(self, key):
        if key == None:
            raise ValueError
        if self.isEmpty():
            raise ValueError
        x = BST.__floor(self.root, key)
        if (x == None):
            return None
        else:
            return x.key

    @staticmethod
    def __floor(x, key):
        if x == None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return BST.__floor(x.left, key)
        t = BST.__floor(x.right, key)
        if t == None:
            return x
        else:
            return t

    def ceiling(self, key):
        if key == None:
            raise ValueError
        if self.isEmpty():
            raise ValueError
        x = BST.__ceiling(self.root, key)
        if x == None:
            return None
        else:
            return x.key

    @staticmethod
    def __ceiling(x, key):
        if x == None:
            return None
        if key == x.key:
            return x
        if key > x.key:
            return BST.__ceiling(x.right, key)
        t = BST.__ceiling(x.left, key)
        if t == None:
            return x
        else:
            return t

    def select(self, k):
        if k < 0 or k >= self.size():
            raise ValueError("called select() with invalid argument: " + k)
        x = BST.__select(self.root, k)
        return x.key

    @staticmethod
    def __select(x, k):
        t = BST.__size(x.left)
        if t > k:
            return BST.__select(x.left, k)
        elif t < k:
            return BST.__select(x.right, k-t-1)
        else:
            return x

    def rank(self, key):
        if key == None:
            raise ValueError("argument to rank() is null")
        return BST.__rank(self.root, key)

    @staticmethod
    def __rank(x, key):
        if x == None:
            return 0
        if key < x.key:
            return BST.__rank(x.left, key)
        elif key > x.key:
            return 1 + BST.__size(x.left) + BST.__rank(x.right, key)
        else:
            return BST.__size(x.left)

    ###############################################
    # Range count and range search.
    ###############################################
    def get_all_keys(self):
        if self.isEmpty():
            return list()
        return self.get_range_keys(self.get_min(), self.get_max())

    def get_range_keys(self, lo, hi):
        if lo == None:
            raise ValueError
        if hi == None:
            raise ValueError

        q = list()
        BST.__get_range_keys(self.root, q, lo, hi)
        return q

    @staticmethod
    def __get_range_keys(x, q, lo, hi):
        if x == None:
            return
        if lo < x.key:
            BST.__get_range_keys(x.left, q, lo, hi)
        if lo <= x.key and hi >= x.key:
            q.append(x.key)
        if hi > x.key:
            BST.__get_range_keys(x.right, q, lo, hi)

###
    def get_data_all_keys(self):
        if self.isEmpty():
            return list()
        return self.get_data_range_keys(self.get_min(), self.get_max())

    def get_data_range_keys(self, lo, hi):
        log = logging.getLogger('BST.get_range_keys')
        log.info('start')
        if lo == None:
            raise ValueError
        if hi == None:
            raise ValueError

        q = list()
        BST.__get_data_range_keys(self.root, q, lo, hi)
        log.info('end')
        return q

    @staticmethod
    def __get_data_range_keys(x, q, lo, hi):
        if x == None:
            return
        if lo < x.key:
            BST.__get_data_range_keys(x.left, q, lo, hi)
        if lo <= x.key and hi >= x.key:
            for k in x.value:
                q.append(x.value[k])
        if hi > x.key:
            BST.__get_data_range_keys(x.right, q, lo, hi)

    #######################################################
    # Check integrity of red-black tree data structure.
    #######################################################
    def check(self):
        if not self.isBST():
            print ("Not in symmetric order")
        if not self.isSizeConsistent():
            print ("Subtree counts not consistent")
        if not self.isRankConsistent():
            print ("Ranks not consistent")
        if not self.is23():
            print ("Not a 2-3 tree")
        if not self.isBalanced():
            print ("Not balanced")
        return self.isBST() and self.isSizeConsistent() and \
                self.isRankConsistent() and self.is23() and \
                self.isBalanced();

    def isBST(self):
        return BST.__isBST(self.root, None, None)

    @staticmethod
    def __isBST(x, lo, hi):
        if x == None:
            return True
        if lo != None and x.key <= lo:
            return False
        return BST.__isBST(x.left, lo, x.key) and \
               BST.__isBST(x.right, x.key, hi)

    def isSizeConsistent(self):
        return BST.__isSizeConsistent(self.root)

    @staticmethod
    def __isSizeConsistent(x):
        if x == None:
            return True
        if x.size != BST.__size(x.left) + BST.__size(x.right) + 1:
            return False
        return BST.__isSizeConsistent(x.left) and BST.__isSizeConsistent(x.right)

    def isRankConsistent(self):
        for i in range(0, self.size()):
            if i != self.rank(self.select(i)):
                return False
        for key in self.get_all_keys():
            if key != self.select(self.rank(key)):
                return False
        return True

    def is23(self):
        return self.__is23(self.root)

    def __is23(self, x):
        if x == None:
            return True
        if BST.__isRed(x.right):
            return False
        if x != self.root and BST.__isRed(x) and BST.__isRed(x.left):
            return False
        return self.__is23(x.left) and self.__is23(x.right)

    def isBalanced(self):
        black = 0
        x = self.root
        while x != None:
            if not BST.__isRed(x):
                black += 1
            x = x.left
        return BST.__isBalanced(self.root, black)

    @staticmethod
    def __isBalanced(x, black):
        if x == None:
            return black == 0
        if not BST.__isRed(x):
            black -= 1
        return BST.__isBalanced(x.left, black)  and BST.__isBalanced(x.right, black)
