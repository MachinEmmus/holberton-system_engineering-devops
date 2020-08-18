# Kill a proce by name
exec{ 'pkill killmenow':
    path    => '/usr/bin/',
    command => 'pkill killmenow',
}
