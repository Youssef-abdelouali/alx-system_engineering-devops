#!/usr/bin/env ruby

# Retrieve the first argument provided from the command line
input = ARGV[0]

# Check if the input matches the pattern
match = input.match(/hbt{2,5}n/)

# If a match is found, print it, otherwise print an empty string
puts match ? match.to_s : ""
