"""Verify the pinned public skill inventory using only the Python standard library."""

import hashlib
import json
import re
import sys
from pathlib import Path


def check(root):
    root = Path(root).resolve()
    data = json.loads((root / 'catalog' / 'manifest.json').read_text(encoding='utf-8'))
    errors = []
    ids = set()
    total = 0
    for skill in data['skills']:
        ident = skill['id']
        if ident in ids or not re.fullmatch(r'[a-z0-9-]+', ident):
            errors.append(f'Invalid or duplicate skill ID: {ident!r}')
            continue
        ids.add(ident)
        expected_path = 'catalog/' + ident
        if skill['catalog_path'] != expected_path:
            errors.append(f'{ident}: invalid catalog path')
            continue
        folder = root / expected_path
        if folder.is_symlink() or not folder.resolve().is_relative_to(root / 'catalog'):
            errors.append(f'{ident}: unsafe skill directory')
            continue
        if not re.fullmatch(r'[0-9a-f]{40}', skill['upstream_commit']):
            errors.append(f'{ident}: source commit is not pinned')
        expected_url = f"https://github.com/{skill['upstream_repository']}/tree/{skill['upstream_commit']}/{skill['upstream_path']}"
        if skill['upstream_url'] != expected_url:
            errors.append(f'{ident}: source URL does not match pinned provenance')
        original = skill['original_files_sha256']
        added = skill['added_files_sha256']
        if set(original) & set(added):
            errors.append(f'{ident}: original and added inventory overlap')
        expected = {**original, **added}
        actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
        if actual != set(expected):
            errors.append(f'{ident}: missing/unlisted files: {sorted(actual ^ set(expected))}')
        for rel, digest in expected.items():
            path = folder / rel
            if path.is_symlink() or not path.resolve().is_relative_to(folder.resolve()):
                errors.append(f'{ident}: unsafe file path: {rel}')
                continue
            if not path.is_file():
                continue
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f'{ident}: hash mismatch: {rel}')
            total += 1
        if 'SKILL.md' not in original:
            errors.append(f'{ident}: missing original SKILL.md')
        if not skill['license_files'] or not set(skill['license_files']).issubset(expected):
            errors.append(f'{ident}: missing license inventory')
    unexpected = {p.name for p in (root / 'catalog').iterdir() if p.is_dir()} - ids
    if unexpected:
        errors.append(f'Unlisted skill directories: {sorted(unexpected)}')
    return errors, len(ids), total


def main():
    errors, count, files = check(Path(__file__).resolve().parents[1])
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    print(f'OK: {count} skills, {files} files verified. Original files and added license notices match the manifest.')
    print('This checks file integrity, not organizer approval or runtime behavior.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
