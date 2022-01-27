# project_py
while '()' in s or '[]' in s or '{}' in s:
  s = s.replace('()', '').replace('[]', '').replace('{}', '')
if len(s) > 0:
  return 'NO'
else:
  return 'YES'
    
