# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 0
    print_hi('Sammy')
    for i in range(1, 5, 2):
        print(i)
    list_ages = [2, 5, 10, 9, 5, 10, 22,1]
    set_ages = set(list_ages)
    print(set_ages)
    new_tuple = ('x', 'y', 'z')
    print(new_tuple)
    class Fish():
        pass
    class ClownFish(Fish):
        pass
    fish = ClownFish()
    isinstance(fish, Fish)
    print (ClownFish)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
