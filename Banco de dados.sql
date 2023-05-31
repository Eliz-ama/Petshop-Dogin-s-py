create database crud;
use crud;

create table promocao(
nome varchar (50) not null,
email varchar (50) not null,
cpf varchar (11) not null primary key
);

select * from promocao;