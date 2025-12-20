N = gets.to_i
S = gets.chomp

(N-S.size).times do
  S = "o" + S
end

puts S