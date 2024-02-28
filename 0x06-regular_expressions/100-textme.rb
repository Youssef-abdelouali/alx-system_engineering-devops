#!/usr/bin/env ruby

# Retrieve the first argument from the command line
input = ARGV[0]

# Use a regular expression to match the pattern /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
match_data = input.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# If a match is found, print the captured groups separated by commas
if match_data
  puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}"
else
  # If no match is found, print nothing
  puts ""
end

