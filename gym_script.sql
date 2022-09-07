-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gym
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gym
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gym` DEFAULT CHARACTER SET utf8 ;
USE `gym` ;

-- -----------------------------------------------------
-- Table `gym`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gym`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(255) NULL,
  `type_user` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym`.`rutines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gym`.`rutines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `type_rutine` TINYINT NULL,
  `time` TINYINT NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_rutines_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_rutines_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `gym`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gym`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `rutine_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_rutines1_idx` (`rutine_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `gym`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_rutines1`
    FOREIGN KEY (`rutine_id`)
    REFERENCES `gym`.`rutines` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `gym` ;

-- -----------------------------------------------------
-- Placeholder table for view `gym`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gym`.`view1` (`id` INT);

-- -----------------------------------------------------
-- Placeholder table for view `gym`.`view2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gym`.`view2` (`id` INT);

-- -----------------------------------------------------
-- View `gym`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym`.`view1`;
USE `gym`;


-- -----------------------------------------------------
-- View `gym`.`view2`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym`.`view2`;
USE `gym`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
