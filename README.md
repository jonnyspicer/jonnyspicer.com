# cdn branch

This is an orphan branch, deliberately disconnected from `main`. It exists only
to back the `img.jonnyspicer.com` subdomain in AWS Amplify, which is mapped to
this branch rather than to `main`.

It is named `cdn` rather than `assets` because the repo already has an `assets/`
directory on `main`, and a branch of the same name makes git commands ambiguous
between the ref and the path.

Everything at the root of this branch is published verbatim at the subdomain:

    photo-2026-08-12.jpg  ->  https://img.jonnyspicer.com/photo-2026-08-12.jpg

`amplify.yml` runs no build. It publishes the branch root as-is, so there is no
Hugo step and no Python step here.

To add an asset: check out this branch (ideally in a separate worktree, since it
shares no history with `main`), drop the file at the root, commit, push. Amplify
redeploys on push.

Do not merge this branch into `main`, or `main` into this one.
