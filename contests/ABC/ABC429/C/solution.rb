N = gets.to_i
A = gets.split.map(&:to_i)

hash = Hash.new()
A.each do |val|
  if hash.has_key?(val)
    hash[val] += 1
  else
    hash[val] = 1
  end
end

res = 0
(hash.values).each do |cnt|
  res += (cnt*(cnt-1)/2) * (N-cnt)
end
puts res