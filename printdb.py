from persistence import *

def main():
    print("Activities")
    activities = repo.activities.findall()
    if activities:
        print(activities.__str__())

    print("Branches")
    activities = repo.activities.findall()
    if activities:
        print(activities.__str__())


if __name__ == '__main__':
    main()