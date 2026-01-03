N = gets.to_i
A,B = [],[]
N.times do
  c,p = gets.split.map(&:to_i)
  A << (c == 1 ? p : 0)
  B << (c == 2 ? p : 0)
end

A2,B2 = Array.new(N+1,0),Array.new(N+1,0)
N.times do |i|
  A2[i+1] = A2[i] + A[i]
  B2[i+1] = B2[i] + B[i]
end

Q = gets.to_i
Q.times do
  l,r = gets.split.map(&:to_i)
  puts "#{A2[r]-A2[l-1]} #{B2[r]-B2[l-1]}"
end

