a,b,c,d = gets.split(" ").map(&:to_f)

tPercentage = b/a
aPercentage = d/c

if tPercentage > aPercentage
  puts "TAKAHASHI"
elsif tPercentage < aPercentage
  puts "AOKI"
else
  puts "DRAW"
end
