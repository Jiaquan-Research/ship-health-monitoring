import fs from "node:fs";
import path from "node:path";

export type ManifestEntry = {
  document_id: string;
  path: string;
  title: string;
  project_scope: string;
  document_class: string;
  authority_level: string;
  lifecycle_state: string;
  audience?: string;
  public_visibility: string;
  retrieval_priority: number;
  copy_role: string;
  canonical_source?: string | null;
  canonical_successor?: string | null;
  hash?: string;
  notes?: string;
  preferred_use?: string;
  warning?: string | null;
};

type PublicManifest = {
  manifest_type: string;
  version: string;
  generated_from: string;
  generated_date: string;
  entries: ManifestEntry[];
};

type MachineManifest = {
  manifest_type: string;
  version: string;
  generated_from: string;
  generated_date: string;
  retrieval_policy: string;
  preferred_entry_points: Record<string, string[]>;
  warnings: string[];
  entries: ManifestEntry[];
};

const root = process.cwd();

function readJson<T>(relativePath: string): T {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), "utf8")) as T;
}

export function publicManifest(): PublicManifest {
  return readJson<PublicManifest>("public/manifests/public_manifest.json");
}

export function machineManifest(): MachineManifest {
  return readJson<MachineManifest>("public/manifests/machine_retrieval_manifest.json");
}

export function repositoryManifest(): PublicManifest {
  return readJson<PublicManifest>("public/manifests/repository_manifest.json");
}

export function entries(): ManifestEntry[] {
  return publicManifest().entries;
}

export function machineEntries(): ManifestEntry[] {
  return machineManifest().entries;
}

export function byId(id: string, source: "public" | "machine" | "repository" = "public"): ManifestEntry {
  const list =
    source === "machine" ? machineEntries() : source === "repository" ? repositoryManifest().entries : entries();
  const found = list.find((entry) => entry.document_id === id);
  if (!found) {
    throw new Error(`Manifest document_id not found: ${id}`);
  }
  return found;
}

export function filterEntries(criteria: Partial<ManifestEntry>): ManifestEntry[] {
  return entries().filter((entry) =>
    Object.entries(criteria).every(([key, value]) => entry[key as keyof ManifestEntry] === value)
  );
}

export const repositoryBaseUrl = "https://github.com/Jiaquan-Research/ship-health-monitoring";

export function sourceHref(entry: ManifestEntry): string {
  const normalizedPath = entry.path.replaceAll("\\", "/");
  return `${repositoryBaseUrl}/blob/main/${normalizedPath}`;
}

export function formatLabel(value: string): string {
  return value.replaceAll("_", " ");
}

export const coreIds = {
  state: "ROOT-SYSTEM-STATE",
  publishing: "ROOT-PUBLISHING-STATUS",
  readme: "ROOT-README",
  marinePackage: "MPV1-PACKAGE",
  marineGaps: "MPV1-GAP-REGISTER",
  marineArtifacts: "MPV1-ARTIFACT-INDEX",
  externalValidation: "EXTVAL-APPROVAL-FREEZE-RECORD",
  externalSpec: "EXTVAL-SPEC",
  framework: "HEF-ARCHITECTURE",
  transportGuide: "TRV2-GUIDE",
  sessionProtocol: "BRV2-SESSION-PROTOCOL",
  executionPackage: "BRV2-EXEC-PACKAGE-README",
  governancePolicy: "GOV-REPOSITORY-POLICY",
  publishingPolicy: "GOV-PUBLISHING-POLICY",
  retrievalPolicy: "GOV-MACHINE-RETRIEVAL-POLICY"
};
