CREATE TABLE MedicineRoute
(
    RouteId INT IDENTITY(101,1) primary key,
    RouteType VARCHAR(50) NOT NULL,
    Status VARCHAR(50),
);

CREATE TABLE MedicineType
(
    MedicineTypeId INT IDENTITY(1,1) primary key,
    MedicineType VARCHAR(50) NOT NULL,
    Status VARCHAR(50) NULL
);

CREATE TABLE MedicineList
(
    MedicineId INT IDENTITY(1,1) PRIMARY KEY ,
    GenericName VARCHAR(50),
    MedicineType INT FOREIGN KEY REFERENCES MedicineType(MedicineTypeId),
    MarketName VARCHAR(50),
    Route INT FOREIGN KEY REFERENCES MedicineRoute(RouteId),
    Potency VARCHAR(50),
    Status VARCHAR(50),
);

-- DROP TABLE MedicineList
-- DROP TABLE MedicineRoute
-- DROP TABLE MedicineType

-- SELECT *
-- FROM MedicineList
-- SELECT *
-- FROM MedicineRoute
-- SELECT *
-- FROM MedicineType
