N = gets.to_i
A,B,C = gets.split.map(&:to_i)

P = 9999
min = P + 1

(0..P).each do |x| 
  (0..P).each do |y|
    tmp = x * A + y * B
    next if (N - tmp) % C != 0 || tmp > N
    z = (N - tmp) / C
    if min > x + y + z
      min = x + y + z
    end
  end
end

p min