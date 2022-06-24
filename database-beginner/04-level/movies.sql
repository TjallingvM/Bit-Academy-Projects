USE netland;
DROP TABLE IF EXISTS films;
CREATE TABLE films (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(255) NOT NULL,
    duur TIME NOT NULL,
    datum_van_uitkomst DATETIME,
    land_van_uitkomst VARCHAR(255),
    omschrijving TEXT NOT NULL,
    youtube_id VARCHAR(255) NOT NULL);

INSERT INTO films(titel,duur, datum_van_uitkomst, land_van_uitkomst, omschrijving, youtube_id)
VALUES
	("Frozen", "01:45","1982-03-20","USA","zusjes beleven nieuwe avonturen in de kou","Zi4LMpSDccc"),
    ("SQL for beginners", "04:20", "2010-01-10","NL", "Leer alles over SQL", "HXV3zeQKqGY"),
    ("Grapje", "03:32", "1987-01-01","UK","Even tussendoor","dQw4w9WgXcQ"),
    ("Good, Bad and Ugly","02:58", "1966-12-23", "ITA","Cowboyavonturen","cqgND_-DRxs"),
    ("Titanic","03:14","1997-11-01","TOK","Waargebeurde rampenfilm", "4S2Ruqhcz78"),
    ("Baby's Day Out", "01:38", "1994-10-13","UK", "Wat gebeurd er als je je baby vergeet en hij op stap gaat", "uTA9mVKQ9lA");
    
    
    