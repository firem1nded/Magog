#!/usr/bin/python3.4
import checker

def main():
    user = 'user@domain.com'
    password = 'password'

    print("Account:", user, password)
    sites = checker.check(user, password)
    for site in sites:
        valid = sites[site]
        print("Site:", site)
        print("Account is", "valid" if valid else "invalid")
        print()

if __name__ == '__main__':
    main()
