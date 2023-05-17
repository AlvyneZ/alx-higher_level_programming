-- A script that creates a database 'hbtn_0d_usa' and a table 'cities'
--  with a unique autogenerated primary key `id` and a foreign key `state_id`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    UNIQUE(`id`),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`state_id`) REFERENCES hbtn_0d_usa.state(id)
);
