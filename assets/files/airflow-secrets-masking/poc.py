"""CVE-2026-111452: key-based redaction checks.

Author: Anass Bali / 0xbaas
Adapted from the original reporting PoC to accept the source module as an argument.
The masking checks are unchanged. The dummy password is Welkom01.
Run in a Python environment containing the target module's dependencies.
The original recorded run used commit df7b8a7 and Python 3.11.9.
"""

import importlib.util
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: python poc.py /path/to/secrets_masker.py")

SRC = Path(sys.argv[1]).expanduser().resolve()
if not SRC.is_file():
    raise SystemExit("Source module not found: " + str(SRC))

print("Loading module: " + SRC.name)
print(f"Exists: {SRC.exists()}")
print(f"Python: {sys.version.split()[0]}")

spec = importlib.util.spec_from_file_location("secrets_masker_under_test", SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

masker = mod.SecretsMasker()
masker.sensitive_variables_fields = list(mod.DEFAULT_SENSITIVE_FIELDS)
masker.hide_sensitive_var_conn_fields = True

MATRIX = [
    # camelCase test cases
    "privateKey",
    "serviceAccount",
    "connectionString",
    "webhookUrl",
    "clientSecret",
    "apiKey",
    "accessToken",
    # single-word control
    "password",
    # snake_case controls
    "private_key",
    "service_account",
    "connection_string",
    "webhook_url",
    "api_key",
    "access_token",
]

print("\n=== Sensitive key detection ===")
results = {}
for key in MATRIX:
    hide = masker.should_hide_value_for_key(key)
    results[key] = hide
    print(f"  {key!r:22} -> {hide}")

# Test dictionary redaction
print("\n=== JSON payload redaction ===")
payload_camel = {
    "privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...",
    "serviceAccount": "my-sa@project.iam.gserviceaccount.com",
    "connectionString": "Server=db;User Id=app;Password=Welkom01;",
    "webhookUrl": "https://hooks.example.com/services/T000/B000/secret-token",
    "note": "not sensitive",
}
redacted_camel = masker.redact(dict(payload_camel))
print(f"  input    : {payload_camel}")
print(f"  redacted : {redacted_camel}")

payload_snake = {
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...",
    "service_account": "my-sa@project.iam.gserviceaccount.com",
    "connection_string": "Server=db;User Id=app;Password=Welkom01;",
    "webhook_url": "https://hooks.example.com/services/T000/B000/secret-token",
}
redacted_snake = masker.redact(dict(payload_snake))
print(f"\n  input    : {payload_snake}")
print(f"  redacted : {redacted_snake}")

# Named value redaction
by_name = masker.redact("-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...", name="privateKey")
print(f"\n  redact(secret, name='privateKey') -> {by_name!r}")
by_name_snake = masker.redact("-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...", name="private_key")
print(f"  redact(secret, name='private_key') -> {by_name_snake!r}")

print("\n=== Summary ===")
leaks = [k for k in ("privateKey", "serviceAccount", "connectionString", "webhookUrl") if not results[k]]
controls_ok = results["private_key"] and results["api_key"] and results["password"]
plaintext_leaked = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASC" in str(redacted_camel)
snake_masked = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASC" not in str(redacted_snake)
print(f"  camelCase keys not detected     : {len(leaks)}")
print(f"  snake_case controls passed     : {controls_ok}")
print(f"  camelCase values remain unmasked: {plaintext_leaked}")
print(f"  snake_case values masked       : {snake_masked}")
if leaks and controls_ok and plaintext_leaked and snake_masked:
    print("  CONFIRMED: camelCase keys bypass key-based redaction")
else:
    print("  NOT confirmed, check the output above")
