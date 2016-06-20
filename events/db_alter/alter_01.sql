ALTER TABLE comment_tab ADD COLUMN content VARCHAR(300) NOT NULL DEFAULT 'content';
ALTER TABLE user_account_tab ADD COLUMN avatar_id VARCHAR(36);
ALTER TABLE event_tab ADD COLUMN avatar_id VARCHAR(36);