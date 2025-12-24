N = gets.to_i
A = gets.split.map(&:to_i)
A.sort!

def binary_search(a,n)
  
  head = 0
  tail = a.size-1
  while head <= tail
    if head == tail
      return (a[head] - n).abs
    elsif head == tail - 1
      return [(a[head] - n).abs,(a[tail] - n).abs].min
    end

    center = (head + tail)/2

    if a[center] == n
      return 0
    elsif a[center] < n
      head = center
    else
      tail = center
    end
  end

  center = (head + tail)/2
  return [(a[center-1] - n).abs,(a[center] - n).abs,(a[center+1] - n).abs].min
end

Q = gets.to_i
Q.times do
  b = gets.to_i
  puts binary_search(A,b)
end
