-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: nota_test
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `comuna`
--

DROP TABLE IF EXISTS `comuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comuna` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `id_region` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_region_idx` (`id_region`),
  CONSTRAINT `id_region` FOREIGN KEY (`id_region`) REFERENCES `region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=346 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comuna`
--

LOCK TABLES `comuna` WRITE;
/*!40000 ALTER TABLE `comuna` DISABLE KEYS */;
INSERT INTO `comuna` VALUES (1,'Camarones',1),(2,'Putre',1),(3,'General Lagos',1),(4,'Iquique',2),(5,'Alto Hospicio',2),(6,'Pozo Almonte',2),(7,'Camiña',2),(8,'Colchane',2),(9,'Huara',2),(10,'Pica',2),(11,'Antofagasta',3),(12,'Mejillones',3),(13,'Sierra Gorda',3),(14,'Taltal',3),(15,'Calama',3),(16,'Ollagüe',3),(17,'San Pedro de Atacama',3),(18,'Maria Elena',3),(19,'Tocopilla',3),(20,'Alto del Carmen',4),(21,'Caldera',4),(22,'Chañaral',4),(23,'Copiapo',4),(24,'Diago de Almagro',4),(25,'Freirina',4),(26,'Huasco',4),(27,'Tierra Amarilla',4),(28,'Vallenar',4),(29,'Andacollo',5),(30,'Canela',5),(31,'Combrbala',5),(32,'Conquimbo',5),(33,'Illapel',5),(34,'La Higuera',5),(35,'La Serena',5),(36,'Los Vilos',5),(37,'Monte Patria',5),(38,'Ovalle',5),(39,'Paihuano',5),(40,'Punitaqui',5),(41,'Rio Hurtado',5),(42,'Salamanca',5),(43,'Vicuña',5),(44,'Algarrobo',6),(45,'Cabildo',6),(46,'Calera',6),(47,'Calle Larga',6),(48,'Cartagena',6),(49,'Casablanca',6),(50,'Catemu',6),(51,'Concón',6),(52,'El Quisco',6),(53,'El Tabo',6),(54,'Hijuelas',6),(55,'Isla de Pascua',6),(56,'Juan Fernández',6),(57,'La Cruz',6),(58,'La Ligua',6),(59,'Limache',6),(60,'Llaillay',6),(61,'Los Andes',6),(62,'Nogales',6),(63,'Olmué',6),(64,'Panquehue',6),(65,'Papudo',6),(66,'Petorca',6),(67,'Puchuncaví',6),(68,'Putaendo',6),(69,'Quillota',6),(70,'Quilpué',6),(71,'Quintero',6),(72,'Rinconada',6),(73,'San Antonio',6),(74,'San Esteban',6),(75,'San Felipe',6),(76,'Santa María',6),(77,'Santo Domingo',6),(78,'Valparaíso',6),(79,'Villa Alemana',6),(80,'Viña del Mar',6),(81,'Zapallar',6),(82,'Alhué',7),(83,'Buin',7),(84,'Calera de Tango',7),(85,'Cerrillos',7),(86,'Cerro Navia',7),(87,'Colina',7),(88,'Conchalí',7),(89,'Curacaví',7),(90,'El Bosque',7),(91,'El Monte',7),(92,'Estación Central',7),(93,'Huechuraba',7),(94,'Independencia',7),(95,'Isla de Maipo',7),(96,'La Cisterna',7),(97,'La Florida',7),(98,'La Granja',7),(99,'Lampa',7),(100,'La Pintana',7),(101,'La Reina',7),(102,'Las Condes',7),(103,'Lo Barnechea',7),(104,'Lo Espejo',7),(105,'Lo Prado',7),(106,'Macul',7),(107,'Maipú',7),(108,'María Pinto',7),(109,'Melipilla',7),(110,'Ñuñoa',7),(111,'Padre Hurtado',7),(112,'Paine',7),(113,'Pedro Aguirre Cerda',7),(114,'Peñaflor',7),(115,'Peñalolén',7),(116,'Pirque',7),(117,'Providencia',7),(118,'Pudahuel',7),(119,'Puente Alto',7),(120,'Quilicura',7),(121,'Quinta Normal',7),(122,'Recoleta',7),(123,'Renca',7),(124,'San Bernardo',7),(125,'San Joaquín',7),(126,'San José de Maipo',7),(127,'San Miguel',7),(128,'San Pedro',7),(129,'San Ramón',7),(130,'Santiago',7),(131,'Talagante',7),(132,'Tiltil',7),(133,'Vitacura',7),(134,'Chépica',8),(135,'Chimbarongo',8),(136,'Codegua',8),(137,'Coínco',8),(138,'Coltauco',8),(139,'Doñihue',8),(140,'Graneros',8),(141,'La Estrella',8),(142,'Las Cabras',8),(143,'Litueche',8),(144,'Lolol',8),(145,'Machalí',8),(146,'Malloa',8),(147,'Marchihue',8),(148,'Mostazal',8),(149,'Nancagua',8),(150,'Navidad',8),(151,'Olivar',8),(152,'Palmilla',8),(153,'Paredones',8),(154,'Peralillo',8),(155,'Peumo',8),(156,'Pichidegua',8),(157,'Pichilemu',8),(158,'Placilla',8),(159,'Pumanque',8),(160,'Quinta de Tilcoco',8),(161,'Rancagua',8),(162,'Rengo',8),(163,'Requínoa',8),(164,'San Fernando',8),(165,'Santa Cruz',8),(166,'San Vicente',8),(167,'Cauquenes',9),(168,'Chanco',9),(169,'Colbún',9),(170,'Constitución',9),(171,'Curepto',9),(172,'Curicó',9),(173,'Empedrado',9),(174,'Hualañé',9),(175,'Licantén',9),(176,'Linares',9),(177,'Longaví',9),(178,'Maule',9),(179,'Molina',9),(180,'Parral',9),(181,'Pelarco',9),(182,'Pelluhue',9),(183,'Pencahue',9),(184,'Rauco',9),(185,'Retiro',9),(186,'Río Claro',9),(187,'Romeral',9),(188,'Sagrada Familia',9),(189,'San Clemente',9),(190,'San Javier',9),(191,'San Rafael',9),(192,'Talca',9),(193,'Teno',9),(194,'Vichuquén',9),(195,'Villa Alegre',9),(196,'Yerbas Buenas',9),(197,'Bulnes',10),(198,'Chillán',10),(199,'Chillán Viejo',10),(200,'Cobquecura',10),(201,'Coelemu',10),(202,'Coihueco',10),(203,'El Carmen',10),(204,'Ninhue',10),(205,'Ñiquén',10),(206,'Pemuco',10),(207,'Pinto',10),(208,'Portezuelo',10),(209,'Quillón',10),(210,'Quirihue',10),(211,'Ránquil',10),(212,'San Carlos',10),(213,'San Fabián',10),(214,'San Ignacio',10),(215,'San Nicolás',10),(216,'Treguaco',10),(217,'Yungay',10),(218,'Alto Biobío',11),(219,'Antuco',11),(220,'Arauco',11),(221,'Cabrero',11),(222,'Cañete',11),(223,'Chiguayante',11),(224,'Concepción',11),(225,'Contulmo',11),(226,'Coronel',11),(227,'Curanilahue',11),(228,'Florida',11),(229,'Hualpén',11),(230,'Hualqui',11),(231,'Laja',11),(232,'Lebu',11),(233,'Los Alamos',11),(234,'Los Angeles',11),(235,'Lota',11),(236,'Mulchén',11),(237,'Nacimiento',11),(238,'Negrete',11),(239,'Penco',11),(240,'Quilaco',11),(241,'Quilleco',11),(242,'San Pedro de la Paz',11),(243,'San Rosendo',11),(244,'Santa Bárbara',11),(245,'Santa Juana',11),(246,'Talcahuano',11),(247,'Tirúa',11),(248,'Tomé',11),(249,'Tucapel',11),(250,'Yumbel',11),(251,'Angol',12),(252,'Carahue',12),(253,'Cholchol',12),(254,'Collipulli',12),(255,'Cunco',12),(256,'Curacautín',12),(257,'Curarrehue',12),(258,'Ercilla',12),(259,'Freire',12),(260,'Galvarino',12),(261,'Gorbea',12),(262,'Lautaro',12),(263,'Loncoche',12),(264,'Lonquimay',12),(265,'Los Sauces',12),(266,'Lumaco',12),(267,'Melipeuco',12),(268,'Nueva Imperial',12),(269,'Padre Las Casas',12),(270,'Perquenco',12),(271,'Pitrufquén',12),(272,'Pucón',12),(273,'Purén',12),(274,'Renaico',12),(275,'Saavedra',12),(276,'Temuco',12),(277,'Teodoro Schmidt',12),(278,'Toltén',12),(279,'Traiguén',12),(280,'Victoria',12),(281,'Vilcún',12),(282,'Villarrica',12),(283,'Corral',13),(284,'Futrono',13),(285,'Lago Ranco',13),(286,'Lanco',13),(287,'La Unión',13),(288,'Los Lagos',13),(289,'Máfil',13),(290,'Mariquina',13),(291,'Paillaco',13),(292,'Panguipulli',13),(293,'Río Bueno',13),(294,'Valdivia',13),(295,'Ancud',14),(296,'Calbuco',14),(297,'Castro',14),(298,'Chaitén',14),(299,'Chonchi',14),(300,'Cochamó',14),(301,'Curaco de Vélez',14),(302,'Dalcahue',14),(303,'Fresia',14),(304,'Frutillar',14),(305,'Futaleufú',14),(306,'Hualaihué',14),(307,'Llanquihue',14),(308,'Los Muermos',14),(309,'Maullín',14),(310,'Osorno',14),(311,'Palena',14),(312,'Puerto Montt',14),(313,'Puerto Octay',14),(314,'Puerto Varas',14),(315,'Puqueldón',14),(316,'Purranque',14),(317,'Puyehue',14),(318,'Queilén',14),(319,'Quellón',14),(320,'Quemchi',14),(321,'Quinchao',14),(322,'Río Negro',14),(323,'San Juan de la Costa',14),(324,'San Pablo',14),(325,'Aysén',15),(326,'Chile Chico',15),(327,'Cisnes',15),(328,'Cochrane',15),(329,'Coyhaique',15),(330,'Guaitecas',15),(331,'Lago Verde',15),(332,'O Higgins',15),(333,'Río Ibáñez',15),(334,'Tortel',15),(335,'Antártica',16),(336,'Cabo de Hornos',16),(337,'Laguna Blanca',16),(338,'Natales',16),(339,'Porvenir',16),(340,'Primavera',16),(341,'Punta Arenas',16),(342,'Río Verde',16),(343,'San Gregorio',16),(344,'Timaukel',16),(345,'Torres del Paine',16);
/*!40000 ALTER TABLE `comuna` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 12:14:56
