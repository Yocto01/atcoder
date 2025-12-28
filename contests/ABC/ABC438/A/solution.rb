D,F = gets.split.map(&:to_i)
a = F
while a <= D
  a += 7
end
puts a == D ? 7 : a - D