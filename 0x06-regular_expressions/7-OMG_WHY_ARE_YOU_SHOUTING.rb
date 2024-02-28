#!/usr/bin/env ruby

# Retrieve the first argument from the command line
input = ARGV[0]

# Use a regular expression to find all matches of the pattern /[A-Z]*/
matches = input.scan(/[A-Z]*/)

# Join all the matching occurrences together and print the result
puts matches.join
