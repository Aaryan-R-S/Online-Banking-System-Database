-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: online_banking_system
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `documents_pdf`
--

DROP TABLE IF EXISTS `documents_pdf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documents_pdf` (
  `document_id` int unsigned NOT NULL AUTO_INCREMENT,
  `loan_id` mediumint unsigned NOT NULL,
  `document_pdf` mediumblob NOT NULL,
  PRIMARY KEY (`document_id`,`loan_id`),
  KEY `loan_id` (`loan_id`),
  CONSTRAINT `documents_pdf_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `non_collateral_loan` (`loan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents_pdf`
--

LOCK TABLES `documents_pdf` WRITE;
/*!40000 ALTER TABLE `documents_pdf` DISABLE KEYS */;
INSERT INTO `documents_pdf` VALUES (10051,10051,_binary 'efcnlkj45r'),(10052,10052,_binary 'f96riehipm'),(10053,10053,_binary 'q66jecnrt2'),(10054,10054,_binary 'lhsfezmfme'),(10055,10055,_binary 'zqth9r0axd'),(10056,10056,_binary '2juh07hcvz'),(10057,10057,_binary '1ie4jvysum'),(10058,10058,_binary 'lphv32itvg'),(10059,10059,_binary 'jljujt02yo'),(10060,10060,_binary 't7mh9heq0k'),(10061,10061,_binary '1q0p88byei'),(10062,10062,_binary 'mbe4dew7d1'),(10063,10063,_binary '0pqhl22tbd'),(10064,10064,_binary '7yekaf6wu8'),(10065,10065,_binary 'fp23z1ka2a'),(10066,10066,_binary 'r8tyk8tm4v'),(10067,10067,_binary '1fwptkrtns'),(10068,10068,_binary 'pdf5hoot4t'),(10069,10069,_binary 'xo88d017l2'),(10070,10070,_binary '57248bzt26'),(10071,10071,_binary 'pdx5nd3w1w'),(10072,10072,_binary '58xhcgyou7'),(10073,10073,_binary 'mqecrjuazp'),(10074,10074,_binary 'j0zph8fdkl'),(10075,10075,_binary 'ne2ar9u3q6');
/*!40000 ALTER TABLE `documents_pdf` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-02 16:05:12
