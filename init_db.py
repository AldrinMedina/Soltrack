import os
import pymysql

connection = pymysql.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT"))
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Contracts (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Abi TEXT NOT NULL,
    Address VARCHAR(100) NOT NULL UNIQUE,
    CreationDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Finished TINYINT(1) DEFAULT 0,
    BuyerAddress VARCHAR(100) NOT NULL,
    SellerAddress VARCHAR(100) NOT NULL,
    PaymentAmount DECIMAL(18, 8) NOT NULL,
    Vaccine VARCHAR(255) NOT NULL
);
""")

connection.commit()
cursor.close()
connection.close()

print("✅ Database initialized")
