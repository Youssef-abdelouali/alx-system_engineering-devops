# Puppet manifest to install Flask and Werkzeug using pip3
exec { 'install_flask_and_werkzeug':
  command => 'pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'pip3 show Flask | grep 2.1.0 && pip3 show Werkzeug | grep 2.1.1',
}
