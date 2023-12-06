-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2023 at 10:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ict_database`
--
CREATE DATABASE IF NOT EXISTS `ict_database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ict_database`;

-- --------------------------------------------------------

--
-- Table structure for table `admin_systems`
--

CREATE TABLE `admin_systems` (
  `Code` char(6) NOT NULL,
  `Admin_System` varchar(30) NOT NULL,
  `Own_Property` enum('Y','N') NOT NULL,
  `Platform` varchar(30) NOT NULL,
  `Environment` enum('S','C','W') NOT NULL,
  `Maintenance_Cost` decimal(8,2) NOT NULL,
  `Use_Codes` set('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15') NOT NULL,
  `Use_other` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_systems`
--

INSERT INTO `admin_systems` (`Code`, `Admin_System`, `Own_Property`, `Platform`, `Environment`, `Maintenance_Cost`, `Use_Codes`, `Use_other`) VALUES
('991901', 'test3', 'Y', 'yeet', 'S', 1300.00, '15', 'test'),
('992100', 'League of Legends', 'N', 'Unreal Engine', 'S', 0.00, '12', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `annex_a-5`
--

CREATE TABLE `annex_a-5` (
  `Year` year(4) NOT NULL DEFAULT current_timestamp(),
  `Agency` varchar(100) NOT NULL,
  `Respondent` varchar(100) NOT NULL,
  `Position` varchar(100) NOT NULL,
  `Division` varchar(100) NOT NULL,
  `Number` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `archiving`
--

CREATE TABLE `archiving` (
  `Code` char(6) NOT NULL,
  `System` tinyint(1) NOT NULL,
  `System_type` enum('Manual','Electronic','Both') NOT NULL,
  `Electronic_mode` enum('Conventional','Cloud') NOT NULL,
  `Conventional_Medium` set('Optical disks','Tape','Microfiche','Hard Disk','External Hard Drive','Diskette') DEFAULT NULL,
  `Other_medium` varchar(70) DEFAULT NULL,
  `Electronic_Info` set('Publications','Audio-visual recordings','Maps','Public documents','Letters','Unprocessed','Photographs') DEFAULT NULL,
  `Other_info` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `automation_software`
--

CREATE TABLE `automation_software` (
  `Code` char(6) NOT NULL,
  `Software` varchar(25) NOT NULL,
  `Lifetime` tinyint(1) NOT NULL,
  `Expiration` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `automation_software`
--

INSERT INTO `automation_software` (`Code`, `Software`, `Lifetime`, `Expiration`) VALUES
('382001', 'MS Visio', 1, NULL),
('382023', 'MS Office XP', 1, NULL),
('991901', 'MS Office XP', 0, '2017'),
('991901', 'MS Visio', 0, '0000'),
('991901', 'Older than MS Office 2003', 1, NULL),
('991901', 'Open Office', 1, NULL),
('991901', 'Open Project', 0, '2013');

-- --------------------------------------------------------

--
-- Table structure for table `cd_usage`
--

CREATE TABLE `cd_usage` (
  `Code` char(6) NOT NULL,
  `CD_Type` varchar(100) NOT NULL,
  `Employees` int(6) DEFAULT NULL,
  `Training` int(6) DEFAULT NULL,
  `Frontline` int(6) DEFAULT NULL,
  `General` int(6) DEFAULT NULL,
  `Projects` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cd_usage`
--

INSERT INTO `cd_usage` (`Code`, `CD_Type`, `Employees`, `Training`, `Frontline`, `General`, `Projects`) VALUES
('382023', 'Multi-function printer (print, copy, etc.)', 16, 0, NULL, NULL, NULL),
('781901', 'Laptop / Notebook / Netbook PC', 300, NULL, NULL, NULL, NULL),
('991901', 'Desktop PC', NULL, NULL, NULL, NULL, 53),
('991901', 'Laptop / Notebook / Netbook PC', NULL, NULL, NULL, NULL, NULL),
('991901', 'Printer only', 21, NULL, NULL, NULL, NULL),
('991901', 'Servers', 21, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cd_year`
--

CREATE TABLE `cd_year` (
  `Code` char(6) NOT NULL,
  `CD_Type` varchar(100) NOT NULL,
  `Owned_1y` int(6) DEFAULT NULL,
  `Leased_1y` int(6) DEFAULT NULL,
  `Owned_2y` int(6) DEFAULT NULL,
  `Leased_2y` int(6) DEFAULT NULL,
  `Owned_3y` int(6) DEFAULT NULL,
  `Leased_3y` int(6) DEFAULT NULL,
  `More` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cd_year`
--

INSERT INTO `cd_year` (`Code`, `CD_Type`, `Owned_1y`, `Leased_1y`, `Owned_2y`, `Leased_2y`, `Owned_3y`, `Leased_3y`, `More`) VALUES
('011932', 'Generator Set', 200, NULL, NULL, NULL, NULL, NULL, NULL),
('382023', 'Printer only', 1300, 1200, NULL, NULL, NULL, NULL, NULL),
('781901', 'Laptop / Notebook / Netbook PC', 12, NULL, NULL, NULL, NULL, NULL, NULL),
('991901', 'External Hard Drive', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('991901', 'Servers', NULL, NULL, NULL, 32, NULL, NULL, NULL),
('991901', 'Smart Card Reader', 21, NULL, NULL, NULL, NULL, NULL, NULL),
('991901', 'Test 2', NULL, NULL, NULL, NULL, NULL, NULL, '546'),
('991901', 'test again', NULL, NULL, NULL, 3, NULL, NULL, NULL),
('991901', 'Test value', NULL, NULL, NULL, NULL, NULL, NULL, '321'),
('992100', 'Laptop / Notebook / Netbook PC', 300, NULL, NULL, NULL, NULL, NULL, NULL),
('992100', 'Small Scanner (ex. flatbed scanner)', 20, NULL, NULL, NULL, NULL, NULL, NULL),
('992100', 'Smart Card Reader', 300, NULL, NULL, NULL, NULL, NULL, NULL),
('992100', 'Wide-format Printer or Plotter', 10, 200, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `databases`
--

CREATE TABLE `databases` (
  `Code` char(6) NOT NULL,
  `DB_Name` varchar(20) NOT NULL,
  `Own_Property` enum('Y','N') NOT NULL,
  `Description` varchar(100) NOT NULL,
  `DB_Software` varchar(30) NOT NULL,
  `Maintenance_Cost` decimal(8,2) NOT NULL,
  `Use_Codes` set('1','2','3','4','5','6','7','8','9','10','11','12','13','14') NOT NULL,
  `Use_other` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `databases`
--

INSERT INTO `databases` (`Code`, `DB_Name`, `Own_Property`, `Description`, `DB_Software`, `Maintenance_Cost`, `Use_Codes`, `Use_other`) VALUES
('991901', 'test', 'N', 'insert description here', 'double', 300.00, '2,6,7', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `data_center`
--

CREATE TABLE `data_center` (
  `Code` char(6) NOT NULL,
  `Data_center` tinyint(1) NOT NULL,
  `Sites` int(4) DEFAULT NULL,
  `Maintenance` enum('In-house','Outsourced') NOT NULL,
  `Back-up_site` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ict_issues`
--

CREATE TABLE `ict_issues` (
  `Code` char(6) NOT NULL,
  `Issues` set('Budget','Opposition','Recruitment','Bandwidth','Delayed funding','Support','ICT skill','Usage','Procurement','Contracts') DEFAULT NULL,
  `Other_issues` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ict_projects`
--

CREATE TABLE `ict_projects` (
  `Code` char(6) NOT NULL,
  `Project` varchar(70) NOT NULL,
  `Description` int(150) NOT NULL,
  `Start` date NOT NULL,
  `End` date NOT NULL,
  `Cost` decimal(8,2) NOT NULL,
  `Strategy` enum('I','O','C') NOT NULL,
  `Status` enum('U','D','O') NOT NULL,
  `Use_codes` set('1','2','3','4','5','6','7','8','9','10','11','12','13','14') NOT NULL,
  `Use_other` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `network`
--

CREATE TABLE `network` (
  `Code` char(6) NOT NULL,
  `LAN` tinyint(1) NOT NULL,
  `Intranet` tinyint(1) NOT NULL,
  `VPN` tinyint(1) NOT NULL,
  `WAN` tinyint(1) NOT NULL,
  `PABX_PBX` tinyint(1) NOT NULL,
  `PBX_Setup` enum('Private','Hosted','VoIP PBX or IP-PBX','Hosted IP') DEFAULT NULL,
  `Internet` tinyint(1) NOT NULL,
  `MOA` set('Dial-up','Leased line','WiFi','DSL','Mobile phone','ISDN','Satellite') DEFAULT NULL,
  `MOA_Other` varchar(30) DEFAULT NULL,
  `ISPs` varchar(100) DEFAULT NULL,
  `Bandwidth` varchar(20) DEFAULT NULL,
  `Employee_net` int(4) DEFAULT NULL,
  `Employee_mail` int(4) DEFAULT NULL,
  `Website` tinyint(1) NOT NULL,
  `URL` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `network`
--

INSERT INTO `network` (`Code`, `LAN`, `Intranet`, `VPN`, `WAN`, `PABX_PBX`, `PBX_Setup`, `Internet`, `MOA`, `MOA_Other`, `ISPs`, `Bandwidth`, `Employee_net`, `Employee_mail`, `Website`, `URL`) VALUES
('781901', 0, 0, 0, 0, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `office_codes`
--

CREATE TABLE `office_codes` (
  `Code` char(6) NOT NULL,
  `Office_ID` smallint(2) UNSIGNED NOT NULL,
  `Year` year(4) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `office_codes`
--

INSERT INTO `office_codes` (`Code`, `Office_ID`, `Year`) VALUES
('011932', 1, '1932'),
('382001', 38, '2001'),
('382023', 38, '2023'),
('781901', 78, '1901'),
('782001', 78, '2001'),
('782100', 78, '2100'),
('921999', 92, '1999'),
('991901', 99, '1901'),
('992021', 99, '2021'),
('992100', 99, '2100');

-- --------------------------------------------------------

--
-- Table structure for table `office_names`
--

CREATE TABLE `office_names` (
  `Office_ID` smallint(2) UNSIGNED NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `office_names`
--

INSERT INTO `office_names` (`Office_ID`, `Name`) VALUES
(1, 'Another Office'),
(38, 'Office for testing'),
(78, 'The next office'),
(92, 'Office of Offices'),
(99, 'Test office');

-- --------------------------------------------------------

--
-- Table structure for table `pc_os`
--

CREATE TABLE `pc_os` (
  `Code` char(6) NOT NULL,
  `PC_OS_Name` varchar(25) NOT NULL,
  `Lifetime` tinyint(1) NOT NULL,
  `Expiration` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pc_os`
--

INSERT INTO `pc_os` (`Code`, `PC_OS_Name`, `Lifetime`, `Expiration`) VALUES
('991901', 'Linux', 1, NULL),
('991901', 'Unreal Engine', 0, '0000'),
('991901', 'Windows 8 and up', 1, NULL),
('991901', 'Windows XP', 0, '2003');

-- --------------------------------------------------------

--
-- Table structure for table `security`
--

CREATE TABLE `security` (
  `Code` char(6) NOT NULL,
  `Protection` tinyint(1) NOT NULL,
  `Measures` set('Software firewall','Policy','Back-up power','Encryption','Hardware firewall','Security service','Security training','Disaster Recovery Plan','Digital signatures','Off-site back-up','Physical restriction','Secure servers','Non-local back-up media') DEFAULT NULL,
  `Other` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `servers`
--

CREATE TABLE `servers` (
  `Code` char(6) NOT NULL,
  `Capacity` enum('Above 4 TB','2 TB to 4 TB','Below 2 TB') NOT NULL,
  `In-house` int(6) DEFAULT NULL,
  `Co-located` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servers`
--

INSERT INTO `servers` (`Code`, `Capacity`, `In-house`, `Co-located`) VALUES
('991901', 'Above 4 TB', NULL, 23),
('991901', '2 TB to 4 TB', 133, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `server_os`
--

CREATE TABLE `server_os` (
  `Code` char(6) NOT NULL,
  `Server_OS_Name` varchar(25) NOT NULL,
  `Lifetime` tinyint(1) NOT NULL,
  `Expiration` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `server_os`
--

INSERT INTO `server_os` (`Code`, `Server_OS_Name`, `Lifetime`, `Expiration`) VALUES
('382001', 'Windows Server 2008', 1, NULL),
('991901', 'Test OS', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `si_systems`
--

CREATE TABLE `si_systems` (
  `Code` char(6) NOT NULL,
  `SI_System` varchar(20) NOT NULL,
  `Own_Property` enum('Y','N') NOT NULL,
  `Platform` varchar(10) NOT NULL,
  `Environment` enum('S','C','W') NOT NULL,
  `Maintenance_Cost` decimal(8,2) NOT NULL,
  `Use_Codes` set('1','2','3','4','5','6','7','8','9','10','11','12','13','14') NOT NULL,
  `Use_other` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `si_systems`
--

INSERT INTO `si_systems` (`Code`, `SI_System`, `Own_Property`, `Platform`, `Environment`, `Maintenance_Cost`, `Use_Codes`, `Use_other`) VALUES
('991901', 'test', 'N', 'test2', 'S', 0.00, '3', NULL),
('992100', 'no', 'N', 'reak', 'S', 0.00, '1,2,3,4', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `special_solutions`
--

CREATE TABLE `special_solutions` (
  `Code` char(6) NOT NULL,
  `Package` varchar(70) NOT NULL,
  `Use_codes` set('1','2','3','4','5','6','7','8','9','10','11','12','13','14') NOT NULL,
  `Use_other` varchar(30) DEFAULT NULL,
  `Maintenance_Cost` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`) VALUES
(1, 'admin', '$2y$10$.HMcEjk7GUtuYxyXybe2lOc4bqS4z8tFuhNAiiTKsUYAKRw2Idjcy'),
(2, 'test', 'test2');

-- --------------------------------------------------------

--
-- Table structure for table `ws_os`
--

CREATE TABLE `ws_os` (
  `Code` char(6) NOT NULL,
  `WS_OS_Name` varchar(25) NOT NULL,
  `Lifetime` tinyint(1) NOT NULL,
  `Expiration` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ws_os`
--

INSERT INTO `ws_os` (`Code`, `WS_OS_Name`, `Lifetime`, `Expiration`) VALUES
('382001', 'Windows NT', 1, NULL),
('382023', 'Mac OS', 1, NULL),
('991901', 'Solaris', 1, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_systems`
--
ALTER TABLE `admin_systems`
  ADD PRIMARY KEY (`Code`,`Admin_System`);

--
-- Indexes for table `annex_a-5`
--
ALTER TABLE `annex_a-5`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `archiving`
--
ALTER TABLE `archiving`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `automation_software`
--
ALTER TABLE `automation_software`
  ADD PRIMARY KEY (`Code`,`Software`);

--
-- Indexes for table `cd_usage`
--
ALTER TABLE `cd_usage`
  ADD PRIMARY KEY (`Code`,`CD_Type`);

--
-- Indexes for table `cd_year`
--
ALTER TABLE `cd_year`
  ADD PRIMARY KEY (`Code`,`CD_Type`);

--
-- Indexes for table `databases`
--
ALTER TABLE `databases`
  ADD PRIMARY KEY (`Code`,`DB_Name`);

--
-- Indexes for table `data_center`
--
ALTER TABLE `data_center`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `ict_issues`
--
ALTER TABLE `ict_issues`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `ict_projects`
--
ALTER TABLE `ict_projects`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `network`
--
ALTER TABLE `network`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `office_codes`
--
ALTER TABLE `office_codes`
  ADD PRIMARY KEY (`Code`),
  ADD KEY `Year` (`Year`) USING BTREE,
  ADD KEY `Office_ID` (`Office_ID`);

--
-- Indexes for table `office_names`
--
ALTER TABLE `office_names`
  ADD PRIMARY KEY (`Office_ID`) USING BTREE;

--
-- Indexes for table `pc_os`
--
ALTER TABLE `pc_os`
  ADD PRIMARY KEY (`Code`,`PC_OS_Name`);

--
-- Indexes for table `security`
--
ALTER TABLE `security`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `servers`
--
ALTER TABLE `servers`
  ADD PRIMARY KEY (`Code`,`Capacity`);

--
-- Indexes for table `server_os`
--
ALTER TABLE `server_os`
  ADD PRIMARY KEY (`Code`,`Server_OS_Name`);

--
-- Indexes for table `si_systems`
--
ALTER TABLE `si_systems`
  ADD PRIMARY KEY (`Code`,`SI_System`);

--
-- Indexes for table `special_solutions`
--
ALTER TABLE `special_solutions`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `ws_os`
--
ALTER TABLE `ws_os`
  ADD PRIMARY KEY (`Code`,`WS_OS_Name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `office_names`
--
ALTER TABLE `office_names`
  MODIFY `Office_ID` smallint(2) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_systems`
--
ALTER TABLE `admin_systems`
  ADD CONSTRAINT `admin_systems_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `annex_a-5`
--
ALTER TABLE `annex_a-5`
  ADD CONSTRAINT `annex_a-5_ibfk_1` FOREIGN KEY (`Year`) REFERENCES `office_codes` (`Year`);

--
-- Constraints for table `archiving`
--
ALTER TABLE `archiving`
  ADD CONSTRAINT `archiving_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `automation_software`
--
ALTER TABLE `automation_software`
  ADD CONSTRAINT `automation_software_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `cd_usage`
--
ALTER TABLE `cd_usage`
  ADD CONSTRAINT `cd_usage_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `cd_year`
--
ALTER TABLE `cd_year`
  ADD CONSTRAINT `cd_year_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `databases`
--
ALTER TABLE `databases`
  ADD CONSTRAINT `databases_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `data_center`
--
ALTER TABLE `data_center`
  ADD CONSTRAINT `data_center_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `ict_issues`
--
ALTER TABLE `ict_issues`
  ADD CONSTRAINT `ict_issues_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `ict_projects`
--
ALTER TABLE `ict_projects`
  ADD CONSTRAINT `ict_projects_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `network`
--
ALTER TABLE `network`
  ADD CONSTRAINT `network_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `pc_os`
--
ALTER TABLE `pc_os`
  ADD CONSTRAINT `pc_os_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `security`
--
ALTER TABLE `security`
  ADD CONSTRAINT `security_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `servers`
--
ALTER TABLE `servers`
  ADD CONSTRAINT `servers_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `server_os`
--
ALTER TABLE `server_os`
  ADD CONSTRAINT `server_os_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `si_systems`
--
ALTER TABLE `si_systems`
  ADD CONSTRAINT `si_systems_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `special_solutions`
--
ALTER TABLE `special_solutions`
  ADD CONSTRAINT `special_solutions_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);

--
-- Constraints for table `ws_os`
--
ALTER TABLE `ws_os`
  ADD CONSTRAINT `ws_os_ibfk_1` FOREIGN KEY (`Code`) REFERENCES `office_codes` (`Code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
