CREATE TABLE `Kiosk` (
	`KioskID`	INTEGER,
	`Location`	TEXT,
	`Rating`	TEXT,
	PRIMARY KEY(`KioskID`)
);

CREATE TABLE `BentoBox` (
	`BentoName`	TEXT,
	`ProductionCost`	TEXT,
	`ContainEgg`	INTEGER,
	`ContainNut`	INTEGER,
	`ContainSeafood`	INTEGER,
	PRIMARY KEY(`BentoName`)
);

CREATE TABLE `KioskBento` (
	`KioskID`	INTEGER,
	`BentoName`	TEXT,
	`SellPrice`	INTEGER,
	FOREIGN KEY(`KioskID`) REFERENCES `Kiosk`(`KioskID`),
	PRIMARY KEY(`KioskID`),
	FOREIGN KEY(`BentoName`) REFERENCES `BentoBox`(`BentoName`)
);