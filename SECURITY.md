# Security and privacy reports

Privacy leakage is treated as a release-blocking defect.

If a commit, issue, artefact, log, or test fixture contains real learner content, stop distribution and remove public access before continuing ordinary development. Do not copy the exposed content into a new issue or discussion while reporting it.

## Private reporting

Use GitHub's private vulnerability reporting feature from the repository's
Security page. Do not open a public issue containing diary material, personal
details, credentials, source excerpts, screenshots, or enough context to
reconstruct the exposure.

If the private reporting control is unexpectedly unavailable, open only a
content-free public issue asking the maintainer to enable a private channel.
Do not describe the vulnerability or affected content in that issue.

## Response to private-content exposure

If real learner content or a secret enters any Git ref, release, issue, Action
log, artefact, or public page:

1. make the repository private immediately and disable affected distribution
   surfaces;
2. preserve a private incident record without copying exposed learner content
   into ordinary project logs;
3. revoke or rotate exposed credentials and tokens;
4. identify every affected commit, branch, tag, release, cache, artefact, and
   fork;
5. remove the content from the working tree and rewrite every affected Git ref;
6. force-update the cleaned refs and remove affected releases or artefacts;
7. ask GitHub Support for cache or view removal when ordinary history rewriting
   cannot remove an exposed object;
8. rerun the repository privacy scanner, secret scanning, and the complete test
   suite against the exact publication candidate;
9. restore public visibility only after the cleaned remote state has been
   independently verified.

History rewriting does not recall existing clones or forks. Treat any public
exposure as potentially permanent and avoid publishing private learning data in
the first place.
