import shutil
for i in range(1,4):
  original = 'custom/FirstFile.txt'
  target = 'custom/' + 'newFile' + str(i) + '.txt'
  shutil.copyfile(original, target)
