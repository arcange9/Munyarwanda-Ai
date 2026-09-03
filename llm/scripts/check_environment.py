import importlib.util,sys
mods=['torch','transformers','datasets','peft','trl','accelerate','yaml']
missing=[m for m in mods if importlib.util.find_spec(m) is None]
print({'python':sys.version,'missing':missing,'status':'ok' if not missing else 'missing_dependencies'})
