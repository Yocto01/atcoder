N = gets.chomp.to_i
a = []
N.times do |i|
  a << gets.chomp.split(" ").map(&:to_i)
end

val = 2000*2000
unique = Array.new(N,0)
total = 0
for i in 1..2000
  for j in 1..2000
    cloud = []
    N.times do |n|
      cloud << n if a[n][0] <= i && a[n][1] >= i && a[n][2] <= j && a[n][3] >= j 
    end
    unique[cloud[0]] += 1 if cloud.size == 1
    total += 1 if cloud.size != 0
  end
end

N.times do |i|
  puts val - total + unique[i]
end
      