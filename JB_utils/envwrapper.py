#!/usr/bin/env python
import os, sys
from collections.abc import Mapping


class JALIB_ENV:
    def __init__(self):
        self._real_env = os.environ;
        self.cache_env : list[Mapping[str, str,]] = [] 
    

    def Get(self) -> Mapping[str, str]:
        ret_env = self._real_env;
        self.cache(ret_env.copy())
        return ret_env
        
    
    def cache(self, environ: Mapping[str, str]): 
        self.cache_env.append(environ);

    
    def checkdiff(self, RUNTIME_ENV):
        for i, env in enumerate( self.cache_env):
            table = 'path'
            if env.get(table) != RUNTIME_ENV.get(table):
                print(f'env in cache at {i} position does not match with {table}');
            table = 'PATH'   
            if env.get(table) != RUNTIME_ENV.get(table):
                print(f'env in cache at {i} position does not match with {table}');
                
                
        
            
        
    def log_env(self):
        for i, env in enumerate( self.cache_env):
            with  open(f'./ENVCACHE_backup_{i}.log', 'w') as f:
                path_table =env
                print(path_table)
                f.write(str(path_table))
                f.close()
        
    def restore(self):
        pass
    
    # makes path into a row using the ; semicolon
    def rowify(self, UserPath : str):
        return UserPath.split(';');
        

    def GetRawUserPath(self) -> str :
        return  str(self._real_env.get('path'))
    
    def PrintEnvPath(self, UserPath : str | list):
        if isinstance(UserPath, str):
           _env_user_path_list = self.rowify(UserPath);
        elif isinstance(UserPath, list):
           _env_user_path_list = UserPath;

        for path in _env_user_path_list:
            print(path)
          


def GetBashrcPath():
    
    return JALIB_ENV().Get()['UserProfile'] + ("/.bashrc")








