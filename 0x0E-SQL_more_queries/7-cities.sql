-- creating cities table in hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	PRIMARY KEY(id),
	id INTEGER NOT NULL AUTO_INCREMENT,
	state_id INTEGER NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
