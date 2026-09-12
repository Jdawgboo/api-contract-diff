"""Compare small path/type/required API contract documents."""
from __future__ import annotations
def diff(before:dict,after:dict)->dict:
 left,right=before.get('fields',{}),after.get('fields',{});shared=set(left)&set(right)
 return {'added':sorted(set(right)-set(left)),'removed':sorted(set(left)-set(right)),'type_changed':sorted(key for key in shared if left[key].get('type')!=right[key].get('type')),'required_changed':sorted(key for key in shared if bool(left[key].get('required'))!=bool(right[key].get('required')))}
def breaking(result:dict)->bool:return bool(result['removed'] or result['type_changed'] or result['required_changed'])
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);r=diff(p['before'],p['after']);r['breaking']=breaking(r);print(json.dumps(r,indent=2))
