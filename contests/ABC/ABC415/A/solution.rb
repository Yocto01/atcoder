N = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)
X = gets.chomp.to_i


puts (a.include?(X) ? "Yes" : "No")