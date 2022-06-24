CREATE DATABASE sterrenstelsel;
USE sterrenstelsel;
CREATE TABLE planeten(naam VARCHAR(255));
INSERT INTO planeten(naam)
VALUES ("Zon"),("Mercurius"),("Venus"),("Aarde"),("Mars");
TRUNCATE TABLE planeten;
ALTER TABLE planeten ADD (diameter INT), ADD (afstand INT), ADD (massa INT);
INSERT INTO planeten(naam, diameter, afstand, massa)
VALUES	("Zon",1392000,0,332946),
		("Mercurius", 4880,57910000,0.1),
		("Venus",12104,108208930,0.9),
        ("Aarde",12756,149597870,1),
        ("Mars",6794,227936640,0.1);

USE sterrenstelsel;
ALTER TABLE planeten
MODIFY naam VARCHAR(255) NOT NULL,
MODIFY diameter INT NOT NULL,
MODIFY afstand INT NOT NULL,
MODIFY massa INT NOT NULL,
ADD bezoek_datum DATETIME;

INSERT INTO planeten(naam, diameter, afstand, massa, bezoek_datum)
VALUES ("Maan", 34748,384400, 81, "1969-07-21");
USE sterrenstelsel;
ALTER TABLE planeten
ADD COLUMN id INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY(id);
INSERT INTO planeten (naam,diameter,afstand,massa)
VALUES ("Mars",6794,227936640,0.1);
USE sterrenstelsel;
UPDATE planeten
SET 
	naam = "Teenalp"
WHERE
	id = 7;

