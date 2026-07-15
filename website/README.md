# jqhe.uk Astro Website v0.1

This is a static Astro implementation of the jqhe.uk public research portal.

Canonical repository: https://github.com/Jiaquan-Research/ship-health-monitoring
Canonical website URL: https://jqhe.uk

## Local Setup

```text
npm install
npm run sync-manifests
npm run validate
npm run build
```

On Windows PowerShell environments where script execution policy blocks `npm`, use `npm.cmd`. If the default npm cache is not writable, use a local cache:

```text
npm.cmd install --cache .npm-cache
```

## Cloudflare Pages Settings

- Root directory: `website`
- Build command: `npm run build`
- Output directory: `dist`

Cloudflare deployment, DNS changes, and domain binding are not performed by this repository task.

## Directory Structure

```text
website/
  src/
    components/
    layouts/
    lib/
    pages/
    styles/
  public/
    manifests/
  scripts/
```

## Manifest Source Model

Repository-level manifests are the sole governed source:

```text
manifest/repository_manifest.json
manifest/public_manifest.json
manifest/machine_retrieval_manifest.json
```

Deployment copies are generated into:

```text
website/public/manifests/
```

They are copied byte-for-byte by:

```text
npm run sync-manifests
```

The sync script parses each source JSON, copies exact bytes, computes SHA-256 for source and destination, and fails if hashes differ. It is run automatically before validation and build.

Public pages default to `public_manifest.json`. Machine Access pages expose `repository_manifest.json` and `machine_retrieval_manifest.json`.

## Publication Guard

`npm run validate` runs manifest synchronization first, then checks that:

- required routes exist;
- manifest JSON parses;
- public and machine manifest entries exist in the repository manifest;
- key metadata matches across manifest views;
- forbidden visibility classes are not exposed through the public manifest;
- generated transport/execution copies are not treated as scientific source authority;
- website derivatives are not repository or scope authorities;
- required source document IDs remain available;
- copied manifest hashes match repository-level source manifests;
- source links use `https://github.com/Jiaquan-Research/ship-health-monitoring`.

`npm run build` runs validation before the Astro static build.

## Updating Website Content

Update repository source documents and governed manifests first. Then run:

```text
npm run sync-manifests
npm run validate
npm run build
```

Do not edit `website/public/manifests/*.json` independently.

## Authority Boundary

Website pages are `WEBSITE_DERIVATIVE` public views. They are never source authority. Frozen package, protocol, state, and governance records remain authoritative within their own scopes.
