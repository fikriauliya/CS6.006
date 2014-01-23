def naive_search(seq):
  for i in range(0, len(seq)):
    if ((len(seq) == 1) or
      (i == 0 and seq[i] > seq[i+1]) or 
      (i == len(seq) - 1 and seq[i] > seq[i-1]) or 
      (seq[i] > seq[i-1] and seq[i] > seq[i+1])):
      return seq[i]
  return None

def divide_and_conquer_search(seq):
  def divide_and_conquer_search_rec(left, right):
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
      return divide_and_conquer_search_rec(left, half - 1)
    if seq[half] < seq[half + 1]:
      return divide_and_conquer_search_rec(half + 1, right)

  return divide_and_conquer_search_rec(0, len(seq) - 1)

def naive_2d_search(seq):
  (width, height) = (len(seq[0]), len(seq))
  is_visited = [[False for x in range(0, width)] for y in range(0, height)]

  def get_val(pos_y, pos_x):
    if pos_x >= 0 and pos_x < width and pos_y >= 0 and pos_y < height: return seq[pos_y][pos_x]
    else: return None

  (pos_x, pos_y) = (0, 0)
  while (True):
    is_visited[pos_y][pos_x] = True

    new_positions = [(pos_y, pos_x - 1), (pos_y, pos_x + 1), (pos_y - 1, pos_x), (pos_y + 1, pos_x)]
    new_position_vals = [get_val(*p) for p in new_positions]
    max_val = new_position_vals[0]
    max_val_index = 0
    for i, val in enumerate(new_position_vals):
      (max_val, max_val_index) = (val, i) if val != None and not is_visited[new_positions[i][0]][new_positions[i][1]] and (max_val == None or val >= max_val) else (max_val, max_val_index)
    
    if max_val == None or seq[pos_y][pos_x] > max_val:
      return seq[pos_y][pos_x]
    else:
      (new_pos_y, new_pos_x) = new_positions[max_val_index]
      if is_visited[new_pos_y][new_pos_x]:
        return seq[pos_y][pos_x]
      else:
        pos_y, pos_x = new_pos_y, new_pos_x

def divide_and_conquer_2d_search(seq):
  (width, height) = (len(seq[0]), len(seq))
  
  def divide_and_conquer_2d_search_rec(left, right):    
    def get_val(pos_y, pos_x):
      if pos_x >= left and pos_x <= right and pos_y >= 0 and pos_y < height: return seq[pos_y][pos_x]
      else: return None

    pos_x = left + (right - left) // 2

    vertical_slice = [seq[i][pos_x] for i in range(0, height)]
    max_val = max(vertical_slice)
    pos_y = vertical_slice.index(max_val)
    left_val = get_val(pos_y, pos_x - 1)
    right_val = get_val(pos_y, pos_x + 1)

    if left_val != None and right_val != None and max_val <= left_val and left_val == right_val:
      return max(divide_and_conquer_2d_search_rec(left, pos_x - 1), divide_and_conquer_2d_search_rec(pos_x + 1, right))
    elif left_val != None and max_val <= left_val:
      return divide_and_conquer_2d_search_rec(left, pos_x - 1)
    elif right_val != None and max_val <= right_val:
      return divide_and_conquer_2d_search_rec(pos_x + 1, right)
    else:
      return max_val
  
  return divide_and_conquer_2d_search_rec(0, width - 1)