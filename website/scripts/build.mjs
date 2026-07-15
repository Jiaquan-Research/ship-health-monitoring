import { spawnSync } from "node:child_process";
import path from "node:path";

const command = process.platform === "win32"
  ? path.join("node_modules", ".bin", "astro.cmd")
  : path.join("node_modules", ".bin", "astro");
const result = spawnSync(command, ["build"], {
  stdio: "inherit",
  shell: process.platform === "win32",
  env: {
    ...process.env,
    ASTRO_TELEMETRY_DISABLED: "1"
  }
});

process.exit(result.status ?? 1);
