# Security Policy

## Scope

This repository contains learning exercises, website experiments and beginner cybersecurity lab notes.

## Reporting a concern

If you find a credential, private key, personal data, unsafe link or other security concern in this repository, please do not reuse or share it. Contact the repository owner privately through GitHub so the issue can be reviewed.

## Publishing checklist

- Never commit passwords, API keys, access tokens, wallet seed phrases or private keys.
- Use placeholders or environment variables for configuration and keep local secret files untracked.
- Review third-party scripts, fonts, images and other assets before publishing.
- Verify external links and any claims displayed by a website before deployment.
- Perform security testing only on systems you own or have explicit permission to test.

A `.gitignore` helps prevent accidental commits but does not remove secrets already committed to Git history. If a real secret was ever committed, revoke or rotate it immediately and review the repository history.
