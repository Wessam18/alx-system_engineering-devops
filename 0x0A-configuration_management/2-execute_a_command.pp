# Using Puppet, create a manifest that kills a process
exec { 'killmenow':
    command => '/usr/bin/pkill killmenow',
}
