create database if not exists chkatt;

use chkatt;

create table if not exists usr_info(
	usr_id bigint unsigned auto_increment primary key not null,
	usr_name varchar(16) not null unique,
	pwd_hash char(64) not null,
	nickname varchar(16),
	status enum('online', 'offline', 'away') default 'offline',
	last_seen timestamp default current_timestamp,
	created_at timestamp default current_timestamp
 ) engine=InnoDB 
	collate utf8_general_ci
  	character set utf8
	auto_increment = 1000;

create table if not exists conversations(
	conv_id bigint unsigned auto_increment primary key not null,
	conv_type enum('private', 'group') not null,
	name varchar(36), -- if conv_type is 'private' this fileds can be null
	created_by bigint unsigned,
	created_at timestamp default current_timestamp,
	foreign key(created_by) references usr_info(usr_id) on delete set null
) engine=InnoDB collate utf8_general_ci character set utf8;

create table if not exists conv_members(
	conv_id bigint unsigned,
	usr_id bigint unsigned,
	role enum('member', 'admin', 'owner') default 'member',
	joined_at timestamp default current_timestamp,
	left_at timestamp null,
	is_active boolean default true,
	primary key(conv_id, usr_id),
	foreign key(conv_id) references conversations(conv_id) on delete cascade,
	foreign key(usr_id) references usr_info(usr_id) on delete cascade
) engine=InnoDB collate utf8_general_ci character set utf8;

create table if not exists messages(
	msg_id bigint unsigned auto_increment primary key,
	conv_id bigint unsigned not null,
	sender_id bigint unsigned not null,
	content text,                     -- 文本消息内容
	msg_type enum('text', 'image', 'file', 'audio', 'video', 'system') default 'text',
	media_url varchar(512),           -- 媒体文件 url（如有）
	status enum('sent', 'delivered', 'read') default 'sent',
	sent_at timestamp default current_timestamp,
	read_at timestamp null,
	foreign key (conv_id) references conversations(conv_id) on delete cascade,
	foreign key (sender_id) references usr_info(usr_id) on delete cascade,
	index idx_conv_sent (conv_id, sent_at)	
) engine=InnoDB collate utf8_general_ci character set utf8;



alter table usr_info add column salt char(32) not null after pwd_hash;
