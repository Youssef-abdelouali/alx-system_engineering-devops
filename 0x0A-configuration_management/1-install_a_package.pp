# This Puppet manifest installs Flask version 2.1.0 using pip3 as the package provider.
# The 'ensure' attribute specifies the exact version of Flask to install.
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
