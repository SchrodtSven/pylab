# Testing data classes - e.g: identity management classes
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-21    

from mypkg.core import Updatable
from dataclasses import dataclass
from typing import Dict, List

@dataclass(slots=True)
class User(Updatable):

    user: str
    passw: str
    groups: List
    id: int = 0
    role: str = 'guest'
    sanitized: bool = False
    
    valid_roles = ['GOD', 'Admin', 'Editor', 'Guest']



if __name__ == "__main__":
    my_usr = User(user='peterpan', passw='FooBar23!', groups=[])
    my_usr.id = 666
    print(666)
    print(my_usr)
    
    my_usr.update({'role': 'God', 'sanitized': True, 'passw1': '10PS33cr31', 'groups': ['Linux', 'MacOS', 'Amiga OS']})
    print(my_usr)