-- creating hbtn_0d_usa database and states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	PRIMARY KEY(id),
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
