N = gets.to_i
A = gets.split.map(&:to_i)
B = gets.split.map(&:to_i)
C = gets.split.map(&:to_i)

a = Array.new(N+1,0)
b = Array.new(N+1,0)
c = Array.new(N+1,0)
N.times do |i|
  a[i+1] = a[i] + A[i]
  b[i+1] = b[i] + B[i] + A[i]
  c[i+1] = c[i] + C[i] + B[i]
end
p a
p b
p c