# update headers response to nginx

exec { 'apt-get':
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['apt-get']
}

service { 'nginx':
    ensure  => running
}

exec { 'mkdir-directory':
    command => '/bin/mkdir -p /var/www/html',
    require => Package['nginx']
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Holberton School',
    require => Exec['mkdir-directory'],
}

exec { 'redirect':
  command => '/bin/sed -i \'s|_;|_;\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGlwu4 permanent;|g\' /etc/nginx/sites-available/default',
  require => Package['nginx']
}

exec { 'header_response':
    command => '/bin/sed -i \'s|_;|_;\n\tadd_header \'X-Served-By\' \"\$HOSTNAME\"; |g\' /etc/nginx/sites-available/default',
    require => Exec['redirect']
}

exec { 'restart':
    command => '/bin/service nginx restart',
    require => Exec['header_response']
}
