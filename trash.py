from numpy import linalg

def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, tuple, len = 3
            The maximum of the entries' diff for each pair in RGB.
    """
    # This is sometimes very important,
    # because sometimes your img_array is of dtype uint8,
    # and if you forgot that, the subsequent computed values
    # might seem misleading to you.
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    res = (np.max(np.abs(RG_diff)),
           np.max(np.abs(GB_diff)),
           np.max(np.abs(RB_diff)),)
    return res


def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, tuple
            res = Frobenius_norm(R-G, G-B, R-B).
    """
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    res = (np.max(np.abs(RG_diff)),
           np.max(np.abs(GB_diff)),
           np.max(np.abs(RB_diff)),)
    return res



def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, tuple
            res = Frobenius_norm(R-G, G-B, R-B).
    """
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    res = (np.sum(np.abs(RG_diff)),
           np.sum(np.abs(GB_diff)),
           np.sum(np.abs(RB_diff)),)
    return res


def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, tuple
            res = Frobenius_norm(R-G, G-B, R-B).
    """
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    res = (linalg.norm(RG_diff, ord='fro'),
           linalg.norm(GB_diff, ord='fro'),
           linalg.norm(RB_diff, ord='fro'),)
    return res


def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, tuple
            res = Frobenius_norm(R-G, G-B, R-B) / img_array.size
    """
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    n_entries = img_array.size
    res = (linalg.norm(RG_diff, ord='fro')/n_entries,
           linalg.norm(GB_diff, ord='fro')/n_entries,
           linalg.norm(RB_diff, ord='fro')/n_entries,)
    return res





color_img = pil_image.open("UTKFace-clean-13plus/14_1_0_20170109214635943.jpg.chip.jpg")
color_array = np.array(color_img)
color_array.shape

print(channel_diff(gray_array))
print(channel_diff(color_array))

color_array[...,0]





plt.subplot(131)
plt.imshow(gray_array[...,0], cmap='gray')
plt.axis('off')
plt.title('R')
plt.subplot(132)
plt.imshow(gray_array[...,1], cmap='gray')
plt.axis('off')
plt.title('G')
plt.subplot(133)
plt.imshow(gray_array[...,2], cmap='gray')
plt.axis('off')
plt.title('B');




plt.subplot(131)
plt.imshow(color_array[...,0], cmap='gray')
plt.axis('off')
plt.title('R')
plt.subplot(132)
plt.imshow(color_array[...,1], cmap='gray')
plt.axis('off')
plt.title('G')
plt.subplot(133)
plt.imshow(color_array[...,2], cmap='gray')
plt.axis('off')
plt.title('B');


thresholds = [10, 20, 30]
# Create folders if they do not exist
for thres in thresholds:
    thres_folder = "threshold-"+str(thres)
    if not os.path.exists(thres_folder):
        os.mkdir(thres_folder)

utk_folder = "UTKFace-clean-13plus"
for fname in os.listdir(utk_folder):
    fpath = os.path.join(utk_folder, fname)
    img_array = plt.read(fpath)
    critical_value = channel_diff(img_array)
    for thres in thresholds:
        if critical_value < thres:
            thres_folder = "threshold-"+str(thres)
            plt.imsave(os.path.join(thres_folder, fname), img_array)


def channel_diff(img_array):
    """
    Input:
        img_array, ndarray
            channel order (R, G, B)

    Return:
        res, float
    """
    img_array = img_array.astype(np.float32)
    RG_diff = img_array[..., 0] - img_array[..., 1]
    GB_diff = img_array[..., 1] - img_array[..., 2]
    RB_diff = img_array[..., 0] - img_array[..., 2]
    res = np.max([np.max(np.abs(RG_diff)),
                  np.max(np.abs(GB_diff)),
                  np.max(np.abs(RB_diff)),])
    return res



thresholds = [10, 35, 45]
# Create folders to put the images in if they do not exist already.
for thres in thresholds:
    thres_folder = "thres-"+str(thres)
    serht_folder = "serht-"+str(thres)  # the complement of thres_folder
    if not os.path.exists(thres_folder):
        os.mkdir(thres_folder)
    if not os.path.exists(serht_folder):
        os.mkdir(serht_folder)

utk_folder = "UTKFace-clean-13plus"
for fname in os.listdir(utk_folder):
    fpath = os.path.join(utk_folder, fname)
    img_array = plt.imread(fpath)
    critical_value = channel_diff(img_array)
    for thres in thresholds:
        if critical_value < thres:
            thres_folder = "thres-"+str(thres)
            plt.imsave(os.path.join(thres_folder, fname), img_array)
        else:
            serht_folder = "serht-"+str(thres)
            plt.imsave(os.path.join(serht_folder, fname), img_array)



thresholds = [10, 35, 45]
# Create folders to put the images in if they do not exist already.
for thres in thresholds:
    thres_folder = "thres-"+str(thres)
    #serht_folder = "serht-"+str(thres)  # the complement of thres_folder
    if not os.path.exists(thres_folder):
        os.mkdir(thres_folder)
    #if not os.path.exists(serht_folder):
    #    os.mkdir(serht_folder)

utk_folder = "UTKFace-clean-13plus"
for fname in os.listdir(utk_folder):
    fpath = os.path.join(utk_folder, fname)
    img_array = plt.imread(fpath)
    critical_value = channel_diff(img_array)
    for thres in thresholds:
        if critical_value < thres:
            thres_folder = "thres-"+str(thres)
            plt.imsave(os.path.join(thres_folder, fname), img_array)
        #else:
        #    serht_folder = "serht-"+str(thres)
        #    plt.imsave(os.path.join(serht_folder, fname), img_array)
