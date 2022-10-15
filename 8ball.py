import random
import os
import platform
import time
import sys
# -------------------------------------------- 
from os import system, name
from colorama import Fore, Back, Style, ansi, init
from sty import fg, bg, ef, rs


plat = sys.platform


random_opt = ['Yes',
            "No",
            "Maybe",
            "Surely not",
            "Possibly",
            "Possibly not",
            "There are many probabilities",
            "Sure",
            "Why would you want that to happen?'",
            "Let's pray that it does",
            "I don't hold out much hope",
            "Obviously",
            "Clearly",
            "Don't even doubt it",
            "Start doubting it",
            "I hope no",
            "In a little while",
            "Yeah, why not",
            "Do you really want to know?"]

def clear():
    if plat == "linux":
        os.system('clear')
    elif plat == "darwin":
        os.system('clear')
    else: 
        os.system('cls')

def menu():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]{fg.rs}
    {fg(219)}[+]-----(github.com/Haiisu)-----[+]{fg.rs}
    {fg(225)}- 1: Play
    {fg(225)}- 2: View logs
    {fg(225)}- 3: Options
    {fg(225)}- 4: Credits
    {fg(225)}- 5: Exit
    ''')


    opst = input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Select an option: {Fore.WHITE}')

    if opst == '1':
        main()
    elif opst == '2':
        reg()
    elif opst == '3':
        opts()
    elif opst == '4':
        cred()
    elif opst == '5':
        exit()
    else:
        clear()
        print(f'\n\n{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(1)}Select an option, plz')
        time.sleep(1.4)
        menu()

def main():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]{fg.rs}
    {fg(219)}[+]-----(github.com/Haiisu)-----[+]{fg.rs}
    ''')

    selct = input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Ask me a question about your future: {Fore.WHITE}')
    time.sleep(0.7)
    uwunt = random.choice(random_opt)
    print(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] Your question: {fg(219)}({fg(177)}{selct}{fg(219)}){Fore.WHITE} My answer:{fg(177)} {uwunt} {Fore.WHITE}\n')
    destfile = r"dat.txt"
    with open(destfile, 'a') as f:
        f.write(f'8Ball | Your question: {selct} | My answer: {uwunt}\n')
    time.sleep(0.4)
    rep()

def rep():
    emp_dnuevo = input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Do you want to play again? {Fore.WHITE} (Y/n): {Fore.WHITE}')

    if emp_dnuevo == 'Y'.lower():
        menu()

    elif emp_dnuevo == 'N'.lower():
        exit()

    else:
        clear()
        print(f'\n{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Select an option, plz {Fore.WHITE}')
        time.sleep(1.4)
        rep()

def opts():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]
    {fg(219)}[+]-----(github.com/Haiisu)-----[+]
    {fg(225)}- 1: Delete the log
    {fg(225)}- 2: Change the language (Coming soon)
    {fg(225)}- 3: Change the style (Coming soon)
    {fg(225)}- 4: Exit
    ''')
    confgop = input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Select an option: {Fore.WHITE}')

    if confgop == '4':
        menu()
    elif confgop == '1':
        borrreg()
    else:
        print(f'\n{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {Fore.RED}This option does not exist or is not available! {Fore.WHITE}')
        time.sleep(1)
        opts()

def borrreg():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]
    {fg(219)}[+]-----(github.com/Haiisu)-----[+]
    ''')
    if os.path.isfile('dat.txt') == False:
        input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Log could not be deleted. The log is already deleted. (Enter){Fore.WHITE}\n')
        opts()
    else:
        print(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Deleting the log, please wait... {Fore.WHITE}\n')
        time.sleep(1.2)
        os.remove('dat.txt')
        input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Log successfully deleted. (Enter) {Fore.WHITE}')
        opts()

def cred():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]
    {fg(219)}[+]-----(github.com/Haiisu)-----[+]
    {fg(225)}• Programmed and designed by Haiisu
    {fg(225)}• Made with a lot of <3
    ''') 
    input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Enter if you want to return to the menu: {Fore.WHITE}')
    time.sleep(0.4)
    menu()

def reg():
    clear()
    print(f'''
            {fg(203)}╭━━━╮   ╭━━╮╱╱╱╭╮╭╮ {fg.rs}
            {fg(204)}┃╭━╮┃   ┃╭╮┃╱╱╱┃┃┃┃ {fg.rs}
            {fg(205)}┃╰━╯┃   ┃╰╯╰┳━━┫┃┃┃ {fg.rs}
            {fg(206)}┃╭━╮┃   ┃╭━╮┃╭╮┃┃┃┃ {fg.rs}
            {fg(207)}┃╰━╯┃   ┃╰━╯┃╭╮┃╰┫╰╮{fg.rs}
            {fg(213)}╰━━━╯   ╰━━━┻╯╰┻━┻━╯{fg.rs}
    {fg(219)}[+]------(Coded by Hxiisu)------[+]
    {fg(219)}[+]-----(github.com/Haiisu)-----[+] {fg.rs}
    ''') 

    archi1=open("dat.txt","r")
    contenido=archi1.read()
    print(contenido)
    archi1.close()
    salir = input(f'{Fore.WHITE}[{fg(205)}8Ball{Fore.WHITE}] {fg(177)}Enter if you want to return to the menu: {Fore.WHITE}')
    time.sleep(0.4)
    menu()


if __name__ == "__main__":
    menu()