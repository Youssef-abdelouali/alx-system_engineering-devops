# This Puppet manifest kills the process named 'killmenow' using pkill

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/local/bin'],
}
