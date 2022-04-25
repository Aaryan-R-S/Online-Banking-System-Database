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
-- Table structure for table `loan_protection_insurance`
--

DROP TABLE IF EXISTS `loan_protection_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_protection_insurance` (
  `policy_id` int unsigned NOT NULL,
  `loan_id` mediumint unsigned NOT NULL,
  PRIMARY KEY (`policy_id`),
  KEY `loan_protection_insurance_ibfk_2` (`loan_id`),
  CONSTRAINT `loan_protection_insurance_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `insurance` (`policy_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `loan_protection_insurance_ibfk_2` FOREIGN KEY (`loan_id`) REFERENCES `loan` (`loan_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_protection_insurance`
--

LOCK TABLES `loan_protection_insurance` WRITE;
/*!40000 ALTER TABLE `loan_protection_insurance` DISABLE KEYS */;
INSERT INTO `loan_protection_insurance` VALUES (100026,10001),(100027,10002),(100028,10003),(100029,10004),(100030,10005),(100031,10006),(100032,10007),(100033,10008),(100034,10009),(100035,10010),(100036,10011),(100037,10012),(100038,10013),(100039,10014),(100040,10015),(100041,10016),(100042,10017),(100043,10018),(100044,10019),(100045,10020),(100046,10021),(100047,10022),(100048,10023),(100049,10024),(100050,10025);
/*!40000 ALTER TABLE `loan_protection_insurance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:58
