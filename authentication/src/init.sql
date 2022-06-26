CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE users (
	id int AUTO_INCREMENT PRIMARY KEY,
	email varchar(50) UNIQUE NOT NULL,
	username varchar(70) NOT NULL, 
	password varchar(500) NOT NULL
);
