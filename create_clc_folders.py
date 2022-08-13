#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: output.py
# Description: Create book folders following CLC categories.
# Author: Feng Wang
# Date: 2022-08-13


import os

context_folders = ['books', ]

def create_folder( line, context_indent, name_indent ):
    global context_folders

    # some of them dose not meet this criteria
    #assert len(context_folders) >= context_indent, f'Error: cannot indent {context_indent} for {line}'

    context_folders = context_folders[:context_indent]
    name = line[name_indent:].strip()
    context_folders.append( name )
    current_folder = '/'.join( context_folders )
    print( f'{line} -> {current_folder}' )
    command = os.makedirs( current_folder, exist_ok=True )
    os.system( f'touch "{current_folder}/.gitkeep"' ) # optional
    return current_folder

def mkfolder( line ):
    global context_folders

    if line[0] == '#':
        return create_folder(line, 1, 4)

    if line[0] == '*':
        return create_folder(line, 2, 3)

    if line[:3] == '  *':
        return create_folder(line, 3, 4)

    if line[:5] == '    *':
        return create_folder(line, 4, 6)

    if line[:7] == '      *':
        return create_folder(line, 5, 8)

    if line[:9] == '        *':
        return create_folder(line, 6, 10)

    if line[:11] == '          *':
        return create_folder(line, 7, 12)

    if line[:13] == '            *':
        return create_folder(line, 8, 14)

    if line[:15] == '              *':
        return create_folder(line, 9, 16)

    if line[:17] == '                *':
        return create_folder(line, 19, 18)

    assert False, f'cannot process {line}'

if __name__ == '__main__':
    # modify this clc.md file to add more categories if necessary.
    with open ( './clc.md' ) as f:
        lines = f.read().splitlines()
    print( f'Read {len(lines)} lines' )
    for line in lines:
        mkfolder( line )

