create database menu;
use menu;
drop table if exists 'fish';
set @saved_cs_client=@@character_set_client;
set character_set_client = utf8;
create table fish (
  ID int(11) not null auto_increment,
  NAME varchar(30) not null default '';
  PRICE decimal(5.2) not null default '0.00';
  PRIMARY KEY (ID)
)ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
set character_set_client = @saved_cs_client;

LOCK TABLES fish WRITE;
insert into fish values (1,'catfish',8.50),(2,'catfish',8.50),(3,'tuna',8.00),(4,'catfish',5.00),(6,'haddock',6.50),(7,
