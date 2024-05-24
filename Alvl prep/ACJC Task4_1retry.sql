CREATE TABLE "Employee" (
	"Employee_ID"	TEXT,
	"Employee_Name"	TEXT,
	"Job_type"	TEXT,
	"Date_of_employment"	TEXT,
	"Service_status"	TEXT,
	PRIMARY KEY("Employee_ID")
);
CREATE TABLE "Sales" (
	"Employee_ID"	TEXT,
	"Total_Sales"	TEXT,
	FOREIGN KEY("Employee_ID") REFERENCES "Employee"("Employee_ID"),
	PRIMARY KEY("Employee_ID")
);
CREATE TABLE "Tech_support" (
	"Employee_ID"	TEXT,
	"Bugs_resolved"	INTEGER,
	FOREIGN KEY("Employee_ID") REFERENCES "Employee"("Employee_ID"),
	PRIMARY KEY("Employee_ID")
);