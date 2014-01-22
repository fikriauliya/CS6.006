def naive_search(seq):
  for i in range(0, len(seq)):
    if ((len(seq) == 1) or
      (i == 0 and seq[i] > seq[i+1]) or 
      (i == len(seq) - 1 and seq[i] > seq[i-1]) or 
      (seq[i] > seq[i-1] and seq[i] > seq[i+1])):
      return seq[i]
  return None

def divide_and_conquer_search(seq):
  def divide_and_conquer_search_rec(seq, left, right):
    if left > right:
      return None
    if left == right:
      return seq[left]
    if right - left == 1:
      return max(seq[left], seq[right])
    
    half = left + (right - left) // 2
    if seq[half] > seq[half - 1] and seq[half] > seq[half + 1]:
      return seq[half]
    if seq[half] < seq[half - 1]:
      return divide_and_conquer_search_rec(seq, left, half - 1)
    if seq[half] < seq[half + 1]:
      return divide_and_conquer_search_rec(seq, half + 1, right)

  return divide_and_conquer_search_rec(seq, 0, len(seq) - 1)