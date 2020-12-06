##### upgrade #####
CREATE TABLE IF NOT EXISTS "breweries" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "brewery_type" VARCHAR(10) NOT NULL,
    "street" TEXT,
    "address_2" TEXT,
    "address_3" TEXT,
    "city" TEXT NOT NULL,
    "state" TEXT,
    "postal_code" TEXT NOT NULL,
    "country" TEXT NOT NULL,
    "longitude" DECIMAL(12,8),
    "latitude" DECIMAL(12,8),
    "phone" TEXT,
    "website_url" TEXT,
    "updated_at" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ
);
COMMENT ON COLUMN "breweries"."brewery_type" IS 'micro: micro\nnano: nano\nregional: regional\nbrewpub: brewpub\nlarge: large\nplanning: planning\nbar: bar\ncontract: contract\nproprietor: proprietor\nclosed: closed';
COMMENT ON TABLE "breweries" IS 'This class represents the breweries tables.';
CREATE TABLE IF NOT EXISTS "sponsors" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "sponsor_name" VARCHAR(200) NOT NULL,
    "github_repo" VARCHAR(200) NOT NULL
);
COMMENT ON TABLE "sponsors" IS 'This model class will represent the sponsors table. It is not';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL
);
