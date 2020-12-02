##### upgrade #####
CREATE TABLE IF NOT EXISTS "chatroom" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "max_concurrent_users" INT NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True
);
CREATE INDEX IF NOT EXISTS "idx_chatroom_created_d59897" ON "chatroom" ("created_at");
CREATE INDEX IF NOT EXISTS "idx_chatroom_updated_1d41e3" ON "chatroom" ("updated_at");
CREATE INDEX IF NOT EXISTS "idx_chatroom_name_f56787" ON "chatroom" ("name");
CREATE INDEX IF NOT EXISTS "idx_chatroom_name_57c5fa" ON "chatroom" ("name", "is_active");
COMMENT ON TABLE "chatroom" IS 'Models a chatroom.';
CREATE TABLE IF NOT EXISTS "chatuser" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "age" SMALLINT NOT NULL,
    "nick_name" VARCHAR(255) NOT NULL UNIQUE
);
CREATE INDEX IF NOT EXISTS "idx_chatuser_created_9c3184" ON "chatuser" ("created_at");
CREATE INDEX IF NOT EXISTS "idx_chatuser_updated_828a26" ON "chatuser" ("updated_at");
COMMENT ON TABLE "chatuser" IS 'Models a chat user.';
CREATE TABLE IF NOT EXISTS "chatmessage" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "message" VARCHAR(255) NOT NULL,
    "chat_room_id" UUID NOT NULL REFERENCES "chatroom" ("id") ON DELETE CASCADE,
    "chat_user_id" UUID NOT NULL REFERENCES "chatuser" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_chatmessage_created_b4c0bf" ON "chatmessage" ("created_at");
CREATE INDEX IF NOT EXISTS "idx_chatmessage_updated_db1ea1" ON "chatmessage" ("updated_at");
COMMENT ON TABLE "chatmessage" IS 'Models a chat message coming from a user in a chatroom.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);
