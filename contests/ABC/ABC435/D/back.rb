n,m = gets.chomp.split(" ").map(&:to_i)
a = Array.new(n+1){[]}
a2 = Array.new(n+1){[]}
b = Array.new(n+1, false)
m.times do |i|
 x,y = gets.chomp.split(" ").map(&:to_i)
 a[x] << y
 a2[y] << x
 visited = Array.new(n+1,false)
 queue = []
 a2[x].each do |j|
  queue << j
 end
 while true
  break if queue.empty?

  p, = queue.shift
  next if visited[p]
  visited[p] = true
  a[p] = a[p] | a[x]
  queue += a2[p]
 
 end
 p a
 p a2
end

q = gets.chomp.to_i
q.times do |i|
  q1,q2 = gets.chomp.split(" ").map(&:to_i)
  if q1 == 1
    b[q2] = true
  else
    can = false
    a[q2].each do |j|
      if b[j]
        can = true
      end
    end
    can = true if b[q2]
    if can
      puts "Yes"
    else
      puts "No"
    end
  end
end
#p b

