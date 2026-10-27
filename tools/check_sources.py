"""Static historical-source check; this does not execute applications."""
import ast, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
known={'projects/Hume/src/Bayesian-RecSys.py','projects/Hume-v1/src/Bayesian-RecSys.py'}
errors=[]; expected=[]; py=nb=0
for p in sorted((root/'projects').rglob('*')):
    if p.suffix=='.py':
        py+=1
        try: ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
        except SyntaxError as exc:
            rel=p.relative_to(root).as_posix()
            (expected if rel in known and exc.lineno==113 else errors).append(f'{rel}:{exc.lineno}: {exc.msg}')
    elif p.suffix=='.ipynb':
        nb+=1
        try:
            data=json.loads(p.read_text())
            for cell in data.get('cells',[]):
                assert not cell.get('outputs') and not cell.get('attachments')
                assert cell.get('execution_count') is None
        except Exception as exc: errors.append(f'{p.relative_to(root)}: {exc}')
print(f'{py} Python files; {nb} notebooks; {len(expected)} documented unfinished files; {len(errors)} unexpected issues')
for item in expected: print('KNOWN INCOMPLETE:',item)
for item in errors: print('ERROR:',item)
raise SystemExit(bool(errors))
