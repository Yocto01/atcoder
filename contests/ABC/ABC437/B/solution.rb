H,W,N = gets.chomp.split(" ").map(&:to_i)
a = []
H.times do |i|
	a << gets.chomp.split(" ").map(&:to_i)
end
b = []
N.times do |i|
	b << gets.to_i
end

shouted = Array.new(H) { Array.new(W, false) }
b.each do |x|
  H.times do |i|
    W.times do |j|
      if a[i][j] == x
        shouted[i][j] = true
      end
    end   
  end 
end

H.times do |i|
  shouted[i].delete(false)
  shouted[i] = shouted[i].size
end
puts shouted.max