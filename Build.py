import os
import shutil

def run():
    # remove the custom folder
    shutil.rmtree("custom", ignore_errors = False)

    # Make dir
    if not os.path.exists('custom'):
        os.makedirs('custom')

    # make file
    with open('custom/FirstFile.txt', 'w') as fp:
        pass
    
    # Add content to the file
    with open('custom/FirstFile.txt', 'w') as fp:
        fp.write("this is the content")

    ## create multiple files
    for i in range(1,4):
        original = "custom/FirstFile.txt"
        target = "custom/" + "newFile" + str(i) + ".txt"
        shutil.copyfile(original, target)


if __name__ == "__main__":
    run()
