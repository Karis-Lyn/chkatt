create user if not exists 'chkatt_server'@'%' 
identified by 'bh@mariaDB1748';--bh@mariaDB1748

grant all privileges on chkatt.* to 'chkatt_server'@'%';

flush privileges;
