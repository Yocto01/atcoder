N,Q = gets.chomp.split(" ").map(&:to_i)
a = Array.new(N+1, false)
cnt = N

Q.times do |c|
  l,r = gets.chomp.split(" ").map(&:to_i) 
  
  for i in l..r
    cnt -= 1 if !a[i]
    a[i] = true
  end
  puts cnt
end