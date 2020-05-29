include stdlib
# Puppet Script to ssh configuration

file_line { 'Use ssh holberton':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Disable Password ':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
