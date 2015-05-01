#!/usr/bin/python3

import unittest


class _Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        # Start with a dummy head so iteration is more straightforward.
        self.head = _Node()

    def __len__(self):
        '''return length of list.'''
        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def append(self, value):
        '''append value to end.'''
        current = self.head
        while current.next:
            current = current.next
        current.next = _Node(value, current.next)
        

    def appendfront(self, value):
        '''append value to front.'''
        current = self.head
        current.next = _Node(value, current.next)

    def clear(self):
        '''remove all values.'''
        #current = self.head
        #while current:
        #pass

    def count(self, value):
        '''return number of occurrences of value.'''
        current = self.head
        count = 0
        while current.next:
            if current.next.value == value:
                count += 1
                current = current.next
            else:
                current = current.next
        return count

    def index(self, value):
        '''
        return first index of value.
        Raises ValueError if the value is not present.
        '''
        current = self.head
        count = 0
        while current.next:
            if current.next.value == value:
                return count
            else: 
                current = current.next
                count += 1
        return ValueError

    def pop(self):
        '''remove and return last item.'''
        pass  # TODO

    def popfront(self):
        '''remove and return first item.'''
        pass  # TODO

    def remove(self, value):
        '''
        remove first occurrence of value.
        Raises ValueError if the value is not present.
        '''
        pass  # TODO


class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_length_empty(self):
        self.assertEqual(0, len(self.list))

    def test_index_while_empty(self):
        self.assertRaises(ValueError, lambda: self.list.index(42))

    def test_remove_while_empty(self):
        self.assertRaises(ValueError, lambda: self.list.remove(42))

    def test_count_while_empty(self):
        self.assertEqual(0, self.list.count(42))

    def test_length(self):
        self.list.append(42)
        self.assertEqual(1, len(self.list))

    def test_index(self):
        self.list.append(42)
        self.assertEqual(0, self.list.index(42))

    def test_remove(self):
        self.list.append(42)
        self.list.remove(42)

    def test_count(self):
        self.list.append(42)
        self.assertEqual(1, self.list.count(42))

    # TODO: Add more test cases as needed.


if __name__ == '__main__':
    unittest.main()

