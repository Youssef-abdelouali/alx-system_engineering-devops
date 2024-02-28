#!/usr/bin/env ruby

# Retrieves the first argument from the command line
input = ARGV[0]

# Use a regular expression to find all matches of the pattern "hb?t?n" in the input string
matches = input.scan(/hb?t?n/)

# Join all the matching occurrences together and print the result
puts matches.join
