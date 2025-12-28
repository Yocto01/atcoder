N = gets.to_i
A = gets.split.map(&:to_i)
A << 0
def binary_search(array, target)

  head = 0
  tail = array.count - 1

  while head <= tail

    center = (head + tail) / 2

    if array[center] == target
      return "index = #{center}"
    elsif array[center] < target
      head = center + 1
    else
      tail = center - 1
    end

  end

  return -1

end
res = N
a = []
now = 0
series = 0
A.each do |n|
  if now == 0
    now = n
    series += 1
    next
  end

  if now == n
    series += 1
  else
    a << [now,series]
    now = n
    series = 1
  end
end
#p a


idx = 0
sz = a.size
dl = []
while true
  #puts "idx = #{idx}, sz = #{sz}"
  #p a
  #p dl
  break if idx >= sz - 1
  dl.sort!
  idx2 = idx+1
  while binary_search(dl,idx2) != -1
    idx2 += 1
  end
  if a[idx][0] == a[idx2][0]
    a[idx][1] += a[idx2][1]
    a[idx2][1] = 0
    dl << idx2
    sz -= 1
  end
  if a[idx][1] < 4
    idx += 1
    next
  end
  a[idx][1] %= 4
  if a[idx][1] == 0
    dl << idx
    idx -= 1
    sz -= 1
  end
end
a[-1][1] %= 4


if a.empty?
  puts 0
  return
end
cnt = 0
a.each do |num,series|
  cnt += series
end
puts cnt
