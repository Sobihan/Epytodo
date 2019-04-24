CREATE DATABASE  IF NOT EXISTS epytodo;

USE epytodo;

CREATE TABLE IF NOT EXISTS user (
    user_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (user_id)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS task (
    task_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    begin datetime NOT NULL,
    end datetime NOT NULL,
    status enum ('not started' , 'in progress', 'done') NOT NULL DEFAULT ('not started'),
    PRIMARY KEY (task_id),
    UNIQUE KEY task_id (task_id)
)
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS user_has_task (
    fk_user_id MEDIUMINT UNSIGNED NOT NULL,
    fk_task_id  MEDIUMINT UNSIGNED NOT NULL
)
ENGINE=InnoDB;
