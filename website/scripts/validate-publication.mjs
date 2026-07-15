import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const root = process.cwd();
const repoRoot = path.resolve(root, "..");
const publicPath = path.join(root, "public/manifests/public_manifest.json");
const machinePath = path.join(root, "public/manifests/machine_retrieval_manifest.json");
const repoPath = path.join(root, "public/manifests/repository_manifest.json");
const sourceManifestDir = path.join(repoRoot, "manifest");
const repositoryBaseUrl = "https://github.com/Jiaquan-Research/ship-health-monitoring";
const oldRepositoryBaseUrl = "https://github.com/jqhe/ship-health-monitoring";

const requiredRoutes = [
  "src/pages/index.astro",
  "src/pages/status.astro",
  "src/pages/research.astro",
  "src/pages/projects.astro",
  "src/pages/projects/ship-health-monitoring/index.astro",
  "src/pages/projects/ship-health-monitoring/marine-package.astro",
  "src/pages/projects/ship-health-monitoring/boundaries.astro",
  "src/pages/projects/ship-health-monitoring/framework.astro",
  "src/pages/projects/ship-health-monitoring/validation.astro",
  "src/pages/projects/ship-health-monitoring/external-validation.astro",
  "src/pages/projects/ship-health-monitoring/deep-research.astro",
  "src/pages/review/index.astro",
  "src/pages/review/deep-research.astro",
  "src/pages/review/external-validation.astro",
  "src/pages/machine/index.astro",
  "src/pages/machine/manifest.astro",
  "src/pages/machine/public-manifest.astro",
  "src/pages/machine/retrieval-manifest.astro",
  "src/pages/machine/governance.astro",
  "src/pages/governance/index.astro",
  "src/pages/about/index.astro"
];

const requiredIds = [
  "ROOT-SYSTEM-STATE",
  "ROOT-PUBLISHING-STATUS",
  "ROOT-README",
  "MPV1-PACKAGE",
  "MPV1-GAP-REGISTER",
  "EXTVAL-APPROVAL-FREEZE-RECORD",
  "EXTVAL-SPEC",
  "TRV2-GUIDE",
  "BRV2-SESSION-PROTOCOL",
  "BRV2-EXEC-PACKAGE-README",
  "HEF-ARCHITECTURE",
  "GOV-REPOSITORY-POLICY",
  "GOV-PUBLISHING-POLICY",
  "GOV-MACHINE-RETRIEVAL-POLICY"
];

const forbiddenPublicVisibility = new Set(["INTERNAL", "ARCHIVE_ONLY", "REVIEW_PACKAGE_ONLY"]);
const comparableFields = ["document_id", "path", "authority_level", "lifecycle_state", "copy_role", "public_visibility"];
const errors = [];

function sha256(bytes) {
  return crypto.createHash("sha256").update(bytes).digest("hex").toUpperCase();
}

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (error) {
    errors.push(`Invalid JSON: ${file}: ${error.message}`);
    return { entries: [] };
  }
}

function assertExists(file, label) {
  if (!fs.existsSync(file)) {
    errors.push(`Missing ${label}: ${file}`);
    return false;
  }
  return true;
}

function assertUnique(entries, field, manifestName) {
  const seen = new Set();
  for (const entry of entries) {
    const value = entry[field];
    if (!value) continue;
    if (seen.has(value)) errors.push(`${manifestName} duplicate ${field}: ${value}`);
    seen.add(value);
  }
}

function compareToRepository(entry, repoById, manifestName) {
  const repoEntry = repoById.get(entry.document_id);
  if (!repoEntry) {
    errors.push(`${manifestName} entry missing from repository manifest: ${entry.document_id}`);
    return;
  }
  for (const field of comparableFields) {
    if (entry[field] !== repoEntry[field]) {
      errors.push(`${manifestName} metadata mismatch for ${entry.document_id}.${field}: ${entry[field]} != ${repoEntry[field]}`);
    }
  }
}

for (const [file, label] of [[publicPath, "public manifest copy"], [machinePath, "machine manifest copy"], [repoPath, "repository manifest copy"]]) {
  assertExists(file, label);
}

const publicManifest = readJson(publicPath);
const machineManifest = readJson(machinePath);
const repoManifest = readJson(repoPath);

const repoById = new Map(repoManifest.entries.map((entry) => [entry.document_id, entry]));
const publicIds = new Set(publicManifest.entries.map((entry) => entry.document_id));
const machineIds = new Set(machineManifest.entries.map((entry) => entry.document_id));

for (const [entries, manifestName] of [[repoManifest.entries, "repository manifest"], [publicManifest.entries, "public manifest"], [machineManifest.entries, "machine retrieval manifest"]]) {
  assertUnique(entries, "document_id", manifestName);
  assertUnique(entries, "path", manifestName);
}

for (const entry of publicManifest.entries) {
  compareToRepository(entry, repoById, "public manifest");
  if (forbiddenPublicVisibility.has(entry.public_visibility)) {
    errors.push(`Forbidden public visibility exposed: ${entry.document_id} ${entry.public_visibility}`);
  }
}

for (const entry of machineManifest.entries) {
  compareToRepository(entry, repoById, "machine retrieval manifest");
}

for (const entry of [...repoManifest.entries, ...publicManifest.entries, ...machineManifest.entries]) {
  if (entry.copy_role === "WEBSITE_DERIVATIVE" && ["REPOSITORY_STATE_AUTHORITY", "SCOPE_AUTHORITY"].includes(entry.authority_level)) {
    errors.push(`Website derivative has authority status: ${entry.document_id} ${entry.authority_level}`);
  }
  if (["TRANSPORT_COPY", "EXECUTION_COPY"].includes(entry.copy_role) && entry.document_class === "SCIENTIFIC_SOURCE") {
    errors.push(`Generated delivery copy classified as scientific source: ${entry.document_id}`);
  }
}

for (const route of requiredRoutes) {
  if (!fs.existsSync(path.join(root, route))) errors.push(`Missing required route file: ${route}`);
}

for (const id of requiredIds) {
  if (!publicIds.has(id) && !machineIds.has(id)) errors.push(`Required source mapping missing from public/machine views: ${id}`);
}

for (const fileName of ["repository_manifest.json", "public_manifest.json", "machine_retrieval_manifest.json"]) {
  const sourcePath = path.join(sourceManifestDir, fileName);
  const copyPath = path.join(root, "public", "manifests", fileName);
  if (!assertExists(sourcePath, `source manifest ${fileName}`) || !assertExists(copyPath, `website manifest copy ${fileName}`)) continue;
  const sourceHash = sha256(fs.readFileSync(sourcePath));
  const copyHash = sha256(fs.readFileSync(copyPath));
  if (sourceHash !== copyHash) errors.push(`Manifest copy hash mismatch for ${fileName}: ${sourceHash} != ${copyHash}`);
}

const manifestSource = fs.readFileSync(path.join(root, "src/lib/manifest.ts"), "utf8");
if (!manifestSource.includes(`repositoryBaseUrl = "${repositoryBaseUrl}"`)) {
  errors.push(`Configured GitHub base URL is not ${repositoryBaseUrl}`);
}

const textFiles = [];
function collectTextFiles(directory) {
  for (const item of fs.readdirSync(directory, { withFileTypes: true })) {
    const full = path.join(directory, item.name);
    if (item.isDirectory()) {
      if (["node_modules", "dist", ".npm-cache", ".astro"].includes(item.name)) continue;
      collectTextFiles(full);
    } else if (/\.(astro|ts|mjs|js|md|json|css|html|txt)$/i.test(item.name)) {
      textFiles.push(full);
    }
  }
}
for (const directory of [path.join(root, "src"), path.join(root, "public")]) {
  if (fs.existsSync(directory)) collectTextFiles(directory);
}
for (const file of [path.join(root, "README.md")]) {
  if (fs.existsSync(file)) textFiles.push(file);
}
for (const file of textFiles) {
  const text = fs.readFileSync(file, "utf8");
  if (text.includes(oldRepositoryBaseUrl)) errors.push(`Old GitHub base URL remains in ${path.relative(root, file)}`);
}

if (errors.length) {
  console.error("Publication validation: FAIL");
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log("Publication validation: PASS");
