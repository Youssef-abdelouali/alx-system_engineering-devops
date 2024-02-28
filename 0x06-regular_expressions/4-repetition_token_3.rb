#!/usr/bin/env ruby

# Retrieve the first argument from the command line
input = ARGV[0]

# Check if the input matches the pattern "hbt*n"
if input.match?(/hbt*n/)
  # If a match is found, directly output the input string
  puts input
else
  # If no match is found, output an empty string
  puts ""
end
