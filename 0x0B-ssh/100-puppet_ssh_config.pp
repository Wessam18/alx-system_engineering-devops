#  using Puppet to make changes to our configuration file

file_line { '/etc/ssh/ssh_config':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication=',
}

file_line { '~/.ssh/scool':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile=',
}
