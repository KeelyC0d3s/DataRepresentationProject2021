CREATE DATABASE IF NOT EXISTS Student_G00387819;

CREATE TABLE IF NOT EXISTS Student_G00387819.heroes (
    `id` int(11) NOT NULL auto_increment,
    `name` varchar(250) NOT NULL,
    PRIMARY KEY  (`id`)
);

INSERT INTO Student_G00387819.heroes(id, name) VALUES (1, 'Batman'), (2, 'Superman'), (3, 'Wonder Woman') AS alias
ON DUPLICATE KEY UPDATE `name`=alias.name;

