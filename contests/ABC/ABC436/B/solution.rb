N = gets.to_i
a = Array.new(N){Array.new(N,0)}

i,j = 0,(N+1)/2-1
a[i][j] = 1
for n in 2..N*N
  sx = i - 1;
  sy = j + 1;
  if sx < 0
    if sy >= N
      i = i+1
    else
      i,j = N-1,sy
    end
  elsif sy >= N
    i,j = sx,0
  elsif a[sx][sy] != 0
    i = i+1
  else
    i,j = sx,sy
  end
  a[i][j] = n
end

N.times do |i|
  puts a[i].join(" ")
end

