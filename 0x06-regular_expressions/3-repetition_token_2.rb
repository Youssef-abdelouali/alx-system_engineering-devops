#!/usr/bin/env ruby

# Retrieve the first argument from the command line
input = ARGV[0]

# Use a regular expression to find the first match of the pattern "hbt+n" in the input string
match = input.match(/hbt+n/)

# If a match is found, print it, otherwise print an empty string
puts match ? match[0] : ""
