# This Puppet manifest installs the Flask package with version 2.1.0 using pip3

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
