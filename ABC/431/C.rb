N,M,K = gets.chomp.split(" ").map(&:to_i)
H = gets.chomp.split(" ").map(&:to_i)
B = gets.chomp.split(" ").map(&:to_i)

H.sort!.reverse!
B.sort!.reverse!

Hmin = H[N-K...N]
Bmax = B[0...K]

K.times do |i|
  if Hmin[i] > Bmax[i]
    puts "No"
    return
  end
end
puts "Yes"