import math

def catalan_number_count_rec(number_of_parantheses_pairs):
  """
  0: empty
  1: ()
  2: ()(), (())
    (0)+1: ()()
    (1)+0: (())
  3: ()()(), (()()), ()(()), (())(), ((()))
    (0)+2: ()()(), ()(())
    (1)+1: (())()
    (2)+0: (()()), ((()))
  """
  if number_of_parantheses_pairs == 0: return 1
  if number_of_parantheses_pairs == 1: return 1

  sum_of_factors = 0
  for i in range(0, number_of_parantheses_pairs):
    sum_of_factors += (catalan_number_count_rec(i) * catalan_number_count_rec(number_of_parantheses_pairs - i - 1))

  return sum_of_factors

def catalan_number_count_iterative(number_of_parantheses_pairs):
  if number_of_parantheses_pairs == 0 or number_of_parantheses_pairs == 1: return 1

  catalans = [0 for _ in range(0, number_of_parantheses_pairs + 1)]
  catalans[0] = 1
  catalans[1] = 1
  for i in range(2, number_of_parantheses_pairs + 1):
    for j in range(0, i):
      catalans[i] += catalans[j] * catalans[i - j - 1]

  return catalans[number_of_parantheses_pairs]

def square_root(number, precision = 4):
  prev_iteration_result = 1
  for i in range(precision):
    cur_iteration_result = (prev_iteration_result + number/prev_iteration_result) / 2
    prev_iteration_result = cur_iteration_result

  return prev_iteration_result

def multiply(x, y):
  if x == 0 or y == 0: return 0
  sign = 1
  if (x < 0 and y > 0) or (x > 0 and y < 0): sign = -1
  x = abs(x)
  y = abs(y)
  max_digit = max(x.bit_length(), y.bit_length())

  if max_digit == 1: return 1

  half_digit = max_digit // 2
  filter_mask = (1 << half_digit) - 1

  x_upper_half = x >> half_digit
  x_lower_half = x & filter_mask
  y_upper_half = y >> half_digit
  y_lower_half = y & filter_mask

  abs_res = ((multiply(x_upper_half, y_upper_half)  << half_digit << half_digit) +
          ((multiply(x_lower_half, y_upper_half) + multiply(x_upper_half, y_lower_half)) << half_digit) +
          (multiply(x_lower_half, y_lower_half)))
  if sign == -1: return ~abs_res + 1
  else: return abs_res

def karatsuba_multiply(x, y):
  if x == 0 or y == 0: return 0
  sign = 1
  if (x < 0 and y > 0) or (x > 0 and y < 0): sign = -1
  x = abs(x)
  y = abs(y)
  max_digit = max(x.bit_length(), y.bit_length())

  if max_digit == 1: return 1

  half_digit = max_digit // 2
  filter_mask = (1 << half_digit) - 1

  x_upper_half = x >> half_digit
  x_lower_half = x & filter_mask
  y_upper_half = y >> half_digit
  y_lower_half = y & filter_mask

  z_0 = karatsuba_multiply(x_lower_half, y_lower_half)
  z_2 = karatsuba_multiply(x_upper_half, y_upper_half)
  z_1 = karatsuba_multiply((x_lower_half + x_upper_half), (y_lower_half + y_upper_half)) - z_0 - z_2

  abs_res = ((z_2  << half_digit << half_digit) +
          (z_1 << half_digit) +
          z_0)
  if sign == -1: return ~abs_res + 1
  else: return abs_res