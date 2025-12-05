S,A,B,X = gets.chomp.split(" ").map(&:to_i)

ans = 0
X.times do |i|
  if i % (A + B) < A
    ans += S
  end
end

puts ans