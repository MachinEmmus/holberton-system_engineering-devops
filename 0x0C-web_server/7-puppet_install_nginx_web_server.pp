# nginx server using puppet

exec { 'apt-get':
    path    => '/usr/bin',
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => installed
}

service { 'nginx':
    ensure  => running,
}

exec { 'mkdir-directory':
    path    => '/bin',
    command => '/bin/mkdir -p /var/www/html',
    require => Package['nginx']
}

file { '/var/www/html/index.html':
    ensure  => file,
    path    => '/var/www/html/index.html',
    content => 'Holberton School',
    require => Exec['mkdir-directory'],
}

exec { 'redirect_me':
    command => '/bin/sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default',
    require  => Package['nginx']
}
