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
-- Table structure for table `prepaid_card`
--

DROP TABLE IF EXISTS `prepaid_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prepaid_card` (
  `card_number` bigint unsigned NOT NULL,
  `cin` int unsigned NOT NULL,
  `prepaid_balance` mediumint unsigned DEFAULT (0),
  PRIMARY KEY (`card_number`),
  KEY `prepaid_card_ibfk_2` (`cin`),
  CONSTRAINT `prepaid_card_ibfk_1` FOREIGN KEY (`card_number`) REFERENCES `card` (`card_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `prepaid_card_ibfk_2` FOREIGN KEY (`cin`) REFERENCES `personal_customer` (`cin`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prepaid_card`
--

LOCK TABLES `prepaid_card` WRITE;
/*!40000 ALTER TABLE `prepaid_card` DISABLE KEYS */;
INSERT INTO `prepaid_card` VALUES (100000000100,100000651,379129),(100000000101,100000652,170536),(100000000102,100000653,496602),(100000000103,100000654,129204),(100000000104,100000655,408026),(100000000105,100000656,346489),(100000000106,100000657,426172),(100000000107,100000658,460480),(100000000108,100000659,306421),(100000000109,100000660,68199),(100000000110,100000661,370243),(100000000111,100000662,59193),(100000000112,100000663,201864),(100000000113,100000664,372719),(100000000114,100000665,124927),(100000000115,100000666,217358),(100000000116,100000667,256957),(100000000117,100000668,109470),(100000000118,100000669,172876),(100000000119,100000670,374483),(100000000120,100000671,373039),(100000000121,100000672,222093),(100000000122,100000673,249627),(100000000123,100000674,55993),(100000000124,100000675,334084),(100000000125,100000676,494499),(100000000126,100000677,293279),(100000000127,100000678,299581),(100000000128,100000679,432310),(100000000129,100000680,234876),(100000000130,100000681,479352),(100000000131,100000682,112968),(100000000132,100000683,216308),(100000000133,100000684,356184),(100000000134,100000685,400794),(100000000135,100000686,411280),(100000000136,100000687,369805),(100000000137,100000688,412800),(100000000138,100000689,281512),(100000000139,100000690,231110),(100000000140,100000691,108259),(100000000141,100000692,468632),(100000000142,100000693,268254),(100000000143,100000694,232411),(100000000144,100000695,191248),(100000000145,100000696,307850),(100000000146,100000697,259576),(100000000147,100000698,152542),(100000000148,100000699,484109),(100000000149,100000700,197644);
/*!40000 ALTER TABLE `prepaid_card` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:12:03
