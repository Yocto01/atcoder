X = gets.chomp.to_i
N = gets.chomp.to_i
W = gets.chomp.split(" ").map(&:to_i)
Q = gets.chomp.to_i
P = []
Q.times do |i|
  P << gets.chomp.to_i
end
setted = Array.new(N, 0)

P.each do |p|
  setted[p-1] = (setted[p-1] + 1) % 2
  val = X
  N.times do |i|
    val += setted[i] * W[i]
  end
  puts val
end
