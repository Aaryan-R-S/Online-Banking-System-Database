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
-- Table structure for table `collateral`
--

DROP TABLE IF EXISTS `collateral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collateral` (
  `collateral_id` int unsigned NOT NULL AUTO_INCREMENT,
  `collateral_name` varchar(25) NOT NULL,
  `collateral_value` int unsigned NOT NULL DEFAULT (0),
  `collateral_owner` int unsigned NOT NULL,
  PRIMARY KEY (`collateral_id`),
  KEY `collateral_ibfk_1` (`collateral_owner`),
  CONSTRAINT `collateral_ibfk_1` FOREIGN KEY (`collateral_owner`) REFERENCES `customer` (`cin`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10051 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collateral`
--

LOCK TABLES `collateral` WRITE;
/*!40000 ALTER TABLE `collateral` DISABLE KEYS */;
INSERT INTO `collateral` VALUES (10001,'Collateral1',900000,100000601),(10002,'Collateral2',400000,100000602),(10003,'Collateral3',1000000,100000603),(10004,'Collateral4',900000,100000604),(10005,'Collateral5',800000,100000605),(10006,'Collateral6',300000,100000606),(10007,'Collateral7',400000,100000607),(10008,'Collateral8',100000,100000608),(10009,'Collateral9',900000,100000609),(10010,'Collateral10',300000,100000610),(10011,'Collateral11',700000,100000611),(10012,'Collateral12',500000,100000612),(10013,'Collateral13',800000,100000613),(10014,'Collateral14',700000,100000614),(10015,'Collateral15',100000,100000615),(10016,'Collateral16',900000,100000616),(10017,'Collateral17',1000000,100000617),(10018,'Collateral18',900000,100000618),(10019,'Collateral19',300000,100000619),(10020,'Collateral20',200000,100000620),(10021,'Collateral21',1000000,100000621),(10022,'Collateral22',200000,100000622),(10023,'Collateral23',100000,100000623),(10024,'Collateral24',1000000,100000624),(10025,'Collateral25',400000,100000625),(10026,'Collateral26',300000,100000626),(10027,'Collateral27',700000,100000627),(10028,'Collateral28',400000,100000628),(10029,'Collateral29',400000,100000629),(10030,'Collateral30',400000,100000630),(10031,'Collateral31',700000,100000631),(10032,'Collateral32',900000,100000632),(10033,'Collateral33',1000000,100000633),(10034,'Collateral34',300000,100000634),(10035,'Collateral35',300000,100000635),(10036,'Collateral36',600000,100000636),(10037,'Collateral37',500000,100000637),(10038,'Collateral38',600000,100000638),(10039,'Collateral39',800000,100000639),(10040,'Collateral40',900000,100000640),(10041,'Collateral41',400000,100000641),(10042,'Collateral42',800000,100000642),(10043,'Collateral43',100000,100000643),(10044,'Collateral44',100000,100000644),(10045,'Collateral45',300000,100000645),(10046,'Collateral46',600000,100000646),(10047,'Collateral47',200000,100000647),(10048,'Collateral48',600000,100000648),(10049,'Collateral49',700000,100000649),(10050,'Collateral50',500000,100000650);
/*!40000 ALTER TABLE `collateral` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26  0:11:55
