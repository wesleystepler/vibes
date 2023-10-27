-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ CREATE TABLES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

CREATE TABLE Users (
    user_name VARCHAR(50) PRIMARY KEY,
    pwd VARCHAR(50),
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE Post (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(30),
    time_posted DATETIME,
    likes INT,
    post_text VARCHAR(280),
    user_name VARCHAR(50),
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);

CREATE TABLE Comment (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT,
    user_name VARCHAR(50),
    comment_text VARCHAR(280),
    FOREIGN KEY (post_id) REFERENCES Post(post_id) ON DELETE CASCADE,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);

CREATE TABLE Is_Friends_With (
    user_name1 VARCHAR(50),
    user_name2 VARCHAR(50),
    FOREIGN KEY (user_name1) REFERENCES Users(user_name) ON DELETE CASCADE,
    FOREIGN KEY (user_name2) REFERENCES Users(user_name) ON DELETE CASCADE,
    PRIMARY KEY (user_name1, user_name2)
);

CREATE TABLE Sends_Request_To (
    user_name1 VARCHAR(50),
    user_name2 VARCHAR(50),
    FOREIGN KEY (user_name1) REFERENCES Users(user_name) ON DELETE CASCADE,
    FOREIGN KEY (user_name2) REFERENCES Users(user_name) ON DELETE CASCADE,
    PRIMARY KEY (user_name1, user_name2),
    CHECK (user_name1 <> user_name2) -- Advanced SQL CHECK
);

CREATE TABLE Likes_Comment (
    user_name VARCHAR(50),
    comment_id INT,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE,
    FOREIGN KEY (comment_id) REFERENCES Comment(comment_id) ON DELETE CASCADE,
    PRIMARY KEY (user_name, comment_id)
);

CREATE TABLE Likes_Post (
    user_name VARCHAR(50),
    post_id INT,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES Post(post_id) ON DELETE CASCADE,
    PRIMARY KEY (user_name, post_id)
);

CREATE TABLE Replies(
    comment_id INT,
    reply_num INT,
    user_name VARCHAR(50),
    time_stamp DATETIME,
    reply_text VARCHAR(280),
    FOREIGN KEY (comment_id) REFERENCES Comment(comment_id) ON DELETE CASCADE,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE,
    PRIMARY KEY (comment_id, reply_num)
);

-- Insert Dummy Data
INSERT INTO Users
VALUES('paulwesleystepler', 'Urmom123!', 'Paul', 'Stepler', 'paulwesleystepler@urmom.com');

INSERT INTO Users
VALUES('anthonyferguson', 'ThomasIsDrinkingALargeCocaCola27', 'Anthony', 'Ferguson', 'anthonyferguson@getwrecked.org');

INSERT INTO Users
VALUES('kathleenmead', 'SeeQuillNotEssQueueEl1', 'Kathleen', 'Mead', 'kathleenmead@whatislife.com')

INSERT INTO Post (category, time_posted, likes, post_text, user_name)
VALUES('food', '2023-10-27 04:29:52', 24, 'Chocolate chip cookies are the actual best', 'anthonyferguson');

INSERT INTO Comment(post_id, user_name, comment_text)
VALUES(1, 'paulwesleystepler','no ur wrong, brownies are better :');

INSERT INTO Likes_Post
VALUES('kathleenmead', 1);

INSERT INTO Sends_Request_To
VALUES('anthonyferguson', 'paulwesleystepler');

INSERT INTO Is_Friends_With
VALUES('paulwesleystepler', 'kathleenmead')

INSERT INTO Is_Friends_With
VALUES('kathleenmead', 'paulwesleystepler')

INSERT INTO Likes_Comment
VALUES('anthonyferguson', 1);

INSERT INTO Replies
VALUES(1, 1, 'kathleenmead', '2023-10-27 05:16:15', 'so fun fact: you are incorrect');

-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ ADD TO TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###
--Create a new User
INSERT INTO Users (user_name, pwd, first_name, last_name, email)
VALUES ('%s', '%s', '%s', '%s', '%s');

INSERT INTO Post (category, time_posted, likes, post_text, user_name)
VALUES ('%s', '%s', '%s', '%s', '%s');

INSERT INTO Comment post_id, user_name, comment_text
VALUES ('%s', '%s', '%s');

INSERT INTO Is_Friends_With (user_name1, user_name2)
VALUES ('%s', '%s');

INSERT INTO Sends_Request_To (user_name1, user_name2)
VALUES ('%s', '%s');

INSERT INTO Likes_Comment (user_name, comment_id)
VALUES ('%s', '%s');

INSERT INTO Likes_Post (user_name, post_id)
VALUES ('%s', '%s');

INSERT INTO Replies (comment_id, reply_num, user_name, time_stamp, reply_text)
VALUES ('%s', '%s', '%s', '%s', '%s');

-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ REMOVE FROM TABLE QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

DELETE FROM User
WHERE user_name = '%s';

DELETE FROM Post
WHERE post_id = '%s';

DELETE FROM Comment
WHERE comment_id = '%s';

DELETE FROM Is_Friends_With
WHERE user_name1 = '%s';

DELETE FROM Sends_Request_To
WHERE user_name1 = '%s';

DELETE FROM Likes_Comment
WHERE user_name = '%s' AND comment_id = '%s';

DELETE FROM Likes_Post
WHERE user_name = '%s' AND post_id = '%s';

DELETE FROM Replies
WHERE reply_num = '%s';


-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ DATA FILTERING QUERIES ~~~~~~~~~~~~~~~~~~~~~~~~ ###

--Display User's Home page
SELECT 
category, time_posted, likes, post_text, user_name FROM Post JOIN Is_Friends_With ON Post.user_name = Is_Friends_With.user_name2 -- friends' posts
WHERE user_name1 = '%s' -- current user
ORDER BY post_id DESC; -- show most recent first, Is_Friends_With WHERE user_name1 = '%s' AND Posts.user_name2 = user_name 

--Display a User's profile
SELECT * FROM Post WHERE user_name = '%s'

--Display User's friends
SELECT user_name2user_name2 FROM Is_Friends_With WHERE user__name1 = '%s';

--Display a specific User's posts
SELECT * From Post WHERE user_name = '%s';

--Display a specific category of posts
SELECT * FROM Post WHERE category = '%s';

--Display a user's liked posts
SELECT * 
FROM Likes_Post NATURAL JOIN Post
WHERE Likes_Post.user_name = '%s';

--Display a user's comments
SELECT * FROM Comments WHERE user_name = '%s';


-- ### ~~~~~~~~~~~~~~~~~~~~~~~~ ADVANCED SQL ~~~~~~~~~~~~~~~~~~~~~~~~ ###
DELIMITER $$
CREATE PROCEDURE updateLikes(IN Liked_Post_ID INT)
UPDATE Post
SET Post.likes = Post.likes + 1 
WHERE Post.post_id = Liked_Post_ID;
$$
DELIMITER ;