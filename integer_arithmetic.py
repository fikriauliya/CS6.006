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