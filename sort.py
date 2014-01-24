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