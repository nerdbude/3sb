#!/usr/bin/env python
# encoding: utf-8
# TITLE: 3SB - SIMPLE STATIC SITE BUILDER
# AUTHOR: 0x17 
# WEBSITE: https://www.nerdbude.com 

import os
import subprocess
import sys
import shutil
from pathlib import Path

class bcolors:
    OK      = '\033[92m'
    FAIL    = '\033[91m'
    RESET   = '\u001b[0m'
    DEFAULT = '\033[35m'
    CHECK   = '\033[33m'
    PINK    = '\033[95m'

def main():
    os.system('clear')

    print('')
    print('')
    print('')
    print(bcolors.DEFAULT + '')
    print('       ██████╗ ███████╗██████╗')
    print('       ╚════██╗██╔════╝██╔══██╗')
    print('        █████╔╝███████╗██████╔╝')
    print('        ╚═══██╗╚════██║██╔══██╗')
    print('       ██████╔╝███████║██████╔╝')
    print('       ╚═════╝ ╚══════╝╚═════╝')
    print('')
    print('  // Simple Static Site Builder / ? for help // ')
    print(' ')
    print(' ' + bcolors.RESET)
    
    while True: 
        # Main Input
        command = input(bcolors.CHECK + "[3SB]" + bcolors.RESET + " >>> ")
        
        # Version
        ver = "0.5"

        # PATH Variablen
        root_dir        = ("/home/pho/CODE/3sb/")
        parent_dir      = ("/home/pho/CODE/3sb/new_post")
        template_post   = ("/home/pho/CODE/3sb/templates/post.html")
        template_footer = ("/home/pho/CODE/3sb/templates/footer.html")
        template_header = ("/home/pho/CODE/3sb/templates/header.html")
        template_menu   = ("/home/pho/CODE/3sb/templates/menu.html")
        new_post        = ("/home/pho/CODE/3sb/new_post/")
        all_posts       = ("/home/pho/CODE/3sb/structure/posts/de/")

        if command == "?":
        # HELP
            print('')
            print('[3SB] - Simple static site builder is just a small')
            print('python project so generate simple static html pages an have the possibility')
            print('to deploy a new menu / header / footer to the whole website without')
            print('changing all the files by hand. Every file within the so called structure')
            print('is handled as a post.')
            print('')
            print(bcolors.FAIL + '?            - Print this help' + bcolors.RESET)
            print('')
            print(bcolors.FAIL + 'status       - structure status' + bcolors.RESET)
            print('               Gives you the structures status like open posts etc. ')
            print('')
            print(bcolors.FAIL + 'init         - initialize new post' + bcolors.RESET)
            print('               Create a new post in "/new_post".') 
            print('               Just enter title, subtitle and release date.')
            print('')
            print(bcolors.FAIL + 'edit         - edit posts' + bcolors.RESET)
            print('               Enter the title of post you want to edit and') 
            print('               Vim opens to edit the post and save it.') 
            print('')
            print(bcolors.FAIL + 'footer       - edit footer' + bcolors.RESET)
            print('               Opens the footer.html template within Vim and')
            print('               let you modify the footer for the whole website.')
            print('')
            print(bcolors.FAIL + 'header       - edit header' + bcolors.RESET)
            print('               Opens the header.html template within Vim and')
            print('               let you modify the header for the whole website.')
            print('')
            print(bcolors.FAIL + 'menu         - edit menu' + bcolors.RESET)
            print('               Opens the websites menu.html template within Vim')
            print('               and let you modify the menu.')
            print('')            
            print(bcolors.FAIL + 'deploym      - deploy menu' + bcolors.RESET)
            print('               Deploy menu to all post-files in structure.' + bcolors.RESET)
            print('')
            print(bcolors.FAIL + 'deployf      - deploy footer' + bcolors.RESET)
            print('               Deploy footer to all post-files in structure')
            print('')
            print(bcolors.FAIL + 'q            - quit' + bcolors.RESET)
            
            print('')
            # STATUS MENU 
        if command == "status":
            new = (len(next(os.walk(parent_dir))[1]))
            list_new = [name for name in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, name))]
            total = 0
            for path in os.listdir(all_posts):
                if os.path.isfile(os.path.join(all_posts, path)):
                    total += 1

            print('')
            print('-------  STATUS  -------')
            print('VERSION:      ', ver)
            print('NEW POSTS:    ', new)
            print('TOTAL POSTS:  ', total)
            print('------------------------')
            print('OPEN POSTS:')
            print(list_new)
            print('')

        if command == "init":
        # NEW POST SEQUENCE
            title = input(bcolors.CHECK + '[enter title]' + bcolors.RESET + ' >>> ' )
            subtitle = input(bcolors.CHECK + '[enter subtitle]' + bcolors.RESET + ' >>> ')
            postdate = input(bcolors.CHECK + '[enter postdate]' + bcolors.RESET + ' >>> ')
            print('')
            print('+-----------------------')
            print('[+] Title: ' + title)
            print('[+] Subtitle: ' + subtitle)
            print('[+] Date: ' + postdate)
            print('+-----------------------')
            print('')
            path = os.path.join(parent_dir , title)
            mode = 0o777
            os.mkdir(path, mode)
            postfilepath = (parent_dir + "/" + title)
            shutil.copy(template_post, postfilepath)
            os.rename(postfilepath + "/post.html", postfilepath + "/" + title + ".html")

        if command == "edit":
            # EDIT POST WITH VIM
            edit = input(bcolors.CHECK + '[EDIT]' + bcolors.RESET + ' >>> ')
            os.system("vim " + new_post + edit + "/" + edit + ".html")
            print('done')
            print('')
        
        if command == "build":
            # building post with header and footer 
            build = input(bcolors.CHECK + '[BUILD]' + bcolors.RESET + ' >>> ')
            build = new_post + '/' + build + '/' + build + '.html'
            buildmodules = [template_header, build, template_footer]
            with open(build, 'w') as outfile:
                for names in buildmodules:
                    with open(names) as infile: 
                        outfile.write(infile.read())
                    outfile.write("\n")

        if command == "header":
            # EDIT HEADER WITH VIM 
            os.system("vim" + template_header)
            print('done.')
            print('')
        
        if command == "footer":
            # EDIT FOOTER WITH VIM
            os.system("vim " + template_footer)
            print('done.')
            print('')
        
        if command == "menu":
            # EDIT MENU WITH VIM
            os.system("vim " + template_menu)
            print('done')
            print('')

        if command == "deploym":
            # delete old menu lines
            all_posts = Path(all_posts)
            to_append = (all_posts / template_menu).read_text()
            
            for html in all_posts.rglob("*.html"):
                lines = html.read_text().splitlines()
                lines = lines[:33] + [to_append] + lines[47:]
                html.write_text("\n".join(lines)) 
            
            print('menu deployed to all posts')

        if command == "deployf":
           # ADD FOOTER TO ALL FILES 
            for root, dirs, files in os.walk(all_posts, topdown = False):
              for name in files:
                  if name.endswith(".html"):
                      file_name = os.path.join(root, name)
                      with open(file_name, 'r+') as fp:
                        lines = fp.readlines()
                        fp.seek(0)
                        fp.truncate()
                        #test 
                        fp.writelines(lines[:-10])
                        footercontent = open(template_footer, 'r').readlines()
                        fp.writelines(footercontent)

            print('footer deployed to all posts')

        if command == "q":
            # CLOSE THE SCRIPT
            os.system('clear')
            break
main()
