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
-- Table structure for table `term_life_insurance`
--

DROP TABLE IF EXISTS `term_life_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `term_life_insurance` (
  `policy_id` int unsigned NOT NULL,
  `insured_person` int unsigned NOT NULL,
  PRIMARY KEY (`policy_id`),
  KEY `insured_person` (`insured_person`),
  CONSTRAINT `term_life_insurance_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `insurance` (`policy_id`),
  CONSTRAINT `term_life_insurance_ibfk_2` FOREIGN KEY (`insured_person`) REFERENCES `personal_customer` (`cin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `term_life_insurance`
--

LOCK TABLES `term_life_insurance` WRITE;
/*!40000 ALTER TABLE `term_life_insurance` DISABLE KEYS */;
INSERT INTO `term_life_insurance` VALUES (100051,100000381),(100052,100000382),(100053,100000383),(100054,100000384),(100055,100000385),(100056,100000386),(100057,100000387),(100058,100000388),(100059,100000389),(100060,100000390),(100061,100000391),(100062,100000392),(100063,100000393),(100064,100000394),(100065,100000395),(100066,100000396),(100067,100000397),(100068,100000398),(100069,100000399),(100070,100000400);
/*!40000 ALTER TABLE `term_life_insurance` ENABLE KEYS */;
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
