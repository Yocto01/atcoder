N = gets.to_i
return if N.odd?

s = []
s2 = []
(N/2).times do |i|
  if i == 0
    s << "()"
    s2 << "()"
    next
  end

  s.each do |a|
    p = "(" * (i+1-a.length/2) + ")" * (i+1-a.length/2);
    s2 << a + p
    (p.length-1).times do |i|
      s2 << p[0..i] + a + p[i+1...p.length]
    end
    s2 << p + a
  end
  s2.uniq!
  s = s2.dup
end
s.sort!

s.each do |a|
  puts a if a.length == N
end
