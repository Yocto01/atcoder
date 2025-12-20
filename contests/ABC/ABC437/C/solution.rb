T = gets.to_i
T.times do
  n = gets.to_i
  a = []
  b = []
  psum = 0
  n.times do 
    w,p = gets.split.map(&:to_i)
    a << [w,p]
    b << w+p
    psum += p
  end
  b.sort!
  ans = 0
  n.times do |i|
    if psum - b[i] >= 0
      ans += 1
      psum -= b[i]
    else
      break
    end
  end
  p ans
end