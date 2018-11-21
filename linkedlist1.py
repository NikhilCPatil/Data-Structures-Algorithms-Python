
class NodeClass(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insertStart(self, data):

        self.size = self.size + 1
        newNode = NodeClass(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # O(1)
    def size(self):
        return self.size

    # O(n)
    def insertEnd(self, data):
        self.size += 1
        newNode = NodeClass(data)
        actulanode = self.head

        while actulanode.nextNode is not None:
            actulanode = actulanode.nextNode
        actulanode.nextNode = newNode


# O(n)
    def traverceList(self):
        actulanode = self.head

        while actulanode is not None:
            print("%d" % actulanode.data)
            actulanode = actulanode.nextNode

    def get_from_position(self,position):

        actulanode = self.head
        counter = 1
        while actulanode:
            if counter == position:
                return actulanode.data
            else:
                actulanode = actulanode.nextNode
                counter+=1
        return 0

    def removeNode(self,data):

        previous = None
        actulanode = self.head
        counter = 1
        while actulanode:
            if actulanode.data == data:
                if counter == 1:
                    actulanode.nextNode = self.head
                else:
                    previous.nextNode = actulanode.nextNode
                    return
            counter+=1
            previous = actulanode
            actulanode = previous.nextNode




linkedlist = Linkedlist()
linkedlist.insertStart(25)
linkedlist.insertStart(35)
linkedlist.insertStart(89)
linkedlist.insertEnd(95)
print("----------------")
linkedlist.traverceList()
linkedlist.removeNode(35)
print("----------------")
linkedlist.traverceList()
# print("Data at position 5 is %d" % linkedlist.get_from_position(1))
