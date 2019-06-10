# filter-3-channeled-grayscale-images
In search for a better method to distinguish RGB images that look more like grayscale images from its true colorful fellows.

My motivation behind this is to clean the UTKFace dataset, tailor it to my need. The jupyter notebook `investigate-UTKFace-grey.ipynb` targets the UTKFace dataset, which can be downloaded, for example, [from kaggle](https://www.kaggle.com/jangedoo/utkface-new/version/1). (Or you might be able to apply the same jupyter notebook to any other image datasets that contain grayscale-like RGB images.)

Note that the user might have to modify the paths inside the jupyter notebook to have it suit for their own computer's directory tree.

### Test result on threshold value = 10, 35, 45 and a small report
- `10`: Images being filtered are quite strictly what we would call grayscale images.
- `35`: About 150 more images being filtered. Aside from the traditional grayscale images, this way of doing with `35` as threshold value filters those old photos, yellow-ish photoes. Notably, it also filtered very few true color images, all of the are photoes of africans.
- `45`: 50 or so more images being filtered, most of them are true color images. It might be due to the fact that they are not pretty colorful, a bit dim for example, that they are being filtered at this threshold value.
