from typing import List, Tuple, Dict, Union

n : int = 5          #use collen syntax  for variables

name: str = "bhoomika"

def sum(a:int, b:int) -> int:  # -> for function return types
    return a+b


numbers: List[int]=[1,2,3,4,5]   #List of integers

person: Tuple[str,int]=(1,"bhoooom") #Tuple of integer and string

sss: Dict[str,int]={"alice":56,"bob":55}#Dictionary with string keys and integer values

# Union type for variables that can hold multiple types
identifier: Union[int,str] ="ID634"
identifier= 83264   #also valid

