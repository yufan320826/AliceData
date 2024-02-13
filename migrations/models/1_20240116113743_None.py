from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32)   COMMENT '用户名' DEFAULT 'root',
    `email` VARCHAR(128)   COMMENT '邮箱',
    `age` INT   COMMENT '年龄',
    `birthday` DATE   COMMENT '生日',
    `user_scl` TIME(6)   COMMENT '用户头像',
    `create_time` DATE   COMMENT '注册时间',
    `password` VARCHAR(32)   COMMENT '密码'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `useravatar` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `avatar_id` INT NOT NULL,
    `image` LONGBLOB   COMMENT '图片',
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_useravat_user_0a0c31f8` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `userdetail` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `bio` LONGTEXT NOT NULL  COMMENT '用户简介',
    `address` VARCHAR(256)   COMMENT '居住地',
    `school` VARCHAR(256)   COMMENT '毕业学院',
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_userdeta_user_ced8644d` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `wish` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `wish_id` INT NOT NULL,
    `wish_title` LONGTEXT   COMMENT '标题',
    `wish_content` LONGTEXT   COMMENT '内容',
    `wish_area` VARCHAR(32)   COMMENT '记录地区'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `user_wish` (
    `user_id` INT NOT NULL,
    `wish_id` INT NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`wish_id`) REFERENCES `wish` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
