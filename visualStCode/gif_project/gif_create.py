import imageio.v3 as iio
filenames = ['gif1_test.jpg', 'gif2_test.jpg', 'gif3_test.jpg']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
iio.imwrite('test.gif', images, duration = 500, loop = 0)