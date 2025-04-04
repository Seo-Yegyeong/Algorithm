# 노드 클래스

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




# Linked list 클래스

class LinkedList:
    def __init__(self):
        self.head = None




    # Linked list 출력

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")




    # 값 탐색 (인덱스 반환)

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1  # 못 찾은 경우
    



    # Linked list 끝에 요소 추가

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # 빈 리스트일 경우
            self.head = new_node
            return
        current = self.head
        while current.next:  # 새 노드를 추가하기 위해 끝 노드까지 이동
            current = current.next
        current.next = new_node




    # 특정 위치에 삽입 (0-based index)

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("인덱스가 범위를 벗어났습니다.")
            current = current.next
        new_node.next = current.next
        current.next = new_node




    # 값으로 삭제 (처음 나타나는 값만)

    def delete(self, data):
        current = self.head
        if current is None:
            return

        # 첫 번째 노드가 삭제 대상일 때

        if current.data == data:
            self.head = current.next
            return

        # 중간 또는 끝 노드 삭제

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("값을 찾을 수 없습니다.")
            return

        prev.next = current.next




'''

<Methods summary>

- search(data) : 해당 값의 인덱스 반환
- append() : 끝에 추가
- insert(index, data) : 중간에 삽입
- delete(data) : 해당 값 삭제

'''