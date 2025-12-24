N = gets.to_i

arr = ["(",")"]

def is_correct?(sc)
  n = 0
  sc.each do |c|
    return false if n < 0
    n += 1 if c == "("
    n -= 1 if c == ")"
  end
  n == 0 ? true : false
end

res = []
arr.repeated_permutation(N) do |bits|
  res << bits.join if is_correct?(bits)
end

res.sort!
res.each do |r|
  puts r
end
