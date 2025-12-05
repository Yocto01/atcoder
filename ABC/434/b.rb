N,M = gets.chomp.split(" ").map(&:to_i)
a = []
N.times do |i|
	a << gets.chomp.split(" ").map(&:to_i)
end


b = Array.new(M){[]}
N.times do |i|
  b[a[i][0]-1] << a[i][1]
end

M.times do |i|
  puts (b[i].sum * 1.0) / b[i].size
end
