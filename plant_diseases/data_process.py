import matplotlib.image as mpimg
#定义数据尺寸
selected_image_size = 224
resize = True
total_sample_size = 10000 # 5k-50k

channel = 1
size = 2

folder_count = 38
image_count = 20 #0-50

if resize == True:
    batch_size=256
else:
    batch_size=64
def get_data(size, total_sample_size):
    #read the image
    image = mpimg.imread(path+'s' + str(1) + '/' + str(1) + '.jpg', 'rw+')
    #reduce the size
    if resize == True:
        image = image[::size, ::size]
    #get the new size
    dim1 = image.shape[0]
    dim2 = image.shape[1]

    count = 0

    #initialize the numpy array with the shape of [total_sample, no_of_pairs, dim1, dim2]
    x_geuine_pair = np.zeros([total_sample_size, 2, 1, dim1, dim2])

    y_genuine = np.zeros([total_sample_size,1])

    for i in range(folder_count):
        for j in range(int(total_sample_size/folder_count)):
            ind1 = 0
            ind2 = 0

            #read images from same directory (genuine pair)
            while ind1 == ind2:
                ind1 = np.random.randint(image_count)
                ind2 = np.random.randint(image_count)

            # read the two images
            img1 = mpimg.imread(path+'s' + str(i+1) + '/' + str(ind1 + 1) + '.jpg', 'rw+')
            img2 = mpimg.imread(path+'s' + str(i+1) + '/' + str(ind2 + 1) + '.jpg', 'rw+')

            #reduce the size
            if resize == True:
                img1 = img1[::size, ::size]
                img2 = img2[::size, ::size]

            #store the images to the initialized numpy array
            print
            x_geuine_pair[count, 0, 0, :, :] = img1
            x_geuine_pair[count, 1, 0, :, :] = img2

            #as we are drawing images from the same directory we assign label as 1. (genuine pair)
            y_genuine[count] = 1
            count += 1

    count = 0
    x_imposite_pair = np.zeros([total_sample_size, 2, 1, dim1, dim2])
    y_imposite = np.zeros([total_sample_size, 1])

    for i in range(int(total_sample_size/image_count)):
        for j in range(image_count):

            #read images from different directory (imposite pair)
            while True:
                ind1 = np.random.randint(folder_count)
                ind2 = np.random.randint(folder_count)
                if ind1 != ind2:
                    break

            img1 = mpimg.imread(path+'s' + str(ind1+1) + '/' + str(j + 1) + '.jpg', 'rw+')
            img2 = mpimg.imread(path+'s' + str(ind2+1) + '/' + str(j + 1) + '.jpg', 'rw+')

            if resize == True:
                img1 = img1[::size, ::size]
                img2 = img2[::size, ::size]

            x_imposite_pair[count, 0, 0, :, :] = img1
            x_imposite_pair[count, 1, 0, :, :] = img2
            #as we are drawing images from the different directory we assign label as 0. (imposite pair)
            y_imposite[count] = 0
            count += 1

    #now, concatenate, genuine pairs and imposite pair to get the whole data
    #print(x_geuine_pair.shape)
    #print(x_imposite_pair.shape)
    X = np.concatenate([x_geuine_pair, x_imposite_pair], axis=0)/255
    Y = np.concatenate([y_genuine, y_imposite], axis=0)

    return X, Y
X, Y = get_data(size, total_sample_size)
