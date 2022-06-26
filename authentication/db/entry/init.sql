-- this file must be in directory ./db/entry

CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE USERS (
	id int AUTO_INCREMENT PRIMARY KEY,
	email varchar(50) UNIQUE NOT NULL,
	username varchar(70) NOT NULL, 
	password varchar(500) NOT NULL
);
