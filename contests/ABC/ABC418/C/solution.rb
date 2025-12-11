N,Q = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)

m = A.max
imos = Array.new(m+2,0)
prefix = Array.new(m+2,0)
A.each do |a|
  imos[1] += 1
  imos[a+1] -= 1
end

prefix[0] = 1
(m+1).times do |i|
  next if m >= imos.size
  imos[i+1] += imos[i]
  prefix[i+1] = imos[i] + prefix[i]
end
#p imos
#p prefix

Q.times do
  b = gets.to_i
  if b > m
    puts -1
    next
  end
  puts prefix[b]
end
