  def draw_tree(self, level=0, prefix=""):
        if self.rightChild:
            self.rightChild.draw_tree(level + 1, prefix + "    ")
        print(" " * 4 * level + prefix + str(self.root))
        if self.leftChild:
            self.leftChild.draw_tree(level + 1, prefix + "    ")
