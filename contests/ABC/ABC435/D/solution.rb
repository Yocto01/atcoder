n,m = gets.chomp.split(" ").map(&:to_i)
a = Array.new(n+1){[]}
a2 = Array.new(n+1){[]}
b = Array.new(n+1, false)
m.times do |i|
 x,y = gets.chomp.split(" ").map(&:to_i)
 #a[x] << y
 a2[y] << x
 #p a
 #p a2
end

q = gets.chomp.to_i
q.times do |i|
  q1,q2 = gets.chomp.split(" ").map(&:to_i)
  if q1 == 1
    queue = [q2]
    while true
      break if queue.empty?
      p = queue.shift
      next if b[p]
      b[p] = true

      a2[p].each do |j|
        next if b[j]
        queue << j
      end
    end
    #p b
  else
    ok = false
    a[q2].each do |j|
      if b[j]
        ok = true
      end
    end
    ok = true if b[q2]
    if ok
      puts "Yes"
    else
      puts "No"
    end
  end
end
#p b

