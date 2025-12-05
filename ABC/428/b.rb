N,K = gets.chomp.split(" ").map(&:to_i)
S = gets.chomp

hash = Hash.new()
N.times do |i|
  break if i + K > N

  substr = S[i...i+K]
  if hash.has_key?(substr)
    hash[substr] += 1
  else
    hash[substr] = 1
  end
end

max = 0
hash.each do |key,value|
  max = [max,value].max
end

maxstr = []
hash.each do |key,value|
  maxstr << key if value == max
end

maxstr.sort!

puts max
puts maxstr.join(" ")
