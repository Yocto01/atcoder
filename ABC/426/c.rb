N,Q = gets.chomp.split(" ").map(&:to_i)

pc = Array.new(N){ |i| [i+1,1]}
oldest = 1
Q.times do |c|
	x,y = gets.chomp.split(" ").map(&:to_i)
  cnt = 0
  if x < oldest
    puts 0
    next
  end

  for i in oldest..x
    cnt += pc[i-1][1]
    pc[y-1][1] += pc[i-1][1]
    pc[i-1][1] = 0
  end
  puts cnt
  oldest = x + 1
end

