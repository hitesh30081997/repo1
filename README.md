# ---- resume: reuse encoder embeddings from a Kaggle dataset ----
EMB_ROOT = "/kaggle/input/datasets/hiteshramrakhiyani53/encoder-embeddings"
EMB_DIR = os.path.join(OUT_DIR, "encoder_embeddings")
os.makedirs(EMB_DIR, exist_ok=True)


def find_embeddings(root):
    """Return the folder that directly contains the audio_*.pt files (any depth)."""
    if not root or not os.path.isdir(root):
        return None
    for dirpath, _, files in os.walk(root):
        if any(f.startswith("audio_") and f.endswith(".pt") for f in files):
            return dirpath
    return None


_src = find_embeddings(EMB_ROOT if RESUME_FROM == "auto" else RESUME_FROM)
if _src:
    print("Linking embeddings from", _src, "->", EMB_DIR)
    for f in os.listdir(_src):
        dst = os.path.join(EMB_DIR, f)
        if f.startswith("audio_") and f.endswith(".pt") and not os.path.exists(dst):
            try:
                os.symlink(os.path.join(_src, f), dst)        # instant, no extra disk space
            except OSError:
                shutil.copy2(os.path.join(_src, f), dst)      # fallback: copy
else:
    print("No embeddings found in", EMB_ROOT, "-> they will be computed")

for k in ENCODERS:   # check every encoder's file name matches what audio_cache() expects
    fn = f"audio_{k}_c{CHUNK_SEC}_mx{MAX_AUDIO_CHUNKS}_ps{int(USE_PARTICIPANT_SEGMENTS)}.pt"
    print(f"  {k:14s} {'FOUND  ' if os.path.exists(os.path.join(EMB_DIR, fn)) else 'MISSING'} {fn}")

_tag = lambda s: re.sub(r"[^A-Za-z0-9]+", "-", s)
CACHE_DIR = os.path.join(OUT_DIR, "cache_base",
                         f"{_tag(TEXT_MODEL)}_mw{MIN_WORDS}_ps{int(USE_PARTICIPANT_SEGMENTS)}"
                         f"_gm{int(USE_EGEMAPS)}_c{CHUNK_SEC}_mx{MAX_AUDIO_CHUNKS}_mel{N_MELS}_ce{int(CHEAP_EGEMAPS)}")
for d in (OUT_DIR, CACHE_DIR, EMB_DIR, TUNE_DIR):
    os.makedirs(d, exist_ok=True)
