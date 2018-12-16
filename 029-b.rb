count = 0

12.times do
  s = gets.chomp.to_s
  count += 1 if s.index("r") != nil
end

puts count
