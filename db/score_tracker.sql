DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    points INT,
    wins INT,
    losses INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team1_score INT,
    team2_score INT,
    team_id INT REFERENCES teams(id)
);