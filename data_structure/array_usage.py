# Access
# Time complexity : O(1)

def access_case():
    arr = [10, 20, 30, 40, 50]
    print(arr[2])  # 30에 바로 접근 (인덱스 2)




# Search
# Time complexity : O(n)

def search_case():
    arr = [10, 20, 30, 40, 50]
    target = 40

    # 선형 탐색
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"{target}은 인덱스 {i}에 있습니다.")




# Insert
# Time complexity : O(n)

def insert_case():
    arr = [10, 20, 30, 40, 50]
    arr.insert(2, 25)  # 인덱스 2에 25 삽입 → 이후 요소들 한 칸씩 밀림
    print(arr)  # [10, 20, 25, 30, 40, 50]




# Delete
# Time complexity : O(n)

def delete_case():
    arr = [10, 20, 30, 40, 50]
    del arr[2]  # 인덱스 2 (30) 삭제 → 이후 요소들 한 칸씩 당김
    print(arr)  # [10, 20, 40, 50]




# The case of inserting/deleting the ending element.
# Time complexity : O(1)

def insert_delete_endpoint():
    arr = [10, 20, 30]
    arr.append(40)   # O(1)
    print(arr)       # [10, 20, 30, 40]

    arr.pop()        # O(1) — 마지막 요소 삭제
    print(arr)       # [10, 20, 30]




'''

<Methods summary>

- insert(i, x)
- del arr[i]
- append(x)
- pop()

'''