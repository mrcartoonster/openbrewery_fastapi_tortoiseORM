##### upgrade #####
ALTER TABLE "sponsors" RENAME COLUMN "github_repo" TO "github_id";
##### downgrade #####
ALTER TABLE "sponsors" RENAME COLUMN "github_id" TO "github_repo";
