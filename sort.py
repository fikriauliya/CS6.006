def insertion_sort(seq):
  for i in range(0,len(seq)):
    for j in range(i, 0, -1):
      if seq[j] < seq[j-1]:
        seq[j], seq[j-1] = seq[j-1], seq[j]
      else:
        break
  return seq

def merge_sort(seq):
  def merge_sort_rec(left, right):
    if left > right:
      return []
    elif left == right:
      return [seq[left]]
    else:
      mid = left + (right - left) // 2
      sorted_left = merge_sort_rec(left, mid)
      sorted_right = merge_sort_rec(mid + 1, right)
      merged = []
      while len(sorted_left) > 0 and len(sorted_right) > 0:
        if sorted_left[0] <= sorted_right[0]:
          merged.append(sorted_left.pop(0))
        else:
          merged.append(sorted_right.pop(0))
      merged.extend(sorted_left)
      merged.extend(sorted_right)
      return merged

  return merge_sort_rec(0, len(seq) - 1)

def min_heap_sort(seq):
  def min_heapify(seq, index):
    left = index * 2 + 1
    right = index * 2 + 2

    if left >= len(seq): return
    elif seq[index] <= seq[left] and (right >= len(seq) or seq[index] <= seq[right]): return
    elif (right >= len(seq) or seq[left] <= seq[right]):
      seq[index], seq[left] = seq[left], seq[index]
      min_heapify(seq, left)
    else:
      seq[index], seq[right] = seq[right], seq[index]
      min_heapify(seq, right)

  def extract_min(seq):
    (seq[0], seq[len(seq)-1]) = (seq[len(seq)-1], seq[0])
    res = seq.pop()
    min_heapify(seq, 0)
    return res

  for i in range((len(seq)-2)//2, -1, -1):
    min_heapify(seq, i)

  sorted_seq = []
  while len(seq) > 0:
    sorted_seq.append(extract_min(seq))

  return sorted_seq