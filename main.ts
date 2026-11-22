// news-image-20261122: copy the finished front page to the output dir.
// Node 22, standard library only, no network. Deterministic: the same
// bytes in, the same bytes out, every run.
//
// The image itself is drawn by draw.py (Python + PIL, shapes only) and
// committed as entry.png; this program only places it where the grader
// looks for it, so two runs always write byte-identical output.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
