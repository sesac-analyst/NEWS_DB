CREATE DATABASE IF NOT EXISTS NEWS_DB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE NEWS_DB;

CREATE TABLE IF NOT EXISTS tbr_platform (
    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(10) NULL,
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(10) NULL,
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_publisher (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(8) NULL,
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_user (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_unique VARCHAR(5) UNIQUE NOT NULL,
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_article (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    platform_id TINYINT UNSIGNED NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    publisher_id INT UNSIGNED NOT NULL,
    title VARCHAR(128) NULL,
    content TEXT NOT NULL,
    author VARCHAR(50) NULL,
    publication_date DATETIME NULL,
    update_date DATETIME NULL,
    article_url VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (platform_id) REFERENCES tbr_platform(id),
    FOREIGN KEY (category_id) REFERENCES tbr_category(id),
    FOREIGN KEY (publisher_id) REFERENCES tbr_publisher(id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_comment(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    article_id INT UNSIGNED NOT NULL,
    user_id INT UNSIGNED NOT NULL,
    content VARCHAR(500) NULL,
    comment_date DATETIME NULL,
    update_date DATETIME NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (article_id) REFERENCES tbr_article(id)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tbr_sticker(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    stk1_name VARCHAR(8) NULL,
    stk1_count SMALLINT NULL,
    stk2_name VARCHAR(8) NULL,
    stk2_count SMALLINT NULL,
    stk3_name VARCHAR(8) NULL,
    stk3_count SMALLINT NULL,
    stk4_name VARCHAR(8) NULL,
    stk4_count SMALLINT NULL,
    stk5_name VARCHAR(8) NULL,
    stk5_count SMALLINT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES tbr_article(id)
)DEFAULT CHARSET=utf8mb4;