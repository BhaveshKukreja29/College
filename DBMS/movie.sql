CREATE database MOVIEDB;
USE MOVIEDB;

CREATE TABLE Actor(
	nam VARCHAR(100),
    gender VARCHAR(20),
    dateOfBirth DATE,
    ethnicity VARCHAR(50),
    actId INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE Director(
	nam VARCHAR(100),
    gender VARCHAR(20),
    dateOfBirth DATE,
    dirId INT AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE Movie(
	genre VARCHAR(50),
    title VARCHAR(50),
    release_date DATE,
    country VARCHAR(100),
    rating FLOAT,
    movieId INT AUTO_INCREMENT PRIMARY KEY, 
    actId INT,
    dirId INT,
    FOREIGN KEY (actId) REFERENCES Actor(actId),
	FOREIGN KEY (dirId) REFERENCES Director(dirId)
);

CREATE TABLE distribution(
	name_distributor VARCHAR(100),
	country VARCHAR(100),
	established INT,
	num_theatres INT,
    movieId INT,
	FOREIGN KEY (movieId) REFERENCES Movie(movieId)
);

CREATE TABLE revenue(
	net BIGINT,
	national_net BIGINT,
	global_net BIGINT,
	movieId INT,
    FOREIGN KEY (movieId) REFERENCES Movie(movieId)
);
