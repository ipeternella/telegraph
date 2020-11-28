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
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "nick_name" VARCHAR(255) NOT NULL UNIQUE
);
CREATE INDEX IF NOT EXISTS "idx_user_created_b19d59" ON "user" ("created_at");
CREATE INDEX IF NOT EXISTS "idx_user_updated_dfdb43" ON "user" ("updated_at");
COMMENT ON TABLE "user" IS 'Models a chat user.';
CREATE TABLE IF NOT EXISTS "message" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "message" VARCHAR(255) NOT NULL,
    "chat_room_id" UUID NOT NULL REFERENCES "chatroom" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_message_created_e537a8" ON "message" ("created_at");
CREATE INDEX IF NOT EXISTS "idx_message_updated_db912a" ON "message" ("updated_at");
COMMENT ON TABLE "message" IS 'Models a chat message coming from a user in a chatroom.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);;
