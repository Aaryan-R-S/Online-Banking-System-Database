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
-- Table structure for table `medical_insurance`
--

DROP TABLE IF EXISTS `medical_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_insurance` (
  `policy_id` int unsigned NOT NULL,
  `insured_person` int unsigned NOT NULL,
  PRIMARY KEY (`policy_id`,`insured_person`),
  KEY `medical_insurance_ibfk_2` (`insured_person`),
  CONSTRAINT `medical_insurance_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `insurance` (`policy_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `medical_insurance_ibfk_2` FOREIGN KEY (`insured_person`) REFERENCES `personal_customer` (`cin`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_insurance`
--

LOCK TABLES `medical_insurance` WRITE;
/*!40000 ALTER TABLE `medical_insurance` DISABLE KEYS */;
INSERT INTO `medical_insurance` VALUES (100071,100000726),(100072,100000727),(100073,100000728),(100074,100000729),(100075,100000730),(100076,100000731),(100077,100000732),(100078,100000733),(100079,100000734),(100080,100000735),(100081,100000736),(100082,100000737),(100083,100000738),(100084,100000739),(100085,100000740),(100086,100000741),(100087,100000742),(100088,100000743),(100089,100000744),(100090,100000745),(100091,100000746),(100092,100000747),(100093,100000748),(100094,100000749),(100095,100000750),(100096,100000751),(100097,100000752),(100098,100000753),(100099,100000754),(100100,100000755);
/*!40000 ALTER TABLE `medical_insurance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:49
