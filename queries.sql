-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ CREATE TABLES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

CREATE TABLE Users (
    user_name VARCHAR(50) PRIMARY KEY,
    pwd VARCHAR(50),
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE Post (
    user_name VARCHAR(50),
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(30),
    time_posted DATETIME,
    likes INT,
    post_text VARCHAR(280),
    FOREIGN KEY (user_name) REFERENCES User(user_name)
);

CREATE TABLE Comment (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT,
    user_name VARCHAR(50),
    comment_text VARCHAR(280),
    FOREIGN KEY (post_id) REFERENCES Post(post_id),
    FOREIGN KEY (user_name) REFERENCES User(user_name)
);

CREATE TABLE Post_Comments (
    post_id INT,
    comment_id INT,
    FOREIGN KEY (post_id) REFERENCES Post(post_id),
    FOREIGN KEY (comment_id) REFERENCES Comment(comment_id)
);

CREATE TABLE Is_Friends_With (
    user_name1 VARCHAR(50),
    user_name2 VARCHAR(50),
    FOREIGN KEY (user_name1) REFERENCES User(user_name),
    FOREIGN KEY (user_name2) REFERENCES User(user_name),
    PRIMARY KEY (user_name1, user_name2)
);

CREATE TABLE Sends_Request_To (
    user_name1 VARCHAR(50),
    user_name2 VARCHAR(50),
    FOREIGN KEY (user_name1) REFERENCES User(user_name),
    FOREIGN KEY (user_name2) REFERENCES User(user_name),
    PRIMARY KEY (user_name1, user_name2)
);

CREATE TABLE Likes_Comment (
    user_name VARCHAR(50),
    comment_id INT,
    FOREIGN KEY (user_name) REFERENCES User(user_name),
    FOREIGN KEY (comment_id) REFERENCES Comment(comment_id),
    PRIMARY KEY (user_name, comment_id)
);

CREATE TABLE Likes_Post (
    user_name VARCHAR(50),
    post_id INT,
    FOREIGN KEY (user_name) REFERENCES User(user_name),
    FOREIGN KEY (post_id) REFERENCES Post(post_id),
    PRIMARY KEY (user_name, post_id)
);

CREATE TABLE Replies(
    comment_id INT,
    reply_num INT AUTO_INCREMENT,
    user_name VARCHAR(50),
    timestamp VARCHAR(16),
    FOREIGN KEY (comment_id) REFERENCES Comment(comment_id),
    FOREIGN KEY (user_name) REFERENCES User(user_name),
    PRIMARY KEY (comment_id, reply_num)
);

-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ ADD TO TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###




-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

