import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const websiteRoot = path.resolve(scriptDir, "..");
const repoRoot = path.resolve(websiteRoot, "..");
const sourceDir = path.join(repoRoot, "manifest");
const destinationDir = path.join(websiteRoot, "public", "manifests");

const manifestFiles = [
  "repository_manifest.json",
  "public_manifest.json",
  "machine_retrieval_manifest.json"
];

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex").toUpperCase();
}

function fail(message) {
  console.error(`Manifest synchronization: FAIL - ${message}`);
  process.exit(1);
}

fs.mkdirSync(destinationDir, { recursive: true });

for (const fileName of manifestFiles) {
  const sourcePath = path.join(sourceDir, fileName);
  const destinationPath = path.join(destinationDir, fileName);

  if (!fs.existsSync(sourcePath)) {
    fail(`missing source manifest: ${path.relative(repoRoot, sourcePath)}`);
  }

  const sourceBytes = fs.readFileSync(sourcePath);
  try {
    JSON.parse(sourceBytes.toString("utf8"));
  } catch (error) {
    fail(`invalid JSON in ${path.relative(repoRoot, sourcePath)}: ${error.message}`);
  }

  fs.copyFileSync(sourcePath, destinationPath);
  const destinationBytes = fs.readFileSync(destinationPath);
  const sourceHash = sha256(sourceBytes);
  const destinationHash = sha256(destinationBytes);

  if (sourceHash !== destinationHash) {
    fail(`${fileName} hash mismatch after copy: ${sourceHash} != ${destinationHash}`);
  }

  console.log(`Manifest synchronized: ${fileName} ${sourceHash}`);
}
