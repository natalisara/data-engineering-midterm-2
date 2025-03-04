-- მომხმარებლების ცხრილის შექმნა
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- საწყისი მონაცემების დამატება
INSERT INTO users (name, age) VALUES ('Alice', 25);
INSERT INTO users (name, age) VALUES ('Bob', 30);
INSERT INTO users (name, age) VALUES ('Charlie', 22);
