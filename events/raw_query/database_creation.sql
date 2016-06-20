BEGIN;
CREATE TABLE `channel_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `name` varchar(100) NOT NULL
)
;
CREATE TABLE `user_account_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `full_name` varchar(100) NOT NULL,
    `email` varchar(100) NOT NULL,
    `password` varchar(100) NOT NULL,
    `token` varchar(100),
    `is_admin` bool NOT NULL,
    `token_expired_on` datetime,
    `avatar_id` varchar(100)
)
;
CREATE TABLE `event_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `title` varchar(100) NOT NULL,
    `description` varchar(300) NOT NULL,
    `location` varchar(300) NOT NULL,
    `start_date` datetime NOT NULL,
    `end_date` datetime NOT NULL,
    `channel_id` integer NOT NULL,
    `creator_id` integer NOT NULL,
    `avatar_id` varchar(100)
)
;
ALTER TABLE `event_tab` ADD CONSTRAINT `creator_id_refs_id_2f0fd717` FOREIGN KEY (`creator_id`) REFERENCES `user_account_tab` (`id`);
ALTER TABLE `event_tab` ADD CONSTRAINT `channel_id_refs_id_8c40061f` FOREIGN KEY (`channel_id`) REFERENCES `channel_tab` (`id`);
CREATE TABLE `participant_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `event_id` integer NOT NULL
)
;
ALTER TABLE `participant_tab` ADD CONSTRAINT `user_id_refs_id_7204a3c6` FOREIGN KEY (`user_id`) REFERENCES `user_account_tab` (`id`);
ALTER TABLE `participant_tab` ADD CONSTRAINT `event_id_refs_id_4463ece6` FOREIGN KEY (`event_id`) REFERENCES `event_tab` (`id`);
CREATE TABLE `like_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `event_id` integer NOT NULL
)
;
ALTER TABLE `like_tab` ADD CONSTRAINT `user_id_refs_id_f851d2b3` FOREIGN KEY (`user_id`) REFERENCES `user_account_tab` (`id`);
ALTER TABLE `like_tab` ADD CONSTRAINT `event_id_refs_id_fbaf9ccd` FOREIGN KEY (`event_id`) REFERENCES `event_tab` (`id`);
CREATE TABLE `comment_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `event_id` integer NOT NULL,
    `main_comment` integer,
    `content` varchar(300) NOT NULL
)
;
ALTER TABLE `comment_tab` ADD CONSTRAINT `user_id_refs_id_2775b4f8` FOREIGN KEY (`user_id`) REFERENCES `user_account_tab` (`id`);
ALTER TABLE `comment_tab` ADD CONSTRAINT `event_id_refs_id_be37c626` FOREIGN KEY (`event_id`) REFERENCES `event_tab` (`id`);
ALTER TABLE `comment_tab` ADD CONSTRAINT `main_comment_refs_id_d1f39561` FOREIGN KEY (`main_comment`) REFERENCES `comment_tab` (`id`);
CREATE TABLE `document_tab` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_date` datetime NOT NULL,
    `updated_date` datetime NOT NULL,
    `user_id` integer,
    `event_id` integer,
    `name` varchar(100),
    `physical_id` varchar(36) NOT NULL,
    `is_main` bool NOT NULL
)
;
ALTER TABLE `document_tab` ADD CONSTRAINT `user_id_refs_id_8aec3ff3` FOREIGN KEY (`user_id`) REFERENCES `user_account_tab` (`id`);
ALTER TABLE `document_tab` ADD CONSTRAINT `event_id_refs_id_ccc935b3` FOREIGN KEY (`event_id`) REFERENCES `event_tab` (`id`);

COMMIT;
