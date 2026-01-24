H,W = gets.chomp.split(" ").map(&:to_i)
a = []
H.times do |i|
	a << gets.chomp.split(" ").map(&:to_i)
end

p a
