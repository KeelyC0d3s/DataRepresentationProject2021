DROP TABLE IF EXISTS Student_G00387819.heroes;
CREATE TABLE Student_G00387819.heroes (
    `id` int(11) NOT NULL auto_increment,
    `name` varchar(250) NOT NULL,
    `gender` varchar(250) NOT NULL,
    `race` varchar(250) NULL,
    `eye_colour` varchar(250) NOT NULL,
    `hair_colour` varchar(250) NOT NULL,
    `full_name` varchar(250) NULL,
    `alter_egos` varchar(250) NULL,
    `place_of_birth` varchar(250) NOT NULL,
    `alignment` varchar(250) NOT NULL,
    `occupation` varchar(250) NOT NULL,
    PRIMARY KEY  (`id`)
);

DROP TABLE IF EXISTS Student_G00387819.user_details;
CREATE TABLE Student_G00387819.user_details (
    `id` int(11) NOT NULL auto_increment PRIMARY KEY,
    `name` VARCHAR(254) NOT NULL,
    `email_address` VARCHAR(254) NOT NULL,
    `username` varchar(254) NOT NULL,
    `salt` VARCHAR(254) NOT NULL,
    `password` VARCHAR(254) NOT NULL
);

