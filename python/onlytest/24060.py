def merge_sort(array, start, end): # a[start..r]을 오름차순 정렬한다.
    if (start < end):
        mid = (start + end) // 2     # q는 start, r의 중간 지점
        merge_sort(array, start, mid)      # 전반부 정렬
        merge_sort(array, mid + 1, end)  # 후반부 정렬
        merge(array, start, mid, end)        # 병합

# a[p..q]와 a[q+1..r]을 병합하여 a[p..r]을 오름차순 정렬된 상태로 만든다.
# a[p..q]와 a[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(array, start, mid, end):
    global cnt, result
    
    i = start
    j = mid + 1
    tmp = []
    while (i <= mid and j <= end):
        if (array[i] <= array[j]):
            tmp.append(array[i]) # tmp[t] <- array[i]; t++; i++;
            i += 1
        else:
            tmp.append(array[j]) # tmp[t] <- array[j]; t++; j++;
            j += 1
    
    while (i <= mid):  # 왼쪽 배열 부분이 남은 경우
        tmp.append(array[i])
        i += 1
    
    while (j <= end):  # 오른쪽 배열 부분이 남은 경우
        tmp.append(array[j])
        j += 1
    
    i = start
    t = 0
    while (i <= end):  # 결과를 array[p..end]에 저장
        array[i] = tmp[t]
        cnt += 1 # 새로 저장할 때마다 카운트 +1
        if cnt == k: # 원하는 k만큼 저장했다면
            result = array[i] # 그때 저장한 값을 result에 저장함
            break # 문제에서 원하는 건 result값이므로 바로 종료함
        i += 1
        t += 1 


n, k = map(int, input("").split())
nums = list(map(int, input("").split()))

cnt = 0
result = -1

merge_sort(nums, 0, len(nums)-1)
print(result)