import os
import cv2
from tqdm import tqdm

def partition_dataset(name, dataset_path):
    path = os.path.join(dataset_path, name)
    new_path1 = os.path.join(dataset_path, name + '_1_1')
    os.makedirs(new_path1, exist_ok=True)

    new_path2 = os.path.join(dataset_path, name + '_1_2')
    os.makedirs(new_path2, exist_ok=True)

    new_path3 = os.path.join(dataset_path, name + '_1_3')
    os.makedirs(new_path3, exist_ok=True)

    new_path4 = os.path.join(dataset_path, name + '_2_1')
    os.makedirs(new_path4, exist_ok=True)

    new_path5 = os.path.join(dataset_path, name + '_2_2')
    os.makedirs(new_path5, exist_ok=True)

    im_list = os.listdir(path)  # 读取文件下所有图像

    for im_name in tqdm(im_list):
        # print(im_name)
        im = cv2.imread(os.path.join(path, im_name))

        h, w, c = im.shape

        im_1_1 = im[0: h // 3, :, :]  # 身体上1/3
        im_1_2 = im[h // 3: 2 * h // 3, :, :]  # 身体中部1/3~2/3
        im_1_3 = im[2 * h // 3:, :, :]  # 身体下面的1/3

        im_2_1 = im[0: h // 2, :, :]  # 身体上方的一半
        im_2_2 = im[h // 2:, :, :]  # 身体下面的1/2

        cv2.imwrite(os.path.join(new_path1, im_name), cv2.resize(im_1_1, (224, 224)))
        cv2.imwrite(os.path.join(new_path2, im_name), cv2.resize(im_1_2, (224, 224)))
        cv2.imwrite(os.path.join(new_path3, im_name), cv2.resize(im_1_3, (224, 224)))
        cv2.imwrite(os.path.join(new_path4, im_name), cv2.resize(im_2_1, (224, 224)))
        cv2.imwrite(os.path.join(new_path5, im_name), cv2.resize(im_2_2, (224, 224)))

if __name__ == '__main__':
    dataset_path = 'datasets/celeb'
    print("划分gallery\n")
    partition_dataset('gallery', dataset_path)
    print("划分query\n")
    partition_dataset('query', dataset_path)
    print("划分train\n")
    partition_dataset('train', dataset_path)
