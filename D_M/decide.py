from collections import Counter
from contextlib import contextmanager
from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return '%s' % self.data

class HistoryList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value=None):
        """
        Adds a new node with that value to the head of the list with an O(1) Time performance.

        arguments: value : any
        returns: None
        """
        node = value
        if type(value) != "class 'linked_list.Node'":
            node = Node(value)

        if self.head:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.head.previous = None
        else:
            self.head = node
            self.head.previous = None
            self.tail = self.head
            self.tail.next = None
        return self
    def includes(self, data):
        for node in self:
            if node.data == data:
                return node.next
        else:
            return False
    def kth_from_end(self,k):
        current = self.tail
        count = 0
        while current:
            if count == k:
                return current.data
            count+=1
            current = current.previous

class DesicionMaker:
    def __init__(self):
        self.score = 0
        self.rolled = None
        self.history_list = HistoryList()
    
    def decide(self):
        result = []
        for number in self.rolled:
            appears = self.rolled[number]
            if appears >= 3 and number == 1:
                self.score += (number * 1000) * (appears - 2)
                for _ in range(appears):
                    result.append(number)

            if appears >= 3 and number != 1:
                self.score += (number * 100) * (appears - 2)
                for _ in range(appears):
                    result.append(number)

            if appears < 3 and number == 1:
                self.score += 100 * appears
                for _ in range(appears):
                    result.append(number)

            if appears < 3 and number == 5:
                self.score += 50 * appears
                for _ in range(appears):
                    result.append(number)
        
        remaining = [x for x in self.rolled  if x not in tuple(result)]
        desicion = "".join(str(digit) for digit in result)

        return desicion,remaining

    def determin(self,rolled):
        self.rolled = Counter(rolled)
        
        
        def decide_save():
            desicion,remaining = self.decide()
            take_next_risk = True if len(remaining) > 3 else False
            yield [desicion,remaining]
            self.history_list.insert(tuple([desicion,take_next_risk]))
            
        # desicion = self.history_list.includes(rolled) 
        #-return [desicion] if desicion else decide_save()
        
        return decide_save()
        



 