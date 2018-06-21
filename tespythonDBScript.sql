DROP TABLE IF EXISTS `testpythondb`.`customer`;
CREATE TABLE  `testpythondb`.`customer` (
  `account_no` int(10) unsigned NOT NULL DEFAULT '0',
  `account_name` varchar(45) NOT NULL DEFAULT '',
  `account_balance` int(10) unsigned NOT NULL DEFAULT '0',
  `account_password` varchar(45) NOT NULL DEFAULT '',
  PRIMARY KEY (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `testpythondb`.`payees`;
CREATE TABLE  `testpythondb`.`payees` (
  `account_number` int(10) unsigned NOT NULL DEFAULT '0',
  `account_name` varchar(45) NOT NULL DEFAULT '',
  `bank` varchar(45) NOT NULL DEFAULT '',
  `customer_account` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`account_number`,`customer_account`),
  KEY `FK_payees_customer` (`customer_account`),
  CONSTRAINT `FK_payees_customer` FOREIGN KEY (`customer_account`) REFERENCES `customer` (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;