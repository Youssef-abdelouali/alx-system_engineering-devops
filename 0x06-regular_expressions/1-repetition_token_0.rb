#!/usr/bin/env ruby

# Retrieve the first argument provided from the command line
input = ARGV[0]

# Check if the input matches the pattern
if input.match?(/hb?t?n/)
  puts input
else
  puts ""
end
