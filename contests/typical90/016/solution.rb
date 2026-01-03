N = gets.to_i
a = gets.split.map(&:to_i)
a.sort!.reverse!
b = [0,0,0]
b[0] = N/a[0]
b[1] = (N-a[0]*b[0])/a[1]
b[2] = (N-a[0]*b[0]-a[1]*b[1])/a[2]
min = 10**10
while true
  break if b[0] <= 0

  b[0] -= 1
  b[1] = (N-a[0]*b[0])/a[1]
  b[2] = (N-a[0]*b[0]-a[1]*b[1])/a[2]
  while true
    break if b[1] <= 0
    break if a[1]*b[1] + a[2]*b[2] == N - a[0]*b[0]
    break if b.sum >= 10000
    b[1] -= 1
    b[2] = (N-a[0]*b[0]-a[1]*b[1])/a[2]
  end
  if b.sum < 10000 && a[0]*b[0] + a[1]*b[1] + a[2]*b[2] == N 
    min = [min,b.sum].min 
    p b
  end 
end

puts min