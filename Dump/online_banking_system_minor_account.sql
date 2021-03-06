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
-- Table structure for table `minor_account`
--

DROP TABLE IF EXISTS `minor_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `minor_account` (
  `account_number` bigint unsigned NOT NULL,
  `minor_first_name` varchar(15) NOT NULL,
  `minor_last_name` varchar(15) NOT NULL,
  `parent_cin` int unsigned NOT NULL,
  `parent_account_number` bigint unsigned NOT NULL,
  PRIMARY KEY (`account_number`),
  UNIQUE KEY `parent_cin` (`parent_cin`),
  KEY `minor_account_ibfk_1` (`parent_account_number`),
  CONSTRAINT `minor_account_ibfk_1` FOREIGN KEY (`parent_account_number`) REFERENCES `savings_account` (`account_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `minor_account_ibfk_2` FOREIGN KEY (`account_number`) REFERENCES `bank_account` (`account_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `minor_account_ibfk_3` FOREIGN KEY (`parent_cin`) REFERENCES `personal_customer` (`cin`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minor_account`
--

LOCK TABLES `minor_account` WRITE;
/*!40000 ALTER TABLE `minor_account` DISABLE KEYS */;
INSERT INTO `minor_account` VALUES (13000000000,'Sam','Douglas',100000001,11000000026),(13000000001,'Edwin','Fowler',100000002,11000000027),(13000000002,'Ryan','Murphy',100000003,11000000028),(13000000003,'Tyler','Brooks',100000004,11000000029),(13000000004,'Connie','Howard',100000005,11000000030),(13000000005,'James','Gibson',100000006,11000000031),(13000000006,'Edwin','Edwards',100000007,11000000032),(13000000007,'Michelle','Morrison',100000008,11000000033),(13000000008,'Alisa','Payne',100000009,11000000034),(13000000009,'Amanda','Watson',100000010,11000000035),(13000000010,'Alfred','Carroll',100000011,11000000036),(13000000011,'Emily','Owens',100000012,11000000037),(13000000012,'Stuart','Murray',100000013,11000000038),(13000000013,'Nicole','Casey',100000014,11000000039),(13000000014,'Nicole','Sullivan',100000015,11000000040),(13000000015,'Dexter','Johnston',100000016,11000000041),(13000000016,'Kelvin','Hawkins',100000017,11000000042),(13000000017,'Amber','Davis',100000018,11000000043),(13000000018,'Sam','Walker',100000019,11000000044),(13000000019,'Maximilian','Barrett',100000020,11000000045),(13000000020,'Kristian','Hamilton',100000021,11000000046),(13000000021,'Albert','Murphy',100000022,11000000047),(13000000022,'Alen','Turner',100000023,11000000048),(13000000023,'Fenton','Jones',100000024,11000000049),(13000000024,'Daryl','Chapman',100000025,11000000050),(13000000025,'Chloe','Henderson',100000026,11000000051),(13000000026,'Carl','Morris',100000027,11000000052),(13000000027,'Ada','Wright',100000028,11000000053),(13000000028,'Antony','Craig',100000029,11000000054),(13000000029,'Rosie','Watson',100000030,11000000055),(13000000030,'Lenny','Brooks',100000031,11000000056),(13000000031,'Lana','Cooper',100000032,11000000057),(13000000032,'Melanie','Martin',100000033,11000000058),(13000000033,'David','Davis',100000034,11000000059),(13000000034,'Roman','Hall',100000035,11000000060),(13000000035,'Tony','Chapman',100000036,11000000061),(13000000036,'Stuart','Davis',100000037,11000000062),(13000000037,'Madaline','Richards',100000038,11000000063),(13000000038,'Elise','Gibson',100000039,11000000064),(13000000039,'Dexter','Rogers',100000040,11000000065),(13000000040,'Fiona','Lloyd',100000041,11000000066),(13000000041,'Vanessa','Phillips',100000042,11000000067),(13000000042,'Penelope','Turner',100000043,11000000068),(13000000043,'Derek','Lloyd',100000044,11000000069),(13000000044,'Antony','Henderson',100000045,11000000070),(13000000045,'Ted','Cooper',100000046,11000000071),(13000000046,'Roland','Warren',100000047,11000000072),(13000000047,'Kelvin','West',100000048,11000000073),(13000000048,'Stuart','Spencer',100000049,11000000074),(13000000049,'Frederick','Perry',100000050,11000000075);
/*!40000 ALTER TABLE `minor_account` ENABLE KEYS */;
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
