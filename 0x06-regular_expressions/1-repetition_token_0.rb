#!/usr/bin/env ruby

# Retrieves the first argument from the command line.
# Scans it for the pattern "hb?t?n" where '?' 
# denotes zero or one occurrence of the preceding character.
# Joins all the matching occurrences together and prints the result.
puts ARGV[0].scan(/hb?t?n/).join
