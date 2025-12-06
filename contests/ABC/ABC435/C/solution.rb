N = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)


down = Array.new(N+1, false)
down[1] = true
cnt = 1
high = a[0] - 1
while high != 0

  cnt += 1
  down[cnt] = true

  if cnt == N
    break
  end

  if high <= a[cnt-1] - 1
    high = a[cnt-1]
  end

  high -= 1
end

puts cnt


  