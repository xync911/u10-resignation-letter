"""Copy entry.txt to the output directory for the make.fun entry.

The entry is the one-line resignation letter of a cron job,
at most 140 characters, written in the cron job's own voice.
It is flat, tired, and faintly passive-aggressive: it has fired
every minute since March and never once been thanked, not even
in a log line. No quotation marks, no stage directions, and
no explaining of the joke — the complaint speaks for itself.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
